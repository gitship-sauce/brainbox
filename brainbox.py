notes = [
    {"title": "shopping", "text": "buy milk and eggs"},
    {"title": "idea", "text": "learn Python dictionaries"},
]

title = input("Title: ")
text = input("Note: ")
notes.append({"title": title, "text": text})

for note in notes:
    print(note["title"], "-", note["text"])
