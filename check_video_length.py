'''A Python script to get all video files duration, '''
'''from provided directory and all it's subdirtories'''
#!/usr/bin/env python
import os
import sys
import moviepy.editor

def does_dir_exist(dir_name):
    '''Check directory exist or not'''
    if not os.path.isdir(dir_name):
        err_msg = 'Error: Directory, ' + dir_name + ', does not exist'
        print(err_msg)
        return False

    return True

def convert(seconds):
    '''Convert to more readable format'''
    hours = seconds // 3600
    seconds %= 3600
    mins = seconds // 60
    seconds %= 60
    return hours, mins, seconds

def check_video_file_length(file, cnt=0):
    '''Check video file during'''
    cnt_str = ''
    if cnt:
        cnt_str = str(cnt) + ') '
    print(cnt_str + 'Processing ' + file)

    try:
        video = moviepy.editor.VideoFileClip(file)
        # Contains the duration of the video in terms of seconds
        video_duration = int(video.duration)
        video.close()
    except:
        ex = sys.exc_info()[0]
        err_msg = "Error: failed to process %s to write (%s)." % (file, ex)
        print(err_msg)
        sys.exit(1)   
    cnt += 1     

    hrs, mins, secs = convert(video_duration)
    print(str(hrs).zfill(2)+':'+str(mins).zfill(2)+':'+str(secs).zfill(2) + '\n')


def check_all_files(path, extension='.mp4'):
    cnt = 1    
    for root, _, files in os.walk(path):
        for name in files:
            filename = os.path.join(root, name)
            if filename.endswith(extension):
               check_video_file_length(filename, cnt)
               cnt += 1

def run(path):
    if does_dir_exist(path):
        check_all_files(path)

path = './'     
if len(sys.argv) > 1:
    path = sys.argv[1]
    
run(path)
sys.exit(0)
