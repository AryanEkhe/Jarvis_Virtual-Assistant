**JARVIS - Voice Controlled Virtual Assistant**
JARVIS is a lightweight, Python-powered voice assistant that listens for commands, fetches real-time updates, plays music, and leverages AI for intelligent web searches—all delivered through voice responses. Built entirely on free-tier APIs and open-source Python libraries.

**Features**
Voice Activation & Interaction: Listens via Google Speech Recognition and responds audibly using text-to-speech.

AI-Powered Web Search: Uses the Google Gemini API to answer complex queries and search for information online.

Real-time News Updates: Fetches and reads aloud the latest news headlines using NewsAPI.

Music Playback: Plays songs stored locally or mapped via configured media URLs.

Hands-Free Control: Operates entirely through spoken commands after a wake-word trigger.

**Tech Stack & Dependencies
Language: Python 3.12.10**


API Services: NewsAPI, Google Gemini API 

**Getting Started**
Prerequisites
Ensure you have Python installed on your system. You will also need free API keys for the following services:

Google Gemini API Key {https://aistudio.google.com}

NewsAPI Key {https://newsapi.org}

Run the assistant:

**Terminal:**
python main.py
Boot Sequence:
JARVIS will initialize with both text and voice confirmation:

"JARVIS is booting up..."

**Wake Word & Voice Commands:
Say "JARVIS" to trigger the listening state, then issue your command:**

Read News: read me the news"

Play Music: play {song name} (What you store with yt music video links in  musicLibrary.py file)"

Web Search: " search for quantum computing" / " tell me about..."

Roadmap / Future Updates
[ ] Online Song Searching: Integrating direct YouTube/online music search via the command interface (standalone script currently built, pending JARVIS integration).

[ ] Expanded smart home or system management commands.

[ ] Custom wake-word engine for offline detection.


**Installation**
Clone the repository:

**Type in terminal: **
git clone https://github.com/your-username/jarvis-virtual-assistant.git

**Install required Dependencies: **
pip install -r requirements.txt

**Environment Setup:**
Insert your API keys into these slots

GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
NEWS_API_KEY = "YOUR_NEWS_API_KEY"


