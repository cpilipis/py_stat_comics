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

newIndex = open("./index.html", "w")

newIndex.write('\n\
<!DOCTYPE html>\n\
<html>\n\
<head>\n\
<title> MACROSOFA.NET </title>\n\
<style>\n\
body {background-color:darkgreen;}\n\
text {color:white; font-family: helvetica;}\n\
p {color:white; font-family: helvetica;}\n\
h1 {color:lightgreen; font-family: courier;}\n\
h2 {color:lightgreen; font-family: courier;}\n\
h3 {color:lightgreen; font-family: courier;}\n\
a {color:yellow;}\n\
div {\n\
    background-color: lightgreen;\n\
    padding: 0px;\n\
    border: 2px solid white;\n\
    margin: 0px;\n\
}\n\
</style>\n\
<link rel="shortcut icon" href="../../sitefavicon.ico" />\n\
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate"/>\n\
<meta http-equiv="Pragma" content="no-cache"/>\n\
<meta http-equiv="Expires" content="0"/>\n\
<script>\n\
  (function(i,s,o,g,r,a,m){i[\'GoogleAnalyticsObject\']=r;i[r]=i[r]||function(){\n\
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),\n\
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)\n\
  })(window,document,\'script\',\'https://www.google-analytics.com/analytics.js\',\'ga\');\n\
\n\
  ga(\'create\', \'UA-78330619-1\', \'auto\');\n\
  ga(\'send\', \'pageview\');\n\
\n\
</script>\n\
</head>\n\
<body>\n\
<h1> MACROSOFA.NET </h1>\n\
<text> Doing linux, videogames, programming, and other nerdy stuff since 2016. <br> </text>\n\
<img src="../../sitethumb.png"alt="An orange couch"title="It\'s a sofa, and it\'s macro. Go figure."><br>\n\
<p>This site is being served by a Raspberry Pi 1, model B.</p>\n\
<br>\n\
<h2>Today\'s web comic</h2>\n\
<img src="'+comic_name+'.png" alt="'+comic_alt+'" width='+comic_width+' height='+comic_height+'><br>\n\
<h3><i>'+comic_alt+'</i></h3>\n\
<p>'+comic_desc+'</p>\n\
<h2><a href="comics">Archive</a></h2>\n\
<text>An archive of comics I made</text>\n\
<h2> <a href="https://www.github.com/blehmeh98"> My Github Page</a>. </h2>\n\
<text> I used to mainly program in Lua, but now I am learning C. I also know basic bits of HTML and CSS. My most current project is a 2d platformer engine sorta thing written in C with the allegro library, with working bounding box collision. If you program in Lua, and you use Love2d to make games, you may want to check out my game base.</text>\n\
<h2> <a href="codestuffs">Stuff I coded and compiled</a></h3>\n\
<text>If I programmed it and did a formal build for all kinds of various platforms, you can find it here.</text>\n\
</body>\n\
</html>')

newIndex.close()

print("All done, check the site.")
