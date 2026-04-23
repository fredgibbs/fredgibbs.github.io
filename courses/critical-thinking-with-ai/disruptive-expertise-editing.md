---
layout: syllabus
course-title: Critical Thinking with AI
course-slug: critical-thinking-with-ai
term: Spring 2026
section: links-guides
title: Food Stories Editing and Submitting Guide
site-name: "Disruptive Expertise"
repository-name: disruptive-expertise
sample-folder: episodes
---

# _{{page.site-name}}_ Editing Guide

This guide is useful ONLY AFTER you have followed the directions for [setting up your repository]({{page.repository-name}}-site-setup) and [setting up your page]({{page.repository-name}}-page-setup).

**Reminder! Create bookmarks for two locations you will be visiting often:**
- YOUR own _{{page.site-name}}_ **REPOSITORY**: https://github.com/USERNAME/{{page.repository-name}}/
  - Replace USERNAME with your GitHub username!
- YOUR own _{{page.site-name}}_ **WEBSITE**: https://USERNAME.github.io/{{page.repository-name}}


## Editing your new page

### Replace content on the sample page
Now that you have a working website and your own page to edit, you're ready to replace all the sample content with your own. 

It's best to write out anything you want on your page in Word or whatever and then copy and paste it into GitHub when you're editing your page. Editing in the tiny GitHub text edit box is annoying and it's too easy to miss typos and other mistakes. 

Once you have replaced the sample text with your own, click the green `Commit changes...` button. 


### Upload Your Image File to GitHub
1. Go to your GitHub repository in your web browser
2. Navigate to YOUR story folder by clicking on it.
3. Click the **Add file** button (upper right)
4. Select **Upload files**
5. Drag your image file into the upload area or click to browse and locate it on your computer.
6. Scroll down and click **Commit changes**


### Edit your page to use the new files
Your page uses two special "include" codes to display your audio recording and image. You need to update these codes to match the files you uploaded.

{% include alert.html class='warning' 
title = 'Take care with filenames' 
text = " 
- Filenames much match **exactly**
- Include the correct file extension (`.jpg`, `.png`, `.gif`, etc.)
- Match capitalization, spaces, underscores, etc.
- Keep the caption text inside the quotes
"
%}

**Page sure your image code references your image upload**
- Find this line on your page: `{%raw%}{% include figure.html image-path="bbq.png" caption="Your caption here" %}`{%endraw%}
- Change what's between the quotes for the `image-path` to be your image filename. 
- Be sure to keep the quotes, and make sure what's between the quotes is EXACTLY the same as the name of the file you uploaded.

**Commit your changes!**
Use the green `Commit Changes` button as usual to save your work.


### Verify Everything Works
After uploading both files and updating code snippets with your filenames (and committing your changes):

1. Wait 1-2 minutes for GitHub Pages to rebuild your site
2. Visit your food story page on your website (you bookmarked it, right?)
3. Check that:
   - Your audio player appears and plays your recording
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

