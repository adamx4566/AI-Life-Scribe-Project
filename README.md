---

# AI Life Scribe

Final project for the Building AI course

## Summary

AI Life Scribe is a personal AI assistant that transforms your daily digital activity—calendar events, messages, locations, and notes—into beautifully written diary entries in the style of your choice, such as Tolkien, Bukowski, or Jane Austen.

## Background

Many people want to reflect on their lives or keep a diary but find it hard to stay consistent, write engagingly, or simply find the time.

* Keeping a daily journal is often time-consuming and difficult to maintain
* People struggle to describe their lives in a meaningful or artistic way
* Memory fades quickly without personal records of our daily lives
* There's a growing interest in using AI for self-reflection and life-logging

This project was inspired by the idea that our lives, however mundane they seem, deserve storytelling. Using AI to narrate life creatively brings emotional and artistic value to everyday moments.

## How is it used?

The user connects their calendar, note-taking app, and optionally shares messages, locations, and to-do lists. At the end of each day, the AI processes these inputs and creates a personalized diary entry in literary or cinematic style.

Use cases:

* Daily self-reflection
* Personal storytelling
* Creating a memoir or life archive
* Mental health journaling
* Artists and writers collecting inspiration

<img src="[https://upload.wikimedia.org/wikipedia/commons/f/f4/Diary_with_feather_pen.jpg](https://images.stockcake.com/public/c/1/7/c17400a1-6be5-49de-af81-70e091460abb/vintage-writing-experience-stockcake.jpg)" width="400">

Sample styles:

* 📜 Jane Austen
* 🧙 Tolkien
* 🥃 Charles Bukowski
* 🎥 Wes Anderson

Example entry:

```
Tuesday, July 22nd, 2025 — in the style of Ernest Hemingway

The sun rose late, and I had little sleep. There was a meeting at 10. It was not good, but it was honest. At lunch, I walked down by the canal. The sky was grey like ash. I wrote two things I did not hate.
```

## Data sources and AI methods

The data is collected from:

* Google Calendar API
* Apple/Google Notes (with user permission)
* Messaging metadata (optionally)
* Location history (optional)

AI techniques used:

* GPT-based natural language generation (OpenAI, LLaMA)
* Style transfer via prompt engineering + fine-tuned models
* Named entity recognition and context modeling
* Sentiment detection and temporal summarization

| Source        | Purpose                      |
| ------------- | ---------------------------- |
| Calendar API  | Detect events, mood, context |
| Notes         | Personal thoughts            |
| Location Data | Add realism and movement     |
| Style Prompt  | Transform into chosen voice  |

## Challenges

* Privacy concerns: Handling personal data requires secure, encrypted processing and storage.
* Hallucination: AI may fabricate events if not clearly guided by input.
* Style limitations: Some voices work better than others; stylization is not always precise.
* Context overload: Too many inputs can reduce coherence.

Ethical note: All data stays local or on encrypted user-controlled servers. No data is stored or sold without consent.

## What next?

Future directions:

* Mobile app version with daily reminders
* Interactive voice journaling
* Visual storytelling (AI-generated images based on entries)
* Export to print-ready memoir format
* Multi-language support

To move forward:

* Collaboration with UX designers
* Beta testers for real-life use
* Privacy/legal consultation
* Possible partnerships with journaling or wellness apps

## Acknowledgments

* Inspired by [Lifelogging](https://en.wikipedia.org/wiki/Lifelogging) and the Quantified Self movement
* Diary image: [Diary with Feather Pen](https://commons.wikimedia.org/wiki/File:Diary_with_feather_pen.jpg) / [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)
* Literary styles based on public domain authors and creative homage

## 🛠️ Quick Install & Run

### 1. Install dependencies

```bash
pip install openai
Linux/macOS: export OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxx"
Windows (PowerShell): $env:OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxx"
python ai_life_scribe.py
---
