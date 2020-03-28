#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 18:52:53 2019

@author: tanja
"""
#
# Sorts files from the folder 'sortDir' into the folder '########'
# whose name begin with '#######'  (account number).

import os
import glob
import shutil
import sys # module for system-specific parametes and functions
import json # Java Scipt object Notation for paring more complex data types

def list_files(start):
     # prints out all filenames in the directory start
    print('files in directory: ' + start + '\n') 
    for dirpath, dirnames, filenames in os.walk(start):
        for filename in filenames :  
            print(filename)
    return filenames


def sortFiles(accountNumber): 
    # set directorys
    cwd = os.getcwd()
    DirToSort = os.path.join(cwd,'sortDir')
    
    #json.dumps([])f.read()
    
    targetDir = os.path.join(DirToSort,'accountNumber')
    
    # get all objects with '#########' in the begining of the name
    os.chdir(DirToSort)
    matchingFiles = glob.glob('accountNumber'+'*')
    
    # move the files
    for file in matchingFiles:
        if os.path.isfile(file):
            filename = os.path.split(file)[1]
            #
            #TODO: include error handler for empty path
            #
            print('moved file '+ filename[1])
            absoluteFilePath = os.path.join(DirToSort,filename) 
            #
            #TODO: include error handler for the case is the file already exists
            #
            shutil.move(absoluteFilePath, targetDir)
            print('to '+ os.path.join(targetDir,file))
            
    os.chdir(cwd)
    

def  main():
    print ('type account number')
    # get account numer and call the sorting-function
    locAccountNumber = input()
    sortFiles(locAccountNumber)
    
    return
    
    