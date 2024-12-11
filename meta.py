import requests
import json

def get_instance_metadata():
  
    base_url = "http://1.2.3.4"
    
    def fetch_metadata(url):
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            content = response.text
            if content.strip().endswith('/'):
                keys = content.splitlines()
                metadata = {}
                for key in keys:
                    metadata[key.strip('/')] = fetch_metadata(url + key)
                return metadata
            else:
                return content
        else:
            return None
    
    return fetch_metadata(base_url)

if __name__ == "__main__":
    try:
        metadata = get_instance_metadata()
        print(json.dumps(metadata, indent=4))
    except requests.exceptions.RequestException as e:
        print(f"Error fetching metadata: {e}")
