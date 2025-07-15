# Reddit Persona Generator

This project builds rich, human-style personas by scraping a user's public Reddit activity and analyzing their tone, interests, and traits using AI.

---

## 🎯 Objective

Given a Reddit user profile URL, this tool:

1. Scrapes their recent posts and comments  
2. Uses (or mocks) a GPT model to generate a detailed user persona  
3. Outputs the result into a `.txt` file inside the `outputs/` folder  

---

## 🛠 Technologies Used

- **Python 3.10+**
- **PRAW** – Reddit API wrapper  
- **OpenAI** – For persona generation (mocked fallback used if quota exhausted)  
- **python-dotenv** – Loads API credentials securely  

---

##  Project Structure

reddit-persona-generator/
├── reddit_scraper.py # Collects Reddit posts/comments using PRAW
├── persona_builder.py # Builds persona from content (or returns a fallback)
├── main.py # Entry script: ties everything together
├── outputs/ # Contains generated personas
├── .env # Stores API keys (excluded via .gitignore)
├── .gitignore # Excludes secrets and virtual environment
├── requirements.txt # Python dependencies

## ⚙️ How to Run

### 1. Clone the repository


git clone https://github.com/Arjun-56/reddit-persona-generator.git
cd reddit-persona-generator

2. Create virtual environment and install packages
 python -m venv venv
 venv\Scripts\activate
 pip install -r requirements.txt

3. Add your API credentials to .env
 Create a .env file with:
REDDIT_CLIENT_ID=your_id
REDDIT_CLIENT_SECRET=your_secret
REDDIT_USER_AGENT=persona-script by arjun
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxx

⚠️ Note on OpenAI Usage
Due to exceeding OpenAI’s free-tier quota during development, the system currently uses a mock GPT fallback to generate personas.

The code is fully functional and designed for seamless integration with OpenAI’s gpt-3.5-turbo once the quota resets or a new key is applied.

All scraping, formatting, and persona logic remains intact and demonstrates full pipeline readiness.

👤 Author
Arjun Mammula
GitHub: @Arjun-56

📌 Notes
This project was created as part of a Generative AI internship assignment.
All output data is synthetic, used purely to demonstrate the system's capabilities.
.env, venv/, and __pycache__/ are ignored via .gitignore.
