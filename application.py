from user import *
import tkinter as tk
from tkinter import messagebox, ttk, simpledialog, filedialog
import os
import json




class InfoFrame(tk.Frame):
    def __init__(self, info_class, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.info_class = info_class
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.entries = {}
        fields = self.info_class.__init__.__annotations__.keys()
        for idx, field in enumerate(fields):
            if field != 'self':
                label = tk.Label(self, text=field.replace('_', ' ').title())
                label.grid(row=idx, column=0)
                entry = tk.Entry(self)
                entry.grid(row=idx, column=1)
                self.entries[field] = entry

        self.submit_button = tk.Button(self, text='Submit', command=self.submit)
        self.submit_button.grid(row=len(fields), column=0, columnspan=2)

        self.result = tk.Text(self, height=10, width=50)
        self.result.grid(row=len(fields) + 1, column=0, columnspan=2)

    def submit(self):
        info_data = {field: entry.get() for field, entry in self.entries.items()}
        info_instance = self.info_class(**info_data)

        self.result.delete(1.0, tk.END)
        self.result.insert(tk.END, str(info_instance.to_dict()))



class AttributesFrame(tk.Frame):
    def __init__(self, attribute_classes, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.attribute_classes = attribute_classes
        self.selected_attribute_class = tk.StringVar()
        self.selected_attribute_class.set(list(attribute_classes.keys())[0]) # Default to the first class
        self.selected_attribute_class.trace('w', self.update_fields) # Update fields when the selection changes
        self.grid()
        self.create_widgets()
        self.update_fields() # Initialize the fields based on the default selection

    def create_widgets(self):
        self.attribute_dropdown = tk.OptionMenu(self, self.selected_attribute_class, *self.attribute_classes.keys())
        self.attribute_dropdown.grid(row=0, column=0, columnspan=2)

        self.fields_frame = tk.Frame(self)
        self.fields_frame.grid(row=1, column=0, columnspan=2)

        self.attributes_list = []

        self.add_button = tk.Button(self, text='Add', command=self.add_attribute)
        self.add_button.grid(row=2, column=0, columnspan=2)

        self.result = tk.Text(self, height=10, width=50)
        self.result.grid(row=3, column=0, columnspan=2)

    def update_fields(self, *args):
        for widget in self.fields_frame.winfo_children():
            widget.destroy()

        self.entries = {}
        attribute_class = self.attribute_classes[self.selected_attribute_class.get()]
        fields = attribute_class.__init__.__annotations__.keys()
        for idx, field in enumerate(fields):
            if field != 'self':
                label = tk.Label(self.fields_frame, text=field.replace('_', ' ').title())
                label.grid(row=idx, column=0)
                entry = tk.Entry(self.fields_frame)
                entry.grid(row=idx, column=1)
                self.entries[field] = entry

    def add_attribute(self):
        attribute_class = self.attribute_classes[self.selected_attribute_class.get()]
        attribute_data = {field: entry.get() for field, entry in self.entries.items() if field != 'self'}
        attribute_instance = attribute_class(**attribute_data)
        self.attributes_list.append(attribute_instance)

        self.result.delete(1.0, tk.END)
        for attribute in self.attributes_list:
            self.result.insert(tk.END, str(attribute.to_dict()) + '\n')






class UserApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('User Information')
        self.user = None
        self.last_created_user_file = 'last_user.json'

        # Top bar menu
        self.menu_bar = tk.Menu(self)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New User", command=self.new_user)
        self.file_menu.add_command(label="Load User", command=self.load_user)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.config(menu=self.menu_bar)

        # Personal Info Frame
        self.personal_info_frame = InfoFrame(info_class=PersonalInfo, master=self)
        self.personal_info_frame.grid(row=0, column=0)

        # Attributes Frame
        attribute_classes = {'Skill': Skill, 'Employment': Employment, 'Education': Education, 'Certificate': Certificate}
        self.attributes_frame = AttributesFrame(attribute_classes=attribute_classes, master=self)
        self.attributes_frame.grid(row=0, column=1)

        self.load_last_user()

    def new_user(self):
        user_name = simpledialog.askstring('New User', 'Enter User Name:')
        if user_name:
            self.user = User(user_name=user_name, personal_info={})
            self.update_display()

    def load_user(self):
        file_name = filedialog.askopenfilename(filetypes=[('JSON Files', '*.json')])
        if file_name:
            self.user = User.load_from_file(file_name)
            self.update_display()

    def update_display(self):
        if self.user:
            self.personal_info_frame.load_info(self.user.personal_info)
            self.attributes_frame.load_attributes(self.user)
            self.user.save_to_file()
            with open(self.last_created_user_file, 'w') as f:
                json.dump({'last_user_file': f'{self.user.user_name}_user.json'}, f)

    def load_last_user(self):
        if os.path.exists(self.last_created_user_file):
            with open(self.last_created_user_file, 'r') as f:
                data = json.load(f)
                last_user_file = data.get('last_user_file')
                if last_user_file and os.path.exists(last_user_file):
                    self.user = User.load_from_file(last_user_file)
                    self.update_display()



if __name__ == "__main__":
    attribute_classes = {'Skill': Skill, 'Employment': Employment, 'Education': Education, 'Certificate': Certificate}
    root = tk.Tk()
    root.title('User Information')

    personal_info_frame = InfoFrame(info_class=PersonalInfo, master=root)
    personal_info_frame.grid(row=0, column=0)

    attributes_frame = AttributesFrame(attribute_classes=attribute_classes, master=root)
    attributes_frame.grid(row=0, column=1)

    root.mainloop()