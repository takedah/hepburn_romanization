import unittest
from hepburn_romanization_py.hepburn_romanization import HepburnRomanization


class TestHepburnRomanization(unittest.TestCase):
    def test_to_romaji(self):
        romaji = HepburnRomanization()
        self.assertEqual(romaji.to_romaji("タケダ"), "takeda")
        self.assertEqual(romaji.to_romaji("ダッチ"), "datchi")
        self.assertEqual(romaji.to_romaji("ラッコ"), "rakko")
        self.assertEqual(romaji.to_romaji("シャチョウ"), "shacho")
        self.assertEqual(romaji.to_romaji("ナンバ"), "namba")
        self.assertEqual(romaji.to_romaji("ダンパ"), "dampa")
        self.assertEqual(romaji.to_romaji("ホンマ"), "homma")
        self.assertEqual(romaji.to_romaji("ウリュウチョウ"), "uryucho")
        self.assertEqual(romaji.to_romaji("サトウ"), "sato")
        self.assertEqual(romaji.to_romaji("オオノ"), "ono")
        self.assertEqual(romaji.to_romaji("チョウオン"), "choon")
        self.assertEqual(romaji.to_romaji("ヨコオ"), "yokoo")


if __name__ == "__main__":
    unittest.main()
