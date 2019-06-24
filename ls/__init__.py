import os
from pathlib import Path

from .args_parser import parse_args


def get_dir_files(path, recursive=False):
    files = []
    
    for file in os.scandir(path):
        files.append(file)
        
        if recursive and file.is_dir():
            files.extend(get_dir_files(os.path.join(path, file)))

    return files


def filter_hidden_files(files):
    return [file for file in files if not file.name.startswith('.')]


def filter_non_folders(files):
    return [file for file in files if file.is_dir()]


def get_file_contents(path):
    try:
        with open(path) as f:
            return list(f.readlines())
    except UnicodeDecodeError as e:
        return []


def get_file_line_count(path):
    file_contents = get_file_contents(path)
    return len(file_contents)


def get_dir_files_count(path):
    return len(get_dir_files(path))


def ls():
    args = parse_args()
    include_hidden_files = args.a
    is_recursive = args.R
    display_file_size = args.l
    display_file_line_count = args.c
    display_only_folders = args.d
    display_folder_files_count = args.d
    reverse_display_order = args.r

    current_path = Path(os.getcwd())
    dir_path = (current_path / Path(args.path)).resolve()
    files = get_dir_files(dir_path, recursive=is_recursive)

    if display_only_folders:
        files = filter_non_folders(files)

    if not include_hidden_files:
        files = filter_hidden_files(files)

    if reverse_display_order:
        files = files[::-1]

    for file in files:
        to_display = []

        if display_file_size:
            file_size = file.stat(follow_symlinks=False).st_size
            to_display.append(file_size)

        to_display.append(file.name)
        
        if display_file_line_count and file.is_file():
            line_count = get_file_line_count(file.path)
            to_display.append(line_count)

        if display_folder_files_count and file.is_dir():
            folder_files_count = get_dir_files_count(file.path)
            to_display.append(folder_files_count)

        print(*to_display)
