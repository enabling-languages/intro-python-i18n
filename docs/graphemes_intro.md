# Graphemes: introduction

> [!IMPORTANT]
> Different solutions detailed below are based on differing versions of Unicode. 
> [Unicode support](versions.md) details
> of some modules are tracked in this repo.

When working with tokenisation and break iterators, it is sometimes necessary to work at the character, syllable, line, or sentence levels. Character level tokenisation is an interesting case. Character level tokenisation could be by character (or codepoint) or by grapheme. A Grapheme is:

<blockquote cite='https://www.unicode.org/glossary/#grapheme'>
<ol>
    <li>A minimally distinctive unit of writing in the context of a particular writing system. For example, ‹b› and ‹d› are distinct graphemes in English writing systems because there exist distinct words like big and dig. Conversely, a lowercase italiform letter a and a lowercase Roman letter a are not distinct graphemes because no word is distinguished on the basis of these two different forms. </li>
    <li>What a user thinks of as a character.</li>
</ol>
<footer style="text-align: end"><a href="https://www.unicode.org/glossary/#grapheme">Grapheme</a>, <a href="https://unicode.org/glossary/"><i class="title">Unicode Glossary</i></a>.</footer>
</blockquote>

The usual way developers handle character level tokenisation of English is via list comprehension or typecasting a string to a list:

```py
>>> t1 = "transformation"
>>> list(t1)
['t', 'r', 'a', 'n', 's', 'f', 'o', 'r', 'm', 'a', 't', 'i', 'o', 'n']

>>> [char for char in t1]
['t', 'r', 'a', 'n', 's', 'f', 'o', 'r', 'm', 'a', 't', 'i', 'o', 'n']

>>> [*t1]
['t', 'r', 'a', 'n', 's', 'f', 'o', 'r', 'm', 'a', 't', 'i', 'o', 'n']
```

This will give you discrete characters, but this approach doesn't work as well for other languages.

Let's take a [Dinka](https://en.wikipedia.org/wiki/Dinka_language) string as an example:

```py
>>> t2 = "dɛ̈tëicëkäŋ akɔ̈ɔ̈n"
>>> [char for char in t2]
['d', 'ɛ', '̈', 't', 'ë', 'i', 'c', 'ë', 'k', 'ä', 'ŋ', ' ', 'a', 'k', 'ɔ', '̈', 'ɔ', '̈', 'n']
```

There is a mixture of precomposed and decomposed character sequences.

```py
>>> import unicodedata as ud
>>> ud.is_normalized('NFC', t2)
True
```

The text is fully precomposed, using Unicode Normalization Form C, but many character sequences that should be treated as a single unit do not exist as single codepoints. How do we work with ä vs ɛ̈? Unicode defines grapheme cluster boundaries in the annex on [Unicode Text segmentation](https://unicode.org/reports/tr29/#Grapheme_Cluster_Boundaries) (UAX #29).

Python has no internal support for handling and processing strings at the grapheme level, although a number of Python packages implement grapheme cluster segmentation based on [UAX #29](https://unicode.org/reports/tr29/#Grapheme_Cluster_Boundaries).

_Unicode documentation refers to legacy grapheme clusters, extended grapheme clusters, and tailored grapheme clusters. Generally, when graphemes are referred to, extended grapheme clusters are meant._

---

![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)
This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
[Enabling Languages](https://github.com/enabling-languages/), 2025.
