#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2025 - Present Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : convert.py

import os


def convert_encoding(input_dir, output_dir, input_encoding="gb2312", output_encoding='utf-8', is_detail=True):
    """
    将指定目录下的文件转换为指定编码格式

    参数:
    input_dir (str): 输入目录路径
    output_dir (str): 输出目录路径
    input_encoding (str): 原始文件编码格式
    output_encoding (str, optional): 目标编码格式，默认为utf-8

    返回:
    tuple: (成功转换数量, 失败数量)
    """
    success = 0
    fail = 0

    for root, dirs, files in os.walk(input_dir):
        # 构造相对路径
        relative_path = os.path.relpath(root, input_dir)
        current_output_dir = os.path.join(output_dir, relative_path)

        # 创建输出目录（如果不存在）
        os.makedirs(current_output_dir, exist_ok=True)

        for filename in files:
            # 防止macOS导出拉屎💩`.DS_Store`
            if filename == ".DS_Store":
                continue
            input_file = os.path.join(root, filename)
            output_file = os.path.join(current_output_dir, filename)

            try:
                # 读取原始文件
                with open(input_file, 'r', encoding=input_encoding, errors='strict') as f_in:
                    content = f_in.read()

                # 写入新编码文件
                with open(output_file, 'w', encoding=output_encoding, errors='strict') as f_out:
                    f_out.write(content)

                success += 1
            except UnicodeDecodeError as e:
                print(f"解码失败: {input_file} - 错误: {e}")
                fail += 1
            except UnicodeEncodeError as e:
                print(f"编码失败: {input_file} - 错误: {e}")
                fail += 1
            except Exception as e:
                print(f"处理文件 {input_file} 时发生意外错误: {e}")
                fail += 1

    if is_detail:
        print(f"转换完成！成功: {success} 个文件，失败: {fail} 个文件")

    return success, fail


# 使用示例
if __name__ == "__main__":
    input_path = "../src/省级GDP/data/source.gb2312"
    output_path = "../src/省级GDP/data/source.utf8"
    source_encoding = "gb2312"

    success, fail = convert_encoding(input_path, output_path, source_encoding)
    print(f"转换完成！成功: {success} 个文件，失败: {fail} 个文件")
