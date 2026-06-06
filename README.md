# 🔬 DeepSage — Your Own AI Research Agent

DeepSage is a multi-agent AI research system built with **LangChain**, **tools** and specialized AI agents that collaborate to perform deep research on any topic.

Instead of relying on a single LLM response, DeepSage orchestrates multiple autonomous agents:

1. **Search Agent** → Finds recent and relevant information.
2. **Reader Agent** → Scrapes and extracts deeper content from selected sources.
3. **Writer Chain** → Synthesizes findings into a structured research report.
4. **Critic Chain** → Reviews, evaluates, and improves the report quality.

The result is a polished research workflow that resembles how a human research team operates.

---

# ✨ Features

* 🔍 Multi-agent research pipeline
* 🌐 Web search integration
* 📄 Automatic content extraction and summarization
* ✍️ AI-generated research reports
* 🧐 Automated report critique and feedback
* 🎨 Premium custom Streamlit UI
* 📥 Download reports as Markdown
* ⚡ Real-time pipeline visualization
* 🧠 Modular LangChain architecture

---

# 🏗️ Architecture

```text
User Query
     │
     ▼
┌─────────────────┐
│ Search Agent    │
│ Find sources    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Reader Agent    │
│ Scrape content  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Writer Chain    │
│ Create report   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Critic Chain    │
│ Review quality  │
└────────┬────────┘
         │
         ▼
   Final Report
```

---

# 📁 Project Structure

```text
DeepSage/
│
├── app.py
├── agents.py
├── pipeline.py
├── tools.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── assets/
│   └── screenshots/
│
└── outputs/
    └── reports/
```

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/ankitaganguly09-hue/DeepSage-YourOwnAIResearchAgent.git
cd DeepSage-YourOwnAIResearchAgent
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Requirements

Example:

```txt
streamlit
langchain
langgraph
langchain-openai
langchain-community
beautifulsoup4
requests
duckduckgo-search
python-dotenv
tiktoken
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root:

```env
MISTRAL_API_KEY=your_api_key_here
```

If using another provider:

```env
ANTHROPIC_API_KEY=your_key
GROQ_API_KEY=your_key
GOOGLE_API_KEY=your_key
```

---

# ⚙️ Agent Design

## Search Agent

Responsibilities:

* Search the web
* Gather recent information
* Collect source references
* Return summarized findings

Example prompt:

```python
Find recent, reliable and detailed information about:
{topic}
```

---

## Reader Agent

Responsibilities:

* Analyze search results
* Select the most relevant URL
* Scrape webpage content
* Extract valuable information

Input:

```text
Search Results
      ↓
Most Relevant Source
      ↓
Detailed Extracted Content
```

---

## Writer Chain

Responsibilities:

* Combine research material
* Organize findings
* Generate a professional report
* Create structured sections

Typical sections:

* Executive Summary
* Background
* Current Developments
* Key Findings
* Future Outlook
* Conclusion

---

## Critic Chain

Responsibilities:

* Evaluate report quality
* Detect missing information
* Score report completeness
* Provide improvement suggestions

Example output:

```text
Quality Score: 8.7/10

Strengths:
- Strong factual coverage
- Clear structure

Weaknesses:
- Limited source diversity
- Missing industry statistics

Recommendations:
- Add more citations
- Expand future outlook
```

---

# ▶️ Running the Application

Start Streamlit:

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

# 📊 Example Workflow

### User Query

```text
Quantum Computing Breakthroughs in 2025
```

### Search Agent

Finds:

* Recent breakthroughs
* Research papers
* Industry announcements

### Reader Agent

Extracts:

* Technical details
* Research insights
* Key findings

### Writer Chain

Produces:

```text
Comprehensive Research Report
```

### Critic Chain

Returns:

```text
Evaluation + Suggestions
```

---

# 🧪 Example Topics

Try:

```text
LLM Agents in 2025

CRISPR Gene Editing

Fusion Energy Progress

Artificial General Intelligence

Climate Engineering

SpaceX Starship Development

Neuromorphic Computing

Quantum Cryptography
```

---

# 📈 Technology Stack

| Layer           | Technology                |
| --------------- | ------------------------- |
| Frontend        | Streamlit                 |
| Orchestration   | LangChain                 |
| Agent Framework | LangGraph (optional)      |
| LLM             | OpenAI / MistralAI / Groq |
| Web Search      | DuckDuckGo / Tavily       |
| Scraping        | BeautifulSoup             |
| Styling         | Custom CSS                |
| Deployment      | Streamlit Cloud / Docker  |

---

# 🐳 Docker Deployment

Create a Dockerfile:

```dockerfile
FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
```

Build:

```bash
docker build -t deepsage .
```

Run:

```bash
docker run -p 8501:8501 deepsage
```

---

# ☁️ Streamlit Cloud Deployment

1. Push repository to GitHub
2. Connect repository to Streamlit Cloud
3. Add secrets:

```toml
OPENAI_API_KEY="your_key"
```

4. Deploy

---

# 🤝 Contributing

Contributions are welcome.

Steps:

```bash
Fork the repository
Create a feature branch
Commit changes
Open a pull request
```

Areas where help is appreciated:

* New agents
* Better scraping
* UI improvements
* Research workflows
* Evaluation systems

---

# 📄 License

MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files to deal in the Software without restriction.

---

# 👩‍💻 Author

**Ankita Ganguly**

DeepSage — Multi-Agent AI Research System

Built with ❤️ using Streamlit, LangChain, and modern AI agent architectures.

---

## Star the Project ⭐

If you found DeepSage useful, consider giving the repository a star and sharing it with the community.
