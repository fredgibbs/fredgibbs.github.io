---
layout: post
title: Linking and Styling Data with QGIS
date: 2015-10-27 00:00:00
---

The [first part](/tutorials/qgis/making-a-map-with-qgis.html) of our tutorial covered some basics of QGIS.

## Adding Complexity with More Data

The county map is a praise-worthy accomplishment if you've never made a map before. But obviously loading a single data set like county boundaries is not super useful on its own.

You are probably already realizing one of the principal challenges of GIS work. The actual display of the map is pretty easy (QGIS does all the work for you!). The challenge lies in finding (or creating) the data you need, as well as making different data sets work with each other. An introductory tutorial is not the place to dive into the many different techniques, but let's work through a typical and relatively straightforward example. 


## Get and Display Data

We've already got counties in the form of shapefile; let's see if we can add population data to our map. We'll get our data from Census.gov again, at their page for [population estimates](http://www.census.gov/popest/data/index.html). This time, however, we aren't going to use a shapefile because we're not interested in drawing geographic features (like county boundaries); we're interested in just the data. 

{% include figure.html src="/images/qgis/county-census-data.png" caption="Census.gov has great data, but not always intuitive ways to access it" class="raw" %}

We want county-level data, so find "Counties" under the left column "Level of Geography", scan to the right following the "Total Population" line and click on the corresponding "V2013" link on the right under "Most Current Data". Under the "Downdloadable Dataset" heading, click "Population, population change...", and click the "Data" link. (It's good to get familiar with websites with good data, but the link to the file is [here](http://www.census.gov/popest/data/counties/totals/2013/files/CO-EST2013-Alldata.csv).) 

Whether you navigate through the website to get to the Data link or use the cheat link, when you click on it you'll see:

{% include figure.html src="/images/qgis/alldata.png" caption="Please do not hit the panic button" %}

Perhaps not what you were expecting. Unlike the previous lesson when we loaded up data specifically made for GIS software, this data is plain text data. It is in a standard file format, CSV, which stands for Comma Separated Values. You could load this into a spreadsheet. We won't, but it would look like:

{% include figure.html src="/images/qgis/census-spreadsheet.png" caption="CSV data isn't so scary in a more familiar form" %}

Hit your browser's back button, then right click the "Data" link, and choose "Save Link As..." (or equivalent for your browser) and save the file wherever you're storing your files for these lessons. Just keep the default file name, _CO-EST2013-Alldata.csv_. 

{% include figure.html class="icon" src="/images/qgis/add-csv-icon.png" %}
To load this data into QGIS, click the icon on the left with a comma (towards the bottom of the icon stack) to "Add Delimited Text Layer". You'll see a new dialog window appear, so that we can tell QGIS a little about our data file so it can load it properly. 

{% include figure.html src="/images/qgis/create-text-layer.png" caption="Importing: the first step to data mastery" %}

Click "Browse" in the upper right to select the CSV file you just downloaded.

Make sure the box "First record has field names" is checked, since this is true for our CSV file. Notice that the preview pane on the bottom tells us how QGIS is interpreting the data in the file. If your CSV file isn't properly formatted, or you've choosen options from this dialog that do not correspond to the CSV file, the preview will show you something isn't right (usually).

{% include figure.html src="/images/qgis/create-text-layer-2.png" caption="Pay attention to the preview to avoid future headaches" %}

Especially if you're someone who just likes to click "OK" without really paying attention, you'll notice the "OK" button is grayed out. Here's why:

This CSV file contains data related to geography (population by counties), but not actually any geographic data about the counties (that's what our other file did). In other words, it's not specifically for mapping; it's just data. So for "Geometry Definiton" we want to select "No Geometry". Now you can click "OK".

Some people expect their map to change here--as if the computer should read our minds--but we haven't told QGIS what to do with this new data. More specifically, we have not indicated how this data relates to the county boundary map we've already loaded.

Let's just check out the data first. Right click on the _CO-EST2013-Alldata_ layer and "Open Attribute Table". Notice that our CSV file has loaded properly and contains lots of great data, like county name (the CTYNAME field) with lots of data about it, including the 2010 population (labeled as CENSUS2010POP. Take notice of the CTYNAME field. Close the Attribute Table.

Now, open the attribute table for our original map of the counties. You'll notice that it, too, contains a field (=column) listing all the county names, but in this file it's called NAMELSAD. Because our two datasets (the county geographic data and the population data) both have the county names. It doesn't matter that one is labeled as CTYNAME and the other as NAMELSAD because we can see (from just browsing through them) that the data is _exactly_ the same (ie county names with Capitalization and the word "County" in each case. Because of this congruity, we can join these tables together so that we can visualize the population data on our county map. Close the attribute table for now.


## Joining Datasets Together

Double click on the original county map layer, or right click and select "Properties", to bring up the Layer Properties dialog.

Click the "Joins" menu from the left. We want to add a new join (you can have many joins; we're just going to do one). Click the green + icon to start the process of creating a new join.

We want to join our original county map to the population data we just loaded into QGIS. You'll see the "Join Layer" field is already pre-filled with your _CO-EST2013-Alldata_ layer (because it's the most recent one we've loaded). Of course we want to link the two datasets by county name. Select the Join field and Target field appropriately (CTYNAME and NAMELSAD, respectively). 

{% include figure.html src="/images/qgis/add-vector-join.png" caption="The last step in joining data" %}

Click "OK" to close the Add Join dialog, then click "OK" to close the Joins dialog.

If you look at your map now, you might be dismayed to see that it looks exactly the same. *But why should we expect it to be any different?* We've created a link between two fields, but haven't told QGIS what it should do with the new data (= county census data) that we've linked to the original county shapefile layer. Creating the join between datasets and telling QGIS what to do with the population data are two distinct steps. 

Before we move to the second step, we should double check that our join has worked by viewing the attribute table for our original layer, scrolling to the right, and noticing that all of the data from the CSV file has been added to our original attribute table. You can also see how QGIS renames the fields to indicate where the data comes from--the CENSUS2010POP field is now labled as _CO-EST2013-Alldata\_CENESUS2010POP_, which is the CSV filename prepended to the original field name.

Take special note of the range of data in the population column that's visible at first glance: they range from around 2000 to 169,000 with most totals in the 20k and 30k range. The important point here is that they are all very reasonable population totals for counties.

Close the attribute table.


## Styling the map based on data

Now on to the second step of useful joins--making our new population data visible. QGIS makes it easy to automatically style data (what is coming to resemble a map) based on the attributes of the various layers. Let's take it upon ourselves to style our map so that the counties are color coded by population size (so, for instance, lighter shades indicate lower populations; darker shades higher population). We've just verified that the population totals in our table make sense for this kind of color coding. 

Return to the Properties menu of the original map. Click the Style Tab.

Look in the upper left of the dialog. Instead of the default Single Symbol (which means that all counties get filled with the same color), choose Graduated. 

Now we need to tell QGIS what data it should use to create our color coding. We're going to use the total poplation of the county (originally from the CSV file but now also available via the county layer via our join).

From the Column dropdwon menu (the second field), select the column labeled _CO-EST2013-Alldata\_CENSUS2010POP_.

Click "Classify" (just under the big white space). This will assign a color to a value range based on the data from our _CENSUS2010POP_ field).

Click "OK" and you'll see finally a new map and the color coding at work. 

{% include figure.html src="/images/qgis/bad-color-coding.png" caption="After all that, everything is lite blue! Really unhelpful." %}


## Making the styling useful

You probably expecting something more interesting and/or useful. This is not an uncommon feeling when dealing with data and tools like QGIS. But we can easily make improvements, and this section of the tutorial walks through the common process of understanding why data is not displaying the way you want.

We know that we selected the correct population field (double check if you're not sure!), and we know the population totals were reasonable.

However, notice the legend displays under the layer name in the layer pane. We can see that the first lite blue color indicates a range (of population, since that's the field we selected) from 82 - 7450856.80. We know from our earlier preliminary inspection that most population totals were closer 30,000 than 7,000,000. It's a good bet that most counties in the US don't have anywhere near 7 million people. Just to make sure, we can bring up the attribute table again and double click on header the population field to sort it in decreasing order and verify that there is no county population that high. *What's going on?*

Let's consider at the possible sources of data, starting with our original CSV file. Bring up the attribute table for the original CSV layer. Look at the _CENSUS2010POP_ field. Click on the field name twice to sort it in descending order. Notice the first value is 37253956. 37 million people is a lot for one county and seems a bit suspicious. 

Look at the CTYNAME field; you can see that this data set contains data for entire states as well as single counties. This is throwing off our graduated scale because _when QGIS calculates the scale range for color coding, it uses the range of values from the original table_, not just the data that appears in the attribute table for the layer to which we joined the data. This seems inconvenient now, and possibly wrong, but it's the way it should work (ie an elevation map of Iowa shouldn't have lots of white at its highest points). 

Again, we have an issue with expectations. The "problem" is not how QGIS works, but that we assumed it should work a certain way and that our county data contained data only for counties (not an unreasonable assumption). In fact, our CSV file of supposed county data came with extra and supposedly helpful data.

We have two main choices to improve the map: remove the state popluations from the original CSV file (not difficult, but annoying), or create our color coding in a different way.

Go back to the Properties dialog and the Style menu for the county layer. Look for the "Mode" dropdown box on the right. Instead of Equal Interval (the same range of values for each color), choose "Equal Quantity" (the same number of counties for each range/color). Click "OK".

Finally, a more useful map.

When you're comfortable with the concepts covered here, move on to the next tutorial in the series, on [using historic maps with QGIS](/tutorials/qgis/using-historic-maps-with-qgis).