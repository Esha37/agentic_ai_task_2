from app.agent import run_agent


topic = "YOLOv8 helmet detection project"
platform = "LinkedIn"
tone = "professional and exciting"


result = run_agent(
    topic,
    platform,
    tone
)


print("\n")
print("=" * 60)
print("FINAL AGENT OUTPUT")
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
