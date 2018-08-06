#!/usr/bin/env python3
# coding=utf-8

import sys

# 讨厌的版本差异！ #
if int(sys.version[0]) == 2:
    input=raw_input


msg = input("Please input something:")

box_width = 50
text_width = len(msg)
left_margin = (box_width - text_width) // 2

print('+' + '-'*box_width + '+')
print('|' + ' '*box_width + '|')
print('|' + ' '*left_margin + msg + ' '*left_margin + '|')
print('|' + ' '*box_width + '|')
print('+' + '-'*box_width + '+')
