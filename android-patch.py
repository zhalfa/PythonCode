#!/usr/bin/python
import os

src ="/home/yuan/diffs";

listname= os.getcwd()+"/patchlst";

android_path = "/home/yuan/panther-android"

def generatePatchList( src ):

    cmd = "find "+ src + " -name *.diff >" + listname;
    os.system( cmd );    

def patchAll():

    fd = open( listname )

    while True :

        content = fd.readline();
        if content == "":
            break

        content = content.rstrip("\n");

        target = content.replace( src,"" );
        target = target.replace( ".diff", "" );
        
        cmd = "patch -p0 " + android_path + target + " < " + content;
        os.system( cmd )

    fd.close();

generatePatchList( src );

patchAll()
