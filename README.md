# Dataset for trace-driven VoD simuation 
In this repo, you can run python script with ffpmeg to segment the videos from real video dataset and log the chunk size.
The chunk size file format is compatible to existing simulation environment such as Pensieve. In this example, we use waterloo dataset with 11 representations. Each video is 10s and we segement it with two 4s chunks.

# Requirements
Python; ffmpeg (with x.264)

## move.py
Move videos with different contents from specified quality level into one folder.
You should modify the "search string" in move.py to select videos of the same quality from the dataset into one folder, which is further used for video segment and chunk size record.\\
e.g. \\
target_string1 = "540x384" \\
target_string2 = "420_750k" \\
destination_folder = ".././video_1"
specifies to move all videos with quality level "540x384" and "750k" into folder ".././video_1"

## chunk.py
Use ffmpeg prompt to segment the videos for a specified quality level and record its size.
You should modify the -vid parameter to specity the video quality level:
e.g.
python chunk.py -vid 1
FFmpeg prompt:
ffmpeg' + ' -ss ' + 0 + ' -to ' + 4 + ' -i '+ video_path + ' -c:v' + ' copy ' + temp_path
-ss is the start time for video segment
-to is the end time
-i is the input video file path
-c:v copy: maintain the original video quality setting
temp_path: path to store the video chunks
