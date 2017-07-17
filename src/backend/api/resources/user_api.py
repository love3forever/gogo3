#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-25 23:18:11
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from flask.blueprints import Blueprint
from flask_restful import Resource, Api, abort
from flask import jsonify
from dataCollector import data_poster
from common_funcs import output

user_blueprint = Blueprint(__name__, 'user_blueprint')
userAPI = Api(user_blueprint, prefix='/api/v1/user')


@userAPI.resource('/<string:userId>/follows')
class UserFollows(Resource):
    """docstring for UserFollows"""

    def get(self, userId):
        if userId:
            data = data_poster.get_user_follows(userId)
            if data:
                result = {
                    'user': userId,
                    'follows': data,
                    'code': 200
                }
                return output(jsonify(result))
            else:
                abort(404, 'user {} follows nobody'.format(userId))
        else:
            abort(404, 'do request with right user id, \
                current id:{}'.format(userId))


@userAPI.resource('/<string:userId>/fans')
class UserFans(Resource):
    """docstring for UserFans"""

    def get(self, userId):
        if userId:
            data = data_poster.get_user_fans(userId)
            if data:
                result = {
                    'user': userId,
                    'fans': data,
                    'code': 200
                }
                return output(jsonify(result))
            else:
                abort(404, 'user {} has no fans at all'.format(userId))
        else:
            abort(404, 'do request with right user id, \
                current id:{}'.format(userId))


@userAPI.resource('/<string:userId>/playlist')
class UserPlaylist(Resource):
    """docstring for UserPlaylist"""

    def get(self, userId):
        if userId:
            data, creator = data_poster.get_user_playlist(userId)
            if data:
                result = {
                    'user': userId,
                    'nickname': creator,
                    'playlist': data,
                    'code': 200
                }
                return output(jsonify(result))
            else:
                abort(404, 'user {} has no playlist at all'
                      .format(userId))
        else:
            abort(404, 'do request with right user id, \
                current id:{}'.format(userId))


@userAPI.resource('/<string:userId>/detail')
class UserDetail(Resource):
    """docstring for UserDetail"""

    def get(self, userId):
        if userId:
            data = data_poster.get_user_index(userId)
            if data:
                result = {
                    'user': userId,
                    'code': 200,
                    'detail': data
                }
                return output(jsonify(result))
            else:
                abort(404, 'user {} has no detail info at all'.format(userId))
        else:
            abort(404, 'do request with right user id, \
                current id:{}'.format(userId))
