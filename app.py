
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from toolkit import add_pdfs, remove_selected, move_up, move_down
from PyPDF2 import PdfMerger


class PDFMergerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("PDF Merger Tool")
        self.master.geometry("600x500")
        self.pdf_list = []
        self.listbox = tk.Listbox(master, width=60, height=15)
        self.listbox.pack(pady=10)

        # Progress bar
        self.progress = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(master, variable=self.progress, maximum=100)
        self.progress_bar.pack(fill='x', padx=10, pady=5)

        btn_frame = tk.Frame(master)
        btn_frame.pack()
        tk.Button(btn_frame, text="Add PDFs", command=lambda: add_pdfs(self)).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="Remove Selected", command=lambda: remove_selected(self)).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(btn_frame, text="Move Up", command=lambda: move_up(self)).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="Move Down", command=lambda: move_down(self)).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(btn_frame, text="Merge PDFs", command=self.merge_pdfs_with_progress, bg="green", fg="white").grid(row=2, column=0, columnspan=2, pady=10)

    def merge_pdfs_with_progress(self):
        if not self.pdf_list:
            messagebox.showwarning("Warning", "No PDF files selected!")
            return
        save_path = filedialog.asksaveasfilename(defaultextension=".pdf",
                                                 filetypes=[("PDF Files", "*.pdf")],
                                                 title="Save Merged PDF")
        if save_path:
            try:
                merger = PdfMerger()
                total = len(self.pdf_list)
                for i, pdf in enumerate(self.pdf_list):
                    try:
                        merger.append(pdf)
                    except Exception as e:
                        messagebox.showerror("Error", f"Failed to append {pdf}: {e}")
                    self.progress.set((i+1)/total*100)
                    self.master.update_idletasks()
                merger.write(save_path)
                merger.close()
                messagebox.showinfo("Success", f"Merged PDF saved to:\n{save_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to merge PDFs: {e}")
            self.progress.set(0)

    def on_drop(self, event):
        files = self.master.tk.splitlist(event.data)
        for file in files:
            if file.lower().endswith('.pdf') and file not in self.pdf_list:
                self.pdf_list.append(file)
                self.listbox.insert('end', file.split('/')[-1])
