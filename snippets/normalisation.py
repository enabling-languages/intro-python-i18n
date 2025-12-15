# Normalisation helper functions
#   Wrappers for normalisation functions that will select normalisation engine based on
#   availability and falling back from pyicu to unicodedataplus to unicodedata
# 
# Copyright 2025 Enabling Languages
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and 
# associated documentation files (the “Software”), to deal in the Software without restriction, including 
# without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the 
# following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT 
# LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO 
# EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER 
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE 
# USE OR OTHER DEALINGS IN THE SOFTWARE.

from functools import partial
import regex

#
# Determine and install module for normalisation, using the priority sequence: 
# pyicu > unicodedataplus > unicodedata
#
try:
    import icu
    USE_ICU = True
    USE_UDP = False
    UVERSION = icu.UNICODE_VERSION 
except ModuleNotFoundError:
    try:
        import unicodedataplus as ud
        USE_UDP = True
    except ModuleNotFoundError:
        import unicodedata as ud
        USE_UDP = False
    USE_ICU = False
    UVERSION = ud.unidata_version

def to_NFKC_Casefold(text: str, use_icu: bool = USE_ICU) -> str:
    """ Perform NFKC_Casefold on string.

    Args:
        text (str): input string
        use_icu (bool, optional): Whether to use PyICU for normalisation . Defaults to USE_ICU value.

    Returns:
        str: normalised string
    """    
    if use_icu:
        normaliser = icu.Normalizer2.getNFKCCasefoldInstance()
        return normaliser.normalize(text)
    pattern = regex.compile(r"\p{Default_Ignorable_Code_Point=Yes}")
    text = regex.sub(pattern, '', text)
    return ud.normalize("NFC", ud.normalize('NFKC', text).casefold())

def normalise(nf: str, text: str, use_icu: bool = USE_ICU) -> str:
    """ Perform Unicode normalisation on string.

    Args:
        nf (str): Unicode normalisation form: one of "NFC", "NFD", "NFKC", "NFKD", "NFKC_CF"
        text (str): input string
        use_icu (bool, optional): whether to use PyICU for normalisation. Defaults to USE_ICU value.

    Returns:
        str: normalised string
    """
    nf = nf.upper()
    if use_icu:
        match nf:
            case "NFKC_CF":
                normaliser = icu.Normalizer2.getNFKCCasefoldInstance()
            case "NFKC":
                normaliser = icu.Normalizer2.getNFKCInstance()
            case "NFD":
                normaliser = icu.Normalizer2.getNFDInstance()
            case "NFKD":
                normaliser = icu.Normalizer2.getNFKDInstance()
            case _:
                normaliser = icu.Normalizer2.getNFCInstance()
        return normaliser.normalize(text)
    elif not use_icu and nf == "NFKC_CF":
        return to_NFKC_Casefold(text, use_icu = False)
    else:
        return ud.normalize(nf, text)

NFC = partial(normalise, "NFC", use_icu = USE_ICU)
NFC.__doc__ = """ Perform NFC normalisation on string."""
NFD = partial(normalise, "NFD", use_icu = USE_ICU)
NFD.__doc__ = """ Perform NFD normalisation on string."""
NFKC = partial(normalise, "NFKC", use_icu = USE_ICU)
NFKC.__doc__ = """ Perform NFKC normalisation on string."""
NFKD = partial(normalise, "NFKD", use_icu = USE_ICU)
NFKD.__doc__ = """ Perform NFKD normalisation on string."""
NFKC_CF = partial(normalise, "NFKC_CF", use_icu = USE_ICU)
NFKC_CF.__doc__ = """ Perform NFKC_Casefold normalisation on string."""
