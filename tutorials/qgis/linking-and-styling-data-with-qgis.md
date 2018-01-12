---
layout: post
title: Linking and Styling Data with QGIS
created: 2015-10-27
updated: 2017-02-12
---

The [first part](/tutorials/qgis/making-a-map-with-qgis.html) of our tutorial covered some basics of QGIS.

## Adding Complexity with More Data
The county map is a praise-worthy accomplishment if you've never made a map before. But obviously loading a single data set like county boundaries is not super useful on its own.

You are probably already realizing one of the principal challenges of GIS work. The actual display of the map is pretty easy (QGIS does all the work for you!). The challenge lies in finding (or creating) the data you need, as well as making different data sets work with each other. An introductory tutorial is not the place to dive into the many different techniques, but let's work through a typical and relatively straightforward example.


## Get and Display Data
We've already got counties in the form of shapefile; let's see if we can add population data to our map. We'll get our data from census.gov again, at their page for [county population estimates](https://www.census.gov/data/datasets/2016/demo/popest/counties-total.html). (The navigation links at census.gov can lead you in circles; using the search function is usually the best way to find data you're after.) This time, however, we aren't going to use a shapefile because we're not interested in drawing geographic features (like county boundaries); we're interested in just the data (populations of counties).

{% include figure.html src="/assets/images/qgis/county-census-data.png" caption="Census.gov has great data, but not always intuitive ways to access it" class="raw" %}

There is a long link in the middle of the page that starts with "County Totals Dataset..." Click it; if you have trouble, you can click [here](http://www.census.gov/popest/data/counties/totals/2014/files/CO-EST2014-alldata.csv).

Now you should see:

{% include figure.html src="/assets/images/qgis/alldata.png" caption="Please do not hit the panic button" %}

Perhaps not what you were expecting. Unlike the previous lesson when we downloaded data specifically made for GIS software, this data is plain text data (yay plain text!). It's in a standard file format, CSV (_Comma Separated Values_). You could load this into a spreadsheet, and it would look like:

{% include figure.html src="/assets/images/qgis/census-spreadsheet.png" caption="CSV data isn't so scary in a more familiar form" %}

For now, hit your browser's back button, then right click the link you just clicked on, and choose "Download Linked File As..." (or the equivalent for your browser) and save the file wherever you're storing your files for these lessons. Just keep the default file name, `co-est2015-alldata.csv`.

{% include figure.html class="icon right" src="/assets/images/qgis/add-csv-icon.png" %}
To load this data into QGIS, click the icon on the left with a comma (towards the bottom of the icon stack) to "Add Delimited Text Layer". You'll see a new dialog window appear, so that we can tell QGIS a little about our data file so it can load it properly.

{% include figure.html src="/assets/images/qgis/create-text-layer.png" caption="Importing: the first step to data mastery" %}

Click "Browse" in the upper right to select the CSV file you just downloaded.

Make sure the box "First record has field names" is checked, since this is true for our CSV file. You can think of the first line of the file as the column headings when viewing the file in Excel. Notice that the preview pane on the bottom tells us how QGIS is interpreting the data in the file. If your CSV file isn't properly formatted, or you've chosen options from this dialog that do not correspond to the CSV file, the preview will show you that something is wrong.

{% include figure.html src="/assets/images/qgis/create-text-layer-2.png" caption="Pay attention to the preview to avoid future headaches" %}

Especially if you're someone who just likes to click "OK" without really paying attention, you'll notice the "OK" button is grayed out to save you from yourself. Here's why:

This CSV file contains data related to geography (population by counties), but not actually any geographic data (our other files did). In other words, it's not specifically for mapping; it's just data. So we need to tell QGIS not to look for any specific geographic data for "Geometry Definition" we want to select "No Geometry". Now you can click "OK".

Some people expect their map to change here---as computers can read our minds---but we haven't told QGIS what to do with this new data. More specifically, we have not indicated how this data relates to the county boundary map we've already loaded.

Let's just check out the data first. Right click on the `co-est2015-alldata` layer and "Open Attribute Table". Notice that our CSV file has loaded properly and contains lots of great data, like county name (the `CTYNAME` field), and the 2010 population (labeled as `CENSUS2010POP`). Take notice of the values in the `CTYNAME` field.

Now, open the attribute table for our original map of the counties (so you'll have two attribute tables open at once). You'll notice that it, too, contains a field (= column) listing all the county names, but in this file it's called `NAMELSAD`. Our two datasets (the county geographic data and the population data) both have the county names, and it doesn't matter that one is labeled as `CTYNAME` and the other as `NAMELSAD` because we can see (from just browsing through them) that the data is _exactly_ the same (they both have county names with Capitalization and the word "County" in each case. Because of this congruity, we can join these tables together so that we can visualize the population data on our county map. Close the attribute tables for now.


## Joining Datasets Together
Double click on the original county map layer, or right click and select "Properties", to bring up the Layer Properties dialog.

Click the "Joins" menu from the left. We want to add a new join (you can have many joins; we're just going to do one). Click the green + icon in the lower left to start the process of creating a new join.

We want to join our original county map to the population data we just loaded. You'll see the "Join Layer" field is already pre-filled with your `co-est2015-alldata` layer (because it's the most recent one we've loaded). As we've already investigated, we want to link the two datasets by county name. Select the Join field and Target field appropriately (`CTYNAME` and `NAMELSAD`, respectively).

{% include figure.html src="/assets/images/qgis/add-vector-join.png" caption="The last step in joining data" %}

Click "OK" to close the Add Join dialog, then click "OK" to close the Joins dialog.

If you look at your map now, you might be dismayed to see that it looks exactly the same. **But why should we expect it to be any different?** We've created a link between two fields, but haven't told QGIS what it should do with the new data (the county census data) that we've linked to the original county shapefile layer. *Creating the join between datasets and telling QGIS what to do with the population data are two distinct steps.*

Before we move to the second step, we should double check that our join has worked. Bring up the attribute table for our original layer, scroll to the right, and notice that all of the data from the CSV file has been added to our original attribute table. You can also see how QGIS renames the fields to indicate where the data comes from---the `CENSUS2010POP` field is now labeled as `co-est2015-alldata\_CENSUS2010POP` (the CSV filename prepended to the original field name).

Take special note of the range of data in the population column (it appears directly to the right of the state name column): the values seem to range from around 2000 to 169,000 with most totals in the 20k and 30k range. The important point here is that they are all very reasonable population totals for counties. This is always a good thing to check---that the data you are working with seems to make sense.

Close the attribute table.


## Styling the Map Based on Data
Now on to the second step of useful joins: making our new population data visible. QGIS makes it easy to automatically style data and therefore make visual analysis much easier. To illustrate, let's style our map so that the counties are color coded by population size (so, per convention, lighter shades indicate lower populations; darker shades indicate higher populations). We've just verified that the population totals in our table make sense for this kind of color coding.

Return to the Properties menu of the original map. Click the Style Tab.

Look in the upper left of the dialog. Instead of the default Single Symbol (which means that all counties get filled with the same color), choose Graduated.

Now we need to tell QGIS what data it should use to create our color coding. We're going to use the total population of the county (originally from the CSV file but now also available via the county layer because of our join).

From the Column dropdown menu (the second field), select the column labeled `co-est2015-alldata\_CENSUS2010POP`.

Click "Classify". This will assign a color to a value range based on the data from our `CENSUS2010POP` field).

Click "OK" and you'll see finally a new map and the color coding at work.

{% include figure.html src="/assets/images/qgis/bad-color-coding.png" caption="After all that, everything is light blue! Really unhelpful." %}

You probably expecting something more interesting and/or useful. This is not an uncommon feeling when dealing with data and tools like QGIS, especially when learning them. We selected a classification scheme that would equally divide our range of data (roughly 0 - 10,000,000) into equally sized bins, roughly 0-2 million, 2-4 million, and so on. This means that since virtually all counties in the U.S. have less than 2 million people, most everything is shaded the lightest color.

Go back to the Properties dialog and the Style menu for the county layer. Look for the "Mode" dropdown box. Instead of "Equal Interval" (the same range of values for each color), choose other values and see what happens. "Natural Breaks" looks like it works pretty well. Click "OK".

When you're comfortable with the concepts covered here, move on to the next tutorial in the series, on [overlaying historic maps with QGIS](/tutorials/qgis/overlaying-historic-maps-with-qgis).
