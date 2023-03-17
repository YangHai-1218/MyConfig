#! /usr/local/bin/python3
import enum
import cv2
import argparse
import numpy as np
import os
from os import path as osp


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('source_path', type=str)
    parser.add_argument('target_path', type=str)
    parser.add_argument('--column_num', type=int, default=2)
    args = parser.parse_args()
    return args

def mkdir_or_exist(dir_name):
    if dir_name == '':
        return
    dir_name = osp.expanduser(dir_name)
    os.makedirs(dir_name, exist_ok=True)



if __name__ == "__main__":
    args = parse_args()
    source_image = cv2.imread(args.source_path)
    mkdir_or_exist(args.target_path)
    column_images = np.split(source_image, args.column_num, axis=1)
    for j, image in enumerate(column_images):
        cv2.imwrite(f"{args.target_path}/{j}.png", image)



