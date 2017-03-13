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

def unzip_me(zipfile, flag=None, flag_arg=None):
    """
        Unzip files with optinal flags support
    """
    arg_data="-{} {}".format(flag, flag_arg if flag_arg else '') if flag else ''
    cmd="unzip {} {}".format(arg_data, zipfile)
    print("CMD: ", cmd)
    code=os.system(cmd)
    return code

def viz_images(path, number_per_class=4, figure_size=(7,7)):
    """
        Visualize images in a neat manner, one row per class
    """
    number_per_class=max(1, min(number_per_class, 5))
    classes=sorted([categ for categ in glob.glob(os.path.join(path,'*')) if os.path.isdir(categ)])
    if not classes:
        raise Exception("No directory for categories.")
    fig=plt.figure(figsize=figure_size)
    G=gridspec.GridSpec(len(classes), number_per_class)
    for x,dir_ in enumerate(classes):
        for col,file_ in enumerate(np.random.choice(glob.glob(os.path.join(dir_,'*')), size=number_per_class, replace=False)):
            subp=fig.add_subplot(G[x,col])
            subp.set_title(os.path.split(file_)[-1],fontsize=8, ha="center")
            if not col: subp.set_ylabel(os.path.split(os.path.split(file_)[0])[-1], rotation=0, labelpad=12, fontsize=14)
            subp.set_xticks([])
            subp.set_yticks([])
            subp.imshow(mpimg.imread(file_))
    fig.tight_layout()
