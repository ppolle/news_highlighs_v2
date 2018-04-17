import unittest
from app.models import NewsSource


class NewsSourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News Source class
    '''

    def setUp(self):
        '''
        set up method that will run before every Test
        '''
        self.new_src = NewsSource("VeganCommunity", "John Doe", "V-Gang", "https://www.instagram.com/p.BhVQpsRgAJm/", "business", "english","us")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_newsrc, NewsSource))

    def test_init(self):
        self.assertEqual(self.new_src.id, "VeganCommunity")
        self.assertEqual(self.new_src.name, "John Doe")
        self.assertEqual(self.new_src.description, "We are Vegan. We are making history by being on the right side of socially accepted wrong")
        self.assertEqual(self.new_src.url, "https://www.instagram.com/p.BhVQpsRgAJm/")
        self.assertEqual(self.new_src.category, "business")
        self.assertEqual(self.new_src.language, "english")
        self.assertEqual(self.new_src.country, "us")
