import subprocess
import sys, os, shlex

def help():
    print('''
    USAGE:
        python batch_denoisor.py [your_vscript_path] [your_video_source_folder] [preset]

    preset:
    - low
    - medium
    - high
    - extreme
    ''')

def get_videos(path:str) -> list:
    # notice that this function is not recursive
    files = os.listdir(path)
    videos = []
    exts = ('mov', 'MOV', 'mp4', 'MP4')
    for f in files:
        if f.split('.')[-1] in exts:
            videos.append(path+'/'+f)
    return videos

def main(*args, **kwargs):
    if len(args) != 4:
        help()
        return

    vscript_source = args[1]
    video_folder = args[2]
    preset = args[3]

    videos = get_videos(video_folder)
    if videos:
        if not os.path.exists(video_folder+'/'+'clean'):
            os.mkdir(video_folder+'/'+'clean')

    for v in videos:
        print("PROCESSING:", v)
        print("\n\n\n\n\n\n")
        process_video(v, vscript_source, preset)

def process_video(vid_path:str, vs_path:str, preset:str) -> None:
    name, ext = vid_path.split('/')[-1].split('.')
    output_name = '/'.join(vid_path.split('/')[:-1])+"/clean/"+name+"[{}]".format(preset)+"."+ext

    vspipe_cmd = shlex.split("vspipe --y4m --arg \"filename={}\" --arg \"preset={}\" {} -".format(vid_path, preset, vs_path))
    ffmpeg_cmd = [
        "ffmpeg", "-i", "pipe:", "-i", vid_path,
        "-map", "0:v:0", "-map", "1:a:0",
        "-c:v", "libx264", "-crf", "22", 
        output_name
    ]

    p1 = subprocess.Popen(vspipe_cmd, stdout=subprocess.PIPE)
    p2 = subprocess.Popen(ffmpeg_cmd, stdin=p1.stdout, stdout=subprocess.PIPE, universal_newlines=True)

    while True:
        output = p2.stdout.readline()
        print(output.strip())
        # Do something else
        return_code = p2.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
            # Process has finished, read rest of the output 
            for output in p2.stdout.readlines():
                print(output.strip())
            break

if __name__ == '__main__':
    main(*sys.argv)