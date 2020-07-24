import os
import unittest

from deutschlandradio import Deutschlandradio

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATA_DIR = os.path.join(
    BASE_DIR, "data"
)


def get_filepath(filename):
    return os.path.join(DATA_DIR, filename)


class TestRadiodeutschland(unittest.TestCase):

    def check(self, filename, beitragsnummer, betrag, datum, faellig_am):
        ard = Deutschlandradio()
        file_path = get_filepath(filename)

        with open(get_filepath(file_path), "r") as f:
            hocr_data = f.read()

        result = ard.extract(hocr_data)

        self.assertEqual(
            result['simple_keys']['beitragsnummer'],
            beitragsnummer
        )
        self.assertEqual(
            result['simple_keys']['betrag'],
            betrag
        )
        self.assertEqual(
            result['simple_keys']['datum'],
            datum
        )
        self.assertEqual(
            result['simple_keys']['faellig_am'],
            faellig_am
        )

    def test_radio_1(self):
        self.check(
            "radio-1.hocr",
            beitragsnummer='123456789',
            betrag='52,50',
            datum='25.09.2018',
            faellig_am='15.10.2018'
        )

    def test_radio_2(self):
        self.check(
            "radio-2.hocr",
            beitragsnummer='123456789',
            betrag='52,50',
            datum='26.03.2020',
            faellig_am='15.04.2020'
        )

    def test_radio_3(self):
        self.check(
            "radio-3.hocr",
            beitragsnummer='123456789',
            betrag='52,50',
            datum='25.06.2019',
            faellig_am='15.07.2019'
        )

