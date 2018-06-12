#!/usr/bin/python

import sys
import glob
import os
import time 

helixPath ='/home/yuan/361-letv/release';
third_path ='/home/yuan/aricent';
android_path ='/home/yuan/letv3.0/out/target/product/msm8660_surf/system/lib/'
des = '/system/lib';
sub = '/helix';
playerLib = 'libhelixplayer.so'

def updateAndroid():

    name= ("libmediaplayerservice.so","libmedia.so")

    for element in name:
        cmd = "adb push "+android_path + element + " "+ des;
        print( cmd );
        os.system( cmd );

def updateHelixSub():

    try:
        os.chdir( helixPath );
        filelist = glob.glob('*.so')

        for element in filelist:
            if element == playerLib:
                continue;
            cmd = 'adb push ' + element + ' ' + des + sub;
            print( element );
            os.system( cmd );
    except:
        print("update helix lib fails")

def update3rdLibs():

    #cmd = 'adb shell mv /system/lib/helix/dmp4.so /system/lib/helix/sdec.so' 
    #os.system( cmd )
    try:
        os.chdir( third_path );
        filelist = glob.glob('*.so')

        for element in filelist:
            cmd = 'adb push ' + element + ' ' + des + sub;
            print( element );
            os.system( cmd );
    except:
        print("update 3rd lib fails")

def updatePlayer():

    print( 'update ' + playerLib  );
    cmd = 'adb shell rm '+ des + '/' + playerLib;
    os.system ( cmd );
    os.chdir( helixPath );
    cmd = 'adb push ' + playerLib + ' ' + des
    os.system( cmd );

def getPID( app ):

    filename = "psinfo.txt";

    cmd = "adb shell pidof " + app  + " >" + filename
    os.system( cmd )

    f = open( filename )
    result = f.readline()
    result = result.rstrip( "\n" )
    f.close()
    os.system ( "rm " + filename )

    return result

def cleanHelix():
    
    cmd = 'adb shell rm ' + des + sub + '/*';
    print( cmd );
    os.system( cmd );


#main
os.system('adb root')
time.sleep(1)
os.system('adb remount')

updateAll= False

if len(sys.argv) >1:
    updateAll= True

if updateAll:
    cleanHelix()
    updateHelixSub()
    updateAndroid()
    update3rdLibs()

updatePlayer()

id = getPID('mediaserver')
os.system ( 'adb shell kill '+ id  )
