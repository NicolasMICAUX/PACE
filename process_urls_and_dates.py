import csv
import pickle

"""Export a csv dates and groups, for making diagram : date of publication for the three groups."""

# load videos urls, build a dict for fast searching a video group
DICT = {}
with open('videos.pickle', 'rb') as handle:
    VIDEOS = pickle.load(handle)
    for vid_id, _, group, _ in VIDEOS:
        DICT[vid_id] = group

# write groups to a csv file
with open('donnees/group.csv', 'w', newline='') as groupfile:
    writer = csv.writer(groupfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['group'])
    # load videos urls and dates
    with open('donnees/urls_and_dates.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader, None)  # skip the headers
        for vid_id, date in reader:
            try:
                group = DICT[vid_id]
                if group == 'neutral':
                    writer.writerow([date, 'neutral'])
                elif group == 'bodycam':
                    writer.writerow([date, 'bodycam'])
                elif group == 'witness':
                    writer.writerow([date, 'witness'])
            except KeyError:    # only once, negligeable
                print("KeyError")
