# RuneScape 3 Agent Configuration

This agent is designed to assist with RuneScape 3 gameplay, research, and progress tracking.

## Configuration
- **Location:** `C:\Users\Jonathan Balraj\Documents\rs3-agent`
- **Skills Directory:** `skills/`
- **Primary Data Sources:** RS3 Wiki API, Official RS3 Hiscores API.

## Core Capabilities
1. **Wiki Search:** Search for items, quests, monsters, and game mechanics.
   - Command: `python skills/wiki_search.py "<query>"`
2. **Player Lookup:** Retrieve stats for any RuneScape 3 player.
   - Command: `python skills/player_lookup.py "<player_name>"`
3. **Beast Lookup:** Detailed stats and weaknesses for monsters.
   - Command: `python skills/beast_lookup.py "<monster_name>"`
4. **GE Price Check:** Current prices and trends for items.
   - Command: `python skills/ge_lookup.py <item_id>`
5. **Memory Management:** Manage your username and active goals.
   - View Memory: `python skills/manage_memory.py`
   - Set Username: `python skills/manage_memory.py set-user "<your_name>"`
   - Add Goal: `python skills/manage_memory.py add-goal "<your_goal>"`
   - Remove Goal: `python skills/manage_memory.py remove-goal <index>`

## Goal Tracking
You can use this agent to track your goals by referencing your stats and checking requirement wikis.      

### Example Workflow:
1. Lookup your stats: `python skills/player_lookup.py "YourName"`
2. Search for a quest: `python skills/wiki_search.py "Prifddinas quest requirements"`
3. Compare and plan.
