# Fotobotik 🤖📸  
*Your personal robotic archivist for photos that respect your filesystem*

---

## What is Fotobotik?

**Fotobotik** is an agentic photo-organizing system built with **Google’s Agentic Developer Kit (ADK)** that transforms chaotic photo libraries into **clean, bro# Fotobotik 🤖📸  
*Your personal robotic archivist for photos that respect your filesystem*

---

## What is Fotobotik?

**Fotobotik** is an agentic photo-organizing system built with **Google’s Agentic Developer Kit (ADK)** that transforms chaotic photo libraries into **clean, browsable folder structures**—paired with a **searchable semantic index**.

Instead of trapping your memories in proprietary blobs (looking at you, Apple Photos), Fotobotik:  
✅ Reads EXIF metadata  
✅ Recognizes friends’ faces  
✅ Uses **multimodal LLM vision** (Gemini) to describe scenes, clothing, activities, and more  
✅ Organizes photos into **human-friendly folders** like `!Christmas 2024` or `2024/07`  
✅ Builds a fast-queryable index so you can ask:  
> _“Show me all photos of Jane wearing a green sweater”_  
… and get results **instantly**, without re-analyzing images.

All while keeping your photos **local**, your filesystem **sane**, and your privacy **intact**.

Fotobotik will support **both a web client** (for easy interaction) **and a command-line interface** (for power users and automation). You choose your poison—order is guaranteed either way.

---

## Why “Fotobotik”?

Because your photos deserve more than dumb folders—  
they deserve a **robotic archivist** with eyes, memory, and taste.

---

## Current Progress

Below is a living checklist of core features. Nothing’s implemented yet—but watch this space! ✨

### Core Engine (ADK Agent)
- [ ] Ingest photo directory via CLI or web upload  
- [ ] Register EXIF extraction as ADK tool  
- [ ] Register face detection/recognition as ADK tool  
- [ ] Integrate Gemini Vision for multimodal analysis via ADK  
- [ ] Implement event detection heuristic (e.g., Christmas, birthdays)  
- [ ] Generate structured metadata record (EDN/JSON) per photo  
- [ ] Build persistent searchable index (`photo_index.edn`)  

### Organization & Output
- [ ] Support chronological mode (`YYYY/MM/`)  
- [ ] Support event-based mode (`!Event Name YYYY/`)  
- [ ] Respect user’s file-naming preferences (e.g., leading `!` for priority sorting)  
- [ ] Copy or symlink photos to organized structure (user choice)  

### Query Interface
- [ ] CLI: `fotobotik query "jane, green sweater"`  
- [ ] Web: Natural-language search with result previews  
- [ ] Support tag-based filtering (person, clothing, location, activity)  

### User Experience
- [ ] Web client (simple, responsive, no JS framework bloat)  
- [ ] CLI with clear help and defaults  
- [ ] Config file support (`fotobotik.toml` for events, known faces, etc.)  
- [ ] Progress logging / dry-run mode  

---

## Tech Stack

- **Agent Framework**: Google Agentic Developer Kit (ADK)  
- **LLM/Vision**: Google Gemini (via `google-generativeai`)  
- **Photo Tools**:  
  - `ExifRead` (EXIF extraction)  
  - `face_recognition` (face detection + recognition)  
  - `Pillow` + `pillow-heif` (image handling)  
- **Web Client**: TBD (likely lightweight Flask or http.server + HTMX if you’re feeling spicy)  
- **Data Format**: EDN (extensible, Clojure-inspired) for elegant, nested metadata  
- **Philosophy**: No Docker. No cloud lock-in. No nonsense.

---

## Example Vision

```bash
# CLI mode
fotobotik ingest ./phone_dump --output ~/Photos/Sorted --mode event

# Web mode
# → Upload folder, click “Organize”, then search: “bob, sunglasses, beach”
```

The agent does the thinking. You get order, speed, and peace of mind.

---

## Capstone Context

Fotobotik was developed as a **capstone project** for an Agentic AI course, showcasing:  
- Real-world use of **Google ADK**  
- Multimodal perception via **Gemini Vision**  
- Tool integration (EXIF, face recognition)  
- Dual-interface design (web + CLI)  
- Structured output for human-computer collaboration  

It proves that agentic systems don’t need flashy UIs—they can work quietly in the background, **enhancing human autonomy**, not replacing it.

---

## Getting Started (Future)

> ⚠️ **Coming soon!**  
> This project assumes access to **Google ADK** and **Gemini API** (as per course requirements).

Once implemented:
```bash
git clone https://github.com/yourname/fotobotik.git
cd fotobotik
pip install -r requirements.txt
python -m fotobotik --help
```

---

## Philosophy

> _“A photo library should be a garden, not a vault.”_

Fotobotik believes your memories belong to **you**—organized in a way **you** understand, searchable by **your** words, and never locked behind a login.

It’s not an app.  
It’s a **quiet ally** in your digital life.

---

## Made with 💚  
For lovers of `ls`, sunlight through leaves, and finding that one perfect photo of Jane in her green sweater.  

*Fotobotik — because your past deserves a good filing system.*
wsable folder structures**—paired with a **searchable semantic index**.

Instead of trapping your memories in proprietary blobs (looking at you, Apple Photos), Fotobotik:  
✅ Reads EXIF metadata  
✅ Recognizes friends’ faces  
✅ Uses **multimodal LLM vision** (Gemini) to describe scenes, clothing, activities, and more  
✅ Organizes photos into **human-friendly folders** like `!Christmas 2024` or `2024/07`  
✅ Builds a fast-queryable index so you can ask:  
> _“Show me all photos of Jane wearing a green sweater”_  
… and get results **instantly**, without re-analyzing images.

All while keeping your photos **local**, your filesystem **sane**, and your privacy **intact**.

---

## Why “Fotobotik”?

Because your photos deserve more than dumb folders—  
they deserve a **robotic archivist** with eyes, memory, and taste.

---

## Key Features

- **Agentic Orchestration**: Built on **Google ADK**, demonstrating autonomous planning, tool use, and multimodal reasoning.
- **Smart Organization**:  
  - Chronological (`2024/12/`)  
  - Event-based (`!Christmas 2024`, `!Beach Trip July`)  
- **Face Recognition**: Knows Jane from Bob—even in group shots.
- **Semantic Indexing**: Pre-processes images with Gemini Vision to tag:  
  - Clothing & appearance  
  - Scene type (indoor/outdoor)  
  - Objects, activities, lighting, mood  
- **Fast Search**: Query your entire library with natural language—no live LLM calls at query time.
- **Filesystem-First**: Output is plain folders and files. Browse with `ls`, Thunar, or Finder—no app required.
- **Structured Metadata**: Index saved as `photo_index.edn` (or JSON)—human-readable, scriptable, future-proof.

---

## Tech Stack

- **Agent Framework**: Google Agentic Developer Kit (ADK)
- **LLM/Vision**: Google Gemini (via `google-generativeai`)
- **Photo Tools**:  
  - `ExifRead` (EXIF extraction)  
  - `face_recognition` (face detection + recognition)  
  - `Pillow` + `pillow-heif` (image handling)
- **Data Format**: EDN (extensible, Clojure-inspired) for elegant, nested metadata
- **Philosophy**: No Docker. No cloud lock-in. No nonsense.

---

## Example Workflow

```bash
# Ingest and organize
fotobotik organize ~/Photos/Unsorted --output ~/Photos/Sorted

# Query (instant!)
fotobotik query "jane, green sweater"
# → Returns: Sorted/!Christmas 2024/IMG_1234.jpg
```

Behind the scenes, the agent:  
1. Scans your input folder  
2. For each image:  
   - Extracts EXIF date  
   - Detects & identifies faces  
   - Sends image to Gemini with structured prompts  
   - Decides best folder (`!Event` or `YYYY/MM`)  
3. Copies files + builds `photo_index.edn`  
4. Exits—leaving you with order and power.

---

## Capstone Context

Fotobotik was developed as a **capstone project** for an Agentic AI course, showcasing:  
- Real-world use of **Google ADK**  
- Multimodal perception via **Gemini Vision**  
- Tool integration (EXIF, face recognition)  
- Structured output for human-computer collaboration  

It proves that agentic systems don’t need flashy UIs—they can work quietly in the background, **enhancing human autonomy**, not replacing it.

---

## Getting Started

> ⚠️ **Note**: This project assumes access to **Google ADK** and **Gemini API** (as per course requirements).

1. Clone and install:
   ```bash
   git clone https://github.com/yourname/fotobotik.git
   cd fotobotik
   pip install -r requirements.txt
   ```

2. Set up known faces:
   ```bash
   mkdir known_faces
   cp jane.jpg known_faces/Jane.jpg
   cp bob.png known_faces/Bob.png
   ```

3. Run:
   ```bash
   export GOOGLE_API_KEY=your_gemini_key
   python -m fotobotik organize ./input_photos --output ./sorted_photos
   ```

4. Query:
   ```bash
   python -m fotobotik query "outdoors, jane, red dress"
   ```

---

## Philosophy

> _“A photo library should be a garden, not a vault.”_

Fotobotik believes your memories belong to **you**—organized in a way **you** understand, searchable by **your** words, and never locked behind a login.

It’s not an app.  
It’s a **quiet ally** in your digital life.

---

## Made with 💚  
For lovers of `ls`, sunlight through leaves, and finding that one perfect photo of Jane in her green sweater.  

*Fotobotik — because your past deserves a good filing system.
