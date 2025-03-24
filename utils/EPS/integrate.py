#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2025 - Present Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : integrate.py

# 整合通过EPS获取的数据集

import pandas as pd
import numpy
import os
from utils.remove import remove_whitespace

def integrate(file_list: list, output_file: str = "data/integrate.csv"):
    all_dfs: list = []
    for file in file_list:
        try:
            df = pd.read_csv(file, encoding="utf-8")
            all_dfs.append(df)
        except Exception as e:
            print(f"读取{file}时出错：{str(e)}")

    if not all_dfs:
        print(f"没有成功读取任何文件或文件路径有误")
        return False

    combined_df = pd.concat(all_dfs, ignore_index=True)
    os.makedirs(os.path.dirname(os.path.abspath(output_file)), exist_ok=True)

    # 移除空格
    combined_df = remove_whitespace(combined_df)

    # 保存拼接后的数据
    combined_df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"结果已保存到: {output_file}")

    return True


