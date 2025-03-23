#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2025 - Present Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : remove.py

import pandas as pd


def remove_whitespace(df):
    # 创建副本避免修改原DataFrame
    df = df.copy()

    # 筛选字符串类型的列（包括object和string类型）
    str_cols = df.select_dtypes(include=['object', 'string']).columns

    # 对每个字符串列应用strip
    for col in str_cols:
        df[col] = df[col].str.strip()

    return df
