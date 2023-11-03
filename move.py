import os
import shutil

# 源文件夹，包含多个子文件夹
source_folder = ".././videos_representations"
 

# 目标文件夹，用于存储包含特定字符串的视频文件
destination_folder = ".././video_1"

if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)

# 要查找的特定字符串
target_string1 = "540x384"
target_string2 = "420_750k"
  
idx = 0

# 遍历源文件夹中的子文件夹
for root, dirs, files in os.walk(source_folder):
    for dir in dirs:
        folder_path = os.path.join(root, dir)
        for file in os.listdir(folder_path):
            #print(file)
            if file.endswith(".mp4") and target_string1 and target_string2 in file:
                print(1)
                target_filename, file_extension = os.path.splitext(file)
                idx += 1
                new_filename = f"{target_filename}_{idx}{file_extension}"
                source_file_path = os.path.join(folder_path, file)
                destination_file_path = os.path.join(destination_folder, new_filename)

                # 复制包含特定字符串的视频文件到目标文件夹
                shutil.copy2(source_file_path, destination_file_path)

print("视频文件已复制到目标文件夹。")
