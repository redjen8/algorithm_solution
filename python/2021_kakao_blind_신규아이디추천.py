import re


def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^\w.-]', '', new_id)
    new_id = re.sub('\.+', '.', new_id)
    new_id = new_id.lstrip(".").rstrip(".")
    if new_id == "":
        new_id = "a"
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.rstrip(".")
    if len(new_id) == 2:
        new_id = new_id + new_id[-1]
    if len(new_id) == 1:
        new_id = new_id + new_id[-1] + new_id[-1]
    print(new_id)


solution(input())
