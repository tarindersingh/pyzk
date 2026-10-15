# -*- coding: utf-8 -*-
import unittest
from struct import pack

from zk import const
from zk.hid import HIDEvent, parse_hid_card


class HIDTests(unittest.TestCase):
    def test_constants(self):
        self.assertEqual(const.EF_HIDNUM, 1 << 10)
        self.assertEqual(const.EF_WRITECARD, 1 << 11)
        self.assertEqual(const.EF_EMPTYCARD, 1 << 12)

    def test_parse_hid_card(self):
        self.assertIsNone(parse_hid_card(b''))
        self.assertIsNone(parse_hid_card(b'\x00\x00\x00\x00'))
        self.assertEqual(parse_hid_card(pack('<I', 11013128)), 11013128)
        self.assertEqual(parse_hid_card(pack('<I', 4294967295)), 4294967295)
        # Trailing bytes from some firmwares are ignored.
        self.assertEqual(parse_hid_card(pack('<I', 42) + b'\xff\xff'), 42)

    def test_hid_event_repr(self):
        event = HIDEvent(99)
        self.assertEqual(event.card, 99)
        self.assertIn('99', str(event))


if __name__ == '__main__':
    unittest.main()
