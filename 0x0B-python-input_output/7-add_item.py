#!/usr/bin/python3
"""
This script that adds all arguments to a Python list, and then save them to a file
"""
save_to_file = __import__("5-save_to_json_file").save_to_json_file
load_from_file = __import__("6-load_from_json_file").load_from_json_file
json = __import__("json")
os = __import__("os")
argv = __import__("sys").argv

lst = []
if os.path.exists("add_item.json"):
    with open('add_item.json', 'r', encoding="utf-8") as f:
        lst = json.load(f)

for i in range(1, len(argv)):
    lst.append(argv[i])

save_to_file(lst, "add_item.json")
