import os
import shutil
import sys

def main():
    f = open(sys.argv[1])
    src = 'dataset'
    trg = sys.argv[2]
    if not os.path.exists(trg):
        os.makedirs(trg)
    for line in f:
        filename = line[:-1].split('/')[-1]
        if not os.path.exists(os.path.join(src, filename[:-3] + 'txt')):
            continue
        src_path = os.path.join(src, filename)
        trg_path = os.path.join(trg, filename)
        shutil.copy(src_path, trg_path)
        filename = filename[:-3] + 'txt'
        src_path = os.path.join(src, filename)
        trg_path = os.path.join(trg, filename)
        shutil.copy(src_path, trg_path)

if __name__ == '__main__':
    main()
