import os

#Set Home Directory to same directory as the script is in
homedir = os.path.abspath('') + "/"

import requests
import json

"""
    SITE READER V0.4
    BY: MICHAEL GAILLING

    A simple and yet incomplete html parser.
    Copyright (C) 2014  Michael Gailling
    
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

VERSION 0.4 NOTES:
-Replaced urllib with requests and json! Seriously, fuck urllib
-Requests stability has allowed me to roll the call to the site into a function called dlsite
-still need ui
-need parsing for scripts. new lines not being generated appropriately
-added homedir handling with os library. Script can be run in any directory now

VERSION 0.3 NOTES:
-outputcode module defined to encapsulate the sorting loop
-added spacing for non tag entities in the code
-added exception handling for lost requests, not sure if working

VERSION 0.2 NOTES:
-First workable version.
-Needs to have exception handling for requests to compensate for lost requests
-Needs Modularization
-Needs UI
"""

def dlsite(url):
    #Make a request to a website to view html
    r = requests.get(url)
    
    #return a string of the source
    return r.text




def outputCode(x):

    
    #Open file with the handler f
    f = open(homedir + "sitecode.txt", "w", encoding='utf-8')
    
    #Declare some vars
    tempstr = ""
    tagfnd = False
    tagcnt = 0
    charcnt = 0
    linecnt = 0
    
    #Loop Through Code
    for i in x:
        charcnt = charcnt +1
        if tagfnd == True:                  #If tagfnd is True then...
            if i == ">":                    #If the char in i is a closing bracket of a tag
                tempstr = tempstr + i       #add the closing bracket to tempstr
                print(tempstr)              #Ouput to screen
                f.write(tempstr + "\n")     #Output to a newline in the file
                linecnt = linecnt + 1
                tagcnt = tagcnt + 1         #add 1 to the tag counter
                tagfnd = False              #Reset tagfnd to False
                tempstr = ""                #Reset tempstr
            else:                           #Otherwise...
                tempstr = tempstr + i       #Continue to collect non bracket chars from the string

        elif i == "<":                      #If the char in i is an opening bracket of a tag
            if tempstr != "":               #If tempstr is not empty
                print(tempstr)              #Output non tag chars to the screen
                f.write(tempstr)            #Output non tag chars to the file
                linecnt = linecnt + 1
            tempstr = i                     #Enter the opening bracket into tempstr
            tagfnd = True                   #set tagfnd to True

        else:                               #No tags detected yet continue collecting
            tempstr = tempstr + i           #Chars till one is found


    
    
    print("Number of Tags : " + str(tagcnt))
    print("Number of Lines: " + str(linecnt))
    print("Number of Chars: " + str(charcnt))
    f.close()                               #ALWAYS
                                            #CLOSE
                                            #THE
                                            #FILE
                                            #... Shit Head! Corrupt files are a bitch

outputCode(dlsite("http://youtube.com"))
