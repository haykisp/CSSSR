import unittest

from Page import Page


class testCases(unittest.TestCase):
    page = None

    def setUp(self):
        self.page = Page()

    def tearDown(self):
        self.page.close()



    def test1(self):
        width = self.page.content().size['width']
        self.assertEqual(1000, width)

    def test2(self):
        margin_left = self.page.content().value_of_css_property("margin-left")
        self.assertEqual(24, margin_left)


