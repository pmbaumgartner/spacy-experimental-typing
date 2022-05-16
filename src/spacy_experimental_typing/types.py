from collections.abc import Container
from typing import Any, Dict, List, Literal, Type, Union

from typing_extensions import TypedDict

ExtendedPattern = TypedDict(
    "ExtendedPattern",
    {
        "IN": Container,
        "NOT_IN": Container,
        "IS_SUBSET": Container,
        "IS_SUPERSET": Container,
        "INTERSECTS": Container,
        "==": Any,
        ">=": Any,
        "<=": Any,
        ">": Any,
        "<": Any,
        "REGEX": str,
    },
    total=False,
)

MatchValue = Union[str, ExtendedPattern]

MatcherTokenAttribute = TypedDict(
    "MatcherTokenAttribute",
    {
        "ORTH": MatchValue,
        "TEXT": MatchValue,
        "NORM": MatchValue,
        "LOWER": MatchValue,
        "LENGTH": int,
        "IS_ALPHA": bool,
        "IS_ASCII": bool,
        "IS_DIGIT": bool,
        "IS_LOWER": bool,
        "IS_UPPER": bool,
        "IS_TITLE": bool,
        "IS_PUNCT": bool,
        "IS_SPACE": bool,
        "IS_STOP": bool,
        "IS_SENT_START": bool,
        "LIKE_NUM": bool,
        "LIKE_URL": bool,
        "LIKE_EMAIL": bool,
        "SPACY": bool,
        "POS": MatchValue,
        "TAG": MatchValue,
        "MORPH": MatchValue,
        "DEP": MatchValue,
        "LEMMA": MatchValue,
        "SHAPE": MatchValue,
        "ENT_TYPE": MatchValue,
        "_": Dict[str, Any],
        "OP": Literal["!", "?", "+", "*"],
    },
    total=False,
)


MatcherPattern = List[MatcherTokenAttribute]
MatcherRules = List[MatcherPattern]
