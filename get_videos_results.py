# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python
# https://developers.google.com/youtube/v3/docs/search/list

import pickle

import os
import googleapiclient.discovery

# TODO : make all requests through this script

def main():
    # * recover VIDEOS *
    with open('videos.pickle', 'rb') as handle:
        VIDEOS = pickle.load(handle)

    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "*************"

    next_page = 'CKYEEAE'  # initialize page token to retrieve

    for i in range(100):  # 100*100=10 000 credits
        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey=DEVELOPER_KEY)

        request = youtube.search().list(
            part="snippet",
            maxResults=50,
            order="date",
            publishedBefore="2019-03-08T00:00:00Z",
            q="police bodycam",
            type="video",
            pageToken=next_page,
            regionCode='US'
        )
        response = request.execute()
        print(response)

        try:
            next_page = response['nextPageToken']
        except KeyError:
            break
        finally:
            for item in response['items']:
                VIDEOS.append((item['id']['videoId'], item['snippet']['title'], 'bodycam', 'us'))

    # * dump VIDEOS *
    with open('videos.pickle', 'wb') as handle:
        pickle.dump(VIDEOS, handle, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    main()
