import os


def get_directory_info(path):
    current = os.getcwd()
    os.chdir(path)
    file_count = 0
    directory_count = 0
    file_size = 0
    for root_dir, cur_dir, files in os.walk('.'):
        for file in files:
            file_path = os.path.join(root_dir, file)
            file_size += os.stat(file_path).st_size
        file_count += len(files)
        directory_count += len(cur_dir)
    print('Number of files:', file_count)
    print('Number of folders:', directory_count)
    print(f'Total size of files: {file_size / 1000000} MB')
    os.chdir(current)


path = input('Please Input the directory that you want to check:\n')
get_directory_info(path)
