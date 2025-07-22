import openai
import os
import json

# ==== CONFIGURATION ====

# Set your OpenAI API key here, or via environment variable
openai.api_key = os.getenv("OPENAI_API_KEY") or "your-api-key-here"

# === STYLES ===
STYLE_PROMPTS = {
    "hemingway": "Write in the style of Ernest Hemingway. Use short, direct, and emotional sentences. Be minimal and impactful.",
    "austen": "Write in the witty and elegant style of Jane Austen. Use 19th-century English and refined phrasing.",
    "tolkien": "Narrate the day's events as an epic tale in the style of J.R.R. Tolkien. Use poetic, noble, and fantastical language."
}

# === EXAMPLE INPUT DATA ===

example_calendar = [
    { "time": "09:00", "event": "Team standup" },
    { "time": "11:30", "event": "Client meeting" },
    { "time": "14:00", "event": "Gym session" },
    { "time": "19:00", "event": "Dinner with Emma" }
]

example_notes = """
Felt anxious in the morning. The client meeting was tense but productive. 
Had dinner with Emma, talked about old times. Laughed a lot.
"""

# === BUILD PROMPT ===

def build_prompt(calendar_data, notes_text, style_name):
    style_prompt = STYLE_PROMPTS.get(style_name.lower(), STYLE_PROMPTS["hemingway"])
    event_text = "\n".join([f"{e['time']} — {e['event']}" for e in calendar_data])

    prompt = f"""
{style_prompt}

Here are today's events:
{event_text}

Personal notes:
{notes_text.strip()}

Write a diary entry for today.
"""
    return prompt.strip()

# === GENERATE DIARY ===

def generate_diary_entry(calendar_data, notes_text, style):
    prompt = build_prompt(calendar_data, notes_text, style)

    print("\n⏳ Generating your diary entry with OpenAI...\n")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8
        )
        return response.choices[0].message['content'].strip()

    except Exception as e:
        return f"❌ Error: {e}"

# === MAIN FUNCTION ===

def main():
    print("Welcome to AI Life Scribe 📝")
    print("Choose a writing style: hemingway / austen / tolkien")
    style = input("Style: ").strip().lower()

    if style not in STYLE_PROMPTS:
        print("⚠️ Unknown style. Using 'hemingway' by default.")
        style = "hemingway"

    diary = generate_diary_entry(example_calendar, example_notes, style)

    print("\n📖 Your AI-generated diary entry:\n")
    print(diary)

# === RUN ===

if __name__ == "__main__":
    main()
