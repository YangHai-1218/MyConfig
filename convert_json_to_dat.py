#! /usr/local/bin/python3
import json 
import numpy as np
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('source_path', type=str)
    parser.add_argument('target_path', type=str)
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()
    source_path = args.source_path
    target_path = args.target_path

    with open(source_path, 'r') as f:
        data = json.load(f)

    iters, loss = [], []
    for d in data:
        iters.append(d[1]/1000)
        loss.append(d[2]-1)

    iters = np.array(iters).reshape(-1)
    loss = np.array(loss).reshape(-1)

    np.savetxt(target_path, np.stack([iters, loss], axis=-1), fmt=['%.2f','%.5f'])