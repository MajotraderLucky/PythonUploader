from django.test import TestCase
from .models import File

class FileModelTest(TestCase):
    def test_file_atrributes(self):
        file = File(file='test.txt')
        self.assertEqual(file.file, 'test.txt')
        self.assertFalse(file.processed)

    def test_file_upload(self):
        file = File(file='test.txt')
        file.save()
        self.assertIsNotNone(file.uploaded_at)

    def test_file_processed(self):
        file = File(file='test.txt')
        file.processed = True
        self.assertTrue(file.processed)