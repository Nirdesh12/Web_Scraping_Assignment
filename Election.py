import requests
from bs4 import BeautifulSoup

# List of Nepali news websites
news_sites = [
    "https://kathmandupost.com",
    "https://thehimalayantimes.com",
    "https://www.onlinekhabar.com"
]

# Search keyword
keyword = "Election"

# Function to scrape a single site
def scrape_site(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        articles_found = []

        # Extract all links from the homepage
        for link in soup.find_all("a", href=True):
            title = link.get_text(strip=True)
            href = link["href"]

            if keyword.lower() in title.lower():
                # Make full URL if relative
                if href.startswith("/"):
                    href = url + href

                articles_found.append((title, href))

        return articles_found  #  Return ALL matching articles

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return []


# Main execution
all_articles = []

for site in news_sites:
    articles = scrape_site(site)
    all_articles.extend(articles)

# Print results
if all_articles:
    print(f"\nArticles mentioning '{keyword}':\n")
    for idx, (title, link) in enumerate(all_articles, 1):  #  No slicing here
        print(f"{idx}. {title}")
        print(f"   Link: {link}\n")
else:
    print("No articles found.")
