#!/usr/bin/python

import sys
import glob
import os
from datetime import date

pkt = "helix-pkt"
helix ='/home/yuan/361-build/release/';
optimized ='/home/yuan/aricent/'
head = '/home/yuan/panther-android/frameworks/base/include/media/'

filelist = []

def showInfo():

    print( helix )
    print( optimized )
    print( head )

def getFileLst( src ):

    global filelist

    filelist = []
    save = os.getcwd()
    os.chdir( src )
    filelist = glob.glob('*.so')
    os.chdir(save)

def copyHelix( src, des ):

    for element in filelist:
        cmd = 'cp ' + src + element + ' ' + des 
        
        if element == 'dmp4.so':
            cmd = cmd + '/sdec.so'

        #print( cmd );
        os.system( cmd );

def copyOptimized( src, des ):

    for element in filelist:
        cmd = 'cp -f ' + src + element + ' ' + des 
        #print( cmd );
        os.system( cmd );

def copyHead( src, des ):        

    headlst = [ 'HelixMediaScanner.h', 'HelixMetaDataDriver.h', 'HelixPlayer.h' ]

    for element in headlst :
        cmd = 'cp ' + src + element + ' ' + des
        #print( cmd )
        os.system( cmd )

def makeDirStructure( des ):
    
    os.system( 'rm -rf ' + des )
    os.system( 'mkdir ' + des )
    save = os.getcwd()
    os.chdir( des );
    os.system( 'mkdir lib' )
    os.system( 'mkdir include' )
    os.chdir( save )
    
#main
showInfo()
dt = date.today()
makeDirStructure( pkt )

lib = pkt + '/lib'

getFileLst( helix )
copyHelix( helix, lib )

getFileLst( optimized )
copyOptimized( optimized , lib )

include = pkt + '/include'
copyHead( head, include )

os.system( 'ls -l ' + lib + ' | wc -l' )    
os.system( 'ls -R ' + pkt )
os.system( 'tar -jcf LePhone-TD-361-' + dt.isoformat() + '.tar.bz2 ' + pkt )
os.system( 'rm -rf ' + pkt )

