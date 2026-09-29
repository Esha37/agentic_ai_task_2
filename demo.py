from app.agent import run_agent


def main():
    print("=" * 60)
    print("TrendPilot - Local Agentic AI Content Assistant")
    print("=" * 60)

    topic = input("\nEnter your topic: ")

    platform = input(
        "Choose platform "
        "(LinkedIn/Instagram/YouTube Shorts/X): "
    )

    tone = input(
        "Choose tone "
        "(professional/funny/exciting): "
    )

    output_type = input(
        "Choose output type "
        "(post/reel script/both): "
    )

    print("\nStarting the Agentic AI workflow...\n")

    result = run_agent(
        topic,
        platform,
        tone
    )

    print("\n" + "=" * 60)
    print("FINAL CONTENT PLAN")
    print("=" * 60)

    print("\nTopic:")
    print(result["topic"])

    print("\nPlatform:")
    print(result["platform"])

    print("\nContent Idea:")
    print(result["content_idea"])

    print("\nCaption:")
    print(result["caption"])

    print("\nHashtags:")
    print(result["hashtags"])

    print("\nReel Script:")
    print(result["reel_script"])

    print("\nReview:")
    print(result["review"])

    print("\nSaved File:")
    print(result["saved_file"])

    print("\nMemory File:")
    print(result["memory_file"])


if __name__ == "__main__":
    main()
