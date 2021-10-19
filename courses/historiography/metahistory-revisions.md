---
layout: syllabus
course-title: Historiography
course-slug: historiography
number: HIST 491-001
term: Fall 2021
section: links-guides
---

#_Metahistory_ Revision Guide

This guide is useful ONLY AFTER you have followed the directions for [setting up your _Metahistory_ repository](metahistory-setup).

Once you have your own copy of the _Metahistory_ repository, and you can see the functioning website based on YOUR repository in YOUR GitHub account (the URL will look like https://github.com/USERNAME/metahistory/), you are ready to proceed.

HINT: Create a bookmark in your browser for https://USERNAME.github.io/metahistory, replacing USERNAME with your GitHub username. You will be going to this page often.

## Create a new page
Working in YOUR repository (the URL will look like https://github.com/USERNAME/metahistory/), find the essay you want to edit. You can always figure out where to go by looking at the ULR of the original page. The folder structure in the repository is reflected in the URL.

## Make a simple change near the top of the page
It doesn't matter what you change, but keep it simple and make a change that you can easily detect. Commit that change to your repository.

## Test your page
- Wait a few minutes after you commit your file. Remember there is a few minutes lag between when you save your file and when those changes appear on the actual webpage.
- Test your page by going to https://USERNAME.github.io/metahistory (you bookmarked it, right?) and navigate to the page you edited. You can also just type in the URL (but please don't): https://USERNAME.github.io/metahistory/essays/FOLDER/FILENAME, where FOLDER is the folder in which you created a new file, and FILENAME is the name of the file you edited.

## Edit away, edit offline
Now you are ready to go in full-on edit mode for your essay. **Please do not edit this long essay in the tiny GitHub text editor** window that has worked well enough to submit reading responses. It makes it WAY TOO EASY to make mistakes that take a LOT OF TIME to fix. You can also lose a lot of work because of a network or power glitch.

You should copy and paste the whole essay to somewhere else, do all your editing (possibly over a period of time, saving as you go), then commit your changes. You are welcome to commit them in smaller batches as well, if you'd like.

For editing, use:
- [Atom](http://atom.io)
- some other text editor
- Dillinger[http://dillinger.io]

## Page build errors
If you commit a file with a syntax error (a missing quote or something like that), you will get an email saying there is a "page build error". Until you fix it, you won't see any subsequent changes you commit to your repository.

## Verify your edits
Retest your page by going to https://USERNAME.github.io/metahistory and navigating to your edited essay. If you see the change you made, everything is work.

## FINISH YOUR EDITS
Save your work as you go! Let me know if you have any questions, and we also have class time for discussions.

## Create a Pull Request  
When you are *completely* done editing, you need to get your local changes (in YOUR repository) to the remote repository, which is the live _Metahistroy_ site that everyone sees. A **pull request** in this context is like asking me, as owner of the _Metahistory_ repository you forked, to "pull" into the main (remote) repository the changes you made in your (local) repository. If I like your changes, I will "accept" the request and if I don't I will "reject" them. Of course I'm not going to reject well-intentioned changes. But this process prevents accidental updates from happening. Everything can be undone, in any case.

## You're done
After you make the pull request, there's nothing else to do! If you notice that you missed a typo or something you can always make another change and another pull request. No problem!
