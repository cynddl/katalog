import scandir
from .models import Movie

MEDIA_EXT = ['mkv', 'avi']


def scan_files(path):
    """
    Recursively scan a directory to find all files with the given extension.
    """
    ext = tuple(MEDIA_EXT)
    for root, _, files in scandir.walk(path):
        for f in files:
            if f.endswith(ext):
                yield Movie(path=root + '/' + f)

