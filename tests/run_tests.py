import sys
from pathlib import Path

# Main project folder ko Python path mein add karna
project_folder = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_folder))

from app.agent import run_agent


test_cases = [
    ("YOLOv8 helmet detection", "LinkedIn", "Professional"),
    ("AI internship experience", "LinkedIn", "Motivational"),
    ("Python learning journey", "Instagram", "Funny"),
    ("Machine learning project", "X/Twitter", "Short and catchy"),
    ("Data annotation struggles", "LinkedIn", "Humorous"),
    ("Model failed in production", "Instagram", "Meme style"),
    ("Final year project", "LinkedIn", "Professional"),
    ("Computer vision project", "YouTube Shorts", "Exciting"),
    ("Debugging FastAPI", "X/Twitter", "Funny"),
    ("Open-source contribution", "LinkedIn", "Inspirational"),
]


results = []

for number, (topic, platform, tone) in enumerate(test_cases, start=1):
    print("\n" + "=" * 60)
    print(f"RUNNING TEST CASE {number}/10")
    print(f"Topic: {topic}")
    print(f"Platform: {platform}")
    print(f"Tone: {tone}")
    print("=" * 60)

    try:
        result = run_agent(
            topic=topic,
            platform=platform,
            tone=tone
        )

        results.append({
            "number": number,
            "topic": topic,
            "platform": platform,
            "status": "PASS",
            "saved_file": result["saved_file"]
        })

        print(f"TEST {number}: PASS")
        print(f"Saved file: {result['saved_file']}")

    except Exception as error:
        results.append({
            "number": number,
            "topic": topic,
            "platform": platform,
            "status": "FAIL",
            "saved_file": str(error)
        })

        print(f"TEST {number}: FAIL")
        print(f"Error: {error}")


report_file = project_folder / "tests" / "test_results.md"

with open(report_file, "w", encoding="utf-8") as file:
    file.write("# TrendPilot Test Results\n\n")
    file.write("| Test | Topic | Platform | Status | Saved File |\n")
    file.write("|---:|---|---|---|---|\n")

    for result in results:
        file.write(
            f"| {result['number']} | "
            f"{result['topic']} | "
            f"{result['platform']} | "
            f"{result['status']} | "
            f"{result['saved_file']} |\n"
        )

print("\nAll tests completed.")
print(f"Report saved at: {report_file}")
