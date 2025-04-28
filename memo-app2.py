import tkinter as tk
from tkinter import filedialog

def save_memo():
    title = title_entry.get()
    memo_text = text_area.get("1.0", tk.END)
    if not title:
        title = "無題"

    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        initialfile=f"{title}.txt",
        filetypes=[("Text files", "*.txt")]
    )
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(memo_text)


root = tk.Tk()
root.title("シンプルメモアプリ")
root.geometry("400x450")

title_label = tk.Label(root, text="タイトル:", font=("Arial", 12))
title_label.pack(pady=(10, 0))

title_entry = tk.Entry(root, font=("Arial", 12))
title_entry.pack(fill="x", padx=10, pady=(0, 10))

text_area = tk.Text(root, font=("Arial", 12))
text_area.pack(expand=True, fill="both", padx=10)


save_button = tk.Button(root, text="保存する", command=save_memo)
save_button.pack(pady=10)

root.mainloop()
