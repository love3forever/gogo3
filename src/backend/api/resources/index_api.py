#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-11 10:32:33
# @Author  : eclipse (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from flask.blueprints import Blueprint
from flask_restful import Resource, Api, abort
from flask import jsonify, url_for
from dataCollector import data_poster
from common_funcs import output
from static_data import index_json

index_blueprint = Blueprint(__name__, "index_blueprint")
indexAPI = Api(index_blueprint, prefix='/api/v1/index')


@indexAPI.resource('/detail')
class Recommand(Resource):
    """docstring for Recommand"""

    def get(self):
        index_data = data_poster.parse_index_data()
        if index_data:
            return output(jsonify(index_data))
        else:
            abort(404, description='no data avaliable')


@indexAPI.resource('/direct')
class DirectData(Resource):
    """docstring for DirectData"""

    def get(self):
        index_data = index_json
        if index_data:
            return output(jsonify(index_data))
        else:
            abort(404, description='no data avaliable')


@indexAPI.resource('/info')
class APILists(Resource):
    """docstring for APILists"""

    def get(self):
        apis = {
            '歌单详情': {
                'url': '/api/v1/playlist/detail/<string:playlist>',
                'example': '/api/v1/playlist/detail/62508699'
            },
            '歌单评论': {
                'url': '/api/v1/playlist/comments/<string:playlist>/page/<int:page>',
                'example': '/api/v1/playlist/comments/625086991/page/1'
            },
            '歌曲详情': {
                'url': 'api/v1/song/detail/<string:songId>',
                'example': 'api/v1/song/detail/18374880'
            },
            '歌曲评论': {
                'url': '/api/v1/song/comments/<string:songId>/page/<int:page>',
                'example': '/api/v1/song/comments/490006672/page/1'
            },
            '歌曲歌词': {
                'url': '/api/v1/song/lyrics/<string:songId>',
                'example': '/api/v1/song/lyrics/405343230'
            },
            '用户详情': {
                'url': '/api/v1/user/<string:userId>/detail',
                'example': '/api/v1/user/98038167/detail'
            },
            '用户粉丝列表': {
                'url': '/api/v1/user/<string:userId>/fans',
                'example': '/api/v1/user/77159064/fans'
            },
            '用户关注列表': {
                'url': '/api/v1/user/<string:userId>/follows',
                'example': '/api/v1/user/77159064/follows'
            },
            '用户歌单': {
                'url': '/api/v1/user/<string:userId>/playlist',
                'example': '/api/v1/user/77159064/playlist'
            },
            '歌手top50歌曲': {
                'url': '/api/v1/artist/<string:artistId>/index',
                'example': '/api/v1/artist/5346/index'
            },
            '歌手专辑': {
                'url': '/api/v1/artist/<string:artistId>/albums',
                'example': '/api/v1/artist/5346/albums'
            },
            '专辑详情': {
                'url': '/api/v1/album/<string:albumId>/detail',
                'example': '/api/v1/album/35696416/detail'
            },
            '专辑评论': {
                'url': '/api/v1/album/<string:albumId>/comments/<int:page>',
                'example': '/api/v1/album/35696416/comments/1'
            }
        }
        return output(jsonify(apis))
