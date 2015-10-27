---
layout: post
title: Making a Map with QGIS
date: 2015-10-26 00:00:00
---

## Preparatory Reading

Even if you have some experience with GIS in general and QGIS in particular, it's always helpful to review the fundamentals. Read through "Introducing GIS", "Vector Data", and "Raster Data" from this [gentle introduction to GIS](http://docs.qgis.org/2.8/en/docs/gentle_gis_introduction/index.html).

If (= when), during your QGIS adventures, you get stuck or have questions, consult the [QGIS Training Manual](http://docs.qgis.org/2.8/en/docs/training_manual/), [the QGIS wiki](http://hub.qgis.org/projects/quantum-gis/wiki/How_do_I_do_that_in_QGIS), and an [array of tutorials](http://qgistutorials.com). You may not at first find exactly what you're looking for, but it's worth browsing through these sites to help better understand the software and prevent conceptual misunderstandings. Be aware that many tutorials are for older versions of QGIS, so the screen shots and menu labels may not match exactly what you see in your version--but often the concepts are the same.

Also, remember that Google searches are your friend. You're not the first one to haul yourself up the learning curve of QGIS; many people have likely posted similar questions on forums where someone eventually provided a useful explanation. Others have written tutorials or blog posts that can shed more light on your issue. You won't always find exactly what you need, but this kind of searching helps you better understand the tool and build your vocabulary for how to search and solve problems on your own.


## Installing QGIS

Installing QGIS is straightforward, but it can seem a bit unfamiliar, so don't worry if you feel confused. This tutorial is based on 2.10 for Mac, though some screenshots are from older versions if they are not significantly different from the current release. Within these tutorials, other than installation instructions, there should be no noticable difference between Mac and PC versions.

The most up to date versions of the necessary components can be found, organized by operating system, at the [QGIS download page](http://hub.qgis.org/projects/quantum-gis/wiki/Download#11-Standalone-Installer-recommended-for-new-users). 

Windows users will need to choose between the 32-bit or 64-bit versions based on your particular operating system. If you don't already know which one you have, read [how to tell](http://windows.microsoft.com/en-us/windows/32-bit-and-64-bit-windows#1TC=windows-7). 

If you have a Mac, you'll need to download and install 3 items, QGIS and two other required small software packages. Installing separate components like this can seem a bit weird if you're not used to installing open source software, but it's actually a very common process.

First, you'll need to make sure you can add new software to your Mac. Go to your System Preferences (under the Apple menu), and bring up the Security & Privacy Pane. Click the Lock in the bottom left to make changes. For the section titled "Allow apps downloaded from:", Check the "Anywhere" radio button.

Here are the links of the downloads you need (just download and install the in order listed):

- [first](http://www.kyngchaos.com/files/software/frameworks/GDAL_Complete-1.11.dmg) Once you see the window with the files you've downloaded, double-click on the "GDAL Complete.pkg" icon, click through the dialog boxes, then do the same for the NumPy.pkg.
- [second](http://www.kyngchaos.com/files/software/python/matplotlib-1.4.3-1.dmg) Similarly, double-click on the matpoltlib.pkg icon to install the last of the components requires by QGIS.
- [third](http://www.kyngchaos.com/files/software/qgis/QGIS-2.10.1-1.dmg) Finally you're ready to install QGIS itself; do this the same way as for the other packages.  


## Be Explicit

When you first start QGIS, you'll get a whole lot of white, a bunch of cryptic icons, and pangs of regret and/or fear. On the left pane of the application window, you can click the 'X' to close the "Browser" panel, since we won't be using it. Be sure to keep the "Layers" panel visible.

{% include figure.html src="/images/qgis/qgis-blank.png" caption="The exhileration and terror of a blank map" %}

Most people expect to see a map, and are frustrated when they don't. QGIS is a powerful but general mapping tool; broad tools of this nature tend not to much without explicit instructions from you. Using these tools successfully, especially mappings tools, often means adjusting your expectations of what they should do automatically. 

We must not assume that QGIS should work like Google Maps and automatically display maps for you. If you're constantly comparing what the tool does to what you hope it will do, you're always going to feel like the tool is working against you. If you are disappointed there is no map, you should ask yourself why you expected to see a map when we haven't given the tool any map data to display.


## Data, not maps

The first thing to recognize when it comes to GIS software like QGIS is that **it doesn't display maps, it displays data** (most of which will have strong geographic ties). _You are in charge of composing the map you want_ from the relevant geographic and social data you're interested in. This might sound annoying, but it's actually incredibly powerful.

The second thing to recognize is that **GIS tools are not only for projects centered on geographic analysis**. Whether you're thinking about people, commodities, ideas, political power, or whatever, these all have a grounding in space with various features (transportation networks like roads or railroads, political boundaries, access to natural resources, wealth disparity, demographic data, etc). While these features might not be a direct concern of yours, they can add extremely useful context to your research. Before easily accessible data and GIS software, the work to create maps for secondary research concerns far exceeded the benefit. The barrier now is far, far lower.


## Acquire Data

Let's start making a map! Just for kicks, let's find a map of all the counties in the US. The first step in making any map is to find the data you need. One of the most common formats for GIS data is called a shapefile. If interested, you can [read more about the standard](http://www.digitalpreservation.gov/formats/fdd/fdd000280.shtml).

There are many places for finding GIS data online, but one important repository to keep on your radar is census.gov. You should spend a few minutes exploring the kinds of data you can find there. You can find county data [on this census.gov page](https://www.census.gov/geo/maps-data/data/tiger-line.html). Towards the middle of the page, click 'Download', then 'Web Interface', then select the layer type (the dropdown menu) 'Counties (and equivalent)'. Click the 'Submit' button, then click 'Download national file'. The file "tl\_2014\_us\_county.zip" should save into your specified downloads directory (it's about 70MB).

After you double click on the file to unzip it, you'll notice that you actually get a directory full of files. This is quite common way of packaging shapefiles (since they come with a number of auxillary files). Since we're going to start acquiring and generating a set of files and directories, now is a good time to create a new directory somewhere on your hard drive to keep everything organized, ideally a high-level directory that's easy to get to (like your Documents folder or equivalent; you can always move it later). You should put your county map directory in there.


## Add Some Data to the Map


{% include figure.html class="icon" src="/images/qgis/add-vector-icon.png" %}

Click 'Add Vector Layer' icon, the topmost of the vertically stacked icons on the left. Choose 'Directory' (since we want to point QGIS to the directory we downloaded), and click 'Browse' to choose the directory where you ultimately saved and unzipped your directory from the census.gov page.

After you click 'Open', you should see the outlines of all US counties. Cool! You've just created your first layer in QGIS with a shapefile you downloaded. The color of your map is likely different than the screenshot here, since QGIS chooses an arbitrary color. We'll adjust the color later.

{% include figure.html src="/images/qgis/qgis-counties.png" caption="Not pretty, but pretty cool" %}

If you were expecting a beautifully colored and stylized map centered on the lower 48 (as most county maps you see online are), you may be a bit underwhelmed at this point. As mentioned earlier, this is not a limitation of QGIS, but again a problem of expectations. All we asked it it do was display outlines of US counties, and that's exactly what it did. 

Note the high zoom level so that all of the Hawaiian islands and Guam can fit in the display area. You can click the Zoom icon at the top and draw a rectangle onto an area you'd like to zoom in to (perhaps the continental US) to see the more familiar-looking boundaries at a smaller scale. Notice that because this is a vector image (and not a raster image like a JPG or PNG or TIF), the image doesn't get fuzzier as you zoom in (QGIS simply redraws the image at the appropriate scale).

If you want to get back to your original zoom level, or you accidently zoom super far in or out (it will happen eventually!), right-click on the layer name on the left in the Layers pane and select the topmost option, "Zoom to layer".


## Digging a Bit Deeper

To see more of what's behind the data we just loaded, right-click on the layer name again and select 'Open Attribute Table'. You'll see data that comes as part of the directory you downloaded. 

{% include figure.html src="/images/qgis/qgis-attributes.png" caption="There is more to your maps than lines on your canvas" %}

There are a bunch of codes and numbers that won't mean much to you. However, you'll notice that it also includes more intutive data, like county names. You can see the two variants visible the NAME and NAMELSAD fields. These fields also allows us to join this dataset with other datasets that also contain county names, which we'll do in part 2.


## Add Some Data to the Map

You can overlay more data by repeating the process. Let's try a different kind of data. Instead of polygons (counties), let's load and display some lines. Get your data for the railways at [Natural Earth Data](http://www.naturalearthdata.com/downloads/10m-cultural-vectors/). Scroll down until you get to Railroads, then download the North American Supplement (this is not all the railways, but it's a smaller file for tutorial purposes). If you get lost on the website, the file is [here](http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/ne_10m_roads_north_america.zip).

{% include figure.html src="/images/qgis/ne-railroads.png" caption="Lots of great data available" %}

Go through the same process as before (click the "Add Vector" icon and choose your directory). Zoom to the layer extent of the railroad layer and you'll see the railroad lines atop of our counties.

{% include figure.html src="/images/qgis/qgis-railroads.png" caption="It's up to you to find and layer data useful for your research" %}

We've loaded two kinds of data, one of polygons for our county boundaries, and one of lines for the railroads. This process of loading shapefiles is the same for displaying countries, railroad lines, bike trails, census tracts, or any other kind of physical or political boundary. There's a LOT of data online that you can freely use to build your maps. **You now have the power!**

When you're comfortable with the concepts covered here, move on to the next tutorial in the series, on [linking and styling data](/tutorials/gis/linking-and-styling-data-with-qgis.html).
