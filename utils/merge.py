#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2025 - Present Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : merge.py

import os
import pandas as pd
import glob

from utils import remove as rm


def merge(input_dir, output_file, encoding="utf-8", file_type="csv", EPS=True):
    # 检查目录是否存在
    if not os.path.isdir(input_dir):
        print(f"错误: 目录 '{input_dir}' 不存在")
        return False

    csv_files = glob.glob(os.path.join(input_dir, f"*.{file_type}"))
    if not csv_files:
        print(f"警告: 在 '{input_dir}' 中没有找到{file_type.upper()}文件")
        return False

    all_dfs = []
    for file in csv_files:
        try:
            if EPS:
                df = pd.read_csv(file, encoding=encoding)[:-2]
            else:
                df = pd.read_csv(file, encoding=encoding)
            all_dfs.append(df)
        except Exception as e:
            print(f"读取{file}时出错：{str(e)}")

    if not all_dfs:
        print(f"没有成功读取任何{file_type.upper()}文件")
        return False

    combined_df = pd.concat(all_dfs, ignore_index=True)
    print(f"拼接完成，总计 {len(combined_df)} 行")

    # 创建输出文件所需的目录（如果不存在）
    os.makedirs(os.path.dirname(os.path.abspath(output_file)), exist_ok=True)

    # 移除空格
    combined_df = rm.remove_whitespace(combined_df)

    # 保存拼接后的数据
    combined_df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"结果已保存到: {output_file}")

    return combined_df
