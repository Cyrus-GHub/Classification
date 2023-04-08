import os
import requests
from googlesearch import search_images


def download_image(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)


def search_and_download_images(query, num_images=10, target_directory='images'):
    os.makedirs(target_directory, exist_ok=True)

    for i, image_url in enumerate(search_images(query, num_results=num_images)):
        try:
            save_path = os.path.join(
                target_directory, f"{query.replace(' ', '_')}_{i}.jpg")
            download_image(image_url, save_path)
            print(f"Downloaded {save_path}")
        except Exception as e:
            print(f"Failed to download {image_url}: {e}")


if __name__ == "__main__":
    celebrity_name = "Angelina Jolie"
    num_images = 10

    target_directory = "celebrity_images"

    search_and_download_images(celebrity_name, num_images, target_directory)
