import os
import re
import time
from urllib.request import urlretrieve

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_soup(browser):
    return BeautifulSoup(browser.page_source, "html.parser")

def download_images(search_query, num_images, directory):
    if not os.path.exists(directory):
        os.mkdir(directory)

    query = "+".join(search_query.split())
    url = f"https://www.google.com/search?q={query}&tbm=isch"

    browser = webdriver.Chrome()
    browser.get(url)

    count = 0
    while count < num_images:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        soup = get_soup(browser)
        images = soup.find_all("img")

        for img in images:
            try:
                img.click()
                time.sleep(1)
                img_url = browser.find_element_by_css_selector("img.n3VNCb").get_attribute("src")

                img_name = re.sub(r"\W+", "", search_query) + "_" + str(count) + ".jpg"
                img_path = os.path.join(directory, img_name)

                urlretrieve(img_url, img_path)
                print(f"Downloaded {img_name}")

                count += 1
                if count >= num_images:
                    break

            except Exception as e:
                print(f"Error: {e}")
                continue

    browser.quit()
    print("Download completed!")

if __name__ == "__main__":
    search_query = "Keanu Reeves"
    num_images = 50
    directory = "model/dataset/Keanu Reeves"
    download_images(search_query, num_images, directory)
