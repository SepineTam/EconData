#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2025 - Present Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : info.py

import os

# 项目根目录
HOME_DIR = os.path.dirname(os.path.abspath(__file__))

# 都有什么数据
SRC_CONTENT = []
with os.scandir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "src")) as entries:
    for entry in entries:
        if entry.is_dir():
            SRC_CONTENT.append(entry.name)

# 其他

