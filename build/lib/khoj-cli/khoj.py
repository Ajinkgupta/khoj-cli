import argparse
import sys
import requests
import json
from colorama import init, Fore

init(autoreset=True)

def search(query):
    url = f"https://khoj.doubtly.in/api/?q={query}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def print_search_result(result):
    print(f"Title: {result['title']}")
    print(f"URL: {Fore.BLUE + result['url']}")
    print(f"Description: {result['description']}")
    print("-" * 50)

def main():
    if len(sys.argv) == 1:
        print("Error: Query required. Usage: khoj <query>")
        return

    query = ' '.join(sys.argv[1:])
    
    results = search(query)
    if results:
        print("Search Results:")
        for result in results:
            print_search_result(result)
    else:
        print("No results found.")

if __name__ == "__main__":
    main()
