#!/usr/bin/env python
import os
import sys
from config.user_inputs import read_config, read_cmd_args
from utils.io import get_FInFile_IO_Dirs
from filters.recovery_error2 import recovQ00
from utils.printing import print_goodbye_message

global root
root = os.getcwd()

def run_recov_q00_calcs():
    "+++ Gather job details +++"
    cmd_args          = read_cmd_args()
    config_           = read_config()
    system_name       = config_[0]
    input_dir         = cmd_args[0]
    output_dir        = cmd_args[1]
    q00_filter        = config_[8]
    list_atoms        = cmd_args[2]
    query             = get_FInFile_IO_Dirs(root,input_dir,output_dir)
    FInFile           = query[0]
    input_files_dir   = query[1]
    output_files_dir  = query[2]
    if (list_atoms==None):
        list_atoms    = config_[1]
        if (list_atoms==None):
            list_atoms    = query[3]
            if (list_atoms == None):
                sys.exit("POLUS| Program complains::: Cannot determine list of atoms")
        
    "+++ Perform RECOV task +++" 
    job =  recovQ00(list_atoms=list_atoms, \
                       system_name=system_name, \
                       working_directory=root, \
                       target_prop="q00", \
                       input_directory=input_files_dir)

    job.write_recov_err_files(threshold=q00_filter, \
                              output_filename = system_name.upper()+"-RECOVERY-Q00")
    
    print_goodbye_message()
