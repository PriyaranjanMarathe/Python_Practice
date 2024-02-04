import requests
from bs4 import BeautifulSoup


def save_to_wayback_machine(url):
    wayback_url = f'http://web.archive.org/save/{url}'
    response = requests.get(wayback_url)

    if response.status_code == 200:
        return f'http://web.archive.org/web/{url}'  # Return the Wayback Machine URL
    else:
        print(f"Failed to save URL '{url}' to Wayback Machine.")
        return None


def save_links_to_wayback(page_url):
    response = requests.get(page_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True)]

        saved_links = []

        for link in links:
            if link.startswith('http'):
                saved_link = save_to_wayback_machine(link)
                if saved_link:
                    saved_links.append(saved_link)

        return saved_links
    else:
        print(f"Failed to fetch page '{page_url}'")
        return []


web_page_url = "https://www.loksatta.com/author/ram-khandekar/"
saved_links = save_links_to_wayback(web_page_url)

for link in saved_links:
    print("Saved link:", link)
