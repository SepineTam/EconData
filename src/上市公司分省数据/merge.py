#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2025 - Present Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : merge.py

from utils.merge import merge
from utils.convert import convert_encoding

def main():
    gb2312_dir = "data/source.gb2312/"
    utf8_dir = "data/source.utf8/"
    output_file = "data/comp.csv"

    convert_encoding(gb2312_dir, utf8_dir, "gb2312")
    merge(utf8_dir, output_file)


if __name__ == "__main__":
    main()
