# 🕵️ Local AI OSINT Auditor

**A 100% Private OSINT Framework.** No API keys, no cloud, no telemetry. All analysis is performed locally using open-weight AI models via Ollama.

## 💡 The Problem
Traditional OSINT tools are either closed-source, cloud-based, or require expensive API keys. Furthermore, analyzing raw OSINT data requires manual effort and leaks the target's data to third-party servers.

## 🚀 The Solution
This framework combines traditional OSINT data collection modules with a **local Large Language Model (LLM)**. It gathers raw data (Instagram profiles, followers, bios) and uses an open-weight AI model to generate a clean, human-readable privacy exposure report.

## 🏗️ Architecture
- **`modules/osint_tool.py`**: OSINT collector for Instagram public data (Your original logic).
- **`ai/ollama_client.py`**: Local AI integration layer (Ollama + Gemma 3 4B).
- **`main.py`**: CLI Orchestrator that ties the modules and AI together.

## 📦 Installation
1. **Install Ollama** and pull the model:
   ```bash
   ollama pull gemma3:4b