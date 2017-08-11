#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-23 20:36:12
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
post_data = {
    "userId": "77159064",
    "offset": "0",
    "total": "true",
    "limit": "100",
    "csrf_token": ""
}

follow_and_fans_data = {
    "userId": "77159064",
    "offset": "0",
    "total": "true",
    "limit": "100",
    "csrf_token": ""
}

playlist_comments = {"rid": "A_PL_0_{}", "offset": "0", "total": "true",
                     "limit": "100", "csrf_token": ""}

# user_playlist = {
#     'uid': '',
#     'offset': "0",
#     'limit': "20",
# }

user_playlist = {
    "csrf_token": "",
    "limit": "36",
    "offset": "0",
    "total": "true",
    "uid": "66891851",
    "wordwrap": "7"
}


# user_playrecord_week = {"uid": "66891851", "type": "0",
#                         "limit": "1000", "offset": "0", "total": "true"}

# user_playrecord_all = {"uid": "66891851", "type": "0",
#                        "limit": "1000", "offset": "0", "total": "true"}

user_playrecord_all = {
    "csrf_token": "",
    "limit": "1000",
    "offset": "0",
    "total": "true",
    "type": "-1",
    "uid": "66891851"
}

user_playrecord_week = {
    "csrf_token": "",
    "limit": "1000",
    "offset": "0",
    "total": "true",
    "type": "-1",
    "uid": "66891851"
}


album_comments = {
    'limit': 20,
    'offset': 0,
    'rid': "R_AL_3_{}",
    'total': 'true'
}

djradio_comments = {
    'limit': 20,
    'offset': 0,
    'rid': "A_DJ_1_{}",
    'total': 'true'
}


def get_user_follows_param(userId):
    follows_data = post_data
    follows_data['userId'] = userId
    return follows_data


def get_user_fans_param(userId):
    fans_data = post_data
    fans_data['userId'] = userId
    return fans_data


def get_user_playlist_param(userId):
    playlist_data = user_playlist
    playlist_data['uid'] = userId
    return playlist_data


def get_playlist_comments_param(playlistId):
    comments_param = playlist_comments
    comments_param['rid'] = comments_param['rid'].format(playlistId)
    return comments_param


def get_user_playrecord_week(userId):
    record_data = user_playrecord_week
    record_data['uid'] = userId
    return record_data


def get_user_playrecord_all(userId):
    record_data = user_playrecord_all
    record_data['uid'] = userId
    return record_data
