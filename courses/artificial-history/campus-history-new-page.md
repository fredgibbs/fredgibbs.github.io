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

Once you have your own copy of the  _{{page.site-name}}_ repository AND your own versioni of the website is running (the URL will look like https://USERNAME.github.io/{{page.repository-name}}/), you are ready to proceed.

### Save time with bookmarks
Create bookmarks for two locations you will be visiting often:
- YOUR own _{{page.site-name}}_ **REPOSITORY**: https://github.com/USERNAME/{{page.repository-name}}/, replacing USERNAME with your GitHub username.
- YOUR own _{{page.site-name}}_ **WEBSITE**: https://USERNAME.github.io/{{page.repository-name}}

## Create a new page
Go to YOUR repository. If you have just enabled GitHub pages (or basically anytime), you can click the "metahistory" link after your username near the top left corner. You should see the list of files in the repository (starting with folders like _data and _includes).

Working in YOUR repository (the URL will look like https://github.com/USERNAME/{{page.repository-name}}/), find the essay you want to edit. You can always figure out where to go by looking at the URL of the original page. The folder structure in the repository is reflected in the URL.

## Make a simple change near the top of the page
It doesn't matter what you change, but keep it simple and make a change that you can easily detect. Commit that change to your repository.

## Test your page
- Wait a few minutes after you commit your file. Remember there is a few minutes lag between when you save your file and seeing it on the website.
- Test your page by going to https://USERNAME.github.io/{{page.repository-name}} (you bookmarked it, right?) and navigate to the page you edited. 

## Edit offline
Now you are ready to go in full-on edit mode for your essay. Although fine for testing, **please do not edit this long essay in the tiny GitHub text editor**. It makes it WAY TOO EASY to make mistakes that take a LOT OF TIME to fix. My favorite editor is [Sublime](https://www.sublimetext.com/)

You should copy and paste the whole essay to somewhere else, do all your editing (possibly over a period of time, saving a local copy as you go), then copy and paste your changes to GitHub. **Make sure you save your file with the EXACT same name as the original.** You are welcome to commit your changes in smaller batches, as well, such as one paragraph at a time.

## Page build errors
If you commit a file with a syntax error (a missing quote or something like that), you will get an email saying there is a "page build error". Until you fix it, you won't see any subsequent changes you commit to your repository.

## FINISH YOUR EDITS
Save your work as you go! Let me know if you have any questions, and we also have class time for discussions.


## Pull Requests
When you are *completely* done editing, you need to get your local changes (in YOUR repository) to the remote repository, which is the live _{{page.site-name}}_ site that everyone sees. A **pull request** in this context is like asking me, as owner of the _{{page.site-name}}_ repository you forked, to "pull" into the main repository the changes you made in your (local) repository. If I like your changes, I will "accept" the request and if I don't I will "reject" them. But this process prevents mistakes and bugs.

### How to create a pull request
- Go to the homepage of YOUR _{{page.site-name}}_ repository, and click the `Pull Request` nav link near the top.
- Click the Green `New Pull Request` button.
- GitHub will show you what changes you are making, line by line (a whole paragraph counts as a line). Verify that the changes are correct.
- Click the Green `Create Pull Request` button.
- You should see near the top a green message that says `Able to merge.` If you don't see that, you should just stop and let me know in class.
- Otherwise, click the Green `Create Pull Request` button.


## You're done
After you make the pull request, there's nothing else to do! If you notice that you missed a typo or something you can always make another change and another pull request. No problem!
