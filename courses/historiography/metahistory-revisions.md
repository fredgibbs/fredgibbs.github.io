---
layout: syllabus
course-title: Historiography
course-slug: historiography
number: HIST 491-001
term: Fall 2021
section: links-guides
---

# _Metahistory_ Revision Guide

This guide is useful ONLY AFTER you have followed the directions for [setting up your _Metahistory_ repository](metahistory-setup).

Once you have your own copy of the _Metahistory_ repository AND you can see the functioning website based on YOUR repository in YOUR GitHub account (the URL will look like https://USERNAME.github.io/metahistory/), you are ready to proceed.

### Save time with bookmarks
Create bookmarks in your browser for two locations you will be visiting often:
- YOUR own _Metahistory_ REPOSITORY: https://github.com/USERNAME/metahistory/, replacing USERNAME with your GitHub username.
- YOUR own _Metahistory_ WEBSITE: https://USERNAME.github.io/metahistory

## Create a new page
Go to YOUR Metahistory repository homepage. If you have just enabled GitHub pages (or basically anytime), you can click the "metahistory" link after your username near the top left corner. You should see the list of files in the repository (starting with folders like _data and _includes).

Working in YOUR repository (the URL will look like https://github.com/USERNAME/metahistory/), find the essay you want to edit. You can always figure out where to go by looking at the URL of the original page. The folder structure in the repository is reflected in the URL.

## Make a simple change near the top of the page
It doesn't matter what you change, but keep it simple and make a change that you can easily detect. Commit that change to your repository.

## Test your page
- Wait a few minutes after you commit your file. Remember there is a few minutes lag between when you save your file and when those changes appear on the actual webpage.
- Test your page by going to https://USERNAME.github.io/metahistory (you bookmarked it, right?) and navigate to the page you edited. You can also just type in the URL (but please don't): https://USERNAME.github.io/metahistory/essays/FOLDER/FILENAME, where FOLDER is the folder in which you created a new file, and FILENAME is the name of the file you edited.

## Edit away, edit offline
Now you are ready to go in full-on edit mode for your essay. **Please do not edit this long essay in the tiny GitHub text editor** window that has worked well enough to submit reading responses. It makes it WAY TOO EASY to make mistakes that take a LOT OF TIME to fix. You can also lose a lot of work because of a network or power glitch.

You should copy and paste the whole essay to somewhere else, do all your editing (possibly over a period of time, saving a local copy as you go), then commit your changes. **Make sure you save your file with the EXACT same name as the original.** You are welcome to commit your changes in smaller batches, as well, such as one paragraph at a time.

For editing, use:
- [Atom](http://atom.io)
- some other text editor
- [Dillinger](http://dillinger.io)

## Page build errors
If you commit a file with a syntax error (a missing quote or something like that), you will get an email saying there is a "page build error". Until you fix it, you won't see any subsequent changes you commit to your repository.

## FINISH YOUR EDITS
Save your work as you go! Let me know if you have any questions, and we also have class time for discussions.

## Pull Requests
When you are *completely* done editing, you need to get your local changes (in YOUR repository) to the remote repository, which is the live _Metahistory_ site that everyone sees. A **pull request** in this context is like asking me, as owner of the _Metahistory_ repository you forked, to "pull" into the main (remote) repository the changes you made in your (local) repository. If I like your changes, I will "accept" the request and if I don't I will "reject" them. Of course I'm not going to reject well-intentioned changes. But this process prevents inadvertent updates from happening to the live _Metahistory_ site.

### How to create a pull request
- Go to the homepage of YOUR _Metahistory_ repository, and click the `Pull Request` nav link near the top.
- Click the Green `New Pull Request` button.
- GitHub will show you what changes you are making, line by line (a whole paragraph counts as a line). Verify that the changes are correct.
- Click the Green `Create Pull Request` button.
- You should see near the top a green message that says `Able to merge.` If you don't see that, you should just stop and let me know in class.
- Otherwise, click the Green `Create Pull Request` button.


## You're done
After you make the pull request, there's nothing else to do! If you notice that you missed a typo or something you can always make another change and another pull request. No problem!
