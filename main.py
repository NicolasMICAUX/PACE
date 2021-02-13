# from youtube_comment_scraper import *   # for getting comments
import pytube                           # for getting video file

# TODO : not working
# from datakund import *
# youtube=datakund.youtube()
#
# # * get search results *
# youtube.search_results()
# # {“body”: [{‘viewsandtime’: ‘viewsandtime’, ‘channel’: ‘channel’, ‘title’: ‘title’, ‘link’: ‘link’}], “success_score”: “100”, “errors”: []}

url = 'https://www.youtube.com/watch?v=4SFhwxzfXNc'

# * get video infos *
# youtube.get_video_info(video_url=url)
# # TODO : use it
#{“body”: {‘DisLikes’: ‘DisLikes’, ‘Title’: ‘Title’, ‘Subscribers’: ‘Subscribers’, ‘Comments’: ‘Comments’, ‘ChannelLink’: ‘ChannelLink’, ‘ChannelName’: ‘ChannelName’, ‘Desc’: ‘Desc’, ‘Views’: ‘Views’, ‘Duration’: ‘Duration’, ‘Publish_Date’: ‘Publish_Date’, ‘Likes’: ‘Likes’}, “success_score”: “100”, “errors”: []}

# * download comments *
# youtube.open(url)
# youtube.keypress("pagedown")
# response = youtube.video_comments()
# data = response['body']
#
# for d in data:
#     print(d['Comment'])
#     print(d['Likes'])
#     print(d['Time'])
#     print(d['UserLink'])

# * download video files for violence automatic analysis *
print(pytube.YouTube(url).streams.get_lowest_resolution().download('/tmp'))