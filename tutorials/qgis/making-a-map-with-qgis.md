---
layout: post
title: Making a Map with QGIS
created: 2015-10-27
updated: 2017-02-12
---

## Troubleshooting

If (= when), during your QGIS adventures, you get stuck or have questions, consult the [QGIS Training Manual](http://www.qgis.org/en/docs/index.html), [the QGIS wiki](http://hub.qgis.org/projects/quantum-gis/wiki/How_do_I_do_that_in_QGIS), and an [array of tutorials](http://qgistutorials.com). You may not at first find exactly what you're looking for, but it's worth browsing through these sites to help sort out conceptual misunderstandings. Be aware that many tutorials are for older versions of QGIS, so the screen shots and menu labels may not match exactly what you see in your version---but often the concepts are the same.

Also, remember that Google searches are your friend. You're not the first one to haul yourself up the learning curve of QGIS; many people have likely posted similar questions on forums where someone eventually provided a useful explanation. Others have written tutorials or blog posts that can shed more light on your issue. You won't always find exactly what you need, but this kind of searching helps you better understand the tool and build your vocabulary for how to search and solve problems on your own.


## Installing QGIS

Installing QGIS is straightforward, but it can seem a bit unfamiliar, so don't worry if you feel confused. This tutorial is based on 2.18 for Mac, though some screenshots are from older versions if they are not significantly different from the current release. Other than installation instructions, there should be no noticeable difference between Mac and PC versions.

The most up to date versions of the necessary components can be found, organized by operating system, at the [QGIS download page](http://qgis.org/en/site/forusers/download.html). **Read the instructions below before downloading.**

**Windows users**: You will need to choose between the 32-bit or 64-bit versions based on your particular operating system. If you don't already know which one you have, you can [figure it out](http://windows.microsoft.com/en-us/windows/32-bit-and-64-bit-windows#1TC=windows-7).

**Mac users**: Before you run the installer, you'll need to make sure you can add new software to your Mac. Go to your System Preferences (under the Apple menu), and click on "Security & Privacy". Click the lock icon in the bottom left to make changes. For the section titled "Allow apps downloaded from:", Check the "Anywhere" radio button. Now you are ready to install. When you open the disk image that you downloaded, you'll see 4 .pkg files that you must install in the order they are numbered. Installing separate components like this can seem a bit weird if you're not used to installing open source software, but it's actually a very common process.

If you see a notice that there is a newer version available, ignore it. Click the "New File" icon in the upper left corner.


## Be Explicit
When you first start QGIS you'll get a whole lot of white, a bunch of cryptic icons, and pangs of regret and/or fear. On the left pane of the application window, if you see a "Browser" panel, you can click the 'X' to close it, since we won't be using it. Be sure to keep the "Layers" panel visible.

{% include figure.html class="full" src="/assets/images/qgis/qgis-blank.png" caption="The exhilaration and terror of a blank map" %}

Most people expect to see a map, and are frustrated when they don't. QGIS is a powerful but general mapping tool; broad tools of this nature tend not to do much without explicit instructions from you. Using these tools successfully, especially mapping tools, often means adjusting your expectations of what they should do automatically.

**We must not assume that QGIS should work like Google Maps** and automatically display maps for you. If you're constantly comparing what the tool does to what you hope or want it will do, you're always going to feel like the tool is working against you. If you are disappointed there is no map, you should ask yourself why you expected to see a map when we haven't given the tool any map data to display.


## Data, not maps
The first thing to recognize is that **GIS software doesn't display maps, it displays data** (most of which will have strong geographic ties). _You must assemble and create your own map_ from the relevant geographic and social data you're interested in. This might sound annoying, but it's actually incredibly powerful.

The second thing to recognize is that **GIS tools are not only for projects centered on geographic analysis**. Whether you're thinking about people, commodities, ideas, political power, or whatever, almost everything has some grounding in space, which has various features (transportation networks like roads or railroads, political boundaries, access to natural resources, wealth disparity, demographic data, etc). While these features might not be a direct concern of yours, they can add extremely useful context to your research. Before easily accessible data and GIS software, the work to create such maps far exceeded the (often unknown) benefit. The barrier now is far, far lower.


## Acquire Data
Let's start making a map! Just for kicks, let's find a map of all the counties in the US. The first step in making any map is to find the data you need. One of the most common formats for GIS data is called a shapefile. The technical details are not important for us, but you can [read more about the standard](http://www.digitalpreservation.gov/formats/fdd/fdd000280.shtml).

There are many places for finding GIS data online, but one important repository to keep on your radar is census.gov. You should spend a few minutes exploring the kinds of data you can find there. You can find county data [on this census.gov page](https://www.census.gov/geo/maps-data/data/tiger-line.html). Towards the middle of the page, click 'Download', then 'Web Interface', then use the 'Select layer type' dropdown menu to choose 'Counties (and equivalent)'. Click the 'Submit' button, then click 'Download national file'. The file `tl\_2016\_us\_county.zip` should save into your specified downloads directory (it's about 70MB). You may have to double click on the downloaded file to unzip it.

You'll notice that you actually get a folder full of files rather than a single file. This is the standard way of packaging shapefiles (which are really a set of files that require each other). Since we're going to start acquiring and generating a set of files and folders/directories, now is a good time to create a new folder somewhere on your hard drive to keep everything organized, ideally a high-level location that's easy to get to (like your Documents folder or Desktop; you can always move it later). You should put your county map directory in there.


## Add Some Data to the Map

{% include figure.html class="icon right" src="/assets/images/qgis/add-vector-icon.png" %}

Click 'Add Vector Layer' icon, the topmost of the vertically stacked icons on the left. Choose 'Directory' (since we want to point QGIS to the folder we downloaded), and click 'Browse' to choose the folder where you ultimately saved (and possibly unzipped) your download from the census.gov page.

After you click 'Open', you should see the outlines of all US counties. Cool! You've just created your first layer in QGIS with a shapefile you downloaded. The color of your map is likely different than the screenshot here, since QGIS chooses an arbitrary color. We'll adjust the color later. Notice that `tl\_2016\_us\_county` appears in the layer pane at the left.

{% include figure.html src="/assets/images/qgis/qgis-counties.png" caption="Not pretty, but pretty cool" %}

If you were expecting a beautifully colored and stylized map centered on the lower 48 (as most county maps you see online are), you may be a bit underwhelmed at this point. As mentioned earlier, this is not a limitation of QGIS, but a problem of expectations. All we asked it it do was display outlines of US counties, and that's exactly what it did.

Note the high zoom level so that all of the Hawaiian islands and Guam can fit in the display area. You can click the Zoom icon at the top and draw a rectangle onto an area you'd like to zoom in to (perhaps the continental US) to see the more familiar-looking boundaries at a smaller scale. Notice that because this is a vector image (and not a raster image like a JPG or PNG or TIF), the image doesn't get fuzzier as you zoom in (QGIS simply redraws the image at the appropriate scale).

If you want to get back to your original zoom level, or you accidentally zoom super far in or out (it will happen eventually!), right-click on the layer name on the left in the Layers pane and select the topmost option, "Zoom to layer".


## Digging a Bit Deeper

To see more of what's behind the data we just loaded, right-click on the layer name again and select 'Open Attribute Table'. You'll see data that comes as part of the directory you downloaded.

{% include figure.html src="/assets/images/qgis/qgis-attributes.png" caption="There is more to your maps than lines on your canvas" %}

There are a bunch of codes and numbers that won't mean much to you. However, you'll notice that it also includes more intuitive data, like county names. You can see the two variants visible the `NAME` and `NAMELSAD` fields. These fields also allows us to join this dataset with other datasets that also contain county names, which we'll do in Part 2.


## Add Some Data to the Map
You can overlay more data by repeating the process. Let's try a different kind of data. Instead of polygons (counties), let's load and display some lines. Get your data for the railways at [Natural Earth Data](http://www.naturalearthdata.com/downloads/10m-cultural-vectors/). Scroll down until you get to Railroads, then download the North American Supplement (this is not all the railways, but it's a smaller file for tutorial purposes).

{% include figure.html class="raw" src="/assets/images/qgis/ne-railroads.png" caption="Lots of great data available" %}

Go through the same process as before (click the "Add Vector" icon and choose your directory). Zoom to the layer extent of the railroad layer and you'll see the railroad lines atop of our counties.

{% include figure.html src="/assets/images/qgis/qgis-railroads.png" caption="It's up to you to find and layer data useful for your research" %}

We've loaded two kinds of data, one of polygons for our county boundaries, and one of lines for the railroads. This process of loading shapefiles is the same for displaying countries, railroad lines, bike trails, census tracts, or any other kind of physical or political boundary. There's a LOT of data online that you can freely use to build your maps. **You now have the power!**

When you're comfortable with the concepts covered here, move on to the next tutorial in the series, on [linking and styling data](/tutorials/qgis/linking-and-styling-data-with-qgis.html).
