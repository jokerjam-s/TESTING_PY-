# view

from notes.data.notes import Note
from notes.services.user_interface import *
from notes.services.note_functions import note_datetime

class NoteView:

    def __init__(self):
        self.ui = UserIterface()

    # запрос новой заметки
    def new_note(self):
        note = Note()
        note.date_start = self.ui.ask_date("Дата: ")
        note.time_start = self.ui.ask_time("Время: ")
        note.text_note = self.ui.ask_str("Текст: ")

        return note

    # запрос номера записи для удаления
    def del_note(self):
        return self.ui.ask_int("Номер записи для удаления: ")

    # редактирование заметки
    def edit_note(self, note: Note):
        note.note_no = note.note_no
        note.date_start = self.ui.ask_date("Дата (" + note.date_start + "): ")
        note.time_start = self.ui.ask_time("Время (" + note.time_start + "): ")
        note.text_note = self.ui.ask_str("Новый текст: ")

        return note


    # отображение списка заметок
    def show_notes(self, notes: list):
        if len(notes) == 0:
            print("Список пуст!")
        else:
            notes.sort(key=note_datetime)
            print("--------------------------------------------------------------")
            print("  #  |    дата    | время | текст ")
            print("--------------------------------------------------------------")
            for l in notes:
                print(" {0:3} | {1} | {2} | {3}".format(l.note_no, l.date_start, l.time_start, l.text_note))

            print("--------------------------------------------------------------")
