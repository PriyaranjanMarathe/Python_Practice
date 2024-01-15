# import requests
#
# url = 'https://www.loksatta.com/lokrang/sattechya-padchayet/marathi-articles-on-yashwantrao-chavan-leadership-part-2-1659235/'
# params = (
#     ('url', url),
# )
#
# response = requests.get('https://archive.org/wayback/available', params=params)
# url_available = response.json()['archived_snapshots']
# print(url_available)
#
# param_save = (('url', 'http://web.archive.org/save/' + url),)
# url_save = requests.post(param_save,  access_key=oNb43tgLyo6RVz7I, secret_key=rsJCF3eOgJMxSaFD)
# print(url_save.json())

import requests


def save_to_wayback_machine(url):
    wayback_url = f'http://web.archive.org/save/{url}'
    response = requests.get(wayback_url)
    if response.status_code == 200:
        print(f"URL '{url}' saved to Wayback Machine successfully.")
    else:
        print(f"Failed to save URL '{url}' to Wayback Machine.")


links_to_save = [
    "https://www.loksatta.com/lokrang/sattechya-padchayet/ram-khandekar-article-on-yashwantrao-chavan-2-1678290/",
    "https://www.loksatta.com/lokrang/sattechya-padchayet/ram-khandekar-article-on-jawaharlal-nehru-1690139/",
    "https://www.loksatta.com/lokrang/sattechya-padchayet/ram-khandekar-article-on-yashwantrao-chavan-3-1693651/",
    "https://www.loksatta.com/lokrang/sattechya-padchayet/article-about-birthday-celebrations-of-yashwantrao-chavan-1702193/",
    "https://www.loksatta.com/lokrang/sattechya-padchayet/yashwantrao-chavan-minister-of-foreign-affairs-and-foreign-minister-1725622/",
    "https://www.loksatta.com/lokrang/sattechya-padchayet-yashwantrao-chavan-p-v-narasimha-rao-1742819/",
    "https://www.loksatta.com/lokrang/sattechya-padchayet/author-ram-khandekar-article-on-narasimha-rao-2-1751361/",
    "https://www.loksatta.com/lokrang/sattechya-padchayet/article-about-pv-narasimha-rao-lifestyle-1756984/",
    "https://www.loksatta.com/lokrang/sattechya-padchayet/narasimha-rao-established-hrd-ministry-1762170/",
    "https://www.loksatta.com/lokrang/sattechya-padchayet/article-about-pv-narasimha-rao-humanity-1766315/",
    "https://www.loksatta.com/lokrang/sattechya-padchayet/ram-khandekar-article-on-narasimha-rao-1770909/",
    "https://www.loksatta.com/lokrang/sattechya-padchayet/ram-khandekar-article-on-narasimha-rao-2-1775505/",
    "https://www.loksatta.com/lokrang/sattechya-padchayet/ram-khandekar-article-on-pv-narasimha-rao-1783832/",
    "https://www.loksatta.com/lokrang/sattechya-padchayet/ram-khandekar-article-on-pv-narasimha-rao-2-1787324/",
    "https://www.loksatta.com/lokrang/sattechya-padchayet/ram-khandekar-article-on-pv-narasimha-rao-3-1791062/",
    "https://www.loksatta.com/lokrang/sattechya-padchayet/author-ram-khandekar-article-on-pv-narasimha-rao-economic-reforms-1794336/",
    "https://www.loksatta.com/lokrang/sattechya-padchayet/author-ram-khandekar-article-on-pv-narasimha-rao-2-1802402/",
    "https://www.loksatta.com/lokrang/sattechya-padchayet/ram-mandir-dispute-and-narasimha-rao-1806238/",
    "https://www.loksatta.com/lokrang/sattechya-padchayet/ram-mandir-dispute-and-narasimha-rao-2-1810574/",
    "https://www.loksatta.com/lokrang/sattechya-padchayet/author-ram-khandekar-article-on-pv-narasimha-rao-3-1814366/",
    "https://www.loksatta.com/author/ram-khandekar/"
    ]
for link in links_to_save:
    save_to_wayback_machine(link)