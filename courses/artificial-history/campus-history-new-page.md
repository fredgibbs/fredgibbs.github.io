---
layout: syllabus
course-title: Artificial History
course-slug: artificial-history
number: HIST 300-009
term: Spring 2025
section: links-guides
site-name: "Campus History"
group-name: unm-digital-history
repository-name: campus-history
repository-url: https://github.com/unm-digital-history/campus-history
site-url: https://unm-digital-history.github.io/campus-history/
---

## _{{page.site-name}}_ Revision Guide

This guide is useful ONLY AFTER you have followed the directions for [setting up your repository](campus-history-setup).

Once you have your own copy of the  _{{page.site-name}}_ repository AND your own version of the website is running (the URL will look like https://USERNAME.github.io/{{page.repository-name}}/), you are ready to proceed.

### Save time with bookmarks
Create bookmarks for two locations you will be visiting often:
- YOUR own _{{page.site-name}}_ **REPOSITORY**: https://github.com/USERNAME/{{page.repository-name}}/
  - Replace USERNAME with your GitHub username!
- YOUR own _{{page.site-name}}_ **WEBSITE**: https://USERNAME.github.io/{{page.repository-name}}

## Create a new page
Go to YOUR repository (the URL will look like https://github.com/USERNAME/{{page.repository-name}}/). You should see the list of files in the repository (starting with folders like _includes and _layouts).

- Click the `essays` folder 
- Click the `Add file` button in the upper right, and `Create New File`
- Type in a folder name for your essay, all lower case and with dashes (example: mesa-vista-hall), and continue typing `/index.md` **DON'T FORGET THE / AT THE BEGINNING**

{% include alert.html class='danger' 
title = 'Name your folder correctly' 
text = " 
It is IMPERATIVE that you name your folder correctly right away, or you will create A LOT of work for yourself (and probably me) later. 
- all lower case, NO CAPITALS ANYWHERE
- no spaces, ONLY DASHES. (no underscores)
- it should like `mesa-vista-hall` or `maxwell-museum` or `johnson-field`
"
%}




- Click the green `Commit changes...` button. Yes, you're saving an empty file.
- Be sure you're still in the `essays` folder.
- Click on the `mesa-vista-hall` folder
- Click on the `index.md` file 
- Near the upper right of the screen, click the copy icon (two overlapping rectangles)
- Click on your new page (index.md) in the folder you created, and paste the text you just copied.
 - Click the green `Commit changes...` button.


## Test your page
- Chill for a minute. Remember there is a lag between when you save your file and the website getting updated.
- Test your page by going to https://USERNAME.github.io/{{page.repository-name}} (you bookmarked it, right?) and add  `/essays/your-new-folder/` to the URL to see your new page. Obviously replace your-new-folder with what you typed in the previous step.

#### Make sure you have `/essays/` in the above URL
Once you can get to your page, bookmark it! It's easy to forget what th URL is to preview your page.

## Create your images folder
You'll notice that no images are showing up on your new page, because we didn't copy any images into your new folder. In fact, you don't even have an `images` folder yet!
- Find some test image you can use from the [NM digital archive](https://econtent.unm.edu/).
- Download an image (it doesn't matter what, you can always replace it later) and put it somewhere you can get to quickly.
- On GitHub, navigate to the folder you just created (via the list of files on the left...)
- Click the `Add file` button in the upper right (just like before), but this time `Upload Files`
- Drag and drop your image file into the big box on the GitHub page.
- Click the green `Commit changes...` button in the bottom left of the page. This time you're saving an actual file!
- Now you've uploaded a file but it's in the wrong place. We want it in an `images` folder.
  - But GitHub doesn't keep track of folders, just files. So we need to rename our file to include a folder name.
- Using the file list on the left, click on your new image file, then the pencil icon to go in edit mode.
- Click on the name of your file at the top so you can edit it.
- Add `images/` to the front of the filename (and you'll see that creates an images directory)
- Click the green `Commit changes...` button.
- If you want to see your new image appear on your page, find the snippet to display an image and change the image-url parameter to your new filename. **IT MUST MATCH EXACTLY**


## Edit offline
Now you are ready to go in full-on edit mode for your essay. Although fine for testing, **please do not edit this long essay in the tiny GitHub text editor**. It makes it WAY TOO EASY to make mistakes that take a LOT OF TIME to fix. 

Instead, you should copy and paste the whole essay in a text editor, and do all your editing (possibly over a period of time, saving a local copy as you go), then copy and paste your changes to GitHub. **Make sure you save your file with the EXACT same name as the original.** You are welcome to commit your changes in smaller batches, as well, such as one paragraph at a time. My favorite editor is [Sublime](https://www.sublimetext.com/).

## Page build errors
If you commit a file with a syntax error (a missing quote or something like that), you will get an email saying there is a "page build error". Until you fix it, you won't see any subsequent changes you commit to your repository.
