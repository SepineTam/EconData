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

from utils import convert
from utils import remove

def concat_csv_files(input_directory, output_file_path, encoding="gbk", is_save=True):
    """
    将指定目录下的所有CSV文件拼接成一个CSV文件

    参数:
    input_directory (str): 包含CSV文件的目录路径
    output_file_path (str): 输出CSV文件的保存路径

    返回:
    bool: 操作是否成功
    """
    # 检查目录是否存在
    if not os.path.isdir(input_directory):
        print(f"错误: 目录 '{input_directory}' 不存在")
        return False

    # 获取目录中所有的CSV文件
    csv_files = glob.glob(os.path.join(input_directory, "*.csv"))

    if not csv_files:
        print(f"警告: 在 '{input_directory}' 中没有找到CSV文件")
        return False

    print(f"找到 {len(csv_files)} 个CSV文件")

    # 用于存储所有DataFrame的列表
    all_dfs = []

    # 读取每个CSV文件并添加到列表中
    for file in csv_files:
        try:
            df = pd.read_csv(file, encoding=encoding)[:-2]
            all_dfs.append(df)
            print(f"成功读取: {file} (行数: {len(df)})")
        except Exception as e:
            print(f"读取 {file} 时出错: {str(e)}")

    if not all_dfs:
        print("没有成功读取任何CSV文件")
        return False

    # 拼接所有DataFrame
    combined_df = pd.concat(all_dfs, ignore_index=True)
    print(f"拼接完成，总计 {len(combined_df)} 行")

    if is_save:
        # 创建输出文件所需的目录（如果不存在）
        os.makedirs(os.path.dirname(os.path.abspath(output_file_path)), exist_ok=True)

        # 保存拼接后的数据
        combined_df.to_csv(output_file_path, index=False, encoding='utf-8')
        print(f"结果已保存到: {output_file_path}")

    return combined_df


if __name__ == "__main__":
    input_gb2312_path = "data/source.gb2312"
    output_utf8_path = "data/source.utf8"
    source_encoding = "gb2312"

    success, fail = convert.convert_encoding(input_gb2312_path, output_utf8_path, source_encoding)
    print(f"转换完成！成功: {success} 个文件，失败: {fail} 个文件")

    input_dir = "data/source.utf8/"
    output_dir = "data/prov_gdp.csv"
    converted = concat_csv_files(input_dir, output_dir, encoding="utf-8", is_save=False)

    # 移除空格
    converted_rm_white = remove.remove_whitespace(converted)
    print("已移除空格")
    converted_rm_white.to_csv(output_dir, index=False, encoding='utf-8')
    print(f"结果已保存到: {output_dir}")


