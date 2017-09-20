# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 

@author: brian
"""

import os
import shutil






def prpy(basedir):
    fc=0
    for root, dirs, files in os.walk(basedir):
        #next four lines skip maven directories
        if '.svn' in dirs:
                dirs.remove('.svn')
        if 'target' in dirs:
            dirs.remove('target')
        for fname in files:
            if fname.endswith('.dic') and fname != 'FACTHeader.dic':
                fc=fc+1
                print(fc, fname)

                full_file_name_with_path=os.path.join(root, fname)
                #print(full_file_name_with_path)
                #append backup to filename
                bname=fname+".backup"
                
                full_bfile_name_with_path=os.path.join(root, bname)
                #get the file

                dicfile=get_lines(full_file_name_with_path)

                #write backup
                shutil.copy2(full_file_name_with_path,full_bfile_name_with_path)
                

                change_list=[]
                   

                
                # loop through the lines, set flag for segment markers
                linenum=0
                for line in dicfile:
                    linenum=linenum+1
                    
                #for lno, line in enumerate(flines, start=1):
                    #print(lno, line)
                    # if marker is SG then next line must be mandatory

                    if '<Loop ID="SG' in line:
                        # lno-1 is current line where the SG marker was found
                        # lno is the next line
                        #print("marker ",linenum)
                        change_list.append(linenum)
                
                for linenum in change_list:
                    #print(linenum)
                
                    
                
                
                   
                    dicfile[linenum] = dicfile[linenum].replace('Req="O"', 'Req="M"')


                    #print(dicfile[linenum])
                                        



                                     


                put_lines(full_file_name_with_path,dicfile)

                #exit(0)
'''                 if fname == 'testwalk.py':
                    with open(fname) as tw:
                        for line in tw:
                            print('--> {}'.format(line))
 '''
#get file by reading all lines
def get_lines(full_file_name_with_path):
    with open(full_file_name_with_path) as f:
        dicfile = f.readlines()
    return dicfile

        
#put file by writing all lines
def put_lines(full_file_name_with_path, dicfile):
    with open(full_file_name_with_path, mode='w') as f:
        f.writelines(dicfile)
        
                            


def main():
    #prpy(r'c:\SVN\iway8\svn\iway8schemas\trunk\ebix\edifact\EDIFACT_D13A\src\main\resources\1.0\D13A\dictionaries')
    prpy(r'c:\SVN\iway8\svn\iway8schemas\trunk\ebix\edifact\EDIFACT_D16A')
    '''
    remove EDIFACT_D13A IN ABOVE LINE TO PRODUCTION RUN
    '''
    

if __name__ == '__main__':
    main()
