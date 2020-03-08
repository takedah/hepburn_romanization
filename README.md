Hepburn Romanization
========

カナ文字列をヘボン式ローマ字に変換します。

https://github.com/takedah/hepburn-romanization のPython版です。

# Requirement

- jaconv

# Usage

サンプルコードです。

```
from hepburn_romanization.hepburn_romanization import HepburnRomanization

hr = HepburnRomanization()
print(hr.to_romaji("ウリュウチョウ"))
```

次のように出力されます。

```
uryucho
```

# Author

- Hiroki Takeda
- takedahiroki@gmail.com

# Linsence

Hepburn Romanization is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
