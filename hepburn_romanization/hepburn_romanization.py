import jaconv
import re


class HepburnRomanization:
    def __init__(self):
        pass
        
    @staticmethod
    def _get_romaji(kana):
        """全角カナ1文字をヘボン式ローマ字に変換

        Args:
            kana (str): 全角カナ1文字
        Returns:
            romaji (str): ヘボン式ローマ字
        Notes:
            ローマ字に変換できない場合Noneを返す。

        """

        KANA_TO_ROMAJI = {
                'ア': 'a', 'イ': 'i', 'ウ': 'u', 'エ': 'e', 'オ': 'o',
                'カ': 'ka', 'キ': 'ki', 'ク': 'ku', 'ケ': 'ke', 'コ': 'ko',
                'サ': 'sa', 'シ': 'shi', 'ス': 'su', 'セ': 'se', 'ソ': 'so',
                'タ': 'ta', 'チ': 'chi', 'ツ': 'tsu', 'テ': 'te', 'ト': 'to', 
                'ナ': 'na', 'ニ': 'ni', 'ヌ': 'nu', 'ネ': 'ne', 'ノ': 'no',
                'ハ': 'ha', 'ヒ': 'hi', 'フ': 'fu', 'ヘ': 'he', 'ホ': 'ho',
                'マ': 'ma', 'ミ': 'mi', 'ム': 'mu', 'メ': 'me', 'モ': 'mo',
                'ヤ': 'ya', 'ユ': 'yu', 'ヨ': 'yo',
                'ラ': 'ra', 'リ': 'ri', 'ル': 'ru', 'レ': 're', 'ロ': 'ro',
                'ワ': 'wa', 'ヲ': 'o',
                'ン': 'n',
                'ガ': 'ga', 'ギ': 'gi', 'グ': 'gu', 'ゲ': 'ge', 'ゴ': 'go',
                'ザ': 'za', 'ジ': 'ji', 'ズ': 'zu', 'ゼ': 'ze', 'ゾ': 'zo',
                'ダ': 'da', 'ヂ': 'ji', 'ヅ': 'zu', 'デ': 'de', 'ド': 'do',
                'バ': 'ba', 'ビ': 'bi', 'ブ': 'bu', 'ベ': 'be', 'ボ': 'bo',
                'パ': 'pa', 'ピ': 'pi', 'プ': 'pu', 'ペ': 'pe', 'ポ': 'po',
                'キャ': 'kya', 'キュ': 'kyu', 'キョ': 'kyo',
                'シャ': 'sha', 'シュ': 'shu', 'ショ': 'sho',
                'チャ': 'cha', 'チュ': 'chu', 'チョ': 'cho',
                'ニャ': 'nya', 'ニュ': 'nyu', 'ニョ': 'nyo',
                'ミャ': 'mya', 'ミュ': 'myu', 'ミョ': 'myo',
                'リャ': 'rya', 'リュ': 'ryu', 'リョ': 'ryo',
                'ギャ': 'gya', 'ギュ': 'gyu', 'ギョ': 'gyo',
                'ジャ': 'ja', 'ジュ': 'ju', 'ジョ': 'jo',
                'ビャ': 'bya', 'ビュ': 'byu', 'ビョ': 'byo',
                'ピャ': 'pya', 'ピュ': 'pyu', 'ピョ': 'pyo'
                }
        try:
            return KANA_TO_ROMAJI[kana]
        except:
            return None

    @staticmethod
    def _sokuon(romaji):
        """ヘボン式ローマ字の促音表記を返す

        Args:
            romaji (str): ヘボン式ローマ字
        Returns:
            sokuon (str): ヘボン式ローマ字の促音表記

        """

        if romaji[:1] == 'c':
            return 't'
        else:
            return romaji[:1]

    @staticmethod
    def _hatsuon(romaji):
        """ヘボン式ローマ字の撥音表記を返す

        Args:
            romaji (str): ヘボン式ローマ字
        Returns:
            sokuon (str): ヘボン式ローマ字の促音表記

        """

        return romaji.replace('nb', 'mb').replace('nm', 'mm').replace('np', 'mp')

    @staticmethod
    def _choon(romaji):
        """ヘボン式ローマ字の長音表記を返す

        Args:
            romaji (str): ヘボン式ローマ字
        Returns:
            sokuon (str): ヘボン式ローマ字の長音表記

        """

        if romaji[-2:] == 'oo':
            end_of_string = 'oo'
            romaji = romaji[:-2]
        else:
            end_of_string = ''
        romaji = re.sub('ou|oo', 'o', romaji)
        romaji = re.sub('uu', 'u', romaji)
        return romaji + end_of_string

    def to_romaji(self, kana):
        """カナ文字列をヘボン式ローマ字に変換

        Args:
            kana (str): 全角カナ文字列
        Returns:
            romaji (str): ヘボン式ローマ字文字列

        """
        kana = jaconv.h2z(kana)
        characters = list(kana)
        position = 0
        translated_string = ''
        while position < len(characters):
            # 促音の場合の処理
            if characters[position] == 'ッ':
                next_character = self._get_romaji(characters[position + 1])
                translated_string += self._sokuon(next_character) 
                position += 1
                continue
            # 拗音の場合の処理
            romaji = None
            for num in (2, 1):
                character = ''.join(characters[position:position + num])
                romaji = self._get_romaji(character)
                if romaji is not None:
                    translated_string += romaji
                    position += num
                    break
            if romaji is None:
                position += 1

        # 撥音の場合の処理
        translated_string = self._hatsuon(translated_string)
        # 長音の場合の処理
        translated_string = self._choon(translated_string)

        return translated_string
