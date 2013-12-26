# coding: utf-8
from __future__ import unicode_literals, print_function

import unittest
from main import DictToKeyValue as D
from collections import OrderedDict


from_object = D.from_object


class SimpleTest(unittest.TestCase):

    example = {
        "menu": {
            "header": "SVG Viewer",
            "items": [
                {"id": "Open"},
                {"id": "OpenNew", "label": "Open New"},
                None,
                {"id": "ZoomIn", "label": "Zoom In"},
                {"id": "ZoomOut", "label": "Zoom Out"},
                {"id": "OriginalView", "label": "Original View"},
                None,
                {"id": "Quality"},
                {"id": "Pause"},
                {"id": "Mute"},
                None,
                {"id": "Find", "label": "Find..."},
                {"id": "FindAgain", "label": "Find Again"},
                {"id": "Copy"},
                {"id": "CopyAgain", "label": "Copy Again"},
                {"id": "CopySVG", "label": "Copy SVG"},
                {"id": "ViewSVG", "label": "View SVG"},
                {"id": "ViewSource", "label": "View Source"},
                {"id": "SaveAs", "label": "Save As"},
                None,
                {"id": "Help"},
                {"id": "About", "label": "About Adobe CVG Viewer..."}
            ]
        }
    }

    def test_example_json(self):
        # from: http://json.org/example

        expect_result = [
            (('menu', 'header'), 'SVG Viewer'),
            (('menu', 'items', 0, 'id'), 'Open'),
            (('menu', 'items', 1, 'id'), 'OpenNew'),
            (('menu', 'items', 1, 'label'), 'Open New'),
            (('menu', 'items', 2), None),
            (('menu', 'items', 3, 'id'), 'ZoomIn'),
            (('menu', 'items', 3, 'label'), 'Zoom In'),
            (('menu', 'items', 4, 'id'), 'ZoomOut'),
            (('menu', 'items', 4, 'label'), 'Zoom Out'),
            (('menu', 'items', 5, 'id'), 'OriginalView'),
            (('menu', 'items', 5, 'label'), 'Original View'),
            (('menu', 'items', 6), None),
            (('menu', 'items', 7, 'id'), 'Quality'),
            (('menu', 'items', 8, 'id'), 'Pause'),
            (('menu', 'items', 9, 'id'), 'Mute'),
            (('menu', 'items', 10), None),
            (('menu', 'items', 11, 'id'), 'Find'),
            (('menu', 'items', 11, 'label'), 'Find...'),
            (('menu', 'items', 12, 'id'), 'FindAgain'),
            (('menu', 'items', 12, 'label'), 'Find Again'),
            (('menu', 'items', 13, 'id'), 'Copy'),
            (('menu', 'items', 14, 'id'), 'CopyAgain'),
            (('menu', 'items', 14, 'label'), 'Copy Again'),
            (('menu', 'items', 15, 'id'), 'CopySVG'),
            (('menu', 'items', 15, 'label'), 'Copy SVG'),
            (('menu', 'items', 16, 'id'), 'ViewSVG'),
            (('menu', 'items', 16, 'label'), 'View SVG'),
            (('menu', 'items', 17, 'id'), 'ViewSource'),
            (('menu', 'items', 17, 'label'), 'View Source'),
            (('menu', 'items', 18, 'id'), 'SaveAs'),
            (('menu', 'items', 18, 'label'), 'Save As'),
            (('menu', 'items', 19), None),
            (('menu', 'items', 20, 'id'), 'Help'),
            (('menu', 'items', 21, 'id'), 'About'),
            (('menu', 'items', 21, 'label'), 'About Adobe CVG Viewer...')
        ]
        self.assertEquals(list(from_object(self.example)), expect_result)

    def test_list(self):
        self.assertEquals(
            list(from_object({'a': [0, 1]})),
            [(('a', 0), 0), (('a', 1), 1)]
        )

    def test_nested_dict(self):
        result = list(from_object({'a': {'b': 'c'}}))
        self.assertEquals(result, [(('a', 'b'), 'c')])

    def test_dict(self):
        result = list(from_object({'a': 'b'}))
        self.assertEquals(result, [(('a',), 'b')])

    def test_ordereddict(self):
        od = OrderedDict([
            ('a', 'b'),
            ('c', 'd'),
            ('x', 'y'),
        ])
        result = list(from_object(od))
        self.assertEquals(
            result, [(('a',), 'b'), (('c',), 'd'), (('x',), 'y')])


if __name__ == '__main__':
    unittest.main()
