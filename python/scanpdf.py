#!/bin/python

import os
import sys
import subprocess

pdf_info = dict () 

def output_pdf( filename, md5 ):

    if md5 in pdf_info:
        print filename + ' == ' + pdf_info[md5]
    else:
        pdf_info[md5] = filename
        print md5 + ':' + filename


def make_md5( filename ):
    cmd = 'md5sum "' + filename + '"'
    p = subprocess.Popen( cmd, shell=True, stdout=subprocess.PIPE)
    val = p.communicate()[0].split()
    return val[0] 

def scanpdf( path ):

    for root, dirs, files in os.walk(path):
        for element in files:
            #if element.endswith('.pdf'):
            filename = os.path.join(root, element )
            md5 = make_md5( filename )
            output_pdf( filename, md5 )

def main():

    if len( sys.argv ) == 2:
        scanpdf( sys.argv[1] )

main()

