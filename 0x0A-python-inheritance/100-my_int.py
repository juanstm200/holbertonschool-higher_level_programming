#!/usr/bin/python3
"""Class MyInt that inherits from int"""


class MyInt(int):
    """Verify that the data matches if it is not integer"""
    def __eq__(self, date):
        return int(self) != date

    """Verify that the data matches if it is integer"""
    def __ne__(self, date):
        return int(self) == date
