import unittest
from speciallecture.csv_printer import CSVPrinter


class TestCSVPrinter(unittest.TestCase):

    def test_read(self):
        
        # with self.assertRaises(FileNotFoundError):
        printer = CSVPrinter("sample.csv")
        l = printer.read()

        self.assertEqual(3, len(l))
