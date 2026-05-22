import tkinter as tk
from tkinter import filedialog, messagebox
from excel_handler import read_excel, save_excel
from crypto_utils import encrypt_value


class EncryptApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Excel Encrypt Tool")
        self.root.geometry("600x500")

        self.file_path = ""
        self.df = None

        tk.Button(
            root,
            text="Choose Excel File",
            command=self.choose_file
        ).pack(pady=10)

        self.columns_listbox = tk.Listbox(
            root,
            selectmode=tk.MULTIPLE,
            width=60,
            height=15
        )
        self.columns_listbox.pack()

        tk.Label(root, text="Encryption Key").pack()

        self.key_entry = tk.Entry(root, show="*", width=40)
        self.key_entry.pack()

        tk.Button(
            root,
            text="Encrypt",
            command=self.encrypt_columns,
            bg="green",
            fg="white"
        ).pack(pady=20)

    def choose_file(self):
        self.file_path = filedialog.askopenfilename(
            filetypes=[
                ("Excel Files",
                 "*.xls *.xlsx *.xlsm *.xlsb *.ods")
            ]
        )

        if self.file_path:
            self.df = read_excel(self.file_path)

            self.columns_listbox.delete(0, tk.END)

            for col in self.df.columns:
                self.columns_listbox.insert(tk.END, col)

    def encrypt_columns(self):
        selected_indexes = self.columns_listbox.curselection()

        if not selected_indexes:
            messagebox.showerror(
                "Error",
                "Please select columns"
            )
            return

        password = self.key_entry.get()

        if not password:
            messagebox.showerror(
                "Error",
                "Enter encryption key"
            )
            return

        selected_columns = [
            self.columns_listbox.get(i)
            for i in selected_indexes
        ]

        for col in selected_columns:
            self.df[col] = self.df[col].apply(
                lambda x: encrypt_value(x, password)
            )

        output = save_excel(
            self.df,
            self.file_path,
            "encrypted"
        )

        messagebox.showinfo(
            "Success",
            f"Encrypted file saved:\n{output}"
        )


root = tk.Tk()
app = EncryptApp(root)
root.mainloop()