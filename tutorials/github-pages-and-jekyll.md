---
layout: post
title: Create a website with GitHub Pages and Jekyll
date: 2017-01-27 00:00:00
---

_A Condensed and slightly modified version of [Amanda Visconti's excellent Programming Historian tutorial](http://programminghistorian.org/lessons/building-static-sites-with-jekyll-github-pages)_

[sample repository](https://github.com/fredgibbs/hello-world-fg)


## Getting started with GitHub Pages
- Read and complete **UP TO** step 2 of this [short Repository tutorial](https://guides.github.com/activities/hello-world/).
  - Check box to create README
- Click "Create new file" button; name it `index.html`.
- Copy what you see at the [sample repository](https://github.com/fredgibbs/hello-world-fg).
- Save your changes with the Commit button
- Create and save the main.css file, too.
- Go to "Settings tab, and scroll down to the "GitHub Pages" section
- Select master branch. Find the link for your website at the top of that section. It should look like `USERNAME.github.io/hello-world`
- If you get 404 error, just wait a few minutes.
- You’ve created a website! :tada:

## While we wait
- GitHub Desktop demo

## Install a Plain Text Editor
- Use [atom](http://atom.io)

## Install GitHub Desktop
- Download and install [GitHub Desktop](https://desktop.github.com/).
- Enter your GitHub username and password when prompted.
- Check box for "install command line tools".
- Don't worry about connecting to a repository right now. Click "done" when you can.
- Create a folder called `ph-workshop` in your `Documents` folder.
- Click "+" in upper left corner.
- Click "clone" in the upper right of the dialog box.
- You should see your "Hello-world" repository; select it.
- Click the button "Clone hello-world repository".
- Clone your repository to `ph-workshop` folder you created above.
- Right-click on the repository name and "View in Finder [Explorer]".
- You can now see your files you "cloned" from your GitHub [=remote] repository.
- Open your index.md file in Atom; make a few changes.
- In GitHub Desktop, type a short commit message and click "Commit to Master"
- In upper right corner, click "Sync" button.
- Now you should be able to see your changes online (same URL as above).

## Install Dependencies
- Pick up our tutorial [here](http://programminghistorian.org/lessons/building-static-sites-with-jekyll-github-pages#command-line-a-idsection1-4a) ("The Command Line").
- **Mac users:** Continue on with the tutorial (and ignore the rest of this section); stop at "Setting up Jekyll".
- **Windows users:** Stop reading at "Installing Dependencies" and follow these directions:
  - Open the application "Windows Terminal", but right-click to open it and choose "Run as Administrator".
  - Install a program called "Chocolately" by copying and pasting this onto your command line (= PowerShell window): `@powershell -NoProfile -ExecutionPolicy unrestricted -Command "(iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))) >$null 2>&1" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin`
  - Close your Terminal window.
  - Open the application "Windows PowerShell", but right-click to open it and choose "Run as Administrator".
  - Copy into PowerShell (and press enter): `choco install ruby -y`
  - Close and reopen Powershell as Administrator.
  - `gem install bundler`
  - `gem install jekyll`
  - If you get an error at this point, follow [these instructions](http://guides.rubygems.org/ssl-certificate-update/).

## Set up Jekyll and your website
- Use your command line to navigate to your `ph-workshop` directory
- `jekyll new JekyllDemo`
- Pick up our tutorial [here](http://programminghistorian.org/lessons/building-static-sites-with-jekyll-github-pages#running-a-website-locally-a-idsection3aa) (Running a website locally).
- Stop at "Tweaking the Settings".

## Explore the website files
- On the command line:
  - Stop your webserver (Cmd or Ctl C).
  - `bundle show minima`
- Open that folder in Finder/Explorer.
- Open another Finder/Explorer window of your `ph-workshop` folder.
- Move the directories from the `minima-2.1.0` folder to your `ph-workshop` folder.
- Explore the \_includes and \_layouts folders; see the [Jekyll Docs](https://jekyllrb.com/docs/includes/) for reference.
- Edit the
