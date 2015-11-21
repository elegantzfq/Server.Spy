
from __future__ import print_function
from collections import OrderedDict
import pprint

__author__ = 'zhangfuqiang'


def cpu_info():
    '''
    :return: the informatin in /proc/CPUinfo
    as a dictionary in the following format:
    CPU_info['proc0]={...}
    CPU_info['proc0]={...}
    '''
    cpu__info = OrderedDict()
    proc_info = OrderedDict()

    nprocs = 0

    with open('/proc/CPUinfo') as f:
        for line in f:
            print(f)


cpu_info()
