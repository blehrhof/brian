# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 

@author: brian
"""

import os
import shutil
import sys
import logging
import logzero
from logzero import logger
# Setup rotating logfile with 3 rotations, each with a maximum filesize of 1MB:
logzero.logfile("edifact.log", maxBytes=1e6, backupCount=3)



# Log messages
# logger.info("This log message goes to the console and the logfile")




def loadelists():

    '''
    nlist = ['Name="6066 Control Value"',
            'Name="6064 Quantity Difference"',
            'Name="5420 Rate Per Unit"',
            'Name="6174 Size"',
            'Name="6348 Currency Rate Base"',
            'Name="5278 Duty/Tax/Fee Rate"',
            'Name="5004 Monetary Amount"',
            'Name="5118 Price"',
            'Name="5394 Price Multiplier"',
            'Name="6060 Quantity"',
            'Name="6314 Measure"',
            'Name="6152 Range Maximum"',
            'Name="6162 Range Minimum"',
            'Name="5402 Rate Of Exchange"',
            'Name="6246 Temperature Setting"',
            'Name="5160 Total Monetary Amount"',
            'Name="7240 Total Number Of Items"']
    '''
    elist = ["6066","6064","5420","6174","6348","5278","5004","5118","5394","6060","6314","6152","6162","5402","6246",
        "5160","7240"]
    return elist



def prpy(basedir):
    fc=0
    elist=loadelists()
    
    for root, dirs, files in os.walk(basedir):
        #next four lines skip maven directories
        if '.svn' in dirs:
            dirs.remove('.svn')
        if 'target' in dirs:
            dirs.remove('target')
        for fname in files:
            if fname.endswith('.dic') and not(fname == 'FACTHeader.dic') and not(fname == 'FACTHeader_PL.dic'):
                fc=fc+1
                #print(fc, fname)
                msg=str(fc)+" "+fname
                logger.info(msg)
                full_file_name_with_path=os.path.join(root, fname)
                #print(full_file_name_with_path)
                #append backup to filename
                bname=fname+".backup"
                
                full_bfile_name_with_path=os.path.join(root, bname)
                #get the file

                dicfile=get_lines(full_file_name_with_path)

                #write backup
                #shutil.copy2(full_file_name_with_path,full_bfile_name_with_path)
                
                # create list of lines with SG loop markers in first pass
                # then go and change them in a 2nd pass
                change_list=[]
                change_elist=[]
                
                   
                # loop through the lines, set flag for segment markers
                linenum=0
                for line in dicfile:
                    linenum=linenum+1
                    
                    # if marker is SG then next line must be mandatory

                    if '<Loop ID="SG' in line:
                        # lno-1 is current line where the SG marker was found
                        # lno is the next line
                        #print("marker ",linenum)
                        change_list.append(linenum)
                
                    # is there a numeric field to change?
                    if 'Name=' in line:
                        loc_in_line=line.find('Name=',0,99)
                        #print(loc)
                        loc_in_line=loc_in_line+6
                        #print(loc)
                        dict_element=line[loc_in_line:loc_in_line+4]
                        #print(dict_element)
                        if dict_element in elist:
                            change_elist.append(linenum-1)





                # change all of the SG lines to make the next line mandatory
                for linenum in change_list:
                    #print(linenum)
                    dicfile[linenum] = dicfile[linenum].replace('Req="O"', 'Req="M"')
                    #print(dicfile[linenum])
                for linenum in change_elist:
                    dicfile[linenum] = dicfile[linenum].replace('Type="N"', 'Type="R"')                                        
                    dicfile[linenum] = dicfile[linenum].replace('Type="AN"', 'Type="R"')                                        



                                     


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
    #print(sys.argv[1])
    std=sys.argv[1]
    #stdu="EDIFACT_D16A"
    stdu=std.upper()
    print("\n\nThis is the standard passed in "+ stdu+"\n\n")
    #prpy(r'c:\SVN\iway8\svn\iway8schemas\trunk\ebix\edifact\EDIFACT_D13A\src\main\resources\1.0\D13A\dictionaries')
    #prpy(r'c:\SVN\iway8\svn\iway8schemas\trunk\ebix\edifact\EDIFACT_D16A')
    #full_path=r'c:\SVN\iway8\svn\iway8schemas\trunk\ebix\edifact\EDIFACT_D16A'
    full_path=r'c://SVN//iway8//svn//iway8schemas//trunk//ebix//edifact//'+stdu
    full_path.join(stdu)
    logger.info(full_path)
    if os.path.exists(full_path) == False:
        logger.info("Bad directory path")
    #quit()
    
    #prpy(r'c:\SVN\iway8\svn\iway8schemas\trunk\ebix\edifact\'+standard)
    prpy(full_path)
    '''
    remove EDIFACT_D13A IN ABOVE LINE TO PRODUCTION RUN
    '''
    

if __name__ == '__main__':
    main()
