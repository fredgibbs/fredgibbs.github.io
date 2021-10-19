---
layout: syllabus
course-title: Historiography
course-slug: historiography
number: HIST 491-001
term: Fall 2021
section: links-guides
---

# Creating your OWN _Metahistory_ repository and workspace

## What is this about and why are we doing it?
As part of the public history aspect of the course, it's important to learn how we can we work collaboratively and non-destructively on a public history website like _Metahistory_. We all have the ability to create, edit, and delete files for the course GitHub repository, but this is a bit dangerous to allow for the entire _Metahistory_ site. Accidents happen. And it's much less stressful to create or edit essays knowing that you can't really mess anything up.

So, we use a really neat feature of GitHub to allow _everyone_ to make their own copy of _Metahistory_ and edit that without fear of breaking anything. When a set of changes are done and you want to publish those changes on the live site, you can easily do that. This guide describes the process of setting up your own work environment. There is a little technical terminology here and there that we need to learn so we can communicate effectively.

## Fork the intro-guide repository
In GitHub speak, **forking** means to create your own copy of someone else's repository for you to edit privately.

- Go to the [Metahistory repository](https://github.com/unm-historiography/metahistory), and click the `Fork` button in the upper right corner (don't click the number).
- You'll see a popup window asking you where you want to fork it, and you'll click on your username (you should only have one choice).
- You'll see the page refresh very quickly.
- Notice the URL! It looks like nothing on the page changed, but you are now looking at the _Metahistory_ repository that is **UNDER YOUR OWN ACCOUNT**. This is evident from the URL and the top left of the GitHub page. The live repository will always have `unm-historiography` in the URL, and the URL for your "fork" of it will have your GitHub username. Either way, the list of files looks exactly the same (for now). One terminology point here: the actual live repository at `unm-historiography` is the **remote** repository; the one you have under your own GitHub account is the **local** repository.

## Enable your website
Now that you have a "local" copy of the repository, you can make it create a live site that shows you how the essays look online rather than just as Markdown text as we see in the repository. This is basically a clone of the existing _Metahistory_ website, except it is connected to your own repository.

- Under the settings tab, scroll down to the `GitHub Pages` section (second from the bottom), and under `source`, change it from `none` to `main branch`. Scroll back down to the GitHub Pages section, and notice that it gives you a URL for YOUR LOCAL version of _Metahistory_. The URL will look like https://USERNAME.github.io/metahistory.

- Wait a few minutes for the site to build, then go to the above URL to see if everything is working. If there is no page, check back in a few minutes. If you've waited over 10 minutes and nothing shows up, something is wrong, and you'll need to review the above steps.

## Do a test edit
Move on to the [next instruction page on editing an existing page](metahistory-revisions), which you will do for your next assignment.
