#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-22 20:56:56
# @Author  : eclipse (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$
import json
from requests import Session
from bs4 import BeautifulSoup
from params_dicts import get_user_follows_param, get_user_fans_param
from encrypter import encrypted_request

host_url = 'https://music.163.com/{}'
indexURL = 'https://music.163.com/discover'
playlist_URL = 'https://music.163.com/playlist?id={}'
user_follows_URL = 'http://music.163.com/weapi/user/getfollows/{}?csrf_token='
user_fans_URL = 'http://music.163.com/weapi/user/getfolloweds?csrf_token='
session = Session()


def get_data_from_web(url):
    # 根据url获取原始数据
    if url:
        origin_data = session.get(url)
        return origin_data or None
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


def get_user_follows(userid):
    post_params = get_user_follows_param(userid)
    follows_list = []
    follows_flag = True
    follows_times = 0
    while follows_flag:
        post_params['offset'] = str(follows_times * 100)
        encrtyed_params = encrypted_request(post_params)
        follows_data = post_data_to_web(
            user_follows_URL.format(userid), encrtyed_params)
        follows_list.extend(follows_data['follow'])
        follows_times += 1
        follows_flag = follows_data['more']
    return follows_list


def get_user_fans(userid):
    post_params = get_user_fans_param(userid)
    fans_list = []
    fans_flag = True
    fans_times = 0
    while fans_flag:
        post_params['offset'] = str(fans_times * 100)
        encrtyed_params = encrypted_request(post_params)
        fans_data = post_data_to_web(user_fans_URL, encrtyed_params)
        fans_list.extend(fans_data['followeds'])
        fans_times += 1
        fans_flag = fans_data['more']
    return fans_list

if __name__ == '__main__':
    pass
