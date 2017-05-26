#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-25 20:59:55
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
from flask.blueprints import Blueprint
from flask_restful import Resource, Api, abort
from flask import make_response, jsonify
from dataCollector import data_poster

playlist_blueprint = Blueprint(__name__, 'playlist')
playlistAPI = Api(playlist_blueprint)


def output(data, headers=None):
    resp = make_response(data)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'POST'
    resp.headers[
        'Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    resp.headers['Content-Type'] = 'application/json;charset=UTF-8'
    return resp


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


playlistAPI.add_resource(
    PlaylistDetail, '/api/v1/playlist/detail/<string:playlistId>',
    endpoint='PlaylistDetail')


playlistAPI.add_resource(
    PlaylistComments, '/api/v1/playlist/comments/<string:playlistId>',
    endpoint='PlaylistComments')
