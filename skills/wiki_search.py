import sys
import urllib.request
import json

def search_wiki(query):
    # RuneScape 3 Wiki API (MediaWiki)
    url = f"https://runescape.wiki/api.php?action=opensearch&search={query.replace(' ', '+')}&limit=5&format=json"
    
    headers = {
        'User-Agent': 'RS3-Assistant-Agent/1.0 (Contact: user@example.com)'
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
        
        # OpenSearch format: [query, [titles], [descriptions], [links]]
        titles = data[1]
        links = data[3]
        
        if not titles:
            print(f"No Wiki results found for '{query}'.")
        else:
            print(f"Top Wiki results for '{query}':")
            for i in range(len(titles)):
                print(f"  - {titles[i]}: {links[i]}")
                
    except Exception as e:
        print(f"Error searching RuneScape Wiki: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python wiki_search.py <query>")
    else:
        search_wiki(" ".join(sys.argv[1:]))
