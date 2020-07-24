import re

from hocron import Hocron, LinePattern


class Deutschlandradio:

    SIMPLE_KEYS = [
        'context',
        'betrag',
        'beitragsnummer',
        'faellig_am',
        'datum'
    ]

    def extract(self, hocr):
        result = {
            'simple_keys': {
                'context': 'ARD ZDF Deutschlandradio',
                'betrag': None,
                'beitragsnummer': None,
                'faellig_am': None,
                'datum': None
            },
            'comp_key': []
        }
        # hocron module is a thin layer of API for HOCR format
        # processing
        hocr = Hocron(hocr)

        beitragsnummer_line_pattern = LinePattern(
            [
                'Beitragsnummer',
                re.compile('^\d\d\d$'),
                re.compile('^\d\d\d$'),
                re.compile('^\d\d\d$')
            ]  # noqa

        )
        betrag_line_pattern = LinePattern(
            [
                'Betrag',
                'von',
                re.compile('\d+,\d+'),
            ]  # noqa

        )
        datum_line_pattern = LinePattern(
            [
                'Datum',
                re.compile('\d\d\.\d\d\.\d\d\d\d'),
            ]  # noqa
        )
        datum_line_pattern = LinePattern(
            [
                'Datum',
                re.compile('\d\d\.\d\d\.\d\d\d\d'),
            ]  # noqa
        )
        faellig_am_line_pattern = LinePattern(
            [
                'sind',
                'am',
                re.compile('\d\d\.\d\d\.\d\d\d\d'),
                'fällig.'
            ]  # noqa
        )
        beitragsnummer = hocr.get_labeled_value(beitragsnummer_line_pattern)
        betrag = hocr.get_labeled_value(betrag_line_pattern)
        datum = hocr.get_labeled_value(datum_line_pattern)
        faellig_am = hocr.get_labeled_value(faellig_am_line_pattern)
        # in future there will be 'comp keys', that's why
        # it is a good idea to keep a separate namespace
        result['simple_keys']['betrag'] = betrag
        result['simple_keys']['beitragsnummer'] = beitragsnummer
        result['simple_keys']['datum'] = datum
        result['simple_keys']['faellig_am'] = faellig_am

        return result
