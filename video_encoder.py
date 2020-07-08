import os
import sys

import argparse
import multiprocessing

import subprocess

def video_necoder(image_dir,img_prefix,fps,encoder_name,output_video):


    rt_v = os.system('ffmpeg -start_number 0 -i {}/{}%4d.png -c:v {} -preset veryslow -r {} -pix_fmt yuv420p {}'.format(image_dir,img_prefix,encoder_name,fps, output_video))
    print(rt_v)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument("--image_dir", type=str)
    parser.add_argument('--img_prefix', type=str)
    parser.add_argument('--output_video', type=str,default='output.mp4')
    parser.add_argument('--fps',type=int,default=30)
    parser.add_argument('--encoder_name',type=str,default='libx264')
    args = parser.parse_args()


    video_necoder(args.image_dir,args.img_prefix,args.fps,args.encoder_name,args.output_video)
    # video_necoder("./tmp","img",30,'libx264',"test.mp4")