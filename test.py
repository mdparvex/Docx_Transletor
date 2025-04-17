import os
import unittest
from app import app

class TestTranslationAPI(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.sample_file_path = "sample_docs/brochure.docx"

    def test_successful_translation(self):
        with open(self.sample_file_path, 'rb') as file:
            data = {
                'file': (file, 'brochure.docx'),
                'source_lang': 'en',
                'target_lang': 'fr'
            }
            response = self.client.post('/translate', content_type='multipart/form-data', data=data)
            self.assertEqual(response.status_code, 200)

    def test_missing_file(self):
        data = {
            'source_lang': 'en',
            'target_lang': 'fr'
        }
        response = self.client.post('/translate', content_type='multipart/form-data', data=data)
        self.assertEqual(response.status_code, 400)

    def test_unsupported_file_type(self):
        with open(__file__, 'rb') as file:
            data = {
                'file': (file, 'not_a_doc.txt'),
                'source_lang': 'en',
                'target_lang': 'fr'
            }
            response = self.client.post('/translate', content_type='multipart/form-data', data=data)
            self.assertEqual(response.status_code, 400)

    def test_missing_language_params(self):
        with open(self.sample_file_path, 'rb') as file:
            data = {
                'file': (file, 'brochure.docx'),
            }
            response = self.client.post('/translate', content_type='multipart/form-data', data=data)
            self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
