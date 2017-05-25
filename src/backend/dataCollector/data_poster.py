#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-22 20:56:56
# @Author  : eclipse (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$
import json
import time
from requests import Session
from bs4 import BeautifulSoup
from params_dicts import get_user_follows_param, get_user_fans_param, get_playlist_comments_param
from encrypter import encrypted_request
from functools import wraps

host_url = 'https://music.163.com/{}'
indexURL = 'https://music.163.com/discover'
playlist_URL = 'https://music.163.com/playlist?id={}'
user_follows_URL = 'http://music.163.com/weapi/user/getfollows/{}?csrf_token='
user_fans_URL = 'http://music.163.com/weapi/user/getfolloweds?csrf_token='
playlist_comments_URL = 'http://music.163.com/weapi/v1/resource/comments/A_PL_0_{}?csrf_token='
playlist_detail_URL = 'http://music.163.com/api/playlist/detail?id={}'
song_comments_URL = 'http://music.163.com/api/v1/resource/comments/R_SO_4_{}/?rid=R_SO_4_{}&offset={}&total=true&limit=100'
song_detail_URL = 'http://music.163.com/api/song/detail?ids=[{}]'
session = Session()


def get_data_from_web(url):
    # 根据url获取原始数据
    time.sleep(1)
    if url:
        origin_data = session.get(url)
        if origin_data.status_code == 200:
            return origin_data
        else:
            print(origin_data.status_code)
            return None
    else:
        return None


def post_data_to_web(url, params):
    result_data = session.post(url, data=params)
    if result_data:
        return json.loads(result_data.text) or None
    else:
        return None


def parse_index_data():
    # 获取首页信息
    index_data = get_data_from_web(indexURL)
    index_content = index_data.content
    index_soup = BeautifulSoup(index_content, 'lxml')
    cvr_list = index_soup.find_all('ul', class_='m-cvrlst f-cb')
    if cvr_list:
        hottest_recommend_lis = cvr_list[0].select('li')
        recommend_data = map(mapper_index_recommend_list,
                             hottest_recommend_lis)
        return recommend_data
    else:
        print('Nothing found')
        return None


def mapper_index_recommend_list(data):
    # 将推荐列表信息转为数组
    if data:
        # 获取歌单图片链接
        img = data.select('img')[0]['src']
        # 获取歌单链接和名称
        play_list_url = data.find_all('a', class_='msk')[0]['href']
        play_list_title = data.find_all('a', class_='msk')[0]['title']
        play_list_id = data.find_all('a', class_='msk')[0]['data-res-id']
        #
        play_count = data.find_all('span', class_='nb')[0].string

        return {
            'img': img,
            'playlistURL': host_url.format(play_list_url),
            'playlistTitle': play_list_title,
            'playTimes': play_count,
            'playlistID': play_list_id
        }
    else:
        return None


def get_playlist_data(playlist_id):
    playlist_url = playlist_URL.format(playlist_id)
    playlist_origin_data = get_data_from_web(playlist_url)
    if playlist_origin_data:
        playlist_soup = BeautifulSoup(playlist_origin_data.content, 'lxml')
        # 获取歌单基本信息
        cntc = playlist_soup.select('.cntc')[0]
        cntc = parse_playlist_cntc(cntc)
        return cntc or None
    else:
        return None


def parse_playlist_cntc(data):
    if data:
        cntc_title = data.select('.f-ff2')[0].string
        tags = data.find_all('a', class_='u-tag')
        cntc_tags = []
        for tag in tags:
            tag_url = tag['href']
            tag_name = tag.select('i')[0].string
            cntc_tags.append({
                'tagURL': tag_url,
                'tagName': tag_name
            })
        cntc_creator_soup = data.find_all('div', class_='user f-cb')[0]
        creator_img = cntc_creator_soup.select('img')[0]['src']
        creator_url = cntc_creator_soup.select('span > a')[0]['href']
        creator_name = cntc_creator_soup.select('span > a')[0].string
        created_time = cntc_creator_soup.select('.time')[0].string
        cntc = {
            'cntcTitle': cntc_title,
            'cntcCreator': {
                'name': creator_name,
                'url': creator_url,
                'img': creator_img
            },
            'cntcCreatedTime': created_time,
        }
        return cntc
    else:
        return None


def data_poster(uid, postURL, keyword, getparamFunc):
    ##########################################
    # uid: 唯一标识符，可以为用户id，歌单id等
    # postURL: 发送post请求的目标url
    # keyword: 返回值目标数据的key
    # getparamFunc: 获取不同请求类型的请求参数的方法
    ##########################################
    if hasattr(getparamFunc, '__call__'):
        post_param = getparamFunc(uid)
        data_list = []
        data_flag = True
        data_times = 0
        while data_flag:
            post_param['offset'] = str(data_times * 100)
            encrtyed_param = encrypted_request(post_param)
            response_data = post_data_to_web(postURL, encrtyed_param)
            if response_data[keyword]:
                data_list.extend(response_data[keyword])
            data_times += 1
            data_flag = response_data['more']
        return data_list
    else:
        print('{} should be callable'.format(str(getparamFunc)))


def get_user_follows(userid):
    # 根据用户id获取关注列表
    return data_poster(userid, user_follows_URL.format(userid),
                       'follow', get_user_follows_param)


def get_user_fans(userid):
    # 根据用户id获取粉丝列表
    return data_poster(userid, user_fans_URL, 'followeds', get_user_fans_param)


def get_playlist_comments(playlistId):
    # 根据歌单id获取评论
    return data_poster(playlistId, playlist_comments_URL.format(
        playlistId), 'comments', get_playlist_comments_param)


def get_playlist_detail(playlistId):
    pass


def get_song_detail(songId):
    # 根据歌曲Id获取详情
    detail_url = song_detail_URL.format(songId)
    detail_data = get_data_from_web(detail_url)
    if detail_data.status_code == 200:
        detail_result = json.loads(detail_data.content)
        return detail_result
    else:
        return None


def get_song_comments(songId):
    data_list = []
    data_flag = True
    data_times = 0
    while data_flag:
        comments_url = song_comments_URL.format(
            songId, songId, 100 * data_times)
        response_data = get_data_from_web(comments_url)
        if response_data:
            response_data = json.loads(response_data.content)
            if response_data['comments']:
                data_list.extend(response_data['comments'])
            data_times += 1
            data_flag = response_data['more']
        else:
            return None
    return data_list

if __name__ == '__main__':
    result = get_song_comments('5272145')
    print(len(result))
    print(result)
