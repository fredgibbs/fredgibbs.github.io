---
layout: post 
title: Document Similarity with R
date: 2013-06-04 00:00:00
category: tutorial
---

When reading historical documents, historians may not consider applications like R that specialize in statistical calculations to be of much help. But historians like to read texts in various ways, and (as [I&#8217;ve argued in another post](http://fredgibbs.net/blog/history-theory/learning-to-read-again/ "learning to read. again.")) R helps do exactly that. By using a special text mining module provides us with a lot of built-in mathematical functions that we can use to explore&#8212;and, more importantly, read&#8212;texts.

This tutorial provides a skeletal recipe for reading a set of texts (a corpus) through the statistical software R. Although we often consider a text a vehicle for meaning, a text can also be considered as a string of words (ordered), or a bag of words (unordered). These words can be represented in ways that are useful for analysis that aren&#8217;t constrained by grammatical order. It is possible, in fact, to read texts as a function, statistically speaking, of how words relate to each other in a single text compared to how they relate to words in other texts.

In other words, we can (and must) learn new ways of reading texts, and to embrace mathematical abstraction and visualization as interpretative allies rather than block-box enemies. The typical humanist creation of meaning from text is no less black-boxy that reading the text through mathematical lenses. These new ways are not the savior of the humanities, and they do not guarantee new insights into anything. They may be utterly useless for your purposes, in the same way that trying to analyze sources through a Marxist or a Feminist lens may be totally unhelpful. But we expect good historians to carry a large bag full of lenses, and R is just another one.

One example of a new ways of reading is the case of document similarity: How do you know what texts are similar to others? Their &#8220;meaning&#8221;? Okay. But let&#8217;s make the reasonable assumption that an author&#8217;s intended meaning dictates her word choice. Therefore, similar documents&#8212;at least those that are not highly allegorical or metaphorical in different ways&#8212;will use similar sets of words in similar ways. Implicitly detecting these patterns is largely how we constitute meaning, even when reading in the traditional way. But it&#8217;s not the only way.

There are several tutorials that can help you get started with R, like [this one](http://www.r-bloggers.com/simple-text-mining-with-r/) and [this one](http://rdatamining.wordpress.com/2011/11/09/using-text-mining-to-find-out-what-rdatamining-tweets-are-about/). The [TM documentation](http://cran.r-project.org/web/packages/tm/vignettes/tm.pdf "TM Documentation") (PDF) proves helpful as well.

Each of these have there own strengths and weaknesses, and I have more or less tried to cobble them together here. What follows is the recipe for creating a basic dendrogram from a small set of documents. This it is more useful as a way of getting you to think differently about your texts than to gain serious proficiency with R itself. But motivation is at least half the battle, and it does cover some of the basic text mining procedures.

## Picking Your Corpus

You&#8217;ll need to have a small set (= corpus) of texts (= documents) to play with. Having a small corpus is a double-edged sword, as it is easier to see what&#8217;s going on, but the results often appear to be trivial and so it&#8217;s easy to think the whole method is worthless. Whether or not you&#8217;ll immediately think R is cool probably depends on selecting a corpus and documents lengths that aren&#8217;t too big or too small. You need to have all of your texts in separate plain text files (like a .txt extension), gathered together in a single directory.

I&#8217;ve created a set of 5 trivial texts. You can [download the zip file](http://fredgibbs.net/tutorials/downloads/corpus.zip), move it to wherever you&#8217;d like on your computer, and unzip it. just remember where you put it, as you&#8217;ll need the directory later.

[Download R](http://cran.wustl.edu/) for your operating system. Usually you&#8217;ll want the click the link that gives you the latest binary. After you download and run it, it will guide you through the installation process. Launch the R application, which should bring up the R &#8220;console&#8221; (= application window), which provides you with an interface to your R workspace. Everything that follows should be done in the R console.

##  Getting Started 

As a preliminary step that isn&#8217;t worth explaining right now:

<pre class="brush: r; title: ; notranslate" title="">Sys.setenv(NOAWT=TRUE)</pre>

Now, download and load up the text mining module with:

<pre class="brush: r; title: ; notranslate" title="">
install.packages(&quot;tm&quot;)
require(&quot;tm&quot;)
</pre>

If you are prompted to select a mirror, pick the location nearest you.

Load your corpus into your workspace with the following command, but replace YOURPATH with the full path to your directory that is full of texts (keep the quotes when you paste in your own path).

<pre class="brush: r; title: ; notranslate" title="">my.corpus &lt;- Corpus(DirSource(&quot;YOURPATH&quot;))</pre>

##  Prepare your Texts 

First thing to do is to normalize the texts, which means to remove punctuation, cases, and numbers. These are called &#8220;transformations&#8221; in R-speak and you can get a list of available transformations by typing:

<pre class="brush: r; title: ; notranslate" title="">
getTransformations
</pre>

(Note that there is one transformation that does not appear on this list, but that is nevertheless handy: &#8220;tolower&#8221; which makes all words lowercase.)

The syntax for using the transformations is:

<pre class="brush: r; title: ; notranslate" title="">
my.corpus &lt;- tm_map(my.corpus, removePunctuation)
</pre>

The tm_map function allows you to perform the same transformations on all of your texts at once. In this case, we apply the removePunctuation transformation to each of the texts in our corpus (my.corpus). These changes (as all others done via the R console) happen only in R space&#8212;nothing alters your original files.

You also might want to remove common words (= stopwords) that obscure the more interesting ones. You can remove standard English stopwords:

<pre class="brush: r; title: ; notranslate" title="">
my.corpus &lt;- tm_map(my.corpus, removeWords, stopwords(&quot;english&quot;))
</pre>

You can also remove your own list of stopwords if you know there are words that appear in every text and might skew your results. There are two ways to do this. If you have a short list, you can create a &#8220;character vector&#8221; (more R-speak) right in the console:

<pre class="brush: r; title: ; notranslate" title="">
my.stops &lt;- c(&quot;history&quot;,&quot;clio&quot;, &quot;programming&quot;)
my.corpus &lt;- tm_map(my.corpus, removeWords, my.stops)
</pre>

If you have a longer list, you can type the words in (or programmatically create) a text file with all of your stopwords. The file should list all of your words with a space in between. Like this:

history clio programming historians text mining&#8230;

From the R console, you import the file, create a character vector, and remove the words:

<pre class="brush: r; title: ; notranslate" title="">
my.list &lt;- unlist(read.table(&quot;PATH TO STOPWORD FILE&quot;, stringsAsFactors=FALSE)
my.stops &lt;- c(my.list)
my.corpus &lt;- tm_map(my.corpus, removeWords, my.stops)
</pre>

Our results will be more useful if we can lemmatize our corpus. Instead of counting &#8220;run&#8221; and &#8220;runs&#8221;, for instance, as 2 separate words, we want to count them as the same word. To lemmatize the corpus means to change all variants of words into the same stem word. 

To do this, we need another package to help with the lemmatizing. But we can use tm_map in way we&#8217;ve already done.

<pre class="brush: r; title: ; notranslate" title="">
install.packages(&quot;Snowball&quot;)
require(&quot;Snowball&quot;)
my.corpus &lt;- tm_map(my.corpus, stemDocument)
</pre>

Now we have a nice (but by no means perfect) corpus to investigate. 

##  SAVE your Place

At this point, you might want to save your &#8220;place&#8221; so to speak, so that you can open this corpus later in another R session with all the transformations already complete. The command line version of this is [here](http://www.statmethods.net/interface/workspace.html "Saving Workspace in Command Line"), but it&#8217;s easier to use the GUI. In the Workspace Menu, choose &#8220;Save Workspace File&#8230;&#8221; and save under a name in a location of your choice. To load your workspace when you want to start again, choose &#8220;Load Workspace File&#8230;&#8221;. 

##  Investigate Your Texts

We want to see our corpus expressed as a document matrix. There are two kinds that are useful to us, depending on how we want to read the text. there are TermDocument matrix and a DocumentTerm matrix. The only difference is how variables are mapped to the X and Y axis of the matrix. TermDocument means that the terms are on the vertical axis and the documents are along the horizontal axis. DocumentTerm is the reverse. Each of these let you see the texts in different ways, although one (or both) may not be very helpful for you.

<pre class="brush: r; title: ; notranslate" title="">
my.tdm &lt;- TermDocumentMatrix(my.corpus)
</pre>

To see the new representation of your corpus, inspect it:

<pre class="brush: r; title: ; notranslate" title="">
inspect(my.tdm)
</pre>

You can see your texts listed across the top and each word listed down the left side. Notice that the words have been lemmatized. The numbers indicate, as you can guess, how many times each word appears in each document.

You can compare your TermDocumentMatrix to a DocumentTermMatrix:

<pre class="brush: r; title: ; notranslate" title="">
my.dtm &lt;- DocumentTermMatrix(my.corpus, control = list(weighting = weightTfIdf, stopwords = TRUE))
inspect(my.dtm)
</pre>

Obviously this is another view with the x and y axes reversed.

Up until now, maybe you have considered your corpus as composed of discrete texts, themselves composed of discrete words. It can be helpful to know how they are associated with each other.

There are commands to compute word frequencies across the whole corpus. This finds all words that appear at least twice in any document. Adjust the 2 to other values. Go crazy!

<pre class="brush: r; title: ; notranslate" title="">
findFreqTerms(my.tdm, 2)
</pre>

You can also inspect word associations, in this case with a minimum threshold of .20:

<pre class="brush: r; title: ; notranslate" title="">
findAssocs(my.tdm, 'mine', 0.20)
</pre>

But sometimes it&#8217;s nice to see visual relationships of words and texts.

<pre class="brush: r; title: ; notranslate" title="">
my.df &lt;- as.data.frame(inspect(my.tdm))
my.df.scale &lt;- scale(my.df)
d &lt;- dist(my.df.scale,method=&quot;euclidean&quot;)
fit &lt;- hclust(d, method=&quot;ward&quot;)
plot(fit)
</pre>

What does the dendrogram say? Terms higher in the plot appear more frequently within the corpus; terms grouped near to each other are more frequently found together. The nice thing about a trivial corpus is that you can easily inspect each document at a glance (and all at the same time) and match that up with what the dendrogram shows. This is also why a corpus that you know something about can help you understand what the dendrogram does, so that it makes more sense when you use it on a corpus you know less well.

Isn&#8217;t this what you discover from reading? In this case, obviously yes. But the dendrogram scales much better than traditional reading techniques. Even with a smaller corpus of hundreds rather than thousands of texts, R is likely to read the texts a bit different from how a person would. It is perhaps useful in seeing what relationships do NOT appear&#8212;perhaps ones that curious and not fully objective readers sort-of want to be there and might more easily identify&#8212;and thus provide an important complement to our own heuristic readings.