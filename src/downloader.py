import os
import requests
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class ImageDownloader:
    def download_image(self, url, folder, filename, delay=10):
        while True:
            try:
                response = requests.get(url, timeout=10, verify=False)  # Disable SSL verification
                if response.status_code == 429:
                    print(f"Rate limited for {url}. Retrying in {delay} seconds...")
                    time.sleep(delay)
                    continue
                response.raise_for_status()
                filepath = os.path.join(folder, filename)
                # Avoid overwriting files
                base, extension = os.path.splitext(filepath)
                counter = 1
                while os.path.exists(filepath):
                    filepath = f"{base}_{counter}{extension}"
                    counter += 1
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                print(f"Downloaded: {filepath}")
                return
            except requests.exceptions.SSLError as ssl_err:
                print(f"SSL error for {url}: {ssl_err}. Retrying in {delay} seconds...")
                time.sleep(delay)
            except requests.exceptions.RequestException as e:
                print(f"Error downloading {url}: {e}. Retrying in {delay} seconds...")
                time.sleep(delay)