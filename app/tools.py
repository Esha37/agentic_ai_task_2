import requests
import re

def ask_ollama(prompt):
    """
    Sends a prompt to Gemma through Ollama
    and returns Gemma's answer.
    """

    url = "http://localhost:11434/api/generate"

    data = {
        "model": "gemma3:4b",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data )

    response.raise_for_status()

    result = response.json()

    return result["response"]


def trend_idea_generator(topic, platform, tone):
    """
    Tool 1:
    Generates content ideas for a topic.
    """

    prompt = f"""
You are a social media content strategist.

Generate 5 creative content ideas about:

Topic: {topic}
Platform: {platform}
Tone: {tone}

Make each idea specific and useful.
Return the ideas as a numbered list.
"""

    return ask_ollama(prompt)


def hashtag_generator(topic, platform):
    """
    Tool 2:
    Generates relevant hashtags.
    """

    prompt = f"""
Generate 8 relevant hashtags for this topic:

Topic: {topic}
Platform: {platform}

Return hashtags only.
Do not write explanations.
"""

    return ask_ollama(prompt)


def caption_writer(topic, platform, tone, content_idea):
    """
    Tool 3:
    Writes a social media caption.
    """

    prompt = f"""
Write a ready-to-publish social media caption.

Topic: {topic}
Platform: {platform}
Tone: {tone}
Content idea: {content_idea}

Requirements:
- Start with a strong hook
- Use short paragraphs
- Keep it clear
- End with a question or call to action
"""

    return ask_ollama(prompt)


def reel_script_generator(topic, tone):
    """
    Tool 4:
    Generates a 30 to 60 second reel script.
    """

    prompt = f"""
Create a 30 to 60 second short-video script.

Topic: {topic}
Tone: {tone}

Include:
1. Opening hook
2. Visual suggestion
3. Voiceover
4. Main explanation
5. Closing call to action
"""

    return ask_ollama(prompt)


def content_reviewer(topic, platform, caption):
    """
    Tool 5:
    Reviews the generated caption.
    """

    prompt = f"""
Review this social media content.

Topic: {topic}
Platform: {platform}

Content:
{caption}

Check:
- Is the hook strong?
- Is the content clear?
- Is the tone suitable?
- Is it too long?
- Is the call to action useful?

Give 3 improvement suggestions.
"""

    return ask_ollama(prompt)


from pathlib import Path
from datetime import datetime


def file_saver(topic, platform, content):
    """
    Tool 6:
    Saves the final agent output into a Markdown file.
    """

    # Move from app folder to the main project folder
    project_folder = Path(__file__).resolve().parent.parent

    # Create the saved_results folder if it does not exist
    output_folder = project_folder / "outputs" / "saved_results"
    output_folder.mkdir(parents=True, exist_ok=True)

    # Make a safe file name
    safe_topic = re.sub(
    r"[^a-zA-Z0-9]+",
    "_",
    topic.lower()
).strip("_")

    safe_platform = re.sub(
    r"[^a-zA-Z0-9]+",
    "_",
    platform.lower()
).strip("_")


    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"{safe_topic}_{safe_platform}_{timestamp}.md"

    file_path = output_folder / file_name

    # Write the content into the Markdown file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("# TrendPilot Content Plan\n\n")
        file.write(f"## Topic\n{topic}\n\n")
        file.write(f"## Platform\n{platform}\n\n")
        file.write("## Generated Content\n\n")
        file.write(content)

    return str(file_path)
