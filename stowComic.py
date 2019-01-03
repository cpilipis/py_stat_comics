#!/usr/bin/python

import os
import sys

data = open("data.txt", "r")
comic_num = int(data.readline()[4:])
print("Comic number is "+str(comic_num))
comic_name = data.readline()[5:].strip("\n")
print("Comic file name is "+comic_name)
comic_alt = data.readline()[4:].strip("\n")
print("Comic alt is "+comic_alt)
comic_desc = data.readline()[5:].strip("\n")
print("Comic description is: "+comic_desc)
comic_width = data.readline()[6:].strip("\n")
print("Comic width is: " + comic_width)
comic_height = data.readline()[7:].strip("\n")
print("Comic height is: " + comic_height)
data.close()
print "Is there another new line?"

os.chdir("./comics")

os.mkdir(str(comic_num))
#Moving the files to the new folder
os.rename("../index.html", "./"+str(comic_num)+"/index.html")
os.rename("../"+comic_name+".png", "./"+str(comic_num)+"/com.png")

#Now we need to update the index for this stowed comic to exclude all the fancy links to other parts of my website, because otherwise I would need to update them whenever I change it on the front page
#It's just easier to only put them on the front page

newIndex = open("./"+str(comic_num)+"/index.html", "w")
newIndex.write('\
<!DOCTYPE html>\
<html>\
<head>\
<title> MACROSOFA.NET </title>\
<style>\
body {background-color:darkgreen;}\
text {color:white; font-family: helvetica;}\
p {color:white; font-family: helvetica;}\
h1 {color:lightgreen; font-family: courier;}\
h2 {color:lightgreen; font-family: courier;}\
h3 {color:lightgreen; font-family: courier;}\
a {color:yellow;}\
div {\
    background-color: lightgreen;\
    padding: 0px;\
    border: 2px solid white;\
    margin: 0px;\
}\
</style>\
<link rel="shortcut icon" href="../../sitefavicon.ico" />\
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate"/>\
<meta http-equiv="Pragma" content="no-cache"/>\
<meta http-equiv="Expires" content="0"/>\
<script>\
  (function(i,s,o,g,r,a,m){i[\'GoogleAnalyticsObject\']=r;i[r]=i[r]||function(){\
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),\
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)\
  })(window,document,\'script\',\'https://www.google-analytics.com/analytics.js\',\'ga\');\
\
  ga(\'create\', \'UA-78330619-1\', \'auto\');\
  ga(\'send\', \'pageview\');\
\
</script>\
</head>\
<body>\
<h1> MACROSOFA.NET </h1>\
<text> Doing linux, videogames, and other nerdy stuff since 2016. <br> </text>\
<img src="../../sitethumb.png"alt="An orange couch"title="It\'s a sofa, and it\'s macro. Go figure."><br>\
<br>\
<h2>Today\'s web comic</h2>\
<img src="com.png" alt="'+comic_alt+'" width='+comic_width+' height='+comic_height+'><br>\
<h3><i>'+comic_alt+'</i></h3>\
<p>'+comic_desc+'</p>\
<h2> <a href="../">Back to archive.</a></h2>\
<p> <a href="../'+str(comic_num - 1)+'">Previous</a> | <a href="../'+str(comic_num+1)+'">Next</a></p>\
</body>\
</html>')

newIndex.close()

#Now we need to update our fancy index to include this newly stowed away comic

comicList = open("./index.html", "r+")

#We should now be at the comic line, at which point we can just write the rest of the file we need
comicList.seek(-17, 2)
stringy = comicList.read()
print(stringy)
comicList.seek(-17, 2)


comicList.write('<p><a href="'+str(comic_num)+'">'+comic_alt+'</a></p>\n</body>\n</html>\n')
