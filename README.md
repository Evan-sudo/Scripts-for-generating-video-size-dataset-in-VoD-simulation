# Dataset for trace-driven VoD simuation 
In this repo, you can run python script with ffpmeg to segment the videos from real video dataset and log the chunk size.
The chunk size file format is compatible to existing simulation environment such as Pensieve. In this example, we use waterloo dataset with 11 representations. Each video is 10s and we segement it with two 4s chunks.

# Requirements
Python; ffmpeg

## move.py
Move videos with different contents from specified quality level into one folder.

## chunk.py
Use ffmpeg prompt to segment the videos for a specified quality level and record its size.
