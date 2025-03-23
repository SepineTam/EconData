#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2025 - Present Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : EPS.py

# 如果数据来源于国家统计局，可以把数据放在"data/source.gb2312/"下，后运行EPS_merge函数即可整理

from utils.merge import merge
from utils.convert import convert_encoding

def EPS_merge(name="name"):
    gb2312_dir = "data/source.gb2312/"
    utf8_dir = "data/source.utf8/"
    output_file = f"data/{name}.csv"

    convert_encoding(gb2312_dir, utf8_dir, "gb2312")
    merge(utf8_dir, output_file)
