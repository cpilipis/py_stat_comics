# py_stat_comics
A set of python scripts to ease uploading comics to a static html site
I used these for my comic strip site [macrosofa.net](http://www.macrosofa.net) a while back, and recently felt like open sourcing it. It's nothing fancy, but it's mine, and I was able to accomplish the task of building a web comic with it.

## How it works, and my workflow
My site is structured as follows:
- I have a static html front page for my current comic. It had both the comic, a description and title, and some links to other parts of my website, including a link to my Github page and a link to the archives for the older comics.
- I have a static html page for listing links to each respective archive comic and a link to go back to the main site.
- I have a static html page for each archive comic, featuring the comic, a description, a title, and a link to go back to the archive.

Before writing this script, my workflow for uploading a new web comic to my site went as follows:
1. I would upload a new comic image to my web server via FTP
2. I would take a template HTML page I set up for a comic in the archives and use it to make a new entry in the archives directory of my site
3. I would move the current comic that is being replaced to that new entry
4. I would copy the description and title from the current HTML page and paste it into the archive one
5. I would manually add an entry to the index page for the archive
6. I would modify the front page to feature the title and description of the new comic, as well as use the new comic

This process was annoying to do every time I wanted to upload a comic to my site, so I set up two python scripts run separately to automate this process.
Now it's as follows:
1. I upload a new comic image to my web server via FTP
2. I run stowComic.py, which automates steps 2, 3, and 4
3. I modify data.txt to easily access the most important options for my HTML site, namely the filename of the image, formal name of the comic, the alt text, the description, the number that this comic is, and the width and height of the comic
4. I run newComic.py, which takes the parameters from data.txt to create a new front page for my website.
I only save two steps out of the process I just described, but this saves me a lot of time when uploading a new comic to the site simply because editing the HTML files manually through SSH while connected to my web server in question was always kind of bulky.

## Is this setup any good for me?

I used this kind of set up because I don't know any Javascript or Ruby or Pearl or PHP or anything I could use to create a more elegant, dynamic, pretty looking solution and because I was hosting this on my own web server. I also made this as a simple Python exercise.
So, if you're in the same camp as me where you know basic HTML and CSS but nothing more dynamic, and you don't care for any kind of crazy shiny dynamic solution, you might actually like this python solution. Chances are you'll modify the python file to use a different html template than my website, and you'll introduce your own CSS file for the site with your own unique theme. You may even add more features and the like to data.txt because you want there to be more differnet pieces of information per comic. But either way, you'll appreciate my scripts as a starting point.
Now, if you know a lick of Javascript or PHP or Ruby or whatever, chances are you'll be able to whip up a way better, cleaner, awesome solution than mine in like two seconds. But mine is still there if you ever feel like it.
