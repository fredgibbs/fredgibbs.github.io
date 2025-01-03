---
layout: post
title: A New Minimalist and Versioned Website
date: 2013-08-09
---

Isn't it silly to expect people to pay $600 for a scarf? Fashion designer Tomas Maier replies that we should all [just have less](http://www.newyorker.com/reporting/2011/01/03/110103fa_fact_colapinto), embracing the philosophy that we should simply have a few nice things that can be replaced when needed. I recently found this logic especially attractive when packing up a house full of too much stuff I just have to have but didn't remotely miss once it was boxed up.

This militant but elegant minimalism permeated my thinking about my website as I began to think about both old and new projects and posts and syllabi upon the dawn of a new academic year. How could I convey what I'm thinking about and working on and teaching in the clearest and simplest way?

<p class="has-pullquote pullquote-adelle" data-pullquote="As for the website, I wondered: How much less could I have?"></p>

I thought I would start by stripping away absolutely everything that isn't absolutely essential: sidebars, categories, tag clouds, antiquated punctuation for print publications, extraneous typefaces, design elements. How small could my headers and footers be? Do I need an extensive list of post categories? Archives organized by date? _An automated navigation bar?_ *An administrative backend?*

I wanted the simplest experience not only for reading, but also for writing and managing what I've written. I never was entirely comfortable that an essay or CV or syllabus existed entirely as an entry in a database table rather than a document that could be managed separately. I wanted, for example, to improve some essays or courses supposedly finished some time ago but that hadn't quite reached their potential. I wanted to embrace the potential of ongoing scholarship (rather than the one and done model that we propogate for silly reasons), yet still maintain the traditional space/time publishing continuum so that people can know what version others may have read at a particular time. This is not to say that Wordpress cannot manage versions of pages, simply that there are far more efficient ways to do that.

<p class="has-pullquote pullquote-adelle" data-pullquote="My only regret is that I put off trying this for so long."></p>
Thus I decided to experiment with using [Jekyll](http://jekyllrb.com/) to create a static website from [Markdown](http://daringfireball.net/projects/markdown/) and [Textile](http://redcloth.org/textile files). **It's far easier to write, revise, and publish than it ever has been.** Jekyll also makes it a snap to work locally and preview any website pages before making them live. Using "Git" to manage my files means that I can easily see where I am in the editing process even after I've put the website down for a while.

Thus the current website has been culled (I have plenty of evidence that not everything is worth saving!), revised, rebirthed, and relocated to [Github Pages](https://github.com/fredgibbs/fredgibbs.github.io.) Obviously there was a small hurdle in using the command line to install the necessary components and learn new markup languages, but the entire exercise was considerably less painful than I expected (even with a few version issues to work out); cobbling together a few tutorials brought the learning curve within easy reach.


<p class="has-pullquote pullquote-adelle" data-pullquote="The difficulty of the installation challenges simply pale in comparison to the joy of not writing HTML and pasting and inevitably correcting text within the pseudo-WYSIWYG editor."></p>
The processed proved unexpectedly rewarding in the ways that using version control forces decisions about writing workflows, serialized scholarship, publishing, archiving, and sharing. It's not that I hadn't previously thought about these issues _in general_, but that I never really had to make decisions about what was most important to me and decide how to implement them. I realized that I had resisted using version control on my website under the auspices of experimental freedom, but it turns out that it was freedom of sloppiness that I wanted. In reality, the layer of bureaucracy that using version control (via Git) adds to my workflow is far less encumbering than the combination of Wordpress, FTP, and Copy and Paste that I had come to see as standard if not inevitable.


<p class="has-pullquote pullquote-adelle" data-pullquote="I resisted using version control on my website under the auspices of experimental freedom, but it was freedom of sloppiness that I wanted."></p>
Using Git to manage (make changes, stage, commit, and push them to the repository) essays and syllabi gleefully challenged invisible habits. I used to think of each version of a document (a syllabus, say) as its own separate file that had to be archived as it changed over time. Now, I'm treating a post or syllabus as a facet of a more abstract object that is continually evolving. Versions that had been separate files that I had to manage are now simply snapshots viewed in the Github history browser. In terms of the revision process, I now have to think carefully about what I am changing and why. I'm still learning to work with greater clarity, purpose, and precision. **Freedom through discipline!**

Have I succeeded at having less? My readers will have to be the judge of whether the new website design is effective, though I think one must agree that there is generally less (and profitably so) than before. In terms of my own workflow, I know that I traded one sophisticated infrastructure in Wordpress for several more specific infrastructures, like Git, Github, Ruby, Jekyll, etc. In a way, I have more. But the gestalt of these tools, each of which does one job very well, makes a much less encumbered experience of writing and revising and staying organized. And it's **way** better than a nice scarf.
