import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"
headers = {"User-Agent": "Mozilla/5.0"}

page = requests.get(URL, headers=headers, timeout=10)
if page.status_code != 200:
    raise SystemExit(f"Request failed: HTTP {page.status_code}")
soup = BeautifulSoup(page.text, "html.parser")

# Found by inspecting: headlines are <h2 data-testid="card-headline">
seen, headlines = set(), []
for item in soup.find_all("h2", attrs={"data-testid": "card-headline"}):
    text = item.get_text(strip=True)
    if text and text not in seen:
        seen.add(text)
        headlines.append(text)

if len(headlines) < 5:
    print(f"Only found {len(headlines)} headlines.")
for i, h in enumerate(headlines[:5], 1):
    print(f"{i}. {h}")
