from tools import trend_idea_generator


topic = "YOLOv8 helmet detection project"
platform = "LinkedIn"
tone = "professional and exciting"

print("Calling Trend Idea Generator...")
print()

result = trend_idea_generator(topic, platform, tone)

print("Generated Ideas:")
print(result)
