# RuneScape 3 Assistant Agent

A specialized assistant for RuneScape 3 designed to provide data-driven advice, wiki information, and player statistics. This tool helps players optimize their gameplay by calculating the "Value of Time" (V) and tracking progress toward major goals like unlocking Prifddinas.

## 🚀 Features

- **Player Stats:** Fetch real-time hiscore data for any player.
- **Wiki Search:** Quick access to RS3 Wiki information for items, quests, and mechanics.
- **Quest Tracking:** Check quest eligibility and completion status via RuneMetrics.
- **Bestiary Lookup:** Get monster weaknesses, life points, and locations.
- **Grand Exchange Prices:** Track item price trends and current market values.
- **Memory Management:** Persistently track your username, goals, and hourly earning potential.

## 🛠️ Getting Started

### Prerequisites
- Python 3.x

### Setup
1. Clone the repository.
2. Ensure you have an active internet connection to reach the RS3 APIs and Wiki.

## 📖 Usage

All core logic is located in the `skills/` directory. You can run these scripts directly from the root:

- **Lookup Player Stats:**
  ```bash
  python skills/player_lookup.py "YourUsername"
  ```
- **Search the Wiki:**
  ```bash
  python skills/wiki_search.py "Prifddinas requirements"
  ```
- **Check Grand Exchange Prices:**
  ```bash
  python skills/ge_lookup.py 7936  # Example: Pure Essence
  ```
- **Manage Your Goals:**
  ```bash
  python skills/manage_memory.py add-goal "Reach 99 Herblore"
  ```

## 🤖 Development

This project was originally created using **Gemini**. Future updates are planned to ensure full compatibility with **Claude Code**.

## ⚖️ License
This project is for educational and personal use in accordance with the RuneScape Fan Content Policy.
