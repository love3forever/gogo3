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

playlist_comments = {"rid": "A_PL_0_{}", "offset": "0", "total": "true",
                     "limit": "100", "csrf_token": ""}


def get_user_follows_param(userId):
    follows_data = post_data
    follows_data['userId'] = userId
    return follows_data


def get_user_fans_param(userId):
    fans_data = post_data
    fans_data['userId'] = userId
    return fans_data


def get_playlist_comments_param(playlistId):
    comments_param = playlist_comments
    comments_param['rid'] = comments_param['rid'].format(playlistId)
    return comments_param
