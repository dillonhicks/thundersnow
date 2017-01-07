from thundersnow.fsutil import find
from thundersnow.ioutil import fulltext
from thundersnow.compat import Path


CWD = str(Path.cwd())


def find_all_python_files_in_directory(path=CWD):
    python_files = list(find(path, '*py'))
    print(python_files)


def get_the_contents_of_all_python_files(path=CWD):
    contents = ''.join(map(fulltext, find(path, '*py')))
    print(contents)


if __name__ == '__main__':
    find_all_python_files_in_directory()
    get_the_contents_of_all_python_files()