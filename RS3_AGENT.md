# RuneScape 3 Agent Configuration

This agent is designed to assist with RuneScape 3 gameplay, research, and progress tracking.

## Configuration
- **Location:** `C:\Users\Jonathan Balraj\Documents\rs3-agent`
- **Primary Data Sources:** RS3 Wiki API, Official RS3 Hiscores API.

## Core Capabilities
1. **Wiki Search:** Search for items, quests, monsters, and game mechanics.
   - Command: `python wiki_search.py "<query>"`
2. **Player Lookup:** Retrieve stats for any RuneScape 3 player.
   - Command: `python player_lookup.py "<player_name>"`
3. **Memory Management:** Manage your username and active goals.
   - View Memory: `python manage_memory.py`
   - Set Username: `python manage_memory.py set-user "<your_name>"`
   - Add Goal: `python manage_memory.py add-goal "<your_goal>"`
   - Remove Goal: `python manage_memory.py remove-goal <index>`

## Goal Tracking
You can use this agent to track your goals by referencing your stats and checking requirement wikis.

### Example Workflow:
1. Lookup your stats: `python player_lookup.py "YourName"`
2. Search for a quest: `python wiki_search.py "Prifddinas quest requirements"`
3. Compare and plan.
