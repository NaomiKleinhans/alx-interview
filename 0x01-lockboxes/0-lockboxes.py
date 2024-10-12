#!/usr/bin/python3
"""
0-lockboxes.py

This module defines a function that determines if all boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Parameters:
        boxes (list of lists): A list where each box contains a list of keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = [0]

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    return all(unlocked)
