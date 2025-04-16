---
layout: syllabus
course-title: Artificial History
course-slug: artificial-history
number: HIST 300-009
term: Spring 2025
section: links-guides
site-name: "Campus History"
repository-url: https://github.com/unm-historiography/metahistory
---

# Creating your OWN {{page.site-name}} repository

## What is this about and why are we doing it?
As part of the public history aspect of the course, it's important to learn how we can we work collaboratively and non-destructively. And it's much less stressful to create or edit essays knowing that you can't really mess anything up.

So, we use a feature of GitHub to allow _everyone_ to make their own copy of _{{page.site-name}}_ and edit that without fear of breaking anything. When a set of changes are done and you want to publish those changes on the live site, you can easily do that. This guide describes the process of setting up your own copy of _{{page.site-name}}_. 


## Fork the intro-guide repository
In GitHub speak, **forking** means to create your own copy of someone else's repository for you to edit privately.

- Go to the [{{page.site-name}} repository](https://github.com/unm-historiography/metahistory), and click the `Fork` button in the upper right corner (don't click the number).
- You'll see a popup window asking you where you want to fork it, and you'll click on your username (you should only have one choice).
- You'll see the page refresh within 5-10 seconds.
- Notice the URL! It looks like nothing on the page changed, but you are now looking at a repository **UNDER YOUR OWN ACCOUNT**. This is evident from the URL and the top left of the GitHub page. The live repository will always have `unm-historiography` in the URL, and the URL for your "fork" of it will have your GitHub username. Either way, the list of files looks exactly the same (for now). One terminology point here: the actual live repository at `unm-historiography` is the **remote** repository; the one you have under your own GitHub account is the **local** repository.

## Enable your website
Now that you have a "local" copy of the repository, you can make it create a live site that shows you how the essays look online rather than just as Markdown text as we see in the repository. This is basically a clone of the existing _Metahistory_ website, except it is connected to your own repository.

- Click the `Settings` nav link near the top of the page
- Click the `Pages` tab (second from the bottom) on the left nav
- Click the box that says `None` and change it to `master`.
- Click the `Save`  button.
- Notice that it gives you a URL for YOUR LOCAL version of _Metahistory_. The URL will look like https://USERNAME.github.io/metahistory/.
- Keep this tab open in your browser, as you'll need it in the next few steps.

- Wait a few minutes for the site to build, then go to the above URL to see if everything is working. If there is no page, check back a few minutes later. If you've waited over 5 minutes and nothing shows up, you'll need to review the above steps.

## Do a test edit
Move on to the [next instruction page on editing an existing page](metahistory-revisions), which you will do for your next assignment.
