import os
import hashlib


def file(f):
    return os.path.join(_base(), f'../../{f}')


def _base():
    return os.path.dirname(__file__)


# find the path of the first file
def findfile(start, name):
    for relpath, dirs, files in os.walk(start):
        if name in files:
            full_path = os.path.join(start, relpath, name)
            return os.path.normpath(os.path.abspath(full_path))


# find the path of the first dir
def finddir(start, name):
    for relpath, dirs, files in os.walk(start):
        if name in dirs:
            full_path = os.path.join(start, relpath, name)
            return os.path.normpath(os.path.abspath(full_path))


def read_file(file_path, offset, length):
    assert os.path.exists(file_path)
    with open(file_path, 'r') as f:
        f.seek(offset)
        data = f.read(length)
    return data


def checksum_data(data):
    return hashlib.sha512(data).hexdigest()
