import sys
import urllib.request

def get_player_stats(player_name):
    # Official RS3 Hiscores (Lite API)
    url = f"https://secure.runescape.com/m=hiscore/index_lite.ws?player={player_name.replace(' ', '+')}"
    
    headers = {
        'User-Agent': 'RS3-Assistant-Agent/1.0 (Contact: user@example.com)'
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            data = response.read().decode('utf-8')
            
        # Skill names in the order they appear in RS3 hiscore_lite
        skills = [
            "Overall", "Attack", "Defence", "Strength", "Constitution", "Ranged", "Prayer", 
            "Magic", "Cooking", "Woodcutting", "Fletching", "Fishing", "Firemaking", 
            "Crafting", "Smithing", "Mining", "Herblore", "Agility", "Thieving", 
            "Slayer", "Farming", "Runecrafting", "Hunter", "Construction", "Summoning", 
            "Dungeoneering", "Divination", "Invention", "Archaeology", "Necromancy"
        ]
        
        lines = data.split('\n')
        stats = {}
        for i, skill in enumerate(skills):
            if i < len(lines):
                parts = lines[i].split(',')
                if len(parts) >= 2:
                    stats[skill] = {"rank": parts[0], "level": parts[1], "xp": parts[2]}
        
        print(f"Stats for {player_name}:")
        for skill, info in stats.items():
            print(f"  {skill}: Level {info['level']} (Rank {info['rank']})")
            
    except Exception as e:
        print(f"Error fetching data for player '{player_name}': {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python player_lookup.py <player_name>")
    else:
        get_player_stats(" ".join(sys.argv[1:]))
