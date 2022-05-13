import os

def get_path():

    current_dir_path = os.path.dirname(os.path.realpath(__file__))
    parent_dir_path = os.path.join(current_dir_path, os.pardir)
    storage_dir_path = os.path.join(parent_dir_path, f'test_data')
    print(storage_dir_path)
    return storage_dir_path