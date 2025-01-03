import os
import ctypes
import requests

import config


def download_image(url, save_path):
    """
    Downloads an image from the URL and saves it.
    """
    try:
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()

        with open(save_path, 'wb') as file:
            file.write(response.content)

        return save_path
    except requests.RequestException as e:
        print(f"Error downloading image from {url}: {e}")

        return None


def get_random_wallhaven_image(api_key, categories, sorting, q=None):
    """
    Gets a random image from Wallhaven API with the specified filters.
    """
    url = f"https://wallhaven.cc/api/v1/search?categories={categories}purity=100&&sorting={sorting}&apikey={api_key}"

    # If q is not None, add it to the request
    if q:
        url += f"&q={q}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data['data']:
            return data['data'][0]['path']

        raise Exception("Wallhaven did not return any suitable images.")
    except requests.RequestException as err:
        print(f"Error calling Wallhaven API: {err}")

        return None


def set_wallpaper(image_path):
    """
    Sets the image as wallpaper.
    """
    ctypes.windll.user32.SystemParametersInfoW(20, 0, str(image_path), 3)


def rename_file(file_name, replacements):
    """
    Replaces parts of the file name according to the replacements dictionary.
    """
    for old, new in replacements.items():
        file_name = file_name.replace(old, new)

    return file_name


def main():
    """
    Main function to get a random image from Wallhaven and set it as wallpaper.
    """
    api_key = config.API_KEY
    wallpaper_folder = os.path.normpath(config.FOLDER_TO_IMAGES)
    os.makedirs(wallpaper_folder, exist_ok=True)

    try:
        # Get settings from the config
        categories = config.CATEGORIES
        sorting = config.SORTING
        q = config.Q

        # Get the image URL
        image_url = get_random_wallhaven_image(api_key, categories, sorting, q)

        if image_url:
            image_name = image_url.split('/')[-1]
            image_name = rename_file(image_name, config.REPLACEMENTS)
            save_path = os.path.join(wallpaper_folder, image_name)
            downloaded_image = download_image(image_url, save_path)

            if downloaded_image:
                set_wallpaper(downloaded_image)
                print(f"Wallpaper downloaded and set: {downloaded_image}")
    except Exception as err:
        print(f"An error occurred: {err}")


if __name__ == "__main__":
    main()
