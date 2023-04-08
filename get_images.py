import os
import re
import requests
from bs4 import BeautifulSoup
import urllib.request

def get_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, "html.parser")

def download_images(search_query, num_images, directory):
    if not os.path.exists(directory):
        os.mkdir(directory)

    query = "+".join(search_query.split())
    url = f"https://www.google.com/search?q={query}&tbm=isch"

    soup = get_soup(url)
    images = soup.find_all("img")

    count = 0
    for img in images:
        try:
            img_url = img["src"]
            if not img_url.startswith("http"):
                img_url = img["data-src"]

            img_name = re.sub(r"\W+", "", search_query) + "_" + str(count) + ".jpg"
            img_path = os.path.join(directory, img_name)

            urllib.request.urlretrieve(img_url, img_path)
            print(f"Downloaded {img_name}")

            count += 1
            if count >= num_images:
                break

        except KeyError:
            continue

    print("Download completed!")

if __name__ == "__main__":
    search_query = "Keanu Reeves"
    num_images = 50
    directory = "model/dataset/Keanu Reeves"
    download_images(search_query, num_images, directory)
