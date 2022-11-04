# -*- coding: utf-8 -*-

"""Path name generator."""

class PathNameGenerator:
    """A abstract class for get a new path name."""
    path_name = -1

    @classmethod
    def new_path_name(cls):
        cls.path_name += 1
        return cls.path_name