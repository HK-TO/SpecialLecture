import unittest
from speciallecture.csv_printer import CSVPrinter


class TestCSVPrinter(unittest.TestCase):

    def test_read1(self):
        
        printer = CSVPrinter("sample.csv")
        line = printer.read()

        self.assertEqual(3, len(line))

    def test_read2(self):
        
        printer = CSVPrinter("sample.csv")
        line = printer.read()

        self.assertEqual(' value2B', line[1][1])

    def test_read3(self):
        
        try:
            printer = CSVPrinter("sample.csv")
            line = printer.read()
            unittest.TestCase.fail("This line should not be involved")
        except Exception as e:
            self.assertRaises(FileNotFoundError)

    # def test_read3_2(self):
        
    #     with self.assertRaises(FileNotFoundError):
    #         printer = CSVPrinter("sample.csv")
    #         printer.read()
