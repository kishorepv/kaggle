import glob
import os
import shutil
import random

def make_sample(sample_dir, train_dir, valid_dir, test_dir, size=10, sep='/'):
    if not os.path.isdir(sample_dir):
        os.mkdir(sample_dir)
    #train_name=train_dir.split(sep)[-1]
    #sample_train=os.path.join(sample_dir,train_name)
    #os.mkdir(sample_train)
    test_name=test_dir.split(sep)[-1]
    sample_test=os.path.join(sample_dir,test_name)
    os.mkdir(sample_test)
    te_dir=test_dir
    te_dname=''
    for testdir_ in glob.glob(os.path.join(test_dir,'*')):
        if (os.path.isdir(testdir_)):
            te_dname=testdir_.split('/')[-1]
            os.mkdir(os.path.join(sample_test,te_dname))
            te_dir=testdir_
    files=random.sample(glob.glob(os.path.join(te_dir,'*')), size)
    for onefile in files:
        shutil.copy2(onefile, os.path.join(sample_test,te_dname))
    for dirx in [train_dir, valid_dir]:
        create_train_valid_sample(dirx, sample_dir, size, sep)

def create_train_valid_sample(src_dir, dest_dir, size, sep):
    dest_name=src_dir.split(sep)[-1]
    dest_base=os.path.join(dest_dir,dest_name)
    os.mkdir(dest_base)
    for dir_ in glob.glob(os.path.join(src_dir,'*')):
        if (os.path.isdir(dir_)):
            dname=dir_.split(sep)[-1]
            dest_subdir=os.path.join(dest_base,dname)
            os.mkdir(dest_subdir)
            all_files=glob.glob(os.path.join(dir_,'*'))
            files=random.sample(all_files, size)
            for onefile in files:
                shutil.copy2(onefile, dest_subdir)

def create_validation_data(train_dir, percent=0.1, sep='/'):
    valid_dir=os.path.join(sep.join(train_dir.split(sep)[:-1]), "valid")
    os.mkdir(valid_dir)
    for dir_ in glob.glob(os.path.join(train_dir,"*")):
        if os.path.isdir(dir_):
            dname=dir_.split(sep)[-1]
            valid_subdir=os.path.join(valid_dir,dname)
            os.mkdir(valid_subdir)
            all_files=glob.glob(os.path.join(dir_,'*'))
            files=random.sample(all_files, int(len(all_files)*percent))
            for onefile in files:
                shutil.move(onefile, valid_subdir)
