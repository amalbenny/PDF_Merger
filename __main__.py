
from tkinterdnd2 import TkinterDnD
from app import PDFMergerApp

if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app = PDFMergerApp(root)
    root.mainloop()