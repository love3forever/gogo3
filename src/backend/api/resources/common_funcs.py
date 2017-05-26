#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-25 22:58:14
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
from flask import make_response


def output(data, headers=None):
    resp = make_response(data)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'POST'
    resp.headers[
        'Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    resp.headers['Content-Type'] = 'application/json;charset=UTF-8'
    return resp
