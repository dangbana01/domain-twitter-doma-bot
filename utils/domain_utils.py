import requests
from bs4 import BeautifulSoup

def fetch_expired_domains_from_godaddy(limit=20):
    """
    Scrape GoDaddy Auctions for expiring/expired domains.
    Returns a list of dicts: [{"domain": "example.com", "price": 0}, ...]
    """
    url = f"https://auctions.godaddy.com/trpSearchResults.aspx?sortby=EndDate&index=0"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        domains = []
        # Find domain listings
        for item in soup.select(".auction-item")[:limit]:
            domain_name = item.select_one(".auctionDomainName")
            price_tag = item.select_one(".current-bid")  # might be empty
            price = 0
            if price_tag:
                try:
                    price = int(price_tag.text.strip().replace("$", "").replace(",", ""))
                except:
                    pass

            if domain_name:
                domains.append({
                    "domain": domain_name.text.strip(),
                    "price": price
                })

        return domains

    except Exception as e:
        print("Error fetching domains:", e)
        return []


def filter_domains(domains, min_price=0, keyword=None):
    """
    Filter domains based on criteria
    - min_price: minimum last sale price
    - keyword: only include domains containing this string
    """
    filtered = []
    for d in domains:
        price = d.get("price", 0) or 0
        name = d.get("domain", "").lower()

        if price >= min_price:
            if keyword:
                if keyword.lower() in name:
                    filtered.append(d)
            else:
                filtered.append(d)

    return filtered
