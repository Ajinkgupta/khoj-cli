import argparse
import requests
from colorama import init, Fore
from bs4 import BeautifulSoup

init(autoreset=True)

def search_khoj(query):
    url = f"https://khoj.doubtly.in/api/?q={query}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def search_ai(query):
    url = f"https://8000-khojai-apiserverengine-4u4ic5d85y0.ws-us110.gitpod.io/api/?q={query}"
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.json().get("model_response")
        if html_content:
            # Parse HTML to extract plain text
            soup = BeautifulSoup(html_content, 'html.parser')
            return soup.get_text()
    return None

def print_search_result(result):
    print(f"Title: {result.get('title')}")
    print(f"URL: {Fore.BLUE + result.get('url')}")
    print(f"Description: {result.get('description')}")
    print("-" * 50)

def main():
    parser = argparse.ArgumentParser(description='Search using Khoj CLI')
    parser.add_argument('query', nargs='+', type=str, help='Search query')
    args = parser.parse_args()
    
    query = ' '.join(args.query)
    
    # Fetch results from the AI API
    ai_response = search_ai(query)
    if ai_response:
        # Print AI response in plain text
        print("AI Response:")
        print(ai_response)
        print("-" * 50)
    
    # Fetch results from the Khoj API
    results = search_khoj(query)
    if results:
        print("Search Results:")
        for result in results:
            print_search_result(result)
    else:
        print("No results found.")

if __name__ == "__main__":
    main()
