# Convert videos to mp3
import os
import subprocess

files = [f for f in os.listdir("videos") if not f.startswith('.')]
for file in files:
    tutorial_number = file.split("_")[0]
    file_name = file.split("_")[1].split(" | ")[0]
    print(tutorial_number, file_name)
    subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{tutorial_number}_{file_name}.mp3"])