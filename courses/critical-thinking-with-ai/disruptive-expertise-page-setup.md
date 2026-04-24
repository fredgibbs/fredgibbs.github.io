---
layout: syllabus
course-title: Critical Thinking with AI
course-slug: critical-thinking-with-ai
term: Spring 2026
section: links-guides
site-name: "Disruptive Expertise"
repository-name: disruptive-expertise
work-folder: essays
example-folder: wikipedia
---

## _{{page.site-name}}_ Page Setup Guide

Once you have your own copy of the  _{{page.site-name}}_ repository AND your own version of the website is running (the URL will look like https://USERNAME.github.io/{{page.repository-name}}/), you are ready to proceed.


{% include alert.html class='warning' title='Be sure everything is working' text="
This guide is useful ONLY AFTER you have followed the directions for [setting up your repository](disruptive-expertise-site-setup). If you just plow forward anyway, nothing will make sense or work.
"%}


### Save time with bookmarks
Create bookmarks for two locations you will be visiting often:
- YOUR own _{{page.site-name}}_ **REPOSITORY**: https://github.com/USERNAME/{{page.repository-name}}/
  - Replace USERNAME with your GitHub username!
- YOUR own _{{page.site-name}}_ **WEBSITE**: https://USERNAME.github.io/{{page.repository-name}}


## Create a folder and blank page
Go to YOUR repository (the URL will look like https://github.com/USERNAME/{{page.repository-name}}/). Make sure you're on the `Code` tab (normally the default view). You should see the list of files in the repository (starting with folders like _data,_includes, _layouts, etc).

- Press the `.` (period) key to go into Editor Mode
- Close the README file that opens by default
- Click on the little arrow to the left of the `{{page.work-folder}}` folder to see its contents
- Click on the `{{page.example-folder}}` to highlight it
- Either right-click and select `Copy` or press Ctrl C (windows) or Cmd C (mac)
- You may see a little permissions box that asks if the Editor can use the clipboard. Allow!
- Press Ctrl V or Cmd V to paste the folder you just copied (or right-click and select `Paste`)
  - You should see a new folder that says `{{page.example-folder}} copy`
- Right-click on the new folder to bring up the context menu and select `Rename`
  - use a short name that makes sense for your project (don't use my-project or something generic; it should reflect your topic)
  
{% include alert.html class='danger' 
title = 'Name your folder correctly!' 
text = " 
Lower case and upper case are not the same. Spaces are horrible. If you don't name your folder correctly, you will be frustrated later.
- use KEBAB case, which means **all-lower-case-and-dashes**:
  - Do-Not-Capitalize-Words
  - Do not use spaces_or_underscores
  - Folder names must look like `mesa-vista-hall` or `maxwell-museum` or `johnson-field`
"
%}

## Commit your changes to rebuild your site
- On the very left of the page is a column of icons; click the one that looks like a network and has a blue circle on it
- There's a message box that you can ignore; click the `Don't show again` link.
- Type in a commit message (for instance, "create new essay folder")
- Click the green `Commit & Push` button
- Your site is now rebuilding!

## Test and bookmark your page
- Chill for a minute: there is about a minute lag between when you commit your file and when your website updates.
- You should also be able to go to https://USERNAME.github.io/{{page.repository-name}}/
- You should see two Wikipedia "cards" on the homepage.
- Once you can get to your working webpage, BOOKMARK IT! Then you can just directly jump to your essay to see it.

## Edit away!
For more details on editing your page and changing the info on your card, move on to the [editing instructions](disruptive-expertise-editing).
