import sys
import urllib.request
import json

def search_beast(name):
    # Official RS3 Bestiary Search API
    search_url = f"https://secure.runescape.com/m=itemdb_rs/bestiary/beastSearch.json?term={name.replace(' ', '+')}"
    
    headers = {
        'User-Agent': 'RS3-Assistant-Agent/1.0 (Contact: user@example.com)'
    }
    
    try:
        req = urllib.request.Request(search_url, headers=headers)
        with urllib.request.urlopen(req) as response:
            beasts = json.loads(response.read().decode('utf-8'))
        
        if not beasts:
            print(f"No monsters found matching '{name}'.")
            return
        
        # Take the first match for detailed lookup
        first_beast = beasts[0]
        beast_id = first_beast['value']
        
        # Detailed data lookup
        data_url = f"https://secure.runescape.com/m=itemdb_rs/bestiary/beastData.json?beastid={beast_id}"
        req_data = urllib.request.Request(data_url, headers=headers)
        with urllib.request.urlopen(req_data) as response_data:
            data = json.loads(response_data.read().decode('utf-8'))
        
        print(f"Monster: {data['name']} (ID: {beast_id})")
        print(f"  Level: {data.get('level', 'N/A')}")
        print(f"  Weakness: {data.get('weakness', 'N/A')}")
        print(f"  Life Points: {data.get('lifepoints', 'N/A')}")
        print(f"  Description: {data.get('description', 'N/A')}")
        if data.get('areas'):
            print(f"  Common Locations: {', '.join(data['areas'])}")
            
    except Exception as e:
        print(f"Error fetching bestiary data: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python beast_lookup.py <monster_name>")
    else:
        search_beast(" ".join(sys.argv[1:]))
