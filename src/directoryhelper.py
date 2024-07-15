from os.path import exists, join, isfile
from os import listdir, mkdir
from shutil import rmtree, copy


def make_copy(src, dst):
    if exists(dst):
        rmtree(dst)
    mkdir(dst)
    for f in listdir(src):
        src_path = join(src, f)
        dst_path = join(dst, f)
        print(f"copying {src_path} to {dst_path}")
        if isfile(src_path):
            copy(src_path, dst_path)
        else:
            make_copy(src_path, dst_path)
