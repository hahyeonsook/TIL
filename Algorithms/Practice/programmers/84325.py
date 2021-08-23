# REF https://programmers.co.kr/learn/courses/30/lessons/84325
import collections


def solution(table, languages, preference):
    languages_preference = collections.defaultdict(int)
    for language, score in zip(languages, preference):
        languages_preference[language] = score

    type_score = collections.defaultdict(int)
    for column in table:
        languages_score = column.split()[::-1]
        type = languages_score[-1]
        for index, language in enumerate(languages_score[:-1]):
            type_score[type] += (index + 1) * languages_preference[language]
    return sorted(type_score.items(), key=lambda x: (-x[1], x[0]))[0][0]


table = [
    "SI JAVA JAVASCRIPT SQL PYTHON C#",
    "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
    "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
    "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
    "GAME C++ C# JAVASCRIPT C JAVA",
]
languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]

print(solution(table, languages, preference))
