import os
import requests
from google_images_search import GoogleImagesSearch

def download_image(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

def search_and_download_images(query, num_images=10, target_directory='images'):
    os.makedirs(target_directory, exist_ok=True)

    gis = GoogleImagesSearch('<your_google_developers_api_key>', '<your_google_custom_search_engine_id>')
    search_params = {
        'q': query,
        'num': num_images,
    }

    gis.search(search_params)

    for i, image in enumerate(gis.results()):
        try:
            save_path = os.path.join(target_directory, f"{query.replace(' ', '_')}_{i}.jpg")
            download_image(image.url, save_path)
            print(f"Downloaded {save_path}")
        except Exception as e:
            print(f"Failed to download {image.url}: {e}")

if __name__ == "__main__":
    celebrity_name = "Angelina Jolie"  # Replace with your desired celebrity name
    num_images = 10  # Adjust the number of images to download
    target_directory = "celebrity_images"  # Set the target directory for saving images

    search_and_download_images(celebrity_name, num_images, target_directory)
