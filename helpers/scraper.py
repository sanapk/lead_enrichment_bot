import requests
from bs4 import BeautifulSoup

def scrape_homepage(url):
    try:
        if not url.startswith("http"):
            url = "https://" + url
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")
        paragraphs = soup.find_all("p")

        # Convert generator to list before printing
        first_10_texts = [p.text.strip() for p in paragraphs[:10]]
        print("\n".join(first_10_texts))  # ✅ Actually prints text, not generator

        return ' '.join(first_10_texts)   # ✅ Returns a proper string
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return ""
