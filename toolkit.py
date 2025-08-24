from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger

def add_pdfs(self):
    """Open a file dialog to select PDF files and add them to the list."""
    try:
        files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
        for file in files:
            if file not in self.pdf_list:
                self.pdf_list.append(file)
                self.listbox.insert('end', file.split("/")[-1])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add PDFs: {e}")

def remove_selected(self):
    """Remove selected PDFs from the list."""
    try:
        selected = self.listbox.curselection()
        for index in reversed(selected):
            self.listbox.delete(index)
            self.pdf_list.pop(index)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to remove selected PDFs: {e}")

def move_up(self):
    """Move the selected PDF up in the list."""
    try:
        selected = self.listbox.curselection()
        if selected and selected[0] > 0:
            index = selected[0]
            self.pdf_list[index], self.pdf_list[index-1] = self.pdf_list[index-1], self.pdf_list[index]
            update_listbox(self)
            self.listbox.selection_set(index-1)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to move PDF up: {e}")

def move_down(self):
    """Move the selected PDF down in the list."""
    try:
        selected = self.listbox.curselection()
        if selected and selected[0] < len(self.pdf_list) - 1:
            index = selected[0]
            self.pdf_list[index], self.pdf_list[index+1] = self.pdf_list[index+1], self.pdf_list[index]
            update_listbox(self)
            self.listbox.selection_set(index+1)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to move PDF down: {e}")

def update_listbox(self):
    """Refresh the listbox to show current PDFs."""
    self.listbox.delete(0, 'end')
    for file in self.pdf_list:
        self.listbox.insert('end', file.split("/")[-1])

def merge_pdfs(self):
    """Merge selected PDFs and save to a file."""
    if not self.pdf_list:
        messagebox.showwarning("Warning", "No PDF files selected!")
        return
    save_path = filedialog.asksaveasfilename(defaultextension=".pdf",
                                             filetypes=[("PDF Files", "*.pdf")],
                                             title="Save Merged PDF")
    if save_path:
        try:
            merger = PdfMerger()
            for pdf in self.pdf_list:
                try:
                    merger.append(pdf)
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to append {pdf}: {e}")
            merger.write(save_path)
            merger.close()
            messagebox.showinfo("Success", f"Merged PDF saved to:\n{save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to merge PDFs: {e}")
        messagebox.showinfo("Success", f"Merged PDF saved to:\n{save_path}")
