#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-25 20:59:55
# @Author  : love3forever
# @Link    : http://example.org
# @Version : $Id$
from flask.blueprints import Blueprint
from flask_restful import Resource, Api, abort
from flask import jsonify
from dataCollector import data_poster
from common_funcs import output
from static_data import static_playlist_detail, static_playlist_comments

playlist_blueprint = Blueprint(__name__, 'playlist')
playlistAPI = Api(playlist_blueprint, prefix='/api/v1/playlist')


@playlistAPI.resource('/detail/<string:playlistId>')
class PlaylistDetail(Resource):
    """docstring for PlaylistDetail"""

    def get(self, playlistId):
        if playlistId:
            data = data_poster.get_playlist_detail(playlistId)
            if data:
                return output(jsonify(data))
            else:
                abort(404, description='no playlist detail info')
        else:
            abort(404, description='do request with right playlist please')


@playlistAPI.resource('/comments/<string:playlistId>')
class PlaylistComments(Resource):
    """docstring for PlaylistComments"""

    def get(self, playlistId):
        if playlistId:
            data = data_poster.get_playlist_comments(playlistId)
            if data:
                result = {
                    'code': 200,
                    'comments': data,
                    'playlistId': playlistId
                }
                return output(jsonify(result))
            else:
                abort(404, description='no playlist comments info')
        else:
            abort(404, description='do request with right playlist please')


@playlistAPI.resource('/detail/static')
class PlaylistDetailStatic(Resource):
    """docstring for PlaylistCommentsStatic"""

    def get(self):
        data = static_playlist_detail
        if data:
            return output(jsonify(data))
        else:
            abort(404, description='no playlist detail info')


@playlistAPI.resource('/comments/static')
class PlaylistCommentsStatic(Resource):
    """docstring for PlaylistCommentsStatic"""

    def get(self):
        data = static_playlist_comments
        if data:
            return output(jsonify(data))
        else:
            abort(404, description='no playlist comments info')


@playlistAPI.resource('/comments/<string:playlistId>/page/<int:page>')
class PlaylistCommentsWithoffset(Resource):

    def get(self, playlistId, page):
        data = data_poster.get_playlist_comments_withoffset(playlistId, page)
        if data:
            return output(jsonify(data))
        else:
            abort(404)
