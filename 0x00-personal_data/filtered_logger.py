#!/usr/bin/env python3
"""
Definition of filter_datum function that returns an obfuscated log message
"""


from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str):
    """returns log message obfuscated
    """
    # pattern = "|".join(fields)
    # return re.sub(f'({pattern})=[^{separator}]+', f'\\1={redaction}', message)
    for field in fields:
        message = re.sub(field+'=.*?'+separator,
                         field+'='+redaction+separator, message)
    return message
