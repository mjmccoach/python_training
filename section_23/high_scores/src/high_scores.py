def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    sorted_scores = high_to_low(scores)
    count = 3

    if len(scores) < 3:
        count = len(scores)

    return sorted_scores[0:count]

def high_to_low(scores):
    scores.sort(reverse = True)
    return scores
