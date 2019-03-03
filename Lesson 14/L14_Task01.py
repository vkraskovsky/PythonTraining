import hashlib
import argparse
from os import path


class File:

    def __init__(self, name):
        self.name = name

    def calc_sum(self):
        file_data = self.read()
        return hashlib.md5(file_data.encode('UTF-8')).hexdigest()

    def read(self):
        file_name = self.name
        with open(file_name, 'r') as file:
            file_data = file.read()
            return file_data


class Manifest:

    def __init__(self, file, hash_sum, name='/home/slava/dev/Temp/L14_Task01/manifest.txt'):
        self.name = name
        self.file = file
        self.hash_sum = hash_sum

    def check_sum(self):
            with open(self.name, 'r') as manifest:
                for line in manifest:
                    if self.file == line.split()[0]:
                        if self.hash_sum == line.split()[1]:
                            return True
                        else:
                            return False

    def save_new(self):
        if path.isfile(self.name):
            with open(self.name, 'r') as manifest:
                for line in manifest:
                    if self.file == line.split()[0]:
                        return True
        else:
            print('Manifest file doesn\'t exist. Creating..')

        print('Record for the file doesn\'t exist. Adding new record..')
        new_hash = self.file + ' ' + self.hash_sum + '\n'
        with open(self.name, 'a') as manifest:
            manifest.write(new_hash)
            return True


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--calc', nargs='*', dest='files_list', default=False, help='Calculate hash sum for files..')
    parser.add_argument('--check', nargs='?', dest='manifest', default=False, help='Check hash sum for files..')
    params = parser.parse_args()

    print(params)
    if params.files_list and params.files_list != []:
        for file in params.files_list:
            if path.isfile(file):
                file_to_calc = File(file)
                checksum = file_to_calc.calc_sum()
                manifest_writer = Manifest(file_to_calc.name, checksum)
                print('Checksum for', file_to_calc.name, 'is', checksum)
                manifest_writer.save_new()
            else:
                print('File', file, 'doesn\'t exist')

    elif params.manifest:
        if path.isfile(params.manifest[0]):
            manifest_file = params.manifest[0]
        else:
            manifest_file = '/home/slava/dev/Temp/L14_Task01/manifest.txt'
        with open(manifest_file, 'r') as manifest:
            for file in manifest:
                file_to_check = File(file.split()[0])
                checksum = file_to_check.calc_sum()
                if path.isfile(file_to_check.name):
                    manifest_checker = Manifest(file_to_check.name, checksum, manifest_file)
                    if manifest_checker.check_sum():
                        print(file_to_check.name, ': OK', checksum)
                    else:
                        print(file_to_check.name, ': FAILED')


if __name__ == '__main__':
    main()
