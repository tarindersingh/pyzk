# -*- coding: utf-8 -*-
"""RF / HID card realtime events (OnHIDNum)."""
from struct import unpack


def parse_hid_card(data):
    """
    Parse a card number from an EF_HIDNUM realtime payload.

    Returns an unsigned 32-bit int, or None when the payload is empty / zero.
    """
    if not data or len(data) < 4:
        return None
    card = unpack('<I', data[:4])[0]
    if card == 0:
        return None
    return card


class HIDEvent(object):
    """One RF/HID card tap reported by the terminal."""

    def __init__(self, card):
        self.card = int(card)

    def __str__(self):
        return '<HIDEvent>: {}'.format(self.card)

    def __repr__(self):
        return '<HIDEvent>: {}'.format(self.card)
