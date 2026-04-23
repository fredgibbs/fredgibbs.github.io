---
layout: syllabus
course-title: Critical Thinking with AI
course-slug: critical-thinking-with-ai
term: Spring 2026
section: links-guides
site-name: "Disruptive Expertise"
repository-name: disruptive-expertise
sample-folder: episodes
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
Go to YOUR repository (the URL will look like https://github.com/USERNAME/{{page.repository-name}}/). You should see the list of files in the repository (starting with folders like _data,_includes, _layouts, etc).

- Click the `{{page.sample-folder}}` folder
- Click the `Add file` button in the upper right, and `Create New File`
- Type in a folder name for your essay:
  - all lower case and with dashes (printing-press) AND
  - CONTINUE typing `/index.md` - **DON'T FORGET THE / AT THE BEGINNING**

{% include alert.html class='danger' 
title = 'Name your folder correctly' 
text = " 
Lower case and upper case are not the same. Spaces are horrible. If you don't name your folder correctly, you will be frustrated later.
- use KEBAB case, which means **all-lower-case-and-dashes**:
  - Do-Not-Capitalize-Words
  - Do not use spaces_or_underscores
  - Folder names must look like `mesa-vista-hall` or `maxwell-museum` or `johnson-field`
"
%}

- Click the green `Commit changes...` button. Yes, you're saving an empty file.


## Copy a sample page into your blank page
- Click on the `{{page.sample-folder}}` folder
- Click on the `wikipedia` folder
- Click on the `index.md` file 
- Near the upper right of the screen, click the copy icon (two overlapping rectangles) to copy all the text.


## Paste the sample into your new blank page
- Click on the folder your created (all lower case and with dashes)
- Click on the index.md file
- Paste the text you just copied.
- Update your page metadata as best you can right now (you'll add an image later)
- Click the green `Commit changes...` button.


## Test and bookmark your page
- Chill for a minute: there is about a minute lag between when you commit your file and when your website updates.
- Test your page by going to https://USERNAME.github.io/{{page.repository-name}} (you bookmarked it, right?) and add  `/episodes/YOUR-NEW-FOLDER/` to the URL to see your new page. Obviously replace your-new-folder with what you typed in the previous step.
- You should also be able to go to https://USERNAME.github.io/{{page.repository-name}}/{{page.sample-folder}}
- Once you can get to your working webpage, BOOKMARK IT! It's easy to forget what the URL is to preview your page.

## Edit away!
For more details on editing your page, check out the [editing instructions](disruptive-expertise-editing).
