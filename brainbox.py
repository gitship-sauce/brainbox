notes = [
    {"title": "shopping", "text": "buy milk and eggs"},
    {"title": "idea", "text": "learn Python dictionaries"},
]

def add_note():
    title = input("Title: ")
    text = input("Note: ")
    notes.append({"title": title, "text": text})

def show_notes():
    for note in notes:
        print(note["title"], "-", note["text"])

def find_note(title):
    for note in notes:
        if note["title"] == title:
            return note

def edit_note():
    title = input("Title: ")
    note = find_note(title)
    note["text"] = input("New text: ")

def delete_note():
    title = input("Title: ")
    note = find_note(title)
    notes.remove(note)

while True:
    choice = input("1 add, 2 show, 3 edit, 4 delete, 5 quit: ")
    if choice == "1":
        add_note()
    elif choice == "2":
        show_notes()
    elif choice == "3":
        edit_note()
    elif choice == "4":
        delete_note()
    elif choice == "5":
        break
