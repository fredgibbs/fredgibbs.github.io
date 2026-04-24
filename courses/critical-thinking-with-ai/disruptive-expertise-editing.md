---
layout: syllabus
course-title: Critical Thinking with AI
course-slug: critical-thinking-with-ai
term: Spring 2026
section: links-guides
title: Food Stories Editing and Submitting Guide
site-name: "Disruptive Expertise"
repository-name: disruptive-expertise
sample-folder: essays
---

# _{{page.site-name}}_ Editing Guide

This guide is useful ONLY AFTER you have followed the directions for [setting up your repository]({{page.repository-name}}-site-setup) and [setting up your page]({{page.repository-name}}-page-setup).

**Reminder! Create bookmarks for two locations you will be visiting often:**
- YOUR own _{{page.site-name}}_ **REPOSITORY**: https://github.com/USERNAME/{{page.repository-name}}/
  - Replace USERNAME with your GitHub username!
- YOUR own _{{page.site-name}}_ **WEBSITE**: https://USERNAME.github.io/{{page.repository-name}}


## Editing your new page
Now that you have a working website and your own page to edit, you're ready to replace all the sample content with your own. 

### Test an edit on your new page
Make sure you're on YOUR repository (the URL will look like https://github.com/USERNAME/{{page.repository-name}}/). Make sure you're on the `Code` tab (normally the default view). You should see the list of files in the repository (starting with folders like _data,_includes, _layouts, etc).

- Press the `.` (period) key to go into Editor Mode
- Click on the little arrow to the left of the your essay folder to see its contents
  - You should see an `images` folder and a file called `index.md`
  - Click on the index.md file to bring it up on the right of your screen
  - Make a simple change to the page title or content
  - Click the network icon on the left, as you did when duplicating the {{page.sample-folder}} folder
  - Enter something like "test edit"
  - Click the Commit button

### Adding your own images
Your `images` folder comes with a bunch of images you don't need. You can delete all of those or leave them. But you'll need to add your own images to your essay.



### Upload Your Image File to GitHub
1. Go to your GitHub repository in your web browser
2. Navigate to YOUR story folder by clicking on it.
3. Click the **Add file** button (upper right)
4. Select **Upload files**
5. Drag your image file into the upload area or click to browse and locate it on your computer.
6. Scroll down and click **Commit changes**


### Edit your page to use the new files
Your page uses a little code snippets to display your images. You need to update any existing snippets to reference the files you uploaded.

{% include alert.html class='warning' 
title = 'Take care with filenames' 
text = " 
- Filenames much match **exactly**
- Include the correct file extension (`.jpg`, `.png`, `.gif`, etc.)
- Match capitalization, spaces, underscores, etc. (`.jpg` ≠ `.jpeg` ≠ `.JPG` )
- Keep the caption text inside the quotes
"
%}

**Page sure your image code references your image upload**
- Find this line on your page: `{%raw%}{% include figure.html image-path="bbq.png" caption="Your caption here" %}`{%endraw%}
- Change what's between the quotes for the `image-path` to be your image filename. 
- Be sure to keep the quotes, and make sure what's between the quotes is EXACTLY the same as the name of the file you uploaded.

**Commit your changes!**


### Verify Everything Works
After uploading an image and updating your code snippets with the filenames of your image files (and committing your changes):

1. Wait 1-2 minutes for GitHub Pages to rebuild your site
2. Visit your page on your website (you bookmarked it, right?)
3. Check that:
   - Your image displays correctly
   - The caption shows properly


### Troubleshooting

**Audio or image doesn't appear?**
- Make sure you didn't accidentally remove or add extra code characters, like {%raw%}{%{%endraw%} or {%raw%}%}{%endraw%}
- Make sure you're not missing any quotation marks 
- Double-check that the file names in your code exactly match the uploaded file names (including capitalization and file extension)
- Wait a few minutes and refresh your browser—GitHub Pages can take time to update

**Image is too large or too small?**
- You can add `width="50%"` to the figure include to control size: