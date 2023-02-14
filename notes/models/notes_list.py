# Взаимодействие с пользователем

from notes.data.notes import Note
from notes.services.user_interface import *

class NoteList:

    def __int__(self):
        self.note_counter = 0
        self.ui = UserIterface()
        self.notes_list = []



