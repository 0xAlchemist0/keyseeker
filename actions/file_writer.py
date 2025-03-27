from pathlib import Path


def write_to_file(content):
    file = Path('hits.txt')
    file.write_text(content)