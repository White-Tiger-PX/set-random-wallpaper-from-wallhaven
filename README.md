<p align="center">
  <a href="README.ru.md"><img src="https://img.shields.io/badge/Русский-Readme-blue" alt="Russian" /></a>&nbsp;&nbsp;
  <a href="README.md"><img src="https://img.shields.io/badge/English-Readme-blue" alt="English" /></a>&nbsp;&nbsp;
  <img src="https://visitor-badge.laobi.icu/badge?page_id=White-Tiger-PX.set-random-wallpaper-from-wallhaven" alt="visitors" />&nbsp;&nbsp;
  <img src="https://img.shields.io/github/stars/White-Tiger-PX/set-random-wallpaper-from-wallhaven?style=social" alt="GitHub stars" />
</p>

# set-random-wallpaper-from-wallhaven

This script allows you to set a random image from Wallhaven as your desktop wallpaper.

## Features

- Downloads a random image from Wallhaven based on the specified categories and sorting options.
- Automatically sets the downloaded image as your desktop wallpaper.
- Allows customization of image categories, sorting, and keyword search.

## Supported Operating Systems

This script is designed specifically for Windows. It uses the `ctypes` library to interact with the Windows API and set the desktop wallpaper.

## Setup

### Configure Image Folders

1. Open the `config.py` file.
2. Set the following values:
   - `API_KEY`: Your Wallhaven API key. You can obtain it by registering on the Wallhaven website.
   - `FOLDER_TO_IMAGES`: Path to the folder where images will be saved.
   - `CATEGORIES`: A string representing the categories of images you want to fetch. For example:
     - `100`: General images only.
     - `010`: Anime images only.
     - `001`: People images only.
     - `110`: General and Anime images.
   - `SORTING`: Sorting options such as `'random'`, `'date_added'`, `'relevance'`, `'views'`, `'favorites'`.
   - `Q`: Optional search keyword.

### Automate the Script Execution

To run the script automatically on system startup, set up a task in **Windows Task Scheduler**:

1. Open the **Task Scheduler** by searching for **Task Scheduler** in the Start menu (or press `Win + R`, type `taskschd.msc`, and press Enter).
2. Click on **Create task** in the right-hand panel.
3. Provide a name for your task (e.g., "Set Random Wallpaper").
4. Go to the **Triggers** tab, and click **New**.
   - Set the **Begin the task** option to **At logon** to ensure the task starts whenever you log into your system.
   - Optionally, check **Repeat task every** and set the interval (e.g., every 1 hour), if you want the task to run periodically.
5. Go to the **Actions** tab, click **New**, and choose **Start a Program**.
6. Browse and select the Python executable. By default, it is located at:
   `C:\Users\YOU_USERNAME\AppData\Local\Programs\Python\YOU_VERSION\python.exe`.
7. In the **Add arguments** field, provide the full path to your script. For example:
   `(C:\path\to\your\set_random_wallpaper_from_wallhaven.py)`
   *(Ensure the path is in quotes if it contains spaces.)*
8. Click **OK** to save the task.

<div style="justify-content: space-between; align-items: center;">
  <div style="text-align: center;">
    <img src="Task Scheduler - General.png" alt="Task Scheduler - General" width="75%" />
  </div>

  <div style="text-align: center;">
    <img src="Task Scheduler - Triggers.png" alt="Task Scheduler - Triggers" width="75%" />
  </div>

  <div style="text-align: center;">
    <img src="Task Scheduler - Actions.png" alt="Task Scheduler - Actions" width="75%" />
  </div>
</div>
