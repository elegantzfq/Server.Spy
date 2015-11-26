
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

    with open('/proc/cpuinfo') as f:
        for line in f.readlines():
            # print(line)
            if not line.strip():
                # end of one processor
                cpu__info['proc%s'% nprocs] = proc_info
                nprocs += 1
                proc_info = OrderedDict()
            else:
                if len(line.split(':')) == 2:
                    proc_info[line.split(':')[0].strip()] = line.split(':')[1].strip()
                else:
                    proc_info[line.split(':')[0].strip()] = ''
    return cpu__info


if __name__ == '__main__':
    CPUinfo = cpu_info()
    print(CPUinfo)
    for processor in CPUinfo.keys():
        print(CPUinfo[processor]['model name'])
