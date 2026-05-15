"""
Daughter pipeline stubs.

The daughter-language names are not finalized. Using neutral internal identifiers.
The daughter-language phonological and morphological transformation specs are not complete.
The daughter-language input token stream source is unresolved.

All three pipelines return not_implemented until their specs are supplied.
Do not implement rules here until the specs are provided.
"""

from ..rule import Rule

RULES_A: list[Rule] = []
RULES_B: list[Rule] = []
RULES_C: list[Rule] = []

NOT_IMPLEMENTED = True  # flag checked by pipeline.py
