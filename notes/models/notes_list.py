# Взаимодействие с пользователем

from notes.data.notes import Note
from notes.views.node_view import NoteView

class NoteList:

    def __init__(self):
        self._note_counter = 0
        self._notes_list = []

    def get_list(self):
        return self._notes_list

    # добавить заметку в список
    def add_note(self, note:Note):
        self._note_counter += 1
        note.note_no = self._note_counter
        self._notes_list.append(note)

    # удаление заметки
    def del_note(self, note):
        self._notes_list.remove(note)

    # поиск заметок с текстом text
    def find_on(self, text):
        return list(filter(lambda n: text in n.text_note))

    # поиск заметки с номером note_no
    def get_note_no(self, note_no):
        note = None
        notes = list(filter(lambda n: note_no == n.note_no, self._notes_list))
        if len(notes) > 0:
            note = notes[0]

        return note

    # замена элемента
    def replace_note(self, old_note, new_note):
        index_note = self._notes_list.index(old_note)
        self._notes_list[index_note] = new_note

