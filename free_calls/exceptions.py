"""Custom exceptions for free_calls"""


class NoValidAPIKeyError(Exception):
    """Raised when all API keys have been exhausted"""
    pass
