---
layout: syllabus
course-title: Critical Thinking with AI
course-slug: critical-thinking-with-ai
term: Spring 2026
section: links-guides
title: DE Editing Guide
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
  - Click on the `index.md` file to bring it up on the right of your screen
  - Replace the `title:` field near the top of the page with YOUR title
  - Replace the `summary:` content as well

- Now you need to commit your changes, like you did when setting up your page:
  - Click the network icon on the left, as you did when duplicating the {{page.sample-folder}} folder
  - Enter something like "update title and summary"
  - Click the `Commit & Push` button

### Adding your own images
Your `images` folder comes with a bunch of images you don't need. You can delete all of those or leave them. But you'll need to add your own images to your essay.



### Uploading images to GitHub
1. Make sure you have your image saved and renamed to kebab case. It will be easier to troubleshoot missing images if the filename tells you what the image is.
2. Go to your GitHub repository, Code tab, editor (via `.`)
3. Expand the `{{page.sample-folder}}` folder to see your own project folder
4. Expand your project folder to see your `images` folder
5. Drag your image file from wherever it is on your computer to the images folder.
6. Make sure it ended up in the images folder! Drag and drop again if need be.
5. Click the network icon at left, type a commit message, and `Commit & Push`.


### Edit your page to use the new files
Your page uses a little code snippets to display your images. You need to update any existing snippets to reference the files you uploaded.

{% include alert.html class='warning' 
title = 'Take care with filenames' 
text = " 
- Filenames much match **exactly**
- Include the correct file extension (`.jpg`, `.png`, `.gif`, `webp`, etc.)
- Match capitalization, spaces, underscores, etc. (`.jpg` ≠ `.jpeg` ≠ `.JPG` )
"
%}

**Page sure your image code references your image upload**
- Find the code on your page: `{%raw%}include images/figure-wrap.html
  image-path="images/books-britannica.jpeg"`{%endraw%}
- Change what's between the quotes for the `image-path` to be your image filename. It should start with `images/` because that's where you just put your image.
- Be sure to keep the quotes, and make sure what's between the quotes is EXACTLY the same as the name of the file you uploaded.
- `Commit & Push` changes as usual.

### Verify Everything Works
After uploading an image and updating your code snippets with the filenames of your image files (and committing your changes):

1. Wait 1-2 minutes for GitHub Pages to rebuild your site
2. Visit your page on your website (you bookmarked it, right?)
3. Check that:
   - Your image displays correctly


### Troubleshooting

**Image doesn't appear?**
- Make sure you didn't accidentally remove or add extra code characters, like {%raw%}{%{%endraw%} or {%raw%}%}{%endraw%}
- Make sure you're not missing any quotation marks 
- Double-check that the file names in your code exactly match the uploaded file names (including capitalization and file extension)
- Wait a few minutes and refresh your browser—GitHub Pages can take time to update.

**Image is too large or too small?**
- You can add `width="50%"` to the figure include to control size, picking whatever percent of the page width that you need.