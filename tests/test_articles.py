import unittest
from app.models import NewsArticle


class NewsArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the NewsArticles class
    '''

    def setUp(self):
        '''
        set up method that will run before every Test
        '''
        self.new_art = NewsArticle("VeganCommunity","John Doe", "V-Gang",
        "We are Vegan. We are making history by being on the right side of socially accepted wrong",
         "https://www.instagram.com/p.BhVQpsRgAJm/", "https://www.instagram.com/p.BhVQpsRgAJm/",
         "2018-04-09")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_art, NewsArticle))

    def test_init(self):
        self.assertEqual(self.new_art.source, "VeganCommunity")
        self.assertEqual(self.new_art.author, "John Doe")
        self.assertEqual(self.new_art.title, "V-Gang")
        self.assertEqual(self.new_art.description, "We are Vegan. We are making history by being on the right side of socially accepted wrong")
        self.assertEqual(self.new_art.url, "https://www.instagram.com/p.BhVQpsRgAJm/")
        self.assertEqual(self.new_art.urlToImage, "https://www.instagram.com/p.BhVQpsRgAJm/")
        self.assertEqual(self.new_art.publishedAt, "2018-04-09")
