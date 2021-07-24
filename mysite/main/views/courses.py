from main.models import Courses


def left_right(courses):
    k = 0
    left = []
    right = []
    for each in courses:
        if k == 0:
            left.append(each)
            k = 1
        elif k == 1:
            right.append(each)
            k = 0
    return left, right
