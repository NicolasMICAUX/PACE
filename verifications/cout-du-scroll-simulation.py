from random import random

NB_VIEWS = 1000000  # TODO : suivant une loi
DURATION = 365 * 24 * 60  # lifetime of the video (mn)    # TODO : suivant une loi
PROBA_SCROLL_COMMENT = 0.2  # TODO : suivant l'utilisateur (?)
ADD_COMMENT_RATIO = 0.005  # normal value
PROBA_ANSWER_COMMENT = 0.01  # proba. of answering a comment when read
GEOM_PARAM = 0.2

def rank_comments(comments_list, current_time):
    """
    Rank comments according to youtube algorithm
    :param comments_list: list of comments
    :param current_time: time since video publication (mn)
    :return: comments: new sorted list of comments
    """
    # TODO : improve function perf
    scores = []  # used to keep scores in order to sort comments
    # to gain perf, reevaluate only 100 first comments

    for _, likes, dislikes, publ_time, user_ratio, nb_ans in comments_list[:100]:
        A = current_time - publ_time
        r = likes / (dislikes or 1)
        scores.append((current_time / 10 + A) * abs(A - 3 * current_time) * ((10 * r + 2 * nb_ans) * (user_ratio / 12 + 1 / 40) + 1))

    new = [x for _, x in sorted(zip(scores, comments_list[:100]), reverse=True)]
    new.extend(comments_list[100:])
    return new

comments = []  # theorical_like_proba, nb likes, nb dislikes, publication time, user_ratio, nb_answer
time = 0
time_interval = DURATION / NB_VIEWS

for viewer in range(int(NB_VIEWS)):
    # display every 10 000 viewers
    if viewer%10000==0:
        print(f'{viewer}/{NB_VIEWS}')
    time += time_interval

    if random() < PROBA_SCROLL_COMMENT:
        # user reads comments
        comments = rank_comments(comments, time)
        # scroll comments (geometric law)
        i = 0
        while i < len(comments) and random() < GEOM_PARAM:
            if random() < 0.1:  # TODO : proba liker un commentaire
                if random() < comments[i][0]:
                    comments[i][1] += 1  # likes comment
                else:
                    comments[i][2] += 1  # dislikes comment
            if random() < PROBA_ANSWER_COMMENT:
                comments[i][5] += 1  # add an answer
            i += 1

    if random() < ADD_COMMENT_RATIO:
        # user add a comment
        comments.append([random(), 0, 0, time, random(), 0])

print(comments)