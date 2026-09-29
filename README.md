# TrendPilot — Local Agentic AI Assistant

TrendPilot is a local Agentic AI assistant built using Python, Ollama, and Gemma 3:4B.

It converts a project topic into a complete social-media content plan.

## Features

- Generates content ideas
- Writes captions
- Generates hashtags
- Creates reel scripts
- Reviews generated content
- Saves results as Markdown files
- Stores memory in JSON
- Uses a multi-step agent workflow

## Technologies

- Python
- Ollama
- Gemma 3:4B
- Requests
- JSON
- Markdown
- Visual Studio Code

## Agent Tools

1. Trend Idea Generator
2. Caption Writer
3. Hashtag Generator
4. Reel Script Generator
5. Content Reviewer
6. File Saver
7. Memory Tool

## Project Workflow

```text
User input
↓
Agent creates a plan
↓
Agent calls multiple tools
↓
Content is generated
↓
Content is reviewed
↓
Result is saved
↓
Memory is stored
↓
Final output is shown
```
## Setup

First, install Ollama and download Gemma:

```powershell
ollama pull gemma3:4b
```

Create and activate the virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install project dependencies:

```powershell
pip install -r requirements.txt
```

## Run the Demo

From the main project folder, run:

```powershell
python demo.py
```

## Run the Tests

```powershell
python .\tests\run_tests.py
```

The project was tested on 10 different inputs, and all 10 tests passed.

## Output Locations

Generated Markdown files are saved in:

```text
outputs\saved_results
```

Memory is saved in:

```text
outputs\memory.json
```

Test results are saved in:

```text
tests\test_results.md
```

Error analysis is saved in:

```text
report\error_analysis.md
```

Screenshots are saved in:

```text
screenshots
```

## Future Improvements

- Add a Streamlit web interface
- Replace JSON memory with SQLite
- Add web trend search
- Add a PDF export option
- Add voice input
- Add a user feedback loop
- Add planner, writer, reviewer, and hashtag agents
- Add GitHub README generation

## Conclusion

TrendPilot demonstrates how Agentic AI can plan a task, use multiple tools, review generated content, save results, and remember previous runs using a local Ollama model.
