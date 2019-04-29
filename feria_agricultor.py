from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.request

options = Options()
options.add_argument("--headless")  # Runs Chrome in headless mode.
options.add_argument('--no-sandbox')  # # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")

url = "https://www.simacr.go.cr/index.php/ferias-a/precios-de-referencias"

browser = webdriver.Chrome(options=options)
browser.get(url)

final_page_li = browser.find_element_by_class_name('pagination-end')
final_page_url = final_page_li.find_element_by_css_selector('a').get_attribute('href')

final_page = int(final_page_url.split('=')[-1])


links = []
for page in range(1, final_page + 1):
    page_url = "%s?start=%d"% (url, page)
    print(page_url)
    browser.get(page_url)
    download_links = browser.find_elements_by_class_name('edocs_link')

    for download_link in download_links:
        download_url = download_link.get_attribute('href')
        file_name = download_url.split('/')[-1]
        urllib.request.urlretrieve(download_url, 'files/%s' % file_name)

        links.append(download_url)


browser.close()

print(links)
