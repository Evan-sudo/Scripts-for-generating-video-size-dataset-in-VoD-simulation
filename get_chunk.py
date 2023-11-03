import os
import subprocess
from pathlib import Path
import argparse


parser = argparse.ArgumentParser(description='Process video files.')

# Quality index of the video u wanna process 
parser.add_argument('-vid', type=str, default = 1, help='Video quality (i = 1-6), from low to high)')
args = parser.parse_args()
video_name = args.vid
video_folder = f'.././video_{video_name}'
temp_folder = f'.././temp'
size_file = f'video_size_{video_name}.txt'

# Create the temp folder
if not os.path.exists(temp_folder):
    os.makedirs(temp_folder)

# Create video file list
video_files = os.listdir(video_folder)
video_files_without_extension = []

for video_file in video_files:
    if video_file.endswith('.mp4'):
        video_path = os.path.join(video_folder, video_file)
        
        # 获取文件名（去掉拓展名）
        file_name_without_extension = os.path.splitext(video_file)[0]
        
        # 添加到列表
        video_files_without_extension.append(file_name_without_extension)


# Sort the video list in ascending order
video_files = sorted(video_files_without_extension, key=lambda x: int(x.split('_')[4]))
# video_files = sorted(video_files, key=lambda x: int((x.split('_')[4]).split('.')[0]))
print(video_files)
with open(size_file, 'w') as f:
    for video_file in video_files:
        video_path = os.path.join(video_folder, video_file) + '.mp4'

        # Use FFMpeg to segment the video
        for i in range(2):
            temp_filename = f'{i+1}_temp.mp4'
            temp_path = os.path.join(temp_folder, temp_filename)
            command = 'ffmpeg' + ' -ss ' + str(i*4)+ ' -to ' + str((i+1)*4) + ' -i '+ video_path + ' -c:v' + ' copy ' + temp_path
            subprocess.call(command,shell=True)
            # Get chunk size
            size = os.path.getsize(temp_path)
            print(size)
            f.write(f'{size}\n')

            # Delete Temp
            os.remove(temp_path)

# Remove Temp
for file in os.listdir(temp_folder):
    file_path = os.path.join(temp_folder, file)
    os.remove(file_path)
os.rmdir(temp_folder)

print("Chunk size stored!")
