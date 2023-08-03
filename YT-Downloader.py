import requests
import re
import os

def download_video(video_url):
    # Download the video from youtube based on the url and converts it to mp3.
    os.system(f'yt-dlp {video_url} -x --audio-format mp3')

def search_youtube_video(title):
    # Replace string spaces by "+" to create the URL query
    search_query = title.replace(' ', '+')
    # Completed URL search query
    url = f'https://www.youtube.com/results?search_query={search_query}'

    # HTTP request to get the search result page's HTML
    response = requests.get(url)
    response.raise_for_status()  # Check if there's any errors with the HTTP request

    # Regex to search for the video's ID through the page's HTML
    video_ids = re.findall(r'/watch\?v=([0-9A-Za-z_-]{11})', response.text)

    if video_ids:
        # Extracts the ID from the first listed video
        first_video_id = video_ids[0]
        # Create a new URL using the first listed video's ID
        video_url = f'https://www.youtube.com/watch?v={first_video_id}'
        return video_url
    else:
        return None

def main():
    video_title = input("Type a title for the video you want to search: ")
    # Function to search the video through youtube
    video_url = search_youtube_video(video_title)
    # Check if the app directory already exists. If not, it creates a new one and download the songs on it.
    print('')
    try:
        os.listdir().index("YT-Downloader")
        print('YT-Downloader folder found. Songs will be downloaded on this folder.')
        print('')
        os.chdir('YT-Downloader')
    except:
        print('Creating YT-Downloader folder...')
        print('')
        os.mkdir('YT-Downloader')
        os.chdir('YT-Downloader')

    if video_url:
        download_video(video_url)
        print('')
        print('Download finished.')
        print('')
        os.chdir('..')
        answer = input('Do you wish to download another song? (Type Y for yes, N for no) ')
        print('')
        main() if answer == 'Y' or answer == 'y' else print('Ok, leaving application...')

    else:
        print(f'No video found with the following title: "{video_title}".')
        print('')
        answer = input('Wanna try again? (Type Y for yes, N for no) ')
        print('')
        main() if answer == 'Y' or answer == 'y' else print('Ok, leaving application...')

if __name__ == "__main__":
    main()
