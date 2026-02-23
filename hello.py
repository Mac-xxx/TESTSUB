"""
SIMPLE URL SCANNER 
"""

# Import the library we need
import requests

# Ask user for a URL
print("Welcome to Simple URL Scanner!")
print("-" * 40)

url = input("Give me a URL to scan: ")

# Add https:// if needed
if not url.startswith('http'):
    url = 'https://' + url

# Try to scan the URL
print(f"\nScanning {url}...")

try:
    # Send request to the website
    response = requests.get(url, timeout=5)
    
    # Show the results
    print("\n SUCCESS!")
    print(f"Status Code: {response.status_code}")
    print(f"Website is working: {'YES' if response.status_code == 200 else 'NO'}")
    
except Exception as error:
    # If something goes wrong
    print(f"\n ERROR: Could not scan the URL")
    print(f"Reason: {error}")
