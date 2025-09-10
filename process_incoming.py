from dotenv import load_dotenv
import os
import json
from urllib import response
import numpy as np
import pandas as pd
import requests
import joblib
from sklearn.metrics.pairwise import cosine_similarity

def create_embedding(text_list):
    r = requests.post("http://localhost:11434/api/embed", json={
        "model" : "bge-m3",
        "input": text_list
    })
    embedding = r.json()['embeddings']
    return embedding



OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
load_dotenv()
API_KEY = os.getenv("API_KEY")


def ask_openrouter(model_slug, system_instruction, incoming_query, related_chunks):
    payload = {
        "model": model_slug,
        "messages": [
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": json.dumps({
                "chunks": related_chunks,
                "question": incoming_query
            })}
        ],
        "max_tokens": 500,
        "temperature": 0.0
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    r = requests.post(OPENROUTER_URL, headers=headers, json=payload)
    r.raise_for_status()
    data = r.json()
    # safe extraction
    assistant_text = data.get("choices", [{}])[0].get("message", {}).get("content", "")
    return assistant_text





df = joblib.load('embeddings.joblib')
incoming_query = input("Ask a Question: ")
question_enbedding = create_embedding([incoming_query])[0]
# print(question_enbedding)

# Find similarities of question embedding with other embeddins
similarities = cosine_similarity(np.vstack(df['embedding']), [question_enbedding]).flatten()
# print(similarities)
top_results = 10
max_indx = similarities.argsort()[::-1][0:top_results]
max_indx_with_extra_chunks = []
for i in max_indx:
    for j in range(5):
        max_indx_with_extra_chunks.append(i+j)
# print(max_indx)
new_df = df.loc[max_indx_with_extra_chunks]
# print(new_df[["title", "number", "text"]])





system_instruction = (
'''
You are an assistant for a deep learning course. 
The user will ask questions about the course, and you will be given relevant transcript excerpts from the videos. 
Answer naturally, as if you are guiding a student. 
Always tell the user where to find the answer by mentioning:
- the video title, 
- the video number, 
- If needed > the start and end times in seconds (and optionally mm:ss).
Do not mention transcripts, chunks, or technical details. 
If the user’s question cannot be answered from the provided excerpts, reply: 
I can only answer questions based on the course material.
'''
)
model_slug = "openai/gpt-oss-20b:free"

related_chunks = new_df[["title", "number", "start", "end", "text"]].to_json(orient= "records")
model_response = ask_openrouter(model_slug, system_instruction, incoming_query, related_chunks)

with open("incoming_query.txt", "w") as f:
    f.write(incoming_query)

with open("model_response.txt", "w") as f:
    f.write(model_response)