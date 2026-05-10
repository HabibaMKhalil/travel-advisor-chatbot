# CSAI 468 - Natural Language Processing Final Project

## Project Overview
This project implements the data collection phase of a Travel Advisor Chatbot.
The chatbot aims to provide users with travel-related information such as
destination descriptions, travel advice, safety tips, and general guidance.

Phase 1 focuses on web scraping, data cleaning, and dataset preparation.

## Data Source
- Wikivoyage (https://en.wikivoyage.org)
- Public, educational use only

## Project Structure
- `scraper/` : Python scripts for data collection
- `data/raw_html/` : Raw downloaded HTML pages
- `data/cleaned_text/` : Cleaned and structured JSON files

## Scraping Approach
Two types of content were collected:
1. Travel tips and general advice
2. Destination pages (cities)

Automatic destination discovery was attempted using heuristic-based crawling.
Due to the heterogeneous structure of Wikivoyage pages, a hybrid approach was
adopted where discovery logic was validated and a curated list of destinations
was used for stable large-scale scraping.

## Technologies Used
- Python 3
- Requests
- BeautifulSoup4

## How to Run
1. Create and activate a virtual environment
2. Install dependencies:
   `pip install requests beautifulsoup4`
3. Run:
   `python scrape_tips.py`
   `python scrape_destinations.py`

## Output
- Raw HTML pages
- Cleaned JSON files ready for NLP processing

## Future Work
Phase 2 will include text preprocessing, intent detection, named entity
recognition, and information retrieval.


# Travel Advisor Chatbot – Phase 2
This phase preprocesses scraped travel content and stores semantic embeddings in a persistent Chroma vector database.

### Steps
1. Clean and normalize text
2. Deduplicate documents
3. Chunk text with overlap
4. Generate embeddings
5. Store vectors in Chroma

### Build Vector Database
python build_vector_db.py
Test Retrieval:
python test_retrieval.py


# Travel Advisor Chatbot – Phase 3

This phase implements a hybrid retrieval pipeline using ChromaDB.
Authoritative sources (e.g., US State Department, WHO) are prioritized.
If no authoritative information is available, the system falls back to general travel data.

The chatbot generates grounded responses using retrieved documents only,
includes citations, and refuses to answer when information is insufficient.

Run Phase 3:
```bash
python -m phase3.main_chat
```

# Travel Advisor Chatbot – Phase 4

A local Retrieval-Augmented Generation (RAG) chatbot for travel advisory questions,
built using Python, Streamlit, and Ollama.

## Features
- Local LLM (no API keys)
- Hybrid retrieval (Phase 3)
- Source-grounded answers
- Chat-style UI
- Privacy-preserving

## Requirements
- Python 3.9+
- Ollama installed
- Model pulled (phi or mistral)

## Setup

1. Start Ollama
2. Pull model:
   ollama pull phi

3. Install dependencies:
   pip install -r requirements.txt

## Run (UI)
streamlit run phase4/streamlit_app.py

## Run (CLI)
python -m phase4.main_app

## Folder Structure
phase4/
├── main_app.py
├── streamlit_app.py
├── rag_pipeline.py
├── llm/
│   └── local_llm.py
