import glob
import os
import shutil
import random
def make_sample(sample_dir, train_dir, test_dir, size=10, sep='/'):
    if not os.path.isdir(sample_dir):
        os.mkdir(sample_dir)
    train_name=train_dir.split(sep)[-1]
    sample_train=os.path.join(sample_dir,train_name)
    os.mkdir(sample_train)
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
    for dir_ in glob.glob(os.path.join(train_dir,'*')):
        if (os.path.isdir(dir_)):
            dname=dir_.split(sep)[-1]
            os.mkdir(os.path.join(sample_train,dname))
            files=random.sample(glob.glob(os.path.join(dir_,'*')), size)
            for onefile in files:
                shutil.copy2(onefile, os.path.join(sample_train,dname))
