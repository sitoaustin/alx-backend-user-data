#!/usr/bin/env python3
"""Regex-ing
"""


from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str):
    """returns log message obfuscated
    """
    pattern = "|".join(fields)
    return re.sub(f'({pattern})=[^{separator}]+', f'\\1={redaction}', message)
