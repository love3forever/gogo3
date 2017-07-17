#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-17 15:50:41
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from fabric.api import *
from fabric.contrib.console import confirm


def run_test():
    with settings(warn_only=True):
        result = local('python tester.py', capture=True)
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")


def commit():
    local('git add -A && git commit')


def push():
    local('git push origin master && git push tx master')


def pre_deployed():
    run_test()
    commit()
    push()
