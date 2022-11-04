# -*- coding: utf-8 -*-

"""Exceptions for errors raised by Photoniqlab."""

class PhotoniqlabError(Exception):
    """Base class for errors raised by Photoniqlab."""

    def __init__(self, *message):
        """Set the error message."""
        super().__init__(' '.join(message))
        self.message = ' '.join(message)

    def __str__(self):
        """Return the message."""
        return repr(self.message)
