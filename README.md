# 🎯 Deep Learning Course RAG System

This project builds a **Retrieval-Augmented Generation (RAG) pipeline** on a YouTube Deep Learning course, enabling intelligent **question answering** from lecture videos.

---

## 📌 Features
- ✅ Downloaded & processed **18 YouTube course videos**
- ✅ Converted video → audio (MP4 → MP3) using **FFmpeg**
- ✅ Transcribed + translated audio using **OpenAI Whisper**
- ✅ Chunked transcripts into **time-aligned JSON files**
- ✅ Generated embeddings with **bge-m3 model (via Ollama)**
- ✅ Stored embeddings & metadata in a **Pandas DataFrame**
- ✅ Indexed with cosine similarity (**sklearn**) for retrieval
- ✅ Used **OpenRouter API (`openai/gpt-oss-20b:free`)** for answer generation
- ✅ Supports semantic search & QA across all videos

---

## 🛠️ Tech Stack
- **Python**
- **FFmpeg** – audio conversion
- **OpenAI Whisper** – transcription & translation
- **Ollama (bge-m3)** – embedding generation
- **Pandas & Joblib** – data handling & persistence
- **scikit-learn** – cosine similarity search
- **OpenRouter API** – LLM for QA

---

## 🚀 Workflow
1. **Data Prep**  
   - Downloaded 18 Deep Learning YouTube videos  
   - Converted MP4 → MP3 with FFmpeg  

2. **Transcription & Translation**  
   - Processed with Whisper (English text)  
   - Automated batching with Python (`os`, `subprocess`)  

3. **Chunking**  
   - Split into time-stamped JSON chunks:  
     ```json
     {
       "number": "1",
       "title": "Introduction",
       "start": 0.0,
       "end": 4.32,
       "text": "With this video I am beginning a deep learning tutorial..."
     }
     ```

4. **Embedding & Indexing**  
   - Generated embeddings with bge-m3 via Ollama  
   - Stored in DataFrame + dumped with Joblib  

5. **Query Handling**  
   - Embedded user query  
   - Retrieved **top 50 similar chunks** (cosine similarity)  

6. **Answer Generation**  
   - Sent query + context to `openai/gpt-oss-20b:free` via OpenRouter  
   - Model produces context-aware response  

---

## ▶️ Usage
Clone the repo:
```bash
git clone https://github.com/akshmhr/rag-based-ai.git
cd rag-based-ai
```
Install dependencies:
```bash
pip install -r requirements.txt
```
## 🙌 Acknowledgements
- OpenAI Whisper
- Ollama
- OpenRouter
- bge-m3 model