#! /usr/local/bin/python3
import cv2
import numpy as np
import argparse
import os

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('source_path', type=str, )
    parser.add_argument('--scale', default=15, type=float)
    parser.add_argument('--tgt_path', type=str, default=None)
    args = parser.parse_args()
    return args



def convertPNG(args):
    # READ THE DEPTH
    im_depth = cv2.imread(args.source_path)
    #apply colormap on deoth image(image must be converted to 8-bit per pixel first)
    im_color= cv2.applyColorMap(cv2.convertScaleAbs(im_depth,alpha=args.scale),cv2.COLORMAP_JET)
    #convert to mat png
    cv2.imwrite(args.source_path.split('.')[0] + '_rgb.png', im_color)
    # im=Image.fromarray(im_color)
    # #save image
    # im.save(args.source_path.split('.')[0] + '_rgb.png',)


if __name__ == '__main__':
    args = parse_args()
    convertPNG(args)
    # # Load the depth image
    # depth_image = cv2.imread(args.source_path, cv2.IMREAD_ANYDEPTH)

    # # Normalize the depth values to the range [0, 1]
    # normalized_depth = cv2.normalize(depth_image, None, 0, 1, cv2.NORM_MINMAX)

    # # Convert the normalized depth to a 
    # # grayscale image
    # depth_gray = (normalized_depth * 255).astype(np.uint8)

    # # Convert the grayscale image to an RGB image
    # depth_rgb = cv2.cvtColor(depth_gray, cv2.COLOR_GRAY2RGB)

    # # Save the resulting RGB image
    # cv2.imwrite('depth_rgb.png', depth_rgb)
    # if args.tgt_path is None:
    #     cv2.imwrite(args.source_path.split('.')[0] + '_rgb.png', depth_rgb)
    # else:
    #     cv2.imwrite(args.tgt_path, depth_rgb)
