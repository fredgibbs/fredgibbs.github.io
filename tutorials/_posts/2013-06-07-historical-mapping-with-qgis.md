--- 
layout: post 
title: Historical Mapping with QGIS
date: 2013-06-07 00:00:00
category: tutorial
---

## Installing QGIS

Installing QGIS is not as straightforward as it could be, so don&#8217;t worry if you get or feel confused. You need to download and install 3 items, QGIS and two other required small software packages. Do QGIS last, since it won&#8217;t install without the other two.

For Macs, you need [this](http://www.kyngchaos.com/files/software/frameworks/GSL_Framework-1.15-2.dmg) and [ this](http://www.kyngchaos.com/files/software/frameworks/GDAL_Complete-1.9.dmg) and [this](http://www.kyngchaos.com/files/software/qgis/QGIS-1.8.0-2.dmg).

If the above links don&#8217;t work, The most up to date versions of the necessary components can be found, organized by operation system, at the [QGIS download page](http://hub.qgis.org/projects/quantum-gis/wiki/Download#11-Standalone-Installer-recommended-for-new-users)

## Using Shapefiles

Shapefiles are standard file formats for conveying map information. If interested, you can [read more about the standard](http://www.digitalpreservation.gov/formats/fdd/fdd000280.shtml). 

You can find a number of useful directory of shapefile repositories, such as the [one here](http://www.statsilk.com/maps/download-free-shapefile-maps).

Just for kicks, let&#8217;s find a map of all the counties in the US, one that&#8217;s listed on [this census.gov page](https://www.census.gov/geo/maps-data/data/tiger-line.html). (Towards the middle of the page, click &#8220;Download,&#8221; and then &#8220;County Shapefile&#8221; links.) You&#8217;ll notice that you actually get a directory full of files. Since we&#8217;re going to start acquiring and generating a files, you might want to create a new directory somewhere to keep everything organized, ideally somewhere that&#8217;s easy to get to (like your desktop) for the time being. You should put your county map directory in there.

## Display a Map

When you first start QGIS, you&#8217;ll get a whole lot of white and a bunch of cryptic icons. The easiest way to begin is to load a map&#8212;or more accurately, a shape file.

Click on the left of the two + icons (Add Vector Layer). Choose Source Type of &#8220;Directory&#8221;, Source Type as &#8220;U.S. Census TIGER/Line&#8221; and clikc &#8220;Browse&#8221; to choose the directory that you downloaded from wherever you saved it.

You should see the outlines of the US counties. Cool.

To see more of what&#8217;s behind this data, right-click on the name of the layer that appears in the Layers column at left. Select &#8220;Open Attribute Table.&#8221; You&#8217;ll see a grid of data that comes as part of the dataset. You&#8217;ll notice that these include county names, for example, which makes things a bit more humanly readable. You can see, for example, how the county names appear in the NAMELSAD field.

## Get and Display Data

This section of the tutorial rephrases some of [this tutorial](http://qgis.spatialthoughts.com/2012/03/using-tabular-data-in-qgis.html), which you may find useful for screenshots.

To really use the power of GIS, you need to find data that you can somehow correlate to the components of the map. In this case, we have already loaded a shapefile of US counties, so we&#8217;d like to have county data, so ideally we can find information at a county level.

Let&#8217;s see if we can find information about, say, the Civil War. A quick search for civil war data turns up an [index of major battle sites](http://archive.org/details/CivilWarBattleSummariesOfMajorBattles). Download the Civil Battle Summaries CSV file. Open this up in a spreadsheet application like Excel. You&#8217;ll notice that a field ridiculously named &#8220;Location1&#8243; fields contains basically the names of counties that we have already loaded into QGIS.

Basically. But not exactly. You&#8217;ll also notice that the field is in a slightly different form than we want, since it has a the two-letter state code appended to the county names. Here&#8217;s when the knowledge of simple scripting comes is extremely useful. Although creating the script has to be the subject of another tutorial, we can use a quick python script to clean up the CSV file so it&#8217;s Location1 field displays only the county name without other accoutrements. You can use the python script to fix it yourself, or you can just [download the improved file](http://fredgibbs.net/downloads/qgis-tutorial/cwb2.csv).

Curiously, to bring in data in a CSV file into QGIS, you need to &#8220;Add Vector Layer,&#8221; just as we did to load the original map. This time, make sure you have &#8220;File&#8221; selected as the input type. Once you have loaded your CSV file, you should see the filename appear in the list of vectors on the left of your map.

Right-Click on the original map layer and select &#8220;Properties&#8221;.

Click the &#8220;Join&#8221; Tab (2nd from right).

Click the + icon.

We want to join this data table to our newly loaded one (called cwb2 for me). More specifically, we want to link the Location1 field of our civil war data file (though it appears as Locati) to the the NAMELSAD field in the original county data file. Select the Join field and Target field appropriately. Click &#8220;OK&#8221; twice.  

Now we&#8217;ve created a link between the county shape and the Civil War battle data, based on county name. Again, this is only a &#8220;virtual&#8221; join, and doesn&#8217;t do anything with the actual files. We can see the data joined together by looking at the attributes for the original layer.

If you look at your map now, you might be dismayed to see that it looks exactly the same. But why should we expect it to be any different? We&#8217;ve created a link between two fields, but haven&#8217;t told QGIS what it should do with the new information (= civil war battle data) that we&#8217;ve linked to the county boundary data. Luckily, GQIS makes it fairly easy to automatically style the map based on the data we&#8217;ve linked it to. In particular, we can change the background color as follows:

Return to the Properties menu of the original map.

Click the Style Tab.

Instead of the default Single Symbol, choose Categorized.

Let&#8217;s adjust the background color based on &#8220;Total Est. Casualties&#8221; from our Civil War table, so select that field from the Column dropdown menu.

Choose a color ramp that you like.

Click &#8220;Classify&#8221; (which assigns a color to a value range).

You can see that QGIS has assigned a different shade of blue for each unique value in the casualties field. This could be useful depending on the values you have, but not for the ones we have. 

We need to tell QGIS not to load all of our values as text, but as numbers, per [these instructions](http://anitagraser.com/2011/03/07/how-to-specify-data-types-of-csv-columns-for-use-in-qgis/).

Once we do that, we can use the &#8220;Graduated&#8221; style, with a mode like &#8220;Natural Breaks&#8221; that gives us fewer colors. You can increased the number of categories (=colors) as well.

Click &#8220;OK&#8221; and you&#8217;ll see the color coding at work.

Imagine doing this with any kind of map and your data.

## Overlay a Historic Map

It can be very helpful to see historic data on modern maps, but it&#8217;s nice to see a bit more of the historic context. 

First you&#8217;ll need a historic map. You can use, for example, the David Rumsey map collection. We can download a map from the 1860s. We might use something like [this one](http://www.davidrumsey.com/luna/servlet/detail/RUMSEY~8~1~234576~5510152:Phelps-&#038;-Watson-s-Historical-And-Mi?sort=Pub_List_No_InitialSort%2CPub_Date%2CPub_List_No%2CSeries_No&#038;qvq=w4s:/when/U.S.%20Civil%20War;sort:Pub_List_No_InitialSort%2CPub_Date%2CPub_List_No%2CSeries_No;lc:RUMSEY~8~1&#038;mi=48&#038;trs=383#). Save in the highest resolution allowed without being logged in, which will be good enough for our purposes.

Here we need to say a few words about map projections, which can be a complicated topic. When just looking at a single map, you might not think much about the particular projection. But when using different maps together, the differences in their projections need to be taken into account. For now it&#8217;s enough to say that the representation of our historic map (whatever it may be) is not going to be the same as modern county boundaries. So we&#8217;ll need to adjust (or more technically rectify) the old map to fit the new one that has our data. 

If this in unclear, pretend our historic map is printed on transparent silly putty. Now imagine stretching it in various directions so all of the state boundaries line up with the modern state boundaries, and fixing it atop the modern map. We can do this, for instance, by sticking pins on certain obvious features through the silly putty and sticking them in the same features on the modern map. Thus the putty will be stretched in various directions (possibly different amounts in different places) but will ultimately come to match the modern one. Obviously this corrupts the historical value of the original.

QGIS has a built-in georeferencer that can help us to this, and you can work through a [good tutorial on the necessary steps](http://qgis.spatialthoughts.com/2012/02/tutorial-georeferencing-topo-sheets.html).