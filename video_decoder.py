import os
import sys

import argparse
import multiprocessing

import subprocess

def video_decoder(video_file,output_dir,img_pre_fix):

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    rt_v = os.system('ffmpeg -i {} {}/{}%04d.png'.format(video_file,output_dir,img_pre_fix))
    print(rt_v)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument("--video_file", type=str)
    parser.add_argument('--output_dir', type=str)
    parser.add_argument('--img_prefix', type=str,default='img')
    # parser.add_argument('--start_time', type=str,default='00:00')
    # parser.add_argument('--img_pre_fix', type=str,default='img')

    args = parser.parse_args()

    video_decoder(args.video_file,args.output_dir,args.img_prefix)

