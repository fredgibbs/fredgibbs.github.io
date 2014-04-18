--- 
layout: course 
title: Advanced Digital History | Using Historical Data
date: 2012-12-31 23:56:31 
categories: [course]
status: draft
---

#This is a DRAFT ONLY

## Course Description
This course explores the theoretical and methodological issues now facing humanistic study in a digital age. It presents a broad survey of how powerful new research methodologies now allow those working in the humanities to ask and answer fundamentally different kinds of questions. It explores topics such as data visualization, geo-spatial analysis, and text mining. On the whole, it aims to provide conceptual fluency on topics such as the uses of new media to present scholarly research, the changing role of museums and libraries, and the politics of authority and expertise in knowledge networks. The course also reflects on the changing nature of the humanities (such as their possible convergence toward the social sciences). This course challenges the typical conceptions of how one ought to produce and consume history as well as provides guidelines for effectively bridging and combining humanities and technology skills that will make you more employable.

## Key Skills
*   Familiarity with various mark-up languages (XML, KML, RDF, TEI)
*   Some competency with various web programming languages (PHP, Javascript)
*   Databases in theory and practice
*   Command line work with Python
*   Various methods of web scraping
*   Using APIs
*   Ability to create maps programmatically
*   Various text mining techniques and tools 

### Course Expectations
* A serious effort for all programming assignments, and continued progress on course projects
* Perseverance and tolerance for frustration with technical difficulty. Must be able to have fun and learn while accomplishing nothing.
* Do not suffer in silence for too long. You will be frustrated and confused in this course, and that's necessary. But there is a point at which it is no longer productive, and then you should ask for help. 

### Course Project
The goal of the course project is to show that you have developed and applied some technical skills relevant to digital history to your research/career(s). The hope is that you'll be able to gradually improve an existing project you've started or completed, or start a new project (or a component of a larger project) that you intend further develop at a later time.

### Grading
Your course grade will be largely determined by effort--both on the quality of your presentations and the extent to which you can show tangible progress on your project throughout the semester. Everyone comes into the course with different skills and backgrounds, so there is no expectation that everyone can do the same things at the end, but that you've moved significantly beyond where you were when you started. However, you do need to be able to actually complete (to a high degree) the assignments and final project to show that you are putting in the effort to acquire the target skills. 

*   Completing assignments: 15%
*   Topic tutorials: 15%
*   Active and intelligent participation in class discussions / labs: 40%
*   Final project: 20%
*   Presentation of Final Project: 10% 


## Schedule

### Introduction to the course and syllabus revisions
Course mechanics, introductions, possible course topics, organize, syllabus, tutorial assignments, final projects


### Command Line Basics
Explore the file system, basic commands, and make a website.
Tutorial in preparation.


### Scripting with Python
Go through the first 40 tutorials on [learnpythonthehardway](http://learnpythonthehardway.org/book/)]


### Introduction to version control
We're going to work with a lot of code for this class, and learning about coding means developing good habits from the start. Version control helps your own programming habits as well as makes it much easier for us to share code with each other---especially handy for debugging! 

Read how to [set up your git repository](https://help.github.com/articles/set-up-git), and familiarize yourself with the [reference manual](http://gitref.org/index.html).

#### Assignment
Create an account at Github, create a repository, and commit your website files there. Post the URL of your repository to the course blog.


### Data Manipulation
Put those python skills to use! 

#### Assignment
* Download civil war CSV file
* Create a python script to:
** Read in the text file line by line
** Strip off the State
** Write the new line to a new text file


### APIs and geolocating
* Read the API TUTORIAL (in development)


### Creating and Interacting with Maps
*   Lab: Creating your own Google Map to see historical data change over time
*   Key skills: KML, shapefiles, QGIS


### Web scraping
We're not limited to data that we can find in nice files. Sometimes, we need to automate our process of gathering data that we can find on the web.

#### Assignment
Find set of pages relevant to your research where data spans multiples pages. Write python script that iterates through the pages, extracts relevant content and saves it to your computer


### Javascript
*   Read through some Javascript tutorials: [1](http://www.tizag.com/javascriptT/) | [2](http://www.quirksmode.org/dom/intro.html) | [3](http://www.hunlock.com/blogs/Essential_Javascript_--_A_Javascript_Tutorial) | [4](http://www.tutorialspoint.com/javascript/javascript_builtin_functions.htm/) | [5](http://docs.jquery.com/Tutorials:How_jQuery_Works)
*   Lab: Using Javascript and JQuery to add functionality to webpages


### Visualizing with D3
* Gentle introductions to D3 via [slides](http://lws.node3.org/#landing-slide)
* [quick demonstration](http://christopheviau.com/d3_tutorial/)
* [website tutorial](http://alignedleft.com/tutorials/d3/)

These and others are listed [here](https://github.com/mbostock/d3/wiki/Tutorials) (though quality varies widely).  

You should also read an introduction to [SVG](http://tutorials.jenkov.com/svg/index.html). After that, you should understand how D3 [creates SVG elements from your data.](http://bost.ocks.org/mike/join/).

### Mapping Networks with Gephi


### Databases
*   Assignment for class: Create a web page with any necessary functionality to show off your data and explorations of it during the course.
*   Read this [Introduction to Databases](http://code.google.com/edu/tools101/mysql.html). Also, spend some time with [ this overview of MySQL](http://www.mysqltutorial.org/basic-mysql-tutorial.aspx).
* For class, and forever beyond, you'll need access to a MySQL database. You can use one through your web host, but it may be easier in the long term to get a PHP, MySQL, Apache envrionemnt running on your own computer for future explorations. There are free packages that install and initialize everything for you, such as [MAMP (mac)](http://www.mamp.info/en/index.html) and [ EasyPHP (windows)](http://www.easyphp.org/) or [WAMP (windows)](http://www.wampserver.com/en/#). These also come with phpMyAdmin that gives you a nice graphical tool via your web browser (rather than the command line) to manage your database, but you can still manually run SQL commands like the tutorials have as examples. Once you have such an environment running on your machine, you'll be able to work much more quickly.
*   Lab: Plan to design and construct a database for your research--we'll consider best practices as you do.
*   Key skills: Database architecture, MySQL, SQL, phpMyAdmin


### PHP
*   Read through this [PHP tutorial](http://www.tizag.com/phpT/syntax.php) and [examples of using forms](http://www.killersites.com/community/index.php?/topic/3064-basic-php-system-view-edit-add-delete-records-with-mysqli/)
*   Lab: Work through various PHP webpages and functionality
*   Key skills: programming fundamentals, PHP datatypes, syntax, likely problems


### Text mining
Some introductory (sort-of) readings: 

* [text mining terminology](http://comminfo.rutgers.edu/~msharp/text_mining.htm) 
* [document similarity through compression](http://parezcoydigo.wordpress.com/2011/10/09/clustering-with-compression-for-the-historian/)
* [19th cen. text problems](http://tedunderwood.com/2011/10/07/the-challenges-of-digital-work-on-early-19c-collections/)
* [Text mining with R](http://cran.r-project.org/web/packages/tm/vignettes/tm.pdf)
* More R tutorials

####Assignment 
Gather some texts and explore


### Topic modeling
* Some introductory (sort-of) readings
* [a literary intro](http://www.matthewjockers.net/2011/09/29/the-lda-buffet-is-now-open-or-latent-dirichlet-allocation-for-english-majors/) 
* [probably the best general intro](http://tedunderwood.com/2012/04/07/topic-modeling-made-just-simple-enough) 
* [interpreting results](http://miriamposner.com/blog/?p=1335) 
* [a guided tour](http://www.scottbot.net/HIAL/?p=19113) 
* [a real history example](http://historying.org/2010/04/01/topic-modeling-martha-ballards-diary/)

####Assignment
Create some topic models for a set of documents, and be prepared to report on what you noticed.


### (Un)anticipated errors and work time
*   Get stuck. Get help.


### Presentations &amp; Conclusions
Presentations of your final projects should be around 10 minutes, with 5 additional minutes for questions and suggestions. Your main goal is to show that you are applying techniques from the course for your own research. But it's also an opportunity to ask for advice!