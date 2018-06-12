#!/usr/bin/python

import sys
import glob
import os
from datetime import date

path= "helix-Checkin"

module = 'mpg/fileformat'
root = '/cvsroot/datatype'

branch = {
    '361_tiger':'hxclient_3_6_1_tiger',
    '361_wolf':'hxclient_3_6_1_wolf',
    '310_atlas':'hxclient_3_1_0_atlas',
    'head':''
}

def buildCVSCmd( branch, root, module ):

    cmd = "cvs -d :ext:yuanzhang@cvs.helixcommunity.org:"
    cmd += root 
    cmd += ' checkout '

    if ( branch != '' ):
        cmd += '-r "'
        cmd += branch
        cmd += '" '

    cmd += module
    return cmd

def makeDirStructure( path ):
    os.chdir( '/home/yuan')
    os.system( 'rm -rf ' + path)
    os.system( 'mkdir ' +  path)

def checkoutAll( path ):

    os.chdir( path )

    for dirName, branchName in branch.iteritems():
        
        save = os.getcwd()
        os.system( 'mkdir ' + dirName )
        os.chdir( dirName );

        cvsCmd = buildCVSCmd( branchName, root, module )
        os.system( cvsCmd )

        os.chdir( save )
#main
makeDirStructure( path )
checkoutAll( path )
