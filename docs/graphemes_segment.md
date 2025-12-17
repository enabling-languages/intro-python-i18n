# Graphemes: segmentation and tokenisation

> [!IMPORTANT]
> Different solutions detailed below are based on differing versions of Unicode. 
> [Unicode support](https://github.com/enabling-languages/intro-python-i18n/wiki/Unicode-support) details
> of some modules are tracked in this repo.

## Regex

The [regex](https://github.com/mrabarnett/mrab-regex) package supports grapheme segmentation.

```py
import regex as re
t2 = "dɛ̈tëicëkäŋ akɔ̈ɔ̈n"
re.findall(r'\X',t2)
# ['d', 'ɛ̈', 't', 'ë', 'i', 'c', 'ë', 'k', 'ä', 'ŋ', ' ', 'a', 'k', 'ɔ̈', 'ɔ̈', 'n']
```

As can be seen, each grapheme is treated as a single unit, so rather than splitting ɛ̈ into two codepoints or characters, it treats it as a single unit.

For the Dinka string, grapheme segmentation will be consistent across implementations. 

If we look at a Devanagari example, differences can be observed between segmentation by different implementations. On older versions of regex:

```py
t3 = "हिन्दी"
re.findall(r'\X',t3)
# ['हि', 'न्', 'दी']
```

This generates three grapheme clusters for the string.

While on the latest versions:

```py
t3 = "हिन्दी"
re.findall(r'\X',t3)
# ['हि', 'न्दी']
```

We will get two grapheme clusters.

Why the difference? The update to UAX #29 for Unicode 15.1 introduced a new rule to grapheme cluster boundary identification. [GB9c](https://www.unicode.org/reports/tr29/tr29-43.html#GB9c) _`Do not break within certain combinations with Indic_Conjunct_Break (InCB)=Linker`_. For Devanagari, prior to Unicode 15.1 grapheme boundaries occurred within conjunct consonants. With the update to Unicode 15.1 the conjunct consonants form a single grapheme. 

> [!WARNING]
> If you are working with text in South Asian and some South East Asian scripts, and grapheme support is required, it is necessary to use a package that supports Unicode 15.1 as a minimum requirement.
>
> Refer to the [Unicode version](docs/versions.md) notes or the packages' documentation.

```py
import icu
import unicodedataplus as ud
linkers = icu.UnicodeSet(r'\p{InCB=Linker}')
for linker in linkers:
    print(f'{ord(linker):04X}\t{linker}\t{ud.name(linker)}\t{ud.block(linker)}')
# 094D	्	DEVANAGARI SIGN VIRAMA	Devanagari
# 09CD	্	BENGALI SIGN VIRAMA	Bengali
# 0ACD	્	GUJARATI SIGN VIRAMA	Gujarati
# 0B4D	୍	ORIYA SIGN VIRAMA	Oriya
# 0C4D	్	TELUGU SIGN VIRAMA	Telugu
# 0D4D	്	MALAYALAM SIGN VIRAMA	Malayalam
```

The key difference is that UAX #29 for Unicode 15.1 onwards treats `094D ( ् ) DEVANAGARI SIGN VIRAMA` as extending the grapheme cluster, while before Unicode 15.1, `U+094D` did not extend the grapheme cluster. 

The following overview of other grapheme solutions will use the latest version of the modules. For the Devanagari example modules using a pre-Unicode 15.1 implementation will give three graphemes and newer solutions will give two.

## Grapheme

Alternatively we could use the [grapheme](https://github.com/alvinlindstam/grapheme) package, which provides a number of functions to manipulate strings using graphemes as the basic unit, rather than individual codepoints, as standard Python string operations do.

__*N.B. The __grapheme__ package hasn't been updated since 2020, and is based on an older version of UAX #29.*__

```py
import grapheme
grapheme.UNICODE_VERSION
# '13.0.0'
list(grapheme.graphemes(t2))
# ['d', 'ɛ̈', 't', 'ë', 'i', 'c', 'ë', 'k', 'ä', 'ŋ', ' ', 'a', 'k', 'ɔ̈', 'ɔ̈', 'n']
```

Likewise, *grapheme* package gives us three grapheme clusters:

```py
list(grapheme.graphemes(t3))
['हि', 'न्', 'दी']
```

## PyICU: 

### Using a break iterator

Alternatively, we could use [PyICU](https://gitlab.pyicu.org/main/pyicu), with icu4c, for grapheme tokenisation.

Using *pyicu* is more complex than using *regex* or *grapheme*, many of the functions available in *icu4c* are low level functions, and it is necessary to develop your own wrapper around it. The break iterator returns a set of breakpoints in the string. It is necessary to iterate through the breakpoints. The [PyICU cheat sheet](https://gist.github.com/dpk/8325992) has a useful function, `iterate_breaks()`, to iterate through each breakpoint in the string.

We then need to create a break iterator instance, and then pass the string and instance to `iterate_breaks()`. In this instance, I will use the root locale for the break iterator.

```py
import icu
def iterate_breaks(text, break_iterator):
    text = icu.UnicodeString(text)
    break_iterator.setText(text)
    lastpos = 0
    while True:
        next_boundary = break_iterator.nextBoundary()
        if next_boundary == -1: return
        yield str(text[lastpos:next_boundary])
        lastpos = next_boundary
bi = icu.BreakIterator.createCharacterInstance(icu.Locale.getRoot())
list(iterate_breaks(t2, bi))
# ['d', 'ɛ̈', 't', 'ë', 'i', 'c', 'ë', 'k', 'ä', 'ŋ', ' ', 'a', 'k', 'ɔ̈', 'ɔ̈', 'n']
```

Alternative code we use in our internal projects:

```py
import icu
def generate_tokens(text, brkiter = None):
    if brkiter is None:
        brkiter = icu.BreakIterator.createWordInstance(icu.Locale.getRoot())
    text = icu.UnicodeString(text)
    brkiter.setText(text)
    i = brkiter.first()
    for j in brkiter:
        yield str(text[i:j])
        i = j

def get_generated_tokens(text, bi = None):
    return [*generate_tokens(text, brkiter=bi)]

iter = icu.BreakIterator.createCharacterInstance(icu.Locale('und'))
get_generated_tokens(t2, iter)
# ['d', 'ɛ̈', 't', 'ë', 'i', 'c', 'ë', 'k', 'ä', 'ŋ', ' ', 'a', 'k', 'ɔ̈', 'ɔ̈', 'n']
```

If we look at the Devanagari string:

```py
get_generated_tokens(t3, iter)
# ['हि', 'न्दी']
```

The *icu4c* break iterator generates two grapheme clusters. 

### ICU regular expressions

Alternatively, it is possible to use `icu.RegexMatcher` to split a string into graphemes:

```py
def find_all(pattern, text, flag=0):
    results = []
    matcher = icu.RegexMatcher(pattern, text, flag)
    while matcher.find():
        results.append(matcher.group())
    return results
find_all(r'\X', t3)
# ['हि', 'न्दी']
```

`icu.RegexMatcher` returns two graphemes.

## graphemeu

This package is a fork of the [grapheme](#grapheme) package and current versions support Unicode 16.0.

```py
from grapheme import graphemes
list(graphemes(t3))
# ['हि', 'न्दी']
```

## pyuegc

Then there is [pyuegc](https://pypi.org/project/pyuegc/).

```py
from pyuegc import EGC, UCD_VERSION
UCD_VERSION
# '16.0.0'

EGC(t2)
# ['d', 'ɛ̈', 't', 'ë', 'i', 'c', 'ë', 'k', 'ä', 'ŋ', ' ', 'a', 'k', 'ɔ̈', 'ɔ̈', 'n']

EGC(t3)
['हि', 'न्दी']
```

*pyegc* splits the string into two grapheme clusters.

## ugrapheme

Another solution is [ugrapheme](https://pypi.org/project/ugrapheme/), which also uses the latest version of Unicode. Unlike the other solutions, _ugrapheme_ creates a class instance providing a range of methods for working with and manipulating strings on a grapheme level rather than a character or codepoint level. To mimic the other solutions, you can cast the object to a list:

```py
from ugrapheme import graphemes
grs = graphemes(t3)
[*grs]    # list(grs)
# ['हि', 'न्दी']
```

or, alternatively  use the `grapheme_split()` function:

```py
from ugrapheme import grapheme_split
grapheme_split(t3)
# ['हि', 'न्दी']
```

## unicode_segmentation_py

The package [unicode_segmentation_py](https://pypi.org/project/unicode-segmentation-py/) is another segmentation tool, which can segment graphemes, words, or sentences.

To identify the version of Unicode supported:

```py
import unicode_segmentation_py as useg
print(useg.UNICODE_VERSION)
```

For grapheme segmentation:

```py
useg.to_graphemes(t2)
# ['d', 'ɛ̈', 't', 'ë', 'i', 'c', 'ë', 'k', 'ä', 'ŋ', ' ', 'a', 'k', 'ɔ̈', 'ɔ̈', 'n']

useg.to_graphemes(t3)
# ['हि', 'न्दी']
```

## uniseg

The [uniseg](https://pypi.org/project/uniseg/) package provides a segmentation solution that handles codepoint, grapheme, word, sentence and line segmentation:

```py
from uniseg.graphemecluster import grapheme_clusters
list(grapheme_clusters(t3))
['हि', 'न्दी']
```

The version if Unicode supported can be identified by:

```py
print(uniseg.unidata_version)
```

## unisegp

The package [unisegp](https://pypi.org/project/unisegp/) is a fork of _uniseg_, and provides a segmentation solution that handles codepoint, grapheme, word, sentence and line segmentation:

```py
from uniseg import unidata_version
unidata_version
# 16.0

from uniseg.graphemecluster import grapheme_clusters
list(grapheme_clusters(t2))
# ['d', 'ɛ̈', 't', 'ë', 'i', 'c', 'ë', 'k', 'ä', 'ŋ', ' ', 'a', 'k', 'ɔ̈', 'ɔ̈', 'n']

list(grapheme_clusters(t3))
# ['हि', 'न्दी']
```

## what2-grapheme

The package [what2-grapheme](https://pypi.org/project/what2-grapheme/):


---

![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)
This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
[Enabling Languages](https://github.com/enabling-languages/), 2025.
