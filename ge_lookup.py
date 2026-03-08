import sys
import urllib.request
import json

def get_item_detail(item_id):
    # Official RS3 Grand Exchange Item Detail API
    url = f"https://secure.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item={item_id}"
    
    headers = {
        'User-Agent': 'RS3-Assistant-Agent/1.0 (Contact: user@example.com)'
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
        
        item = data.get("item", {})
        if not item:
            print(f"No item data found for ID {item_id}.")
            return
        
        print(f"Item: {item['name']}")
        print(f"  Description: {item['description']}")
        print(f"  Current Price: {item['current']['price']}")
        print(f"  Today's Trend: {item['today']['trend']} ({item['today']['price']})")
        print(f"  30-day Change: {item['day30']['change']}")
        
    except Exception as e:
        print(f"Error fetching GE data for item {item_id}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ge_lookup.py <item_id>")
    else:
        get_item_detail(sys.argv[1])
