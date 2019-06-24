import unittest
import os
import shutil
from ls import get_dir_files, get_dir_files_count, get_file_contents, get_file_line_count 

from .stubs import create_temp_file, get_test_file_path, TEST_DIR_PATH, TEST_SUBDIR_PATH


class TestFilesHelpers(unittest.TestCase):
    def setUp(self):
        os.mkdir(TEST_DIR_PATH)
        create_temp_file(get_test_file_path('a.md'), 'hello')
        create_temp_file(get_test_file_path('b.md'), 'world')

        os.mkdir(TEST_SUBDIR_PATH)
        create_temp_file(get_test_file_path('c.md', is_subdir=True),
                         'hello world')

    def assert_array_equal(self, a, b):
        for element in a:
            self.assertIn(element, b)
        self.assertEqual(len(a), len(b))

    def test_non_recursive_get_dir_files(self):
        files = get_dir_files(TEST_DIR_PATH, recursive=False)
        files_names = [file.name for file in files]
        expected_files = ['a.md', 'b.md', 'temp_testsubdir']
        self.assert_array_equal(expected_files, files_names)

    def test_recursive_get_dir_files(self):
        files = get_dir_files(TEST_DIR_PATH, recursive=True)
        files_names = [file.name for file in files]
        expected_files = ['a.md', 'b.md', 'temp_testsubdir', 'c.md']
        self.assert_array_equal(expected_files, files_names)

    def test_get_file_contents(self):
        paths = [
            get_test_file_path('a.md'),
            get_test_file_path('b.md'),
            get_test_file_path('c.md', is_subdir=True),
        ]
        expected_files_contents = ['hello', 'world', 'hello world']
        files_contents = [get_file_contents(path) for path in paths]

        # Should only be one-lined files
        for file_contents in files_contents:
            self.assertTrue(len(file_contents), 1)
        
        # Only keep the first line to reuse the helper
        files_contents = [lines[0] for lines in files_contents]
        self.assert_array_equal(expected_files_contents, files_contents)

    def test_get_file_line_count(self):
        path = get_test_file_path('a.md')
        file_line_count = get_file_line_count(path)
        expected_lines_count = 1
        self.assertEqual(file_line_count, expected_lines_count)

    def test_get_dir_files_count(self):
        folder_files_count = get_dir_files_count(TEST_SUBDIR_PATH)
        expected_folder_files_count = 1
        self.assertEqual(folder_files_count, expected_folder_files_count)

    def tearDown(self):
        shutil.rmtree(TEST_DIR_PATH)


if __name__ == '__main__':
    unittest.main()
