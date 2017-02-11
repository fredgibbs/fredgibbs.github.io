---
layout: syllabus
title: Introduction to Digital Humanities
term: Winter 2017
number: HIST 698-002
date: 2017-01-04 00:00:00
section: schedule
---

# IN PROGRESS!
This syllabus is a living document and changes frequently, depending on what's going on in the course, though the general workload will remain more or less as indicated. If you print it out, you'll need to keep your paper version up to date with the online version.

In general, we will spend the beginning part of classes talking about the assignment due that day, addressing questions or concerns that arose while completing it, troubleshooting, and discussing more technical aspects of the tool/method and its practical utility. Then we'll move on to the next tool/method with a general introduction, discussion of its potentials and limitations, work through some tutorials, and go over the assignment for the next meeting (and make sure everyone is ready to tackle it).

Very rarely are all readings listed required (though all assignments are); I try to list relevant readings that I think are worth knowing about and allow everyone to focus on what's most interesting to them and bring their interests and perspectives to our discussions.

## Spy on your colleagues
- [Angelica](https://sasariti.github.io/)
- [Imani](https://imanico.github.io/)
- [Jonathan](https://quintj.github.io/)
- [Josh](https://joshuarrrr.github.io/)
- [Kaitlyn](https://k8lyn6.github.io/)
- [Marisol](https://filamarisol.github.io/)
- [Nicholas](nrholterman.github.io)
- [Paula](https://pr-curtis.github.io/)
- [Sarah](https://spswanz.github.io/)
- [Scott](https://skirycki.github.io/)



## 1: Ethos of Digital Humanities / Digital Historiography

### Before Class
William Cronon, [The Public Practice of History in and for a Digital Age](http://www.historians.org/perspectives/issues/2012/1201/The-Public-Practice-of-History-in-and-for-a-Digital-Age.cfm).

Julia Flanders, [The Productive Unease of 21st-century Digital Scholarship](http://digitalhumanities.org/dhq/vol/3/3/000055/000055.html).

Stephen Ramsay, [DH Types One and Two](http://stephenramsay.us/2013/05/03/dh-one-and-two/).

Mark Sample, [The Digital Humanities Is Not About Building, It’s About Sharing](http://webcache.googleusercontent.com/search?q=cache:IyRYK7RWT8cJ:www.samplereality.com/2011/05/25/the-digital-humanities-is-not-about-building-its-about-sharing/+&cd=1&hl=en&ct=clnk&gl=us).

Lisa Spiro, ["This Is Why We Fight": Defining the Values of the Digital Humanities](http://dhdebates.gc.cuny.edu/debates/text/13)

### In Class
- Introduction to [Zotero](http://zotero.org), [GitHub](http://github.com) (+ version control with git), [GitHub Pages](https://pages.github.com), [Markdown](https://guides.github.com/features/mastering-markdown/#intro).
- Connect to the Zotero Library.
- Set up GitHub account, and complete the [Hello world tutorial](https://guides.github.com/activities/hello-world/).



## 2: The Command Line
Some of the most powerful tools you might use for digital research and publishing don't have a GUI (Graphical User Interface) for many reasons that we'll discuss. If you haven't used a command line interface before, it can be disorienting, but we'll try for a very gentle introduction.

If you have Windows, you'll need to use PowerShell; if you have a Mac, you'll need to use your Terminal application. For our purposes, they are functionally equivalent.

### Before class
Review Sample and Spiro from last week (since we didn't get to them).

Jim Mussell, “Doing and Making: History as Digital Practice,” in Tony Weller (ed.), _History in the Digital Age_ (London: Routledge, 2013), 79–94.

Read through (but don't worry about completing) the in-class tutorials beforehand; we'll go through them in class with some deviations. Please come to class with questions about the terms and concepts so we can be most efficient with our work time.


### In class
We'll work through some basic examples with the Command Line and Pandoc and troubleshoot any issues you run into.

- Dennis Tenen and Grant Wythoff, [Sustainable Authorship in Plain Text using Pandoc and Markdown](http://programminghistorian.org/lessons/sustainable-authorship-in-plain-text-using-pandoc-and-markdown).
- Download and install [pandoc](http://pandoc.org/installing.html). Work through this [introduction to pandoc on the command line](http://pandoc.org/getting-started.html).
- [Intro to bash](http://programminghistorian.org/lessons/intro-to-bash) (Windows users: don't use Git Bash as the tutorial indicates, use Powershell instead).
- Another tool to note: [ImageMagick](http://www.imagemagick.org/script/index.php).
- Create a simple website with GitHub Pages.

### Useful References
[GitHub Markdown Reference Guide](https://guides.github.com/features/mastering-markdown/) and a more [stylized PDF](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf). This [Markdown sandbox](http://daringfireball.net/projects/markdown/dingus) allows you to experiment and see what your Markdown will look like in HTML and on a webpage.

If you haven't found it already, I highly recommend that you use [Atom](https://atom.io) as your text editor.



## 3: Digital Publishing

We'll use our new knowledge of the command line and several tutorials to help us install Jekyll (which is what GitHub uses) and manage our websites more easily. First, we'll talk about different strategies for and reasons why you might want to be more hands on with your own digital presence.

### Before class (why you might care about your own website)
It is not necessary to read each of these in great depth, but you should skim through each to take away what you find interesting. This reading list is a bit long simply to provide a number of perspectives and considerations, not because they are all absolutely essential readings.

For your response essay: please comment on what you found attractive or repulsive about the readings in terms of professional identity? Any interesting perspectives you hadn’t considered? Particularly specious arguments? Omissions?

Christopher P. Long, [The Googled Graduate Student](http://cplong.org/2013/09/the-googled-graduate-student/).

Jentery Sayers, [Do You Need Your Own Website while on the Job Market](http://www.chronicle.com/blogs/profhacker/do-you-need-your-own-website-while-on-the-job-market/35825).

Patrick Iber, [A Defence of Academic Twitter](https://www.insidehighered.com/advice/2016/10/19/how-academics-can-use-twitter-most-effectively-essay).

Katrina Gulliver, [10 Commandments of Twitter for Academics](http://chronicle.com/article/10-Commandments-of-Twitter-for/131813/).

Chuck Tyron, [Blogging, Scholarship, and the Networked Public Sphere](http://mediacommons.futureofthebook.org/mla2009/tryon/mla2009draft).

Kim Barbour and David Marshall, [The Academic Online: Constructing Persona Through the World Wide Web](http://journals.uic.edu/ojs/index.php/fm/article/view/3969/3292).

Also, read through the tutorials below so that you can start to conceptualize what we'll be doing. Come to class with lots of questions about these, which we can address before we start and as we go. If you'd like to jump into the tutorials and do them, that's great, but it's more important to build familiarity with the various tools and steps to get them running.

### In class
We're going to set up our websites locally (that is, on our own computers) so that we don't have to do everything via GitHub. We'll install Jekyll, the software that GitHub Pages uses to make our websites (but first we have to install some software that Jekyll requires). The tutorials can get confusing, we're going to go through them together with some deviations.

- Zotero, Zotfile, and Dropbox
- Review of previous technologies and a few related examples.
- Brief introduction to GitHub Desktop and review of branches.
- We are going to work through Amanda Visconti, [Building a static website with Jekyll and GitHub Pages](http://programminghistorian.org/lessons/building-static-sites-with-jekyll-github-pages). There is some review of what we did last time, so it should seem familiar, and you can skip some of the steps. Follow the relevant Mac or Windows instructions when they diverge under the "Installing Dependencies" section. - **Stop at the "Setting up Jekyll" section because we've already got a website to connect to.**
- We won't be using the automatic blog feature of Jekyll for now, so you should read through that section, but don't worry about doing it.

For another perspective and for reference, see Keith Miyake, [Create Your (FREE) Website Using Github and Jekyll](http://digitalfellows.commons.gc.cuny.edu/2016/03/21/create-your-free-website-using-github-and-jekyll/).

Remember: once you start using git on the command line, you can always [undo just about anything](https://github.com/blog/2019-how-to-undo-almost-anything-with-git).


## 4: Typography + HTML + CSS
Getting a handle on the fundamentals of design and typography goes a long way in improving communication. We're going to practice typography with our CVs.

### Before class
- [Thinking with Type](http://thinkingwithtype.com)
- [Intro to HTML and CSS](http://learn.shayhowe.com/html-css/) (read through chapter 6)
- [The Elements of Typographic Style Applied to the Web](http://webtypography.net/toc/)

### In class
- Zotero, Zotfile, and Dropbox (neglected last time)
- Command line + pandoc review; ImageMagick
- GitHub Desktop tour
- Using branches to edit your CV
- Using git on the command line
- Review and clarify the HTML and CSS tutorials
- Fork demo repository for sample code
- Jekyll, Markdown, HTML, CSS localhost review
- Introduction to [Jekyll includes and templates](https://jekyllrb.com/docs/includes/)
- CSS Frameworks (like http://getskeleton.com)
- Begin fleshing out and styling your own site/pages
  - Home (index.md)
  - About
  - 698-Portfolio
  - CV
- Start playing with more complex web frameworks (like [Bootstrap](http://getbootstrap.com))

## 5: Digital Spatial History

### Before class
Richard White, [What is spatial history](http://www.stanford.edu/group/spatialhistory/cgi-bin/site/pub.php?id=29)?

Anne Kelly Knowles, [A More Humane Approach to Digital Scholarship](http://parameters.ssrc.org/2016/08/a-more-humane-approach-to-digital-scholarship/)

David J. Bodenhamer, "The Spatial Humanities: Space, Time and Place in the New Digital Age," in Tony Weller (ed.), _History in the Digital Age_ (London: Routledge, 2013), 23-38.


### In class
- Zotero, Zotfile, and Dropbox (neglected last time, again)
- Using branches for working copies of files
- More on Jekyll layouts and themes
  - Default installation and [minima theme](https://github.com/jekyll/minima).
  - Creating your own layouts to minimize maintenance
- Using and learning from CSS Frameworks (like [skeleton](http://getskeleton.com))
- Continue fleshing out and styling your own site/pages
  - Home (index.md)
  - About
  - 698-Portfolio
  - CV
- Start getting familiar with more complex web frameworks (like [Bootstrap](http://getbootstrap.com))

After we get a little more situated with our portfolios we'll turn to the mapping articles for this week. Then, playing around with maps:

- [Google Maps tutorial](http://programminghistorian.org/lessons/googlemaps-googleearth)
- Google Earth and Historic Maps demo
- [Carto](https://carto.com)
- [MapBox](https://www.mapbox.com/showcase/)
- [StoryMaps](http://story.maps.arcgis.com/home/index.html)
- If you decide you love web programming: [Leaflet](http://leafletjs.com)


## 6: Mapping with QGIS

### Before class
I. N. Gregory and A. Hardie, “Visual GISting: Bringing Together Corpus Linguistics and Geographical Information Systems,” _Literary and Linguistic Computing_ 26, no. 3 (2011): 297–314.

Matthew Wilkens, "Geolocation Extraction and Mapping of Nineteenth-Century U.S. Fiction."

- So as not to lose your hard-earned knowledge from last time, continue fleshing out and styling your own site/pages. Don't be afraid about breaking anything. You should break stuff. Remember, you can use branches to keep good working copies of your files as you experiment.
- Complete the [Google Maps tutorial](http://programminghistorian.org/lessons/googlemaps-googleearth). Compared to what you've been doing, this is going to be SO EASY.
- Download and install [QGIS](http://www.qgis.org/en/site/).
- MAC USERS: When you open the disk image that you download, you'll see 4 .pkg files that you must install in the order they are numbered.


### In class
- Jekyll gems themes review
- Layouts and includes review
- CSS frameworks and boilerplates (like [skeleton](http://getskeleton.com) or [milligram](https://milligram.github.io))
- Consider the Nav Bar (like https://mobiforge.com/design-development/mobile-friendliness-101-how-to-build-a-fixed-navigation-bar).
- Readings discussion
- Google Maps and Earth questions
- More on historic maps in Google Earth
- Troubleshoot any installation issues and go over the QGIS interface and other basic GIS concepts.

- Web map tools/resources to be aware of:
  - [MapWarper](http://mapwarper.net)
  - [MapAnalyst](http://www.mapanalyst.org/index.html)
  - [Historic Census Data](https://www.nhgis.org)
  - [StoryMaps](http://story.maps.arcgis.com/home/index.html)
  - [Carto](https://carto.com)
  - [MapBox](https://www.mapbox.com/showcase/)
  - If you decide you love web programming: [Leaflet](http://leafletjs.com)


## 7: GIS and Portfolio Questions

### Before class
- Gergely Baics, [Mapping as Process: Food Access in Nineteenth-Century New York](https://globalurbanhistory.com/2016/05/17/mapping-as-process-food-access-in-nineteenth-century-new-york/).
- Scan through 3-5 [DH GIS Projects](http://anterotesis.com/wordpress/dh-gis-projects/). It's a mixed bag. They may be defunct, overly technical, totally confusing, or kind of awesome. Be prepared to highlight for everyone else the intriguing and questionable features of the sites you explored. Questions to keep in mind:
  - How does mapping/GIS figure into the project? Is it necessary?
  - What kind of data is being used? Where is it from? Is it accessible or reusable?
  - How much does the design of the site matter in taking it seriously?
  - How would you rate its usability?
- Work on your portfolios! Keep in mind the criteria below. In general, aim to do simple things well. See how simple you can make your site, but with a clear and consistent design aesthetic (and required content, of course). **Bring questions to class!** This is your best chance to get technical help before you are largely on your own before the portfolio review. It's also usually the case that people benefit from hearing explanations even if they haven't encountered or care about that particular issue

### In class
- GIS Project critiques and discussion
- Portfolio questions (includes, layouts, HTML, CSS, Markdown, typography, design, etc)
- Work through 3 simple [Mapping with QGIS tutorials](http://fredgibbs.net/tutorials/)
- For future reference, you get stuck or have questions, consult the [QGIS Training Manual](http://docs.qgis.org/2.2/en/docs/training_manual/), [the QGIS wiki](http://hub.qgis.org/projects/quantum-gis/wiki/How_do_I_do_that_in_QGIS), and an [array of tutorials](http://qgistutorials.com)
- MapBox Demo and data movement
- Start your own maps (for your portfolio)


## 8: Portfolio Critiques

### Before class
- Work on your portfolios! Keep in mind the criteria below. In general, aim to do simple things well. See how simple you can make your site, but with a clear and consistent design aesthetic (and required content, of course).

### In class
- Portfolio critiques. You'll show off your portfolio for the rest of the class and explain what you're trying to do and where you've had trouble. There are two main goals here: 1) to have a deadline to keep portfolios moving forward; 2) get ideas from other people (from their own sites as well as questions/comments). Questions we will address in class for each site:
  - Existence of basic pages and content
  - Is there a consistent layout and navigation scheme?
  - Typographic crimes? Consistency?
  - Where does the design help or hinder the site and content?
  - What is extraneous? What is missing?


## SPRING BREAK

## 9: Text Mining
Under what circumstances are these techniques useful? How can they be used most effectively? We're going to talk about the different formats of data these tools require, problems moving from one to the other; pros and cons of their various approaches, and whatever you newly discovered about your sources from taking a broad view of your sources/data.

### Before class
- Ted Underwood, [Seven ways humanists are using computers to understand text](https://tedunderwood.com/2015/06/04/seven-ways-humanists-are-using-computers-to-understand-text/).
- Shlomo Argamon et al., [Gender, Race, and Nationality in Black Drama, 1950-2006: Mining Differences in Language Use in Authors and Their Characters](http://digitalhumanities.org/dhq/vol/3/2/000043/000043.html).
- Look through [Mining the Dispatch](http://dsl.richmond.edu/dispatch/).    


#### Skim through some OCR readings
- Andrew J. Torget & Jon Christensen, [Mapping Texts: Visualizing American Historical Newspapers](http://journalofdigitalhumanities.org/1-3/mapping-texts-project-by-andrew-torget-and-jon-christensen/).
- Patrick Spedding, “‘The New Machine’: Discovering the Limits of ECCO,” _Eighteenth-Century Studies_ 44, no. 4 (2011): 437–53.
- OCR Correction [here](https://usesofscale.com/gritty-details/basic-ocr-correction/) and [here](https://tedunderwood.com/2013/12/10/a-half-decent-ocr-normalizer-for-english-texts-after-1700/).
- The [Early Modern OCR Project](http://emop.tamu.edu).
- Various OCR correction tutorials at _Programming Historian_.


### In class
- Load some of your texts into [Voyant](http://voyant-tools.org/) and write a critique of one of the [projects that have used it](http://docs.voyant-tools.org/about/examples-gallery/)    
- Play around with [Timeline Curator](http://www.cs.ubc.ca/group/infovis/software/TimeLineCurator/)
- Loading data into [Bookworm](http://bookworm.culturomics.org/)



## 10: Topic Modeling

### Before class
Ted Underwood, [Topic Modeling Made Just Simple Enough](http://tedunderwood.com/2012/04/07/topic-modeling-made-just-simple-enough/).

Megan R. Brett, [Topic Modeling: A Basic Introduction](http://journalofdigitalhumanities.org/2-1/topic-modeling-a-basic-introduction-by-megan-r-brett/).

Andrew Goldstone and Ted Underwood, "The Quiet Transformations of Literary Studies: What Thirteenth Thousand Scholars Could Tell Us."

Scott Weingart, [Topic Modeling for Humanists: A Guided Tour](http://www.scottbot.net/HIAL/?p=19113).

Cameron Blevins, [Topic Modeling Martha Ballard's Diary](http://historying.org/martha-ballards-diary/).

### In class
- Install and use [MALLET](http://programminghistorian.org/lessons/topic-modeling-and-mallet) to topic model some of your sources.
- Load up some of your sources into [Overview](https://www.overviewdocs.com/), and compare what you can learn from "raw" topic modeling with MALLET and Overview's presentation of your documents.



## 11: Network Analysis

### Before Class
Scott B. Weingart, [Demystifying Networks, Parts I and II](http://journalofdigitalhumanities.org/1-1/demystifying-networks-by-scott-weingart/).

Elijah Meeks and Maya Krishnan, [Introduction to Network Analysis and Representation](http://dhs.stanford.edu/dh/networks/).

Dmitry Paranyushkin, [Identifying the Pathways for Meaning Circulation using Text Network Analysis](http://noduslabs.com/research/pathways-meaning-circulation-text-network-analysis/).

Skim through the documentation for [Palladio](http://hdlab.stanford.edu/palladio/), especially via the [help page](http://hdlab.stanford.edu/palladio/help/).


### In Class
- Upload data and create a network graph with Palladio.
- Download, install, and model texts with [Gephi](http://gephi.org), using Martin Grandjean, [Introduction to Network Analysis and Visualization](http://www.martingrandjean.ch/gephi-introduction/). You might also consult [another set of tutorials](https://seinecle.github.io/gephi-tutorials/) for additional perspectives.


## 12: Critiquing Digital Scholarship
What are the fundamental criteria for critiquing digital history projects? How much does the traditional peer review model need to change to accommodate new types of historical work/projects?

Journal of American History, [Digital History Reviews](http://jah.oah.org/submit/digital-history-reviews/).

Modern Language Association, [Guidelines for Evaluating Work in Digital Humanities and Digital Media](http://www.mla.org/resources/documents/rep_it/guidelines_evaluation_digital).

Todd Presner, [Evaluating Digital Scholarship](http://idhmc.tamu.edu/commentpress/digital-scholarship/).

Cameron Blevins, [The New Wave of Review](http://www.cameronblevins.org/posts/the-new-wave-of-review/).

Fred Gibbs, “The Poetics of Digital Scholarship,” in Matt Bernico and Manuela Kölke (eds.), _Ontic Flows: From Digital Humanities to Posthumanities_, 101-122. (New York and Dresden: Atropos Press, 2016).


## 13: Digital Literacies/Pedagogy
Johanna Drucker, [Humanities Approaches to Graphical Display](http://digitalhumanities.org/dhq/vol/5/1/000091/000091.html).

John Theibault, [Visualizations and Historical Arguments](http://writinghistory.trincoll.edu/evidence/theibault-2012-spring/).

Elijah Meeks, [Infoviz and New Literacies](https://dhs.stanford.edu/algorithmic-literacy/infoviz-and-new-literacies/).

[Visualeyes](http://www.viseyes.org/)    
[Viewshare](http://viewshare.org)    
[Flowing Data](http://flowingdata.com)


## 14: OPEN


## 15: Loose ends, conclusions, etc.
