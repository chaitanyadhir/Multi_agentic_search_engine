from serpapi import GoogleSearch
import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup
import time

def search_and_scrape_duckduckgo(query, max_results=4, max_paragraphs=10):
    url = "https://html.duckduckgo.com/html/"
    headers = {"User-Agent": "Mozilla/5.0"}
    data = {"q": query}
    
    resp = requests.post(url, headers=headers, data=data)
    soup = BeautifulSoup(resp.text, "html.parser")

    results = []
    for a in soup.select(".result__title a")[:max_results]:
        link = a['href']
        text = scrape_page(link, max_paragraphs)
        results.append(text)
        time.sleep(1)  # Be polite

    return results

def scrape_page(url, max_paragraphs=10):
    try:
        resp = requests.get(url, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]
        return "\n".join(paragraphs[:max_paragraphs])
    except Exception as e:
        return f"[Error scraping {url}: {e}]"
