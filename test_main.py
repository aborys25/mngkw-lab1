import unittest
from unittest import TestCase
import main
import unittest
import csv


class Test(TestCase):

    def odczyt(ktoraKolumne):
        kolumnatestujaca = []
        with open("details.csv", "r", encoding="utf-8") as plik:
            read = csv.reader(plik)
            for wiersz in read:
                kolumnatestujaca.append(wiersz[ktoraKolumne])

        return kolumnatestujaca

    def test_odczyt(self):
        kolumny = main.readCSV()
        kolumna1 = kolumny[0]
        kolumna2 = kolumny[1]
        kolumna1test = Test.odczyt(0)
        kolumna2test = Test.odczyt(1)

        self.assertEqual(kolumna1, kolumna1test)
        self.assertEqual(kolumna2, kolumna2test)

    def test_kolumna3(self):
        kolumna3 = main.kolumna3(Test.odczyt(1))
        kolumna3test = Test.odczyt(2)
        self.assertEqual(kolumna3, kolumna3test)

    def test_kolumna4(self):
        kolumna4 = main.kolumna4(Test.odczyt(1))
        kolumna4test = Test.odczyt(3)
        self.assertEqual(kolumna4, kolumna4test)

    def test_kolumna5(self):
        kolumna5 = main.kolumna5(Test.odczyt(1))
        kolumna5test = Test.odczyt(4)
        self.assertEqual(kolumna5, kolumna5test)

    def test_kolumna6(self):
        kolumna6 = main.kolumna6(Test.odczyt(1))
        kolumna6test = Test.odczyt(5)
        self.assertEqual(kolumna6, kolumna6test)

    def test_kolumna7(self):
        kolumna7 = main.kolumna7(Test.odczyt(1))
        kolumna7test = Test.odczyt(6)
        self.assertEqual(kolumna7, kolumna7test)

    def test_kolumna8(self):
        kolumna8 = main.kolumna8(Test.odczyt(0))
        kolumna8test = Test.odczyt(7)
        self.assertEqual(kolumna8, kolumna8test)

    def test_kolumna9(self):
        kolumna9 = main.kolumna9(Test.odczyt(0))
        kolumna9test = Test.odczyt(8)
        self.assertEqual(kolumna9, kolumna9test)

    def test_kolumna10(self):
        kolumna10 = main.kolumna10(Test.odczyt(0))
        kolumna10test = Test.odczyt(9)
        self.assertEqual(kolumna10, kolumna10test)

if __name__ == '__main__':
    unittest.main()

