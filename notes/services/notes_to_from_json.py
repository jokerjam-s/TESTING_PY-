# Сохранение, чтениеи данных в json

import json

from notes.data.notes import Note


class NotesToTromJson:
    # сохранение списка данных в json
    #   data - данные для сохранения
    #   file_name - файл для сохранения
    #   при ошибке возвращает код ошибки, 0 - успех
    def notes_to_json(self, data, file_name):
        err_state = 0
        try:
            with open(file_name, "w") as json_file:
                json.dump(data, json_file, default=lambda x: x.__dict__, sort_keys=True, indent=2)
        except OSError as ex:
            print(ex)
            err_state = ex.errno
        except:
            print("Ошибка записи файла!")
            err_state = -1

        return err_state


    # чтениеи списка заметок из файла json
    #   file_name - файл с данными
    #   при ошибке возвращает пустой список
    def notes_from_json(self, file_name):
        notes = []

        try:
            with open(file_name, "r") as json_file:
                text = json.load(json_file)
            for n in text:
                note = Note()
                note.note_no = n["note_no"]
                note.text_note = n["text_note"]
                note.date_start = n["date_start"]
                note.time_start = n["time_start"]
                notes.append(note)
        except OSError as ex:
            print(ex)

        return notes


