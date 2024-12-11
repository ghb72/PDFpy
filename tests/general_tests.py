# tests/test_files.py
import unittest
from PDFpy.files import FileManager

class TestFileManager(unittest.TestCase):
    def test_list_files(self):
        result = FileManager.list_files()
        self.assertIsInstance(result, list)

# tests/test_fortran.py
import unittest
from PDFpy.fortran import FortranExecutor

class TestFortranExecutor(unittest.TestCase):
    def test_run_pdf(self):
        # Here you should add specific tests for your Fortran environment
        pass

# tests/test_xyz.py
import unittest
from PDFpy.xyz import XYZFilter

class TestXYZFilter(unittest.TestCase):
    def test_filter_xyz(self):
        # Here you should add specific tests for filtering XYZ files
        pass

if __name__ == '__main__':
    unittest.main()
