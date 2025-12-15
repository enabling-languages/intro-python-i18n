# Unicode support

__Current Unicode version:__ 17.0

* [Unicode standard](https://www.unicode.org/versions/Unicode17.0.0/)
* [Core specification](https://www.unicode.org/versions/Unicode17.0.0/core-spec/)
* [Unicode Character Database](https://www.unicode.org/Public/UCD/latest/) (UCD)

## Python

|Python version |Unicode |
|-------------  |------  |
|3.14  |16.0  |
|3.13  |15.1  |
|3.12  |15.0  |
|3.11  |14.0  |
|3.10  |13.0  |
|3.9   |13.0  |
|3.8   |12.1  |
|3.7   |11.0  |
|3.6   |9.0   |
|3.5   |8.0   |
|3.4   |6.3   |
|3.3   |6.1   |

The version of Unicode used by version of Python being used, can be found using the `unicodedata` module:

```py
import unicodedata
print(unicodedata.unidata_version)
```

## PyICU / ICU4C

|ICU4C Release |CLDR |Unicode |
|------------- |---- |------- |
|ICU 77 |47 |16.0 |
|ICU 76 |46 |16.0 |
|ICU 75 |45 |15.1 |
|ICU 74 |44 |15.1 |
|ICU 73 |43 |15 |
|ICU 72 |42 |15 |
|ICU 71 |41 |14 |
|ICU 70 |40 |14 |
|ICU 69 |39 |13 |
|ICU 68 |38 |13 |
|ICU 67 |37 |13 |
|ICU 66 |36.1 |13 |
|ICU 65 |36 |12 |
|ICU 64 |35 |12 |
|ICU 63 |34 |11 |
|ICU 62 |33.1 |11 |
|ICU 61 |33 |10 |
|ICU 60 |32 |10 |
|ICU 59 |31 |9 |
|ICU 58 |30.0.2 |9 |
|ICU 57 |29 |8 |
|ICU 56 |28 |8 |
|ICU 55 |27.0.1 |7 |
|ICU 54 |26 |7 |
|ICU 53 |25 |6.3 |
|ICU 52 |24 |6.3 |
|ICU 51 |23 |6.2 |
|ICU 50 |22.1 |6.2 |
|ICU 49 |21.0.1 |6.1 |

See [icu.unicode.org/download/](https://icu.unicode.org/download/)

The version of Unicode used by the installed version of _icu4c_:

```py
import icu
print(icu.ICU_VERSION)
print(icu.UNICODE_VERSION)
```

## Unicode support for selected packages

A range of modules extend Python's Unicode support, below we list latest versions of modules by the Unicode version they support.

### Unicode 17.0 support

Packages that provide Unicode 17.0 support:

* [graphemeu](https://pypi.org/project/graphemeu/)
* [pyunormalize](https://pypi.org/project/pyunormalize/)
* [unimoji](https://pypi.org/project/unimoji/)
* [what2-grapheme](https://pypi.org/project/what2-grapheme/)

### Unicode 16.0 support

Packages that provide Unicode 16.0 support:

* [demicode](https://pypi.org/project/demicode/)
* [pyuegc](https://pypi.org/project/pyuegc/)
* [regex](https://pypi.org/project/regex/)
* [ugrapheme](https://pypi.org/project/ugrapheme/)
* [unicode-age](https://pypi.org/project/unicode-age/)
* [unicode-charnames](https://pypi.org/project/unicode-charnames/)
* [unicodedata2](https://pypi.org/project/unicodedata2/)
* [unicodedataplus](https://pypi.org/project/unicodedataplus/)
* [unicode-rbnf](https://pypi.org/project/unicode-rbnf/)
* [unicode-segmentation-py](https://pypi.org/project/unicode-segmentation-py/)
* [unidata-blocks](https://pypi.org/project/unidata-blocks/)
* [unisegp](https://pypi.org/project/unisegp/)
* [uniseg](https://pypi.org/project/uniseg/)
* [uwcwidth](https://pypi.org/project/uwcwidth/)

### Unicode 13.0 support

* [grapheme](https://pypi.org/project/grapheme/)

## Other packages

* [charex](https://pypi.org/project/charex/)
* [ftfy](https://pypi.org/project/ftfy/)
* [plsfix](https://pypi.org/project/plsfix/)
* [unicode-charset](https://pypi.org/project/unicode-charset/)
* [wcwidth](https://pypi.org/project/wcwidth/)
* [words-segmentation](https://pypi.org/project/words-segmentation/)
