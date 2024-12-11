# tests/test_pdf.py
import unittest
from PDFpy.pdf_pyrunner import PDFCalculator
import numpy as np

class TestPDFCalculator(unittest.TestCase):
    def test_histogram(self):
        pdf_calc = PDFCalculator('example.xyz')
        hist, dmean = pdf_calc.histogram()
        self.assertIsInstance(hist, np.ndarray)
        self.assertIsInstance(dmean, float)

    def test_smooth(self):
        pdf_calc = PDFCalculator('example.xyz')
        hist, dmean = pdf_calc.histogram()
        smoothed = pdf_calc.smooth(hist, 10)
        self.assertIsInstance(smoothed, list)

    def test_gauss_convolution(self):
        pdf_calc = PDFCalculator('example.xyz')
        hist, dmean = pdf_calc.histogram()
        gauss = pdf_calc.gauss_convolution(hist, 1.0)
        self.assertIsInstance(gauss, np.ndarray)

    def test_calc_pdf(self):
        pdf_calc = PDFCalculator('example.xyz')
        hist, dmean = pdf_calc.histogram()
        pdf_calc.calc_pdf(hist)
        # Add more assertions as needed

if __name__ == '__main__':
    unittest.main()
