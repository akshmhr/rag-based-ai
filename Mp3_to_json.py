import whisper
import json
import os
model = whisper.load_model("turbo")

audios = os.listdir("audios")

for audio in audios:
   
    numbers = audio.split("_")[0]
    title = audio.split("_")[1][:-4]
    print(numbers, title)
    result = model.transcribe(audio = f"audios/{audio}")
    chunks = []
    for segment in result["segments"]:
        chunks.append({"number" : numbers, "title" : title, "start" : segment["start"], "end" : segment["end"], "text" : segment["text"]})
    
    chunks_with_metadata = {"chunks": chunks, "text": result["text"]}

    with open(f"jsons/{audio.split(".mp3")[0]}.json", "w") as f:
        json.dump(chunks_with_metadata, f)
    