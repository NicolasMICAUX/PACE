from bs4 import BeautifulSoup  # for parsing html files
import re
import os
import pickle

# * parse all html files of youtube searches placed in data/ *
def parse_data_html_files():
    """
    Place html files like this :
    data/
        neutral/
            en/
                some_file.html
            fr/
        bodycam/
        witness/

    Then this script process them and adds them to videos.pickle
    """
    # load existing VIDEOS
    try:
        with open('videos.pickle', 'rb') as handle:
            VIDEOS = pickle.load(handle)
    except FileNotFoundError:
        VIDEOS = []

    # patterns to parse files, and youtube links
    pattern = re.compile("https://www.youtube.com/watch\?v=(.*)")
    pattern2 = re.compile('data/(neutral|bodycam|witness)/(en|fr)')

    # for all files in data/
    for root, dirs, files in os.walk("data/"):
        for file in files:
            # parse filename
            groups = pattern2.search(root)  # neutral|bodycam|witness, language
            print(file)
            path_to_file = os.path.join(root, file)
            page = open(path_to_file)
            # parse file with BeautifulSoup
            soup = BeautifulSoup(page.read(), features="html.parser")
            titles = soup.find_all('a', {'id': 'video-title'})
            # Number of videos found
            print(len(titles))
            for title in titles:
                # Append to VIDEOS
                vid_id = pattern.search(title['href']).group(1)
                VIDEOS.append((vid_id, title['title'], groups.group(1), groups.group(2)))
                # TODO : DOUBLONS !!! use dict instead of VIDEOS list

    # dump videos
    with open('videos.pickle', 'wb') as handle:
        pickle.dump(VIDEOS, handle, protocol=pickle.HIGHEST_PROTOCOL)

# * Converts a date in french format to a date DD/MM/YYYY *
def process_date(date):
    replacements = [
        (' janv. ', '/01/'),
        (' févr. ', '/02/'),
        (' mars ', '/03/'),
        (' avr. ', '/04/'),
        (' mai ', '/05/'),
        (' juin ', '/06/'),
        (' juil. ', '/07/'),
        (' août ', '/08/'),
        (' sept. ', '/09/'),
        (' oct. ', '/10/'),
        (' nov. ', '/11/'),
        (' déc. ', '/12/')
    ]
    for old, new in replacements:
        date = re.sub(old, new, date)
    return date