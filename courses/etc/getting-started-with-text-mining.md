---
layout: default
title: getting started with text mining | fredgibbs  
---

# Getting Started with Text Mining
This page presents a list of resources potentially useful for anyone who is relatively new to text mining, wants to see what's possible, what's not, and wants to do a bit of playing around with it. This is not a comprehensive list of everything written about text mining. It is geared toward non-technical novices. Articles that deal with particular algorithms or complicated statistics concepts have been omitted to encourage sanity and experimental play.

In general, it's grouped by what seem to be the most pervasive topics and themes relevant to text mining in general.


## Common Misconceptions That Probably Aren't Helping You
- You need to have BIG DATA.
- There is a single best way to do text mining.
- Text mining is quantitative and the humanities are qualitative.
- Text mining is necessarily technical and makes you grow a giant beard and wear oversized metal-rimmed glasses.
- Data is data and if you just plug it into some tools, you'll learn cool things.
- People should make better tools to make text mining easier.
- All of the work preparing data is not what historians do.


## General Methodology Articles
A few general articles to explain the big picture:

Ted Underwood, [Where to Start with Text Mining](http://tedunderwood.com/2012/08/14/where-to-start-with-text-mining/).

[Basic introduction of text mining principles and terminology](http://www.cch.kcl.ac.uk/legacy/teaching/av1000/textanalysis/method.html).

John Burrows, [Textual Analysis](http://www.digitalhumanities.org/companion/view?docId=blackwell/9781405103213/9781405103213.xml&chunk.id=ss1-4-4) from _A Companion to Digital Humanities_. 

Stanford Literary Lab, [Quantitative Formalism: an Experiment](http://litlab.stanford.edu/LiteraryLabPamphlet1.pdf).

Fred Gibbs, [Learning to Read. Again](http://fredgibbs.net/posts/post/text%20mining/learning-to-read-again/).

Dan Cohen, [Searching for the Victorians](http://www.dancohen.org/2010/10/04/searching-for-the-victorians/).

D. Sculley and B. M. Pasanek, “Meaning and Mining: The Impact of Implicit Assumptions in Data Mining for the Humanities,” Literary and Linguistic Computing 23, no. 4 (September 29, 2008): 409–24.

Andrew Goldstone and Ted Underwood , "The Quiet Transformations of Literary Studies: What Thirteen Thousand Scholars Could Tell Us," forthcoming in _New Literary History_. 


## Online Project Sites
To see some of the techniques presented in a open an accessible way:

Rob Nelson, [Mining the Dispatch](http://dsl.richmond.edu/dispatch/).    
Cameron Blevins, [Topic Modeling Martha Ballard's Diary](http://historying.org/martha-ballards-diary/).    
[With Criminal Intent](http://criminalintent.org/)


## Research Articles
Some traditional-looking articles with text mining as a core method:

Shlomo Argamon et al., [Gender, Race, and Nationality in Black Drama, 1950-2006: Mining Differences in Language Use in Authors and Their Characters](http://digitalhumanities.org/dhq/vol/3/2/000043/000043.html).

Lauren Klein and Jacob Eisenstein, “[Reading Thomas Jefferson with TopicViz: Towards a Thematic Method for Exploring Large Cultural Archives](http://src-online.ca/index.php/src/article/view/121/259),” Scholarly and Research Communications 4, no. 3 (2013).


## Tools

### Tools you need to install on your computer
Some of the easiest ways to get started is to use an online tool that saves you the step of installing software.

[Google n-gram viewer](https://books.google.com/ngrams)    
[Bookworm](http://bookworm.culturomics.org/)    
[Voyant](http://voyant-tools.org/) and a [list of projects that have used it](http://docs.voyant-tools.org/about/examples-gallery/)    
[Overview](http://overview.ap.org/faq/); begin with a short [introductory video](http://vimeo.com/71483614)    

### Tools you need to install on your computer
If you want to get a bit more serious about text mining, or if you get tired of having to do everything online, there are a few excellent tools that give you tremendous text mining power, but very little in the way of visual interfaces.

[AntConc](ttp://www.antlab.sci.waseda.ac.jp/software.html), with a very [helpful tutorial](http://www.antlab.sci.waseda.ac.jp/software/AntConc_Help_3.1.2/AntConc_Help.htm).


# Working with Digital Texts
One of the scariest conceptual leaps that humanists must make is moving from printed archival materials to digital files that you can't touch or mimeograph. This shift requires not only a new way of thinking about texts, but also how to organize them, access them, and how they relate to each other. It also requires 


## Places to get texts and OCR Projects
[Chroncling America](http://chroniclingamerica.loc.gov/) Digitized Newspapers from the Library of Congress.    
eMOP | [Early Modern OCR Project](http://emop.tamu.edu/).    
EEBO | [Early English Books Online](http://eebo.chadwyck.com/home).    

Your local libraries may know of local repositories for digital data as well.


# Working with Data
One of the neat advantages of text mining is the way you can combine multiple data sources at larger than usual scales. Usually this will mean finding data from multiple sources, and of course they won't be in the same format. In order to make use of all your texts, you'll need to make sure the data are suitable for machine processing with standardized formats, not stray characters, etc. 

**Getting your data to look nice takes FAR LONGER than you want it to, than you think it should, than you think it deserves to.** It is arguably the most difficult and crucial part of the process.** Exploratoring your corpus algorithmically is quite fun, but unless you like to geek out with python scripts and regular expressions, cleaning data is decidedly the unfun part of text mining. But the key to success here is to remind yourself that even when preparing data, _you are doing history_, not trying to get ready for it. It's the digital vesion of combing through the archives. Not glamorous, but necessary, and there certainly are both art and science aspects to it.


## Normalizing Data
For more on the basic concepts of organizing data:
Hadley Wickham, [Tidy Data](http://vita.had.co.nz/papers/tidy-data.pdf).

[Open Refine](http://openrefine.org/) is a excellent tool for normalizing data. Begin with the 3 tutorial videos to get a sense of what it can do.

Seth van Hooland, Ruben Verborgh, Max De Wilde, [Cleaning Data with OpenRefine](http://programminghistorian.org/lessons/cleaning-data-with-openrefine.)

[DataWrangler](http://vis.stanford.edu/wrangler/)


## DIY
If you want to really use text mining methods, you'll need some facility with data beyond what pre-packaged tools give you. They simply can't account for all th circumstances you'll encounter. 

But you're in luck! There is a great tool for getting your data into *any format you need*! It's called python, and it's a progamming language that is easy to learn and very powerful in terms of manipulating data. To get started:    
[Commmand Line Crash Course](http://learnpythonthehardway.org/book/appendixa.html)

[Set up your working environment](http://learnpythonthehardway.org/book/ex0.html)

Start learning python fundamentals at [Code Academy](http://www.codecademy.com/en/tracks/python) and [Learn Python the Hard Way](http://learnpythonthehardway.org/book/).

Once you get a better feel for the basics, see what else you can do at [The Programming Historian](programminghistorian.org).


## Dealing with OCR issues
Almost all digital text that isn't born digital goes through some kind of OCR process, which can yield inaccuracies in the transcription process. Depending on the scale of your analysis and what it is your looking for, these may or may not cause difficulties.

If you are just starting out with text mining techniques, these errors are not terribly important.

If you want to do more careful literary or linguistic study, these errors might become sufficiently annoying that they should be corrected. 


[Mining for the Meanings of a Murder: The Impact of OCR Quality on the Use of Digitized Historical Newspapers](http://www.digitalhumanities.org/dhq/vol/8/1/000168/000168.html).    
Ted Underwood, [Basic OCR Correction](http://usesofscale.com/gritty-details/basic-ocr-correction/).    
Ted Underwood, [A Half-Decent OCR Normalizer for English Texts after 1700](http://tedunderwood.com/2013/12/10/a-half-decent-ocr-normalizer-for-english-texts-after-1700/).    
Laura Turner O'Hara, [Cleaning OCR’d text with Regular Expressions](http://programminghistorian.org/lessons/cleaning-ocrd-text-with-regular-expressions).


## Processing Images
You might lots of photos of documents that are begging to be turned into digital text. But you need to work at scale, which means having some kind of process to deal with your images in bulk rather than one at a time.

Miriam Posner, [Batch-processing photos from your archive trip](http://miriamposner.com/blog/?p=678).


## Staying Organized
To any meaningful text analysis, you're going to work with non-trivial amounts of texts, documents, files. **You don't need big data!** But if it's more than you can really keep in your head or possibly read in a resonable amount of time, or you would like to be more efficient at figuring out what zero in on, you'll need to stay organized so that you know what you've done to what texts.

If you are going to be processing files directly, either to improve images, do OCR, or subject them to computational methods, you'll want to be able to keep your files organized on your filesystem--meaning a directory / folder structure that makes sense.

You can also use Zotero or similar organizational tools, but this creates some distance between you and the actual files which can be annoying if you are often working with them directly, either trying to upload them to online tools, or feed them into tools you've downloaded to use on your own machine.

William J Turkel, [Workflows and Digital Sources](http://williamjturkel.net/how-to/) (and explore the links!).


## Topic Modeling
One of the techniques most in vogue at the moment is topic modeling. These articles cover the fundamental concepts, most with lots of links to various kinds of explanations (most are very accessbile, but some are probably more technical or mathematical than you want.)

Megan R. Brett, [Topic Modeling: A Basic Introduction](http://journalofdigitalhumanities.org/2-1/topic-modeling-a-basic-introduction-by-megan-r-brett/).

Scott Weingart, [Topic Modeling for Humanists: A Guided Tour](http://www.scottbot.net/HIAL/?p=19113).

Elijah Meeks and Scott Weingart, [The Digital Humanities Contribution to Topic Modeling](http://journalofdigitalhumanities.org/2-1/dh-contribution-to-topic-modeling/). Follow the links in this brief introduction!

[Topic Modeling and MALLET](http://programminghistorian.org/lessons/topic-modeling-and-mallet).

Miriam Posner, [Very Basic Strategies for Interpreting Results from the Topic Modeling Tool](http://miriamposner.com/blog/?p=1335).

