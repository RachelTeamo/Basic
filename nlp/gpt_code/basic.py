import torch
import os

def read_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        all_data = f.read().split('\n\n')


if __name__ == '__main__':
    train_data = read_data(os.path.join('data', 'train.txt'))
    import pdb; pdb.set_trace()
    print("haha")