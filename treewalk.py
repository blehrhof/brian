import os
import sys
import shutil
#import re
indir = r'C:\SVN\iway8\svn\iway8schemas\trunk\ebix\edifact\EDIFACT_D13A\src\main\resources\1.0\D13A\dictionaries'
#indir.replace("\",'//')
#indir = 'C://SVN//iway8//svn//iway8schemas//trunk//ebix//edifact//EDIFACT_D13A//src//main//resources//1.0//D13A//dictionaries//'
#print(indir)
for root, dirs, filenames in os.walk(indir):
    for f in filenames:
        print(f)
#       fullpath=os.path.join(indir,f)
#       log=open(fullpath,'r')        
#       print(log)
#os.scandir(indir)
#print(os.DirEntry)
        # full file name to backup file with file name.back
        full_path_bak=os.path.join(indir,f+'.back')
        print(full_path_bak)
        # full file name to file with file name
        full_path=os.path.join(indir,f)
        print(full_path)
        # copy file to filename.back before changing it.
        shutil.copy(full_path,full_path_bak)
        
        dicfile=open(full_path,'r')
#        print(dicfile)
        linenum=0
        for line in dicfile:
            linenum=linenum+1
            print(linenum, line)

        file.close()

