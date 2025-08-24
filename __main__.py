import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger

class PDFMergerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("PDF Merger Tool")
        self.master.geometry("500x400")
        
        self.pdf_list = []

        # Listbox to display selected PDFs
        self.listbox = tk.Listbox(master, width=60, height=15)
        self.listbox.pack(pady=10)

        # Button frame
        btn_frame = tk.Frame(master)
        btn_frame.pack()

        tk.Button(btn_frame, text="Add PDFs", command=self.add_pdfs).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="Remove Selected", command=self.remove_selected).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(btn_frame, text="Move Up", command=self.move_up).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="Move Down", command=self.move_down).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(btn_frame, text="Merge PDFs", command=self.merge_pdfs, bg="green", fg="white").grid(row=2, column=0, columnspan=2, pady=10)

    def add_pdfs(self):
        files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
        for file in files:
            if file not in self.pdf_list:
                self.pdf_list.append(file)
                self.listbox.insert(tk.END, file.split("/")[-1])

    def remove_selected(self):
        selected = self.listbox.curselection()
        for index in reversed(selected):
            self.listbox.delete(index)
            self.pdf_list.pop(index)

    def move_up(self):
        selected = self.listbox.curselection()
        if selected and selected[0] > 0:
            index = selected[0]
            self.pdf_list[index], self.pdf_list[index-1] = self.pdf_list[index-1], self.pdf_list[index]
            self.update_listbox()
            self.listbox.selection_set(index-1)

    def move_down(self):
        selected = self.listbox.curselection()
        if selected and selected[0] < len(self.pdf_list) - 1:
            index = selected[0]
            self.pdf_list[index], self.pdf_list[index+1] = self.pdf_list[index+1], self.pdf_list[index]
            self.update_listbox()
            self.listbox.selection_set(index+1)

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for file in self.pdf_list:
            self.listbox.insert(tk.END, file.split("/")[-1])

    def merge_pdfs(self):
        if not self.pdf_list:
            messagebox.showwarning("Warning", "No PDF files selected!")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".pdf",
                                                 filetypes=[("PDF Files", "*.pdf")],
                                                 title="Save Merged PDF")
        if save_path:
            merger = PdfMerger()
            for pdf in self.pdf_list:
                merger.append(pdf)
            merger.write(save_path)
            merger.close()
            messagebox.showinfo("Success", f"Merged PDF saved to:\n{save_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()