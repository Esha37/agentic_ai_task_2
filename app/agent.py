import re

from app.tools import (
    trend_idea_generator,
    hashtag_generator,
    caption_writer,
    reel_script_generator,
    content_reviewer,
    file_saver
)

from app.memory import save_memory


def run_agent(topic, platform, tone):
    """
    Runs the complete TrendPilot agent workflow.
    """

    print("\n[Agent] Understanding the user request...")

    print("\n[Agent] Creating a plan:")
    print("1. Generate content ideas")
    print("2. Select the best idea")
    print("3. Write a caption")
    print("4. Generate hashtags")
    print("5. Create a reel script")
    print("6. Review the content")
    print("7. Save the final result")
    print("8. Store memory")

    # Tool 1: Generate content ideas
    print("\n[Tool Called] Trend Idea Generator")

    ideas = trend_idea_generator(
        topic,
        platform,
        tone
    )

    print("[Agent] Ideas generated successfully.")

    # Select the first useful line as the content idea
        # Select the first numbered idea from Gemma's response
    numbered_ideas = []

    for line in ideas.splitlines():
        clean_line = line.strip()

        if re.match(r"^(\*\*)?\d+[\.\)]", clean_line):
            numbered_ideas.append(clean_line)

    if numbered_ideas:
        selected_idea = numbered_ideas[0]
    else:
        selected_idea = "Create an engaging project story."



    # Tool 2: Write caption
    print("\n[Tool Called] Caption Writer")

    caption = caption_writer(
        topic,
        platform,
        tone,
        selected_idea
    )

    # Tool 3: Generate hashtags
    print("\n[Tool Called] Hashtag Generator")

    hashtags = hashtag_generator(
        topic,
        platform
    )

    # Tool 4: Generate reel script
    print("\n[Tool Called] Reel Script Generator")

    reel_script = reel_script_generator(
        topic,
        tone
    )

    # Tool 5: Review content
    print("\n[Tool Called] Content Reviewer")

    review = content_reviewer(
        topic,
        platform,
        caption
    )

    # Combine all generated content
    final_content = f"""
# TrendPilot Content Plan

## Topic

{topic}

## Platform

{platform}

## Tone

{tone}

## Content Idea

{selected_idea}

## Caption

{caption}

## Hashtags

{hashtags}

## Reel Script

{reel_script}

## Content Review

{review}
"""

    # Tool 6: Save final result
    print("\n[Tool Called] File Saver")

    saved_file = file_saver(
        topic,
        platform,
        final_content
    )

    print(f"[Agent] Final content saved to: {saved_file}")

    # Tool 7: Save memory
    print("\n[Tool Called] Memory Tool")

    memory_file = save_memory(
        topic,
        platform,
        tone,
        saved_file
    )

    print(f"[Agent] Memory saved to: {memory_file}")

    # Return complete result
    final_result = {
        "topic": topic,
        "platform": platform,
        "tone": tone,
        "content_idea": selected_idea,
        "caption": caption,
        "hashtags": hashtags,
        "reel_script": reel_script,
        "review": review,
        "saved_file": saved_file,
        "memory_file": memory_file
    }

    return final_result
