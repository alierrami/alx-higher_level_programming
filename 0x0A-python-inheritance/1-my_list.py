#!/usr/bin/python3
"class mylist"


class MyList(list):
    """subclass from list"""

    def print_sorted(self):
        """print the list"""
        print(sorted(self))
