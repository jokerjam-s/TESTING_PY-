# сравнение записей по дате времени
from notes.data.notes import Note
from datetime import datetime

def note_datetime(note: Note):
    return datetime.strptime(note.date_start + " "+note.time_start, "%d.%m.%Y %H:%M")


