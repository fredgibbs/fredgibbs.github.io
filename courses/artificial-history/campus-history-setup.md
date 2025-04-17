---
layout: syllabus
course-title: Artificial History
course-slug: artificial-history
number: HIST 300-009
term: Spring 2025
section: links-guides
site-name: "Campus History"
group-name: unm-digital-history
repository-url: https://github.com/unm-digital-history/campus-history
site-url: https://unm-digital-history.github.io/campus-history/
---

# Creating your OWN {{page.site-name}} repository

## What is this about and why are we doing it?
As part of the public history aspect of the course, it's important to learn how we can we work collaboratively and non-destructively. And it's much less stressful to create or edit essays knowing that you can't really mess anything up.

So, we use a feature of GitHub to allow _everyone_ to make their own copy of _{{page.site-name}}_ and edit that without fear of breaking anything. When a set of changes are done and you want to publish those changes on the live site, you can easily do that. This guide describes the process of setting up your own copy of _{{page.site-name}}_. 


## Create a GitHub account
- Go to [github.com](https://github.com) and click the "Sign up" button.
- I highly recommend your UNM email, but use whatever you want. 
- Your username can be your UNM NetID, or something totally different. 


## Fork the intro-guide repository
In GitHub speak, **forking** means to create your own copy of someone else's public repository so that you can play around with your own copy and leave the original alone.
- Be sure you are logged into GitHub
- Go to the [{{page.site-name}} repository]({{page.repository-url}}), and click the `Fork` button in the upper right corner (don't click the number).
- We want the default settings, so just click the green  "Create fork" button.
- You'll see the page refresh within 5-10 seconds.
- Notice the URL! It looks like nothing on the page changed, but you are now looking at a repository **UNDER YOUR OWN ACCOUNT**. This is evident from the URL and the top left of the GitHub page. The live repository will always have `u{{page.group-name}}` in the URL, and the URL for your "fork" of it will have your GitHub username. Either way, the list of files looks exactly the same (for now). 


## Enable your website
You now have a "local" copy of the repository, which is all files that make the website work. Now, let's enable your own working copy of the  _{{page.site-name}}_ site. As you edit your essay, you can see how the essays actually look online (instead of just Markdown files with code snippets). 

- Click the `Settings` nav link near the top of the page
- Click the `Pages` link on the left nav
- Click the button that says `None` and change it to `master`
- Click the `Save`  button
- Click the `Actions` tab, and wait for the orange yellow dot to turn green
- Click on `Settings` and then `Pages` again.
- Click the "Visit site" button to see YOUR COPY of the _{{page.site-name}}_ site. It looks EXACTLY the same, but is being built from YOUR repository.
