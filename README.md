# JARVIS - Voice Controlled Virtual Assistant

Welcome to **JARVIS**! A lightweight, Python-powered voice assistant that listens for commands, fetches real-time updates, plays music, and leverages AI for intelligent web searches—all delivered through voice responses. Built entirely on free-tier APIs and open-source Python libraries.
---
## Table of Contents

* [Features](#features)
* [Tech Stack & Dependencies](#tech-stack--dependencies)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Environment Setup](#environment-setup)
* [Usage](#usage)
* [Roadmap / Future Updates](#roadmap--future-updates)

---
## Features

* **Voice Activation & Interaction**: Listens via Google Speech Recognition and responds audibly using text-to-speech.
* **AI-Powered Web Search**: Uses the Google Gemini API to answer complex queries and search for information online.
* **Real-time News Updates**: Fetches and reads aloud the latest news headlines using NewsAPI.
* **Music Playback**: Plays songs stored locally or mapped via configured media URLs in `musicLibrary.py`.
* **Hands-Free Control**: Operates entirely through spoken commands after a wake-word trigger.

---

## Tech Stack & Dependencies

* **Language**: Python 3.12.10
* **API Services**: [NewsAPI](https://newsapi.org), [Google Gemini API](https://aistudio.google.com)

---

## Getting Started

### Prerequisites

Ensure you have Python installed on your system. You will also need free API keys for the following services:
* [Google Gemini API Key](https://aistudio.google.com)
* [NewsAPI Key](https://newsapi.org)

### Installation

1. **Clone the repository:**
   `git clone https://github.com/your-username/jarvis-virtual-assistant.git`

2. **Navigate into the project directory:**
   `cd jarvis-virtual-assistant`

3. **Install required dependencies:**
   `pip install -r requirements.txt`

### Environment Setup

Insert your API keys into these slots inside your project file:

* `GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"`
* `NEWS_API_KEY = "YOUR_NEWS_API_KEY"`

---

## Usage

1. **Run the assistant:**
   `python main.py`

2. **Boot Sequence:**  
   JARVIS will initialize with both text and voice confirmation:
   > *"JARVIS is booting up..."*

3. **Wake Word & Voice Commands:**  
   Say **"JARVIS"** to trigger the listening state, then issue your command:
   * **Read News**: *"read me the news"*
   * **Play Music**: *"play {song name}"* (Plays YouTube music video links stored in `musicLibrary.py`)
   * **Web Search**: *"search for quantum computing"* / *"tell me about..."*

---

## Roadmap / Future Updates

* [ ] **Online Song Searching**: Integrating direct YouTube/online music search via the command interface (standalone script currently built, pending JARVIS integration).
* [ ] Expanded smart home or system management commands.
* [ ] Custom wake-word engine for offline detection.
