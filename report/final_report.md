# TrendPilot — Local Agentic AI Assistant Using Ollama

## 1. Project Overview

TrendPilot is a local Agentic AI assistant that converts a project topic into a complete social-media content plan.

The user provides a topic, platform, tone, and output type. The agent then creates a plan, calls multiple tools, reviews the generated content, saves it as a Markdown file, and stores information about the run in memory.

The project uses Ollama and the Gemma 3:4B local language model.

## 2. Problem Statement

Creating social-media content for technical projects can require many separate tasks:

- Finding a content idea
- Writing a caption
- Creating hashtags
- Writing a short-video script
- Reviewing the content
- Saving the final result

TrendPilot combines these tasks into one automated Agentic AI workflow.

## 3. Tools and Technologies Used

- Python
- Ollama
- Gemma 3:4B
- Requests library
- JSON memory
- Markdown file saving
- Visual Studio Code
- Windows 11
- GitHub or Google Drive for submission

## 4. Tools Implemented

### Trend Idea Generator

Generates creative content ideas based on the topic, platform, and tone.

### Caption Writer

Creates a ready-to-publish social-media caption.

### Hashtag Generator

Generates relevant hashtags for the selected topic and platform.

### Reel Script Generator

Creates a 30–60 second video script with a hook, visuals, voiceover, and closing.

### Content Reviewer

Reviews the generated content and suggests improvements.

### File Saver

Saves the final content plan as a Markdown file.

### Memory Tool

Stores the topic, platform, tone, saved file path, and creation time in `outputs/memory.json`.

## 5. Agent Workflow

The workflow is:

```text
User input
↓
Agent understands the request
↓
Agent creates a plan
↓
Trend Idea Generator
↓
Caption Writer
↓
Hashtag Generator
↓
Reel Script Generator
↓
Content Reviewer
↓
File Saver
↓
Memory Tool
↓
Final output
```

```markdown
## 6. Example Input

Topic: YOLOv8 helmet detection project

Platform: LinkedIn

Tone: Professional and exciting

Output type: Post and reel script

## 7. Example Output

The agent generates:

- Content idea
- Caption
- Hashtags
- Reel script
- Review comments
- Saved file path
- Memory file path

## 8. Demo

The CLI demo is started with:

python demo.py

The demo asks the user for:

- Topic
- Platform
- Tone
- Output type

Screenshots are available in the screenshots folder.

## 9. Testing

The agent was tested on 10 different inputs:

1. YOLOv8 helmet detection
2. AI internship experience
3. Python learning journey
4. Machine learning project
5. Data annotation struggles
6. Model failed in production
7. Final year project
8. Computer vision project
9. Debugging FastAPI
10. Open-source contribution

All 10 test cases passed successfully after fixing the Windows filename issue.

The test report is available at:

tests/test_results.md

## 10. Error Analysis

The agent was reviewed for weak or failed outputs.

Identified issues included:

- Unsafe characters in Windows filenames
- Incorrect selection of the first content idea
- Unsupported or invented project metrics
- Extra text in reel scripts
- Broad or irrelevant hashtags

Fixes included:

- Filename sanitization
- Numbered-idea extraction
- Metric validation instructions
- Structured reel-script prompts
- Platform-specific hashtag instructions

Detailed analysis is available in:

report/error_analysis.md

## 11. What I Learned

- How to run a local LLM with Ollama
- How to connect Python with Gemma
- The difference between a chatbot and an AI agent
- How to create and use agent tools
- How to design a multi-step workflow
- How to save outputs and memory
- How to test and improve an AI application

## 12. Future Improvements

- Add a Streamlit interface
- Replace JSON memory with SQLite
- Add web trend search
- Add a user feedback loop
- Add PDF export
- Add separate planner, writer, reviewer, and hashtag agents
- Add project README generation
- Add voice input

## 13. Conclusion

TrendPilot demonstrates that Agentic AI is not only about generating text. It is about understanding a goal, planning steps, using tools, reviewing results, saving outputs, and remembering useful information.

The project successfully uses Ollama and Gemma 3:4B to create a complete local Agentic AI workflow.
