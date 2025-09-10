import os
audios = os.listdir("audios")
for audio in audios:
    print(f"{audio.split(".mp3")[0]}.json")