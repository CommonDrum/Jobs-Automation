from user import *
import tkinter as tk
from tkinter import messagebox, ttk
import os
import json


class PersonalInfoFrame(tk.Frame):
    def __init__(self, parent, info: PersonalInfo, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.config(background='lightblue')

        self.info = info

        self.create_label(text="First Names:", row=0, column=0)
        self.first_names_entry = self.create_entry(row=0, column=1, initial_text=info.first_names)

        self.create_label(text="Last Name:", row=1, column=0)
        self.last_name_entry = self.create_entry(row=1, column=1, initial_text=info.last_name)

        self.create_label(text="Birthday:", row=2, column=0)
        self.birthday_entry = self.create_entry(row=2, column=1, initial_text=info.birthday)

        self.create_label(text="Phone:", row=3, column=0)
        self.phone_entry = self.create_entry(row=3, column=1, initial_text=str(info.phone))

        self.create_label(text="Email:", row=4, column=0)
        self.email_entry = self.create_entry(row=4, column=1, initial_text=info.email)

        self.create_label(text="City:", row=5, column=0)
        self.city_entry = self.create_entry(row=5, column=1, initial_text=info.city)

        self.create_label(text="Postcode:", row=6, column=0)
        self.postcode_entry = self.create_entry(row=6, column=1, initial_text=info.postcode)

        self.create_label(text="LinkedIn:", row=7, column=0)
        self.linkedin_entry = self.create_entry(row=7, column=1, initial_text=info.linkedin)

        self.create_label(text="Website:", row=8, column=0)
        self.website_entry = self.create_entry(row=8, column=1, initial_text=info.website)

        self.edit_button = tk.Button(self, text="Edit", command=self.edit_info)
        self.edit_button.grid(row=9, column=0, columnspan=2)

    def create_label(self, text, row, column):
        label = tk.Label(self, text=text, bg=self['background'])
        label.grid(row=row, column=column)
        return label

    def create_entry(self, row, column, initial_text="", columnspan=1):
        entry = tk.Entry(self)
        entry.grid(row=row, column=column, columnspan=columnspan)
        entry.insert(0, initial_text)
        return entry

    def edit_info(self):
        self.info.first_names = self.first_names_entry.get()
        self.info.last_name = self.last_name_entry.get()
        self.info.birthday = self.birthday_entry.get()
        self.info.phone = int(self.phone_entry.get())
        self.info.email = self.email_entry.get()
        self.info.city = self.city_entry.get()
        self.info.postcode = self.postcode_entry.get()
        self.info.linkedin = self.linkedin_entry.get()
        self.info.website = self.website_entry.get()

        print("Information updated for", self.info.first_names, self.info.last_name)

class AttributesFrame():
    def __init__(self) -> None:
        pass

root = tk.Tk()

info = PersonalInfo("John", "Doe", "2000-01-01", 1234567890, "john.doe@example.com", "Some City", "12345", "linkedin.com/in/johndoe", "johndoe.com")
info_frame = PersonalInfoFrame(root, info)
info_frame.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

root.mainloop()
