import unittest
from unittest.mock import MagicMock
import toolkit

class DummyApp:
    def __init__(self):
        self.pdf_list = []
        self.listbox = MagicMock()
        self.listbox.curselection = MagicMock(return_value=[0])
        self.listbox.delete = MagicMock()
        self.listbox.insert = MagicMock()
        self.listbox.selection_set = MagicMock()

class TestToolkit(unittest.TestCase):
    def setUp(self):
        self.app = DummyApp()
        self.app.pdf_list = ["a.pdf", "b.pdf", "c.pdf"]

    def test_move_up(self):
        self.app.listbox.curselection.return_value = [1]
        toolkit.move_up(self.app)
        self.assertEqual(self.app.pdf_list, ["b.pdf", "a.pdf", "c.pdf"])

    def test_move_down(self):
        self.app.listbox.curselection.return_value = [1]
        toolkit.move_down(self.app)
        self.assertEqual(self.app.pdf_list, ["a.pdf", "c.pdf", "b.pdf"])

    def test_remove_selected(self):
        self.app.listbox.curselection.return_value = [1]
        toolkit.remove_selected(self.app)
        self.assertEqual(self.app.pdf_list, ["a.pdf", "c.pdf"])

    def test_update_listbox(self):
        toolkit.update_listbox(self.app)
        self.app.listbox.insert.assert_any_call('end', 'a.pdf')
        self.app.listbox.insert.assert_any_call('end', 'b.pdf')
        self.app.listbox.insert.assert_any_call('end', 'c.pdf')

if __name__ == "__main__":
    unittest.main()
    
