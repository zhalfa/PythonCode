#!/bin/python

import os
import sys
import re
import glob


def ProcessList( path, lst ):
    for element in lst:
        name_in = path + element;
        name_out = path + "out/" + element; 
        process_html( name_in, name_out )
  
def get_title( content ):
    ret = ''
    title = re.search( r'<title.*</title>', content, flags=re.I);

    if title:
        ret = title.group()
        title_len = len( ret )
        ret = ret[7: title_len -8];

        ret = ret.decode('big5', 'strict')

    return ret

def process_html( file_name, new_name ):

    fobj=open( file_name, "r" )
    content = fobj.read()
    fobj.close()

    if len( content ) == 0 :
        return

    title = get_title( content )

    print file_name, title 

    new_content = re.sub( r'"http[^> ]*"', r'', content )
    new_content = re.sub( r"'http[^> ]*'", r'', new_content )
    #print( new_content )

    #remove script
    new_content = re.sub( r"<script.*</script>", r'', new_content, flags=re.I)
    new_content = re.sub( r"<a.*</a>", r'', new_content, flags=re.I)
    new_content = re.sub( r'<link.*/>', r'', new_content, flags=re.I)
    new_content = re.sub( r'<img.*/>', r'', new_content, flags=re.I)
    new_content = re.sub( r'<form.*</form>', r'', new_content, flags=re.I)
    new_content = re.sub( r'<iframe.*</iframe>', r'', new_content, flags=re.I)
    new_content = re.sub( r'<dl.*</dl>', r'', new_content, flags=re.I)
    new_content = re.sub( r'<div.*id="overture_ads_top".*</div>', r'', new_content, flags=re.I)
    new_content = re.sub( r'<td.*class="dedo_bar_option_border".*</td>', r'', new_content, flags=re.I)
    new_content = re.sub( r'action=".*"', r'', new_content, flags=re.I)
    #new_content = re.sub( r'href *= *".*"', r'', new_content, flags=re.I)

    fobj = open( new_name, "w")
    fobj.write( new_content )
    fobj.close()


def main():

    path='/home/yuan/test/'
    if len( sys.argv ) == 2 :
        path = sys.argv[1]

    os.chdir( path )
    htmlst = glob.glob( '*.htm' )
    htmlst += glob.glob( '*.html' )

    if (not os.path.exists('out')):
        os.mkdir( 'out' )

    ProcessList( path, htmlst )

main()
