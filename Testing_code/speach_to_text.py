import whisper
import json

model = whisper.load_model("turbo")
audio = whisper.load_audio("audios/1_Introduction.mp3")
audio = whisper.pad_or_trim(audio)

result = model.transcribe(audio)
# print(result["segments"])
chunks = []
for segment in result["segments"]:
    chunks.append({"start" : segment["start"], "end" : segment["end"], "text" : segment["text"]})
print(chunks)

with open("output.json", "w") as f:
    json.dump(chunks, f)