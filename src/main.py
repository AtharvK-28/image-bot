import os
import random
import time
from image_search import ImageSearch
from downloader import ImageDownloader

def main():
    names = [""] # List of names to search for images
    base_folder = os.path.join(os.path.expanduser("~"), "Desktop", "image-bot-demo")
    num_images = 1  # Number of images per name

    if not os.path.exists(base_folder):
        os.makedirs(base_folder)

    image_searcher = ImageSearch()
    image_downloader = ImageDownloader()

    for name in names:
        print(f"\nSearching for images of '{name}'...")
        try:
            image_urls = image_searcher.search_images(name, max_results=num_images)
        except Exception as e:
            print(f"Rate limit or search error for '{name}': {e}")
            time.sleep(30)
            continue

        print(f"Found {len(image_urls)} images. Downloading to '{base_folder}'...")
        player_name = name
        for idx, url in enumerate(image_urls, 1):
            filename = f"{player_name}_{idx}.jpg"
            image_downloader.download_image(url, base_folder, filename)
            time.sleep(random.uniform(10,30))

    print("\nAll downloads completed!")

if __name__ == "__main__":
    main()
