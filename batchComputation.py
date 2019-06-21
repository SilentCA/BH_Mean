import os
import logging


logging.basicConfig(level=logging.INFO)


# Path Setting
#-------------------------------
DATA_DIR = './data'


'''
`os.walk(top)`会遍历top下的所有目录，并返回含有所有目录下的子目录和文件列表
元组的迭代器，详细地说明可以参考文档：
https://docs.python.org/3/library/os.html#os.walk

对于一般情况的使用，把需要处理的所有文件放在同一个目录下，如'/data'，那么
dirpath, dirnames, filenames = os.walk('./data').__next__() 返回的为遍历到
的第一个目录，即dirpath为'./data'，dirnames为空列表（因为'./data'目录中没有
子目录），filenames为'./data'目录下所有文件组成的列表。

Ex.
./data
    file_1
    file_2
    file_3

而当把需要处理的文件分别放在了不同的目录下，并把这些目录都放在'./data'目录下时，
那么dirpath, dirnames, filenames = os.walk('./data').__next__()返回的
dirpath为'./data'，dirnames为'./data'目录下的所有子目录（即放了需要处理的文件
的目录），filenames为空列表（因为'./data'目录中没有文件）。

当得到了一个目录下需要处理的文件列表之后，就可以通过循环处理文件。

Ex.
./data
+---dir_1
|       file_1
|
+---dir_2
|       file_2
|
\---dir_3
        file_3

'''
# DATA_DIR中的所有文件夹和目录
_, paths, files = os.walk(DATA_DIR).__next__()


for idx, data_file in enumerate(paths):
    # do something
    pass
