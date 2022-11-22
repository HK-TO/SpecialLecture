import unittest
from speciallecture.csv_printer import CSVPrinter


class TestCSVPrinter(unittest.TestCase):

    def test_read(self):
        
        with self.assertRaises(FileNotFoundError):
            printer = CSVPrinter("sample2.csv")
            l = printer.read()

        self.assertEqual(2, len(l))
