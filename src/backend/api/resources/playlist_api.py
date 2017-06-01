#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-25 20:59:55
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
from flask.blueprints import Blueprint
from flask_restful import Resource, Api, abort
from flask import jsonify
from dataCollector import data_poster
from common_funcs import output

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
