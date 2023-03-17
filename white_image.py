#! /usr/local/bin/python3
import enum
import cv2
import argparse
import numpy as np
import os
from os import path as osp


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('source_paths', type=str, nargs='+')
    parser.add_argument('-r', type=int, default=128)
    parser.add_argument('-g', type=int, default=128)
    parser.add_argument('-b', type=int, default=128)
    args = parser.parse_args()
    return args

def mkdir_or_exist(dir_name):
    if dir_name == '':
        return
    dir_name = osp.expanduser(dir_name)
    os.makedirs(dir_name, exist_ok=True)



if __name__ == "__main__":
    args = parse_args()
    for source_path in args.source_paths:
        source_image = cv2.imread(source_path)
        mask = (source_image[..., 0] == args.r) & (source_image[..., 1] == args.g)  & (source_image[..., 2] == args.b) 
        source_image[mask] = 255
        cv2.imwrite(source_path.split('.')[0] + '_white.png', source_image)
