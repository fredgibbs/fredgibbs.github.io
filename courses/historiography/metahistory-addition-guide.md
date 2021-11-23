---
layout: syllabus
course-title: Historiography
course-slug: historiography
number: HIST 491-001
term: Fall 2021
section: links-guides
---

# _Metahistory_ Addition Guide

This guide is useful ONLY AFTER you have followed the directions for [setting up your _Metahistory_ repository](metahistory-setup) AND have done some [_Metahistory_ revisions](metahistory-revisions).

Before proceeding, make sure you have your own copy of the _Metahistory_ repository, and you can see the functioning website based on YOUR repository in YOUR GitHub account (the URL will look like https://github.com/USERNAME/metahistory/).

### Save time with bookmarks
Create bookmarks in your browser for two locations you will be visiting often:
- YOUR own _Metahistory_ REPOSITORY: https://github.com/USERNAME/metahistory/, replacing USERNAME with your GitHub username.
- YOUR own _Metahistory_ WEBSITE: https://USERNAME.github.io/metahistory

## Grab the sample page
- Similar to what you did when getting your page for revisions, grab the [raw code of the starter essay](https://raw.githubusercontent.com/unm-historiography/metahistory/master/essays/starter.md). (The web version of the starter is [here](https://unm-historiography.github.io/metahistory/essays/starter.html).)
- Working in YOUR repository (the URL will look like https://github.com/USERNAME/metahistory/), go into the `essays` folder **and appropriate subfolder for the time period or theme of your essay.**
- Create a new page for your essay the same way you create posts for your reading responses. CAREFUL WITH THE FOLLOWING:
  - **Be sure your filename is all lower case and uses hyphens instead of spaces!**
  - Don't forget the `.md` extension, just like your reading reflections.
  - It's easy to modify the title later. You can do this by clicking the pencil icon to edit the file, and then click on the filename to edit it.
- Paste in the code you copied from the starter essay.
- Edit the header of your file (the metadata between the `---` marks at the top) to reflect your TITLE, SUBTITLE, NAME.
- Ignore the `toc-blurb` and `toc-image` fields for now.
- To get your page to show on the left nav, find `toc-section` name and change the value to one of the following:
  - antiquity
  - medieval
  - early-modern
  - enlightenment
  - modern
  - postmodern
  - thematic
- Commit your new page.


## Test your page
- **You MUST have your essay publicly accessible to participate in the peer review process!**
- Test your page by going to https://USERNAME.github.io/metahistory (you bookmarked it, right?) and navigate to your page. Remember there is a short lag between when you commit your file and when those changes appear on the actual webpage.
- If your page is not showing up in the left nav, check the `toc-section` parameter.
  - Even if that's not working, you can still test/view your essay at: https://USERNAME.github.io/metahistory/essays/FOLDER/FILENAME, where FOLDER is the folder in which you created a new file, and FILENAME is the name of the file you created.
- Once you have a working page, add the URL of your essay to our [class list](https://github.com/unm-historiography/2021-fall/blob/main/metahistory-topics.md).

### Troubleshootoing
If your page never appears, check these in the following order:
- Are you really tired or frustrated? Trust me, just take a break. It's WAY TOO EASY to miss little details when exhausted or in a hurry.
- Make sure the URL you are trying to access matches the folder structure in your repository.
- Double check your metadata at the top of the page is correct, including the `---` above AND below the data.
- Double check that all the image code blocks are intact and you're not missing any brackets or quotes.


## Page build errors
If you commit a file with a syntax error (a missing quote or something like that), you should get an email from GitHub saying you have a "page build error". Until you fix it, you won't see any subsequent changes you save on your online version.
