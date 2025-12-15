# An idiosyncratic exploration of Python internationalisation

*This repo is based on notes developed for internal projects, and made available as a community resource. Over time additional topics will become available.*

> [!NOTE]
> The key documents, discussing internationalisation, in the Python documentation are the [Unicode HOWTO](https://docs.python.org/3/howto/unicode.html) and [Internationalisation modules](https://docs.python.org/3/library/i18n.html), which discusses [`gettext`](https://docs.python.org/3/library/gettext.html) and [`locale`](https://docs.python.org/3/library/locale.html).

## Introduction

The Unicode glossary defines internationalisation as:

<blockquote cite="https://unicode.org/glossary/#internationalization">
<p>The process of designing and implementing a software product so that it can be easily localized, with few if any structural changes. Ideally, an internationalized software product can be localized simply by translating messages and other text displayed to a user, and by adapting icons and other visual elements. An "internationalized" software product is also known as a "localizable" product. Also known by the abbreviation "i18n" and the term "World-Readiness".</p>
<footer><a href="https://unicode.org/glossary/#internationalization">Internationalization</a>, <a href="https://unicode.org/glossary/"><i class="title">Unicode Glossary</i></a>.</footer></blockquote>

The Unicode definition aligns with the definitions from other sources, including Python's documentation, and aligns with many developers' understanding of internationalisation.

For global projects, or projects focusing on lesser used and minority languages, it is necessary to go beyond the basic understanding of internationalisation support that only focuses on localisation infrastructure.

## Python internationalisation

Python's inbuilt modules are:

- Language and locale insensitive, although some can use libc based formatting and parsing.
- Will have varying degrees of support for Unicode.
- May yield different results than other languages and tools.

### Documentation

1. [Unicode versions](docs/versions.md) supported by Python, ICU4C, and selected packages.
2. Strings
   1. Codepoints, code units and characters
   2. Normalisation
   3. [Graphemes](docs/graphemes.md)
       1. Introduction
       2. Segmentation and tokenisation
       3. Indexing and splicing 
   4. Case mapping
   5. Case insensitivity
      1. Case folding
      2. String matching and comparison
      3. Collation 
   6. Segmentation
   7. Transliteration
<<<<<<< HEAD
   8. Other string transformations
3. Sorting
=======
   9. Other string transformations
4. Sorting
>>>>>>> ba57ba3e1cbbd643d5da87c90c3f1466fa3d051b
    1. Introduction
    2. Locale
    3. Unicode collation and sorting
       1. PyUCA
       2. PyICU
       3. Sorting emoji
    4. Natural sorting
    5. Various packages:
       1. Pandas

---

![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)
This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
[Enabling Languages](https://github.com/enabling-languages/), 2025.

