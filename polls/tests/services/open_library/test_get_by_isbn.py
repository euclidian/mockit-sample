from django.test import TestCase
from unittest.mock import patch
from polls.services.open_library.get_by_isbn import GetByIsbn

class GetByIsbnTestCase(TestCase):
    def setUp(self):
        pass
    
    def mocked_mockit():
        return 'mocked'

    @patch('polls.services.open_library.get_by_isbn.mockit', mocked_mockit)
    def test_hello(self):
        subject = GetByIsbn('hello')
        self.assertEqual(subject.perform(), "hellohashedhellomocked")