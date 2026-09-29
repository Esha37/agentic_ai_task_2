import json
from pathlib import Path
from datetime import datetime


def save_memory(topic, platform, tone, saved_file):
    """
    Saves information about the current agent run.
    """

    project_folder = Path(__file__).resolve().parent.parent

    memory_file = project_folder / "outputs" / "memory.json"

    memory_file.parent.mkdir(parents=True, exist_ok=True)

    new_record = {
        "topic": topic,
        "platform": platform,
        "tone": tone,
        "saved_file": saved_file,
        "created_at": datetime.now().isoformat()
    }

    if memory_file.exists():
        with open(memory_file, "r", encoding="utf-8") as file:
            memory_data = json.load(file)
    else:
        memory_data = []

    memory_data.append(new_record)

    with open(memory_file, "w", encoding="utf-8") as file:
        json.dump(memory_data, file, indent=4)

    return str(memory_file)


def load_memory():
    """
    Loads previous agent runs.
    """

    project_folder = Path(__file__).resolve().parent.parent

    memory_file = project_folder / "outputs" / "memory.json"

    if not memory_file.exists():
        return []

    with open(memory_file, "r", encoding="utf-8") as file:
        return json.load(file)
