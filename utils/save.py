#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2025 - Present Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : save.py

import pandas as pd
import os
from typing import Union

# 默认扩展映射保持不变
_EXTENSION_METHOD_MAP = {
    'csv': 'to_csv',
    'dta': 'to_stata',
    'xlsx': 'to_excel',
    'xls': 'to_excel',
    'parquet': 'to_parquet',
    'json': 'to_json',
    'html': 'to_html',
    'hdf': 'to_hdf',
    'h5': 'to_hdf',
    'feather': 'to_feather',
    'pkl': 'to_pickle',
    'pickle': 'to_pickle',
    'sql': 'to_sql',
    'txt': 'to_csv',
}

# 添加全局默认路径属性
if not hasattr(pd, 'save_path'):
    pd.save_path = "data/"  # 初始化默认路径属性


def _save(
        self,
        name: str,
        path: Union[str, None] = None,  # 修改为None
        extension=None,
        **kwargs
):
    """
    增强版保存方法，支持全局默认路径

    :param name: 基础文件名（不含扩展名）
    :param path: 存储目录（默认使用pd.save_path，最后回退到当前目录）
    :param extension: 文件扩展名或列表
    :param kwargs: 保存参数
    """
    # 确定最终保存路径（优先级：传入参数 > 全局设置 > 当前目录）
    if extension is None:
        extension = ["csv"]

    final_path = path or pd.save_path or "./"

    # 统一处理扩展名类型
    extensions = [extension] if isinstance(extension, str) else extension

    # 自动创建目录
    os.makedirs(final_path, exist_ok=True)

    # 遍历所有扩展格式进行保存
    for ext in extensions:
        method_name = _EXTENSION_METHOD_MAP.get(ext.lower(), f'to_{ext.lower()}')
        if not hasattr(self, method_name):
            raise ValueError(f"Unsupported extension: {ext}")

        filename = f"{name}.{ext}"
        full_path = os.path.join(final_path, filename)
        getattr(self, method_name)(full_path, **kwargs)


# 注册到DataFrame
pd.DataFrame.save = _save
