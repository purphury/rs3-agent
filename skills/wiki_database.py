import sys
import urllib.request
import json

def query_wiki_cargo(table, fields, where=None):
    # RuneScape Wiki Cargo API (MediaWiki)
    base_url = "https://runescape.wiki/api.php?action=cargoquery&format=json"
    
    url = f"{base_url}&tables={table}&fields={fields.replace(' ', '')}"
    if where:
        url += f"&where={where.replace(' ', '%20')}"
    
    headers = {
        'User-Agent': 'RS3-Assistant-Agent/1.0 (Contact: user@example.com)'
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
        
        results = data.get("cargoquery", [])
        if not results:
            print(f"No results found in table '{table}' for query: {where}")
            return []
        
        # Cargo returns nested dicts: [{"title": {"Field1": "Val1"}}, ...]
        clean_results = [r["title"] for r in results]
        return clean_results
            
    except Exception as e:
        print(f"Error querying Wiki Cargo: {e}")
        return []

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python wiki_database.py <table> <fields> [where_clause]")
        print("Example: python wiki_database.py Quests 'Name, Difficulty, QP' 'Name=\"Cooks Assistant\"'")
    else:
        table = sys.argv[1]
        fields = sys.argv[2]
        where = sys.argv[3] if len(sys.argv) > 3 else None
        
        results = query_wiki_cargo(table, fields, where)
        for res in results:
            print(json.dumps(res, indent=2))
