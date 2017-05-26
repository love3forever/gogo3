#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-25 21:01:45
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from flask import Flask
from resources.playlist_api import playlist_blueprint

app = Flask(__name__)
app.register_blueprint(playlist_blueprint)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=33333)
