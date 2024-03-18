import zipfile
import tempfile
import os
from sys import argv
import shutil
import logging


z_file_path = argv[1]
logger = logging.getLogger()
print(logger)


def main():
    logger.warning(f'Zip file name: {z_file_path}')
    deleted_items = []
    with tempfile.TemporaryDirectory() as tmpdir:
        os.path.exists(tmpdir)

    with zipfile.ZipFile(z_file_path) as zip_ref:
        zip_ref.extractall(tmpdir)
    for root, dirs, files in os.walk(tmpdir):
        relative_path = os.path.relpath(root, tmpdir)
        if "__init__.py" in files:
            continue
        if relative_path != ".":
            deleted_items.append(relative_path)
            try:
                shutil.rmtree(root)
            except OSError as error:
                logging.ERROR(f'Not this time:{root} : {error.strerror}')

    with open(os.path.join(tmpdir, "cleaned.txt"), 'a') as clean_file:
        deleted_items.sort()
        for line in deleted_items:
            clean_file.write(line + '\n')
        clean_file.close()
    shutil.make_archive(z_file_path[:-4] + '_new', 'zip', tmpdir)
    shutil.rmtree(tmpdir)
    logger.warning(f'New archive: {clean_file}')


if __name__ == "__main__":
    main()
