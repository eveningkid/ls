import unittest
from ls import filter_hidden_files, filter_non_folders

from .stubs import DirEntry

class TestFilters(unittest.TestCase):
    def setUp(self):
        self.files = [
            DirEntry('.a'), 
            DirEntry('.b'), 
            DirEntry('d', is_dir = True),
        ]

    def test_filter_hidden_files(self):
        filtered = filter_hidden_files(self.files)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].name, 'd')

    def test_filter_non_folders(self):
        filtered = filter_non_folders(self.files)
        self.assertEqual(len(filtered), 1)
        self.assertTrue(filtered[0].is_dir())


if __name__ == '__main__':
    unittest.main()
