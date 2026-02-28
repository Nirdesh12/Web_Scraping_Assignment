import requests
from bs4 import BeautifulSoup
import json

news_sites = [
    "https://kathmandupost.com",
    "https://thehimalayantimes.com",
    "https://www.onlinekhabar.com"
]

keyword = "Election"

# Function to extract full article content
def get_article_content(article_url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(article_url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")
        content = " ".join([p.get_text(strip=True) for p in paragraphs])

        return content[:2000]  # limit size (optional)

    except Exception as e:
        print(f"Error fetching article {article_url}: {e}")
        return ""


# Function to scrape a site
def scrape_site(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        articles_found = []

        for link in soup.find_all("a", href=True):
            title = link.get_text(strip=True)
            href = link["href"]

            if keyword.lower() in title.lower() and title:
                if href.startswith("/"):
                    href = url + href

                print(f"Fetching content: {title}")

                # 🔥 Fetch full article content
                content = get_article_content(href)

                articles_found.append({
                    "title": title,
                    "content": content,
                    "source": url
                })

        return articles_found

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return []


# Main
all_articles = []

for site in news_sites:
    all_articles.extend(scrape_site(site))

# Save JSON
with open("election.json", "w", encoding="utf-8") as f:
    json.dump(all_articles, f, indent=4, ensure_ascii=False)

print("Full article data saved to election.json")
