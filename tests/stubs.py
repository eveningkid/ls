import os


# -- Class stubs

class DirEntry:
    """Simplified DirEntry stub as os.DirEntry cannot be instantiated."""
    def __init__(self, name = '', path = '', is_dir = False):
        self.name = name
        self.path = path
        self.is_dir_ = is_dir

    def is_dir(self):
        return self.is_dir_


# -- Files helpers

TEST_DIR_PATH = os.path.join(os.path.dirname(__file__), 'temp_testdir')
TEST_SUBDIR_PATH = os.path.join(TEST_DIR_PATH, 'temp_testsubdir')


def get_test_file_path(path, is_subdir=False):
    parent_path = TEST_DIR_PATH
    
    if is_subdir:
        parent_path = TEST_SUBDIR_PATH

    return os.path.join(parent_path, path)


def create_temp_file(path, contents):
    with open(path, 'w') as temp_file:
        temp_file.write(contents)
