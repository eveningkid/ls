from argparse import ArgumentParser


def parse_args():
  parser = ArgumentParser(description='list directory contents')
  parser.add_argument('path', help='path to directory')
  parser.add_argument('-a', action='store_true', help='include hidden files')
  parser.add_argument('-R', action='store_true', help='recursively show files')
  parser.add_argument('-l', action='store_true', help='display file size')
  parser.add_argument('-c', action='store_true', help='display file line count')
  parser.add_argument('-d', action='store_true', help='display only folders and files count')
  parser.add_argument('-r', action='store_true', help='reverse display order')
  return parser.parse_args()
