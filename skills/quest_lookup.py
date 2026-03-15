import sys
import urllib.request
import json

def get_player_quests(player_name):
    # RuneMetrics Quest API
    url = f"https://apps.runescape.com/runemetrics/quests?user={player_name.replace(' ', '+')}"
    
    headers = {
        'User-Agent': 'RS3-Assistant-Agent/1.0 (Contact: user@example.com)'
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
        
        # The API returns a dict with a "quests" list
        quests = data.get("quests", [])
        
        if not quests:
            print(f"No quest data found for player '{player_name}'. (Note: Profile must be public)")
            return
        
        completed = [q for q in quests if q['status'] == 'COMPLETED']
        started = [q for q in quests if q['status'] == 'STARTED']
        not_started = [q for q in quests if q['status'] == 'NOT_STARTED']
        
        total_qp = sum(q['questPoints'] for q in completed)
        
        print(f"Quest Summary for {player_name}:")
        print(f"  Completed: {len(completed)}")
        print(f"  Started: {len(started)}")
        print(f"  Not Started: {len(not_started)}")
        print(f"  Total Quest Points: {total_qp}")

        # List completed quest titles
        completed_titles = [q['title'] for q in completed]
        print(f"\nCompleted Quests: {', '.join(completed_titles)}")
        
        # If a specific quest title is passed as a second argument, check its status
        if len(sys.argv) > 2:
            search_title = " ".join(sys.argv[2:]).lower()
            for q in quests:
                if search_title in q['title'].lower():
                    print(f"\nStatus for '{q['title']}': {q['status']}")
                    print(f"  Difficulty: {q['difficulty']}")
                    print(f"  Eligible: {'Yes' if q['userEligible'] else 'No'}")
            
    except Exception as e:
        print(f"Error fetching quest data: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python quest_lookup.py <player_name> [optional_quest_title]")
    else:
        get_player_quests(sys.argv[1])
