#!/usr/bin/python

import sys
import glob
import os

android_bin="/home/yuan/panther-android/prebuilt/linux-x86/toolchain/arm-eabi-4.4.3/bin/arm-eabi-gcc"
helix_debug=

def getPID( app ):
    filename = "psinfo.txt";

    cmd = "adb shell pidof " + app  + " >" + filename
    os.system( cmd )

    f = open( filename )
    result = f.readline()
    result = result.rstrip( "\n" )
    f.close()
    os.system ( "rm " + filename )

    if result != "":
        return result
    else:
        return ""

id = getPID('mediaserver')
print( id )

#os.system("adb forward tcp:5039 tcp:5039");
cmd = "adb shell gdbserver tcp:5039 --attach " + id
#os.system( cmd );

