---
layout: post
title: Using Historic Maps with QGIS
created: 2015-10-27
updated: 2017-02-12
---

This tutorial is the third of three tutorials on getting started with QGIS. The [first part](/tutorials/qgis/making-a-map-with-qgis.html) of our tutorial covered some basics of QGIS. The [second part](/tutorials/qgis/linking-and-styling-data-with-qgis.html) of our tutorial showed some ways of adding data to a map.


## Using Data with Historic Maps
It can be very helpful to see historic data on modern maps, but it's nice to see the historic context as well.

First you'll need a historic map. You can use, for example, the David Rumsey map collection. We can download a map (say, of railway lines) from the 1860s. We might use something like [this one](http://www.davidrumsey.com/luna/servlet/detail/RUMSEY~8~1~263514~5524264:Transcontinental-routes-of-Pacific-?sort=Pub_List_No_InitialSort&qvq=w4s:/where/United+States;sort:Pub_List_No_InitialSort;lc:RUMSEY~8~1&mi=11&trs=3774#).

{% include figure.html class="full" src="/assets/images/qgis/rumsey.png" caption="Historic maps + GIS = better historical insight" %}

To download your own version of the map, click the "Export" button near the upper right corner, and choose the "extra large" size (as always, save the file with your others for these lessons). This will be good enough for tutorial purposes (though normally you'll want to work with the highest resolution available).


## Map Projections

Here we must pause to consider map projections, though we're only going to scratch the non-technical surface of an incredibly complex topic. When just looking at a single map, you might not think much about the particular projection---that is, how a curved surface of the Earth gets represented on a flat piece of paper or your screen. But when trying to line up different maps on top of each other, the differences in their projections need to be taken into account. For now it's enough to say that the projection of a historic map (whatever it may be) is unlikely to be the same as a modern map. So we'll need to digitally warp the old map (kind of like re-projecting it) so that it better lines up with the modern map.

Here's a conceptual description of what we want to do. Pretend you have a reasonably accurate (nothing cartoonish or highly stylized) historic map of the U.S. printed on transparent silly putty sitting atop a modern paper map of the U.S. They won't line up exactly, but they will be vaguely close.

Now imagine stretching your putty map in various directions (push and pulling it at various points, and not always symmetrically) to align it with the modern map. To keep the silly putty stretched out, stick pins through the silly putty at obvious geographic features (coastlines) or political boundaries (state borders) and through the same features on the modern map. Thus the putty will be stretched in various directions (often different amounts in different places on the map/image) but will ultimately come to match the modern one. The two maps will line up very closely in places near to our pins and perhaps less so everywhere else where we haven't directly lined it up.

In a very crude way, this process "re-projects" the historic map from one coordinate system to another one. It's more technically accurate to say that we are "geo-rectifying" the map/image by indicating where a spot on historic map aligns with our modern county lines.


## Loading Images
Geo-rectifying a historic map complicates the process of loading an image into QGIS, so let's start with the simple example of just loading an image.


### Load a modern raster image
The map we've made so far is totally flat; let's add a bit of terrain. We can do this by adding a raster image of topographic features (a visual representation of elevation data). Get an image from [Natural Earth](http://www.naturalearthdata.com/downloads/50m-raster-data/50m-shaded-relief/) by clicking the "Download small size" button.

Once downloaded, you can add this image to the map by clicking the "Add Raster Image" icon (one below the Add Vector Layer), navigate to the directory that you downloaded and unzipped (just like our shapefile directories), and select `SR_50M.tif`. Right click on the layer and "Zoom to layer" to center our image.

{% include figure.html src="/assets/images/qgis/topo0.png" caption="Adding a raster image of elevation data" %}

You can see that this image has obscured our county map, so let's rearrange our layers. QGIS layers the data on the canvas as they appear in the Layers pane from bottom to top (so what's on top obscures what's beneath it). Drag the county map layer above the image layer we just added.

{% include figure.html src="/assets/images/qgis/topo1.png" caption="Use the image as a base map instead" %}

Let's zoom in a bit to see the continental U.S., which reveals a bit more detail.

{% include figure.html src="/assets/images/qgis/topo2.png" caption="Combining images and data" %}

Let's blend the layers a bit rather than just overlay them. In the Properties menu for the county boundaries layer, set Blending Mode to "Darken", and the Layer Transparency to 20% (feel free to play around with these setting to see what effects you can create). This will enable us to see more of a blend of the county data atop the topographic data.

{% include figure.html src="/assets/images/qgis/topo3.png" caption="You're probably appreciating well designed maps a bit more now" %}

For now, "Zoom to Layer" of the county boundary layer.

### Load a historic raster image
{% include figure.html class="icon right" src="/assets/images/qgis/add-raster-icon.png" %}
Now, let's load our historic map the same way. (Click the "Add Raster Layer" icon and point to the Rumsey JPG image you downloaded). The "Coordinate Reference Selector" dialog box will open. Here QGIS is trying to figure out how to match up our raster image to the vector map. Just press "OK" and we'll hope for the best (you know you want to!).

{% include figure.html src="/assets/images/qgis/historic1.png" caption="Well, that didn't work." %}

**What's that block in the lower right corner of the canvas?** Yep, that's the map image we just added as a layer. Zoom out a few times to see the big picture. Shockingly, QGIS did not magically do what we wanted and line up the historic map perfectly on the modern outline of the U.S. So much for artificial intelligence.

{% include figure.html src="/assets/images/qgis/add-image-1.png" caption="Notice the world in the upper left. Looks like we have a CRS problem."%}

In reality, since the digital image file of our historic map did not include any Coordinate Reference information (most don't, only in cases where someone has done the work we're about to do), there was no way it could align with our existing layers.

_So how did we load the image of elevation data so easily?_ The modern topo map we downloaded was generated according to a modern projection and a file in the downloaded directly specified what it was. A scanned map such as a historic map of railway lines often will not have projection information associated with it. We'll rectify this shortcoming in the following section. For now, right-click on the historic map image and remove it so it's not in our way.


## Using QGIS to Overlay your Historic Image
Our first step is to "georeference" our historic map. As already mentioned, to georeference a map means to associate points on the (historic) map image with points on our vector map (of county boundaries). QGIS has a built-in georeferencer that makes this easy. The idea is to load an image of a map into QGIS, mark at least three points on the raster image (our historic map) and where they correspond to the vector image (our map of counties).

Under the Raster menu, choose Georeferencer.

{% include figure.html src="/assets/images/qgis/georeferencer.png" caption="Line up your raster images of historic maps and modern vector maps with QGIS" %}

{% include figure.html class="icon right" src="/assets/images/qgis/add-raster-icon.png" %}
Once the dialog box appears, click the upper left icon to load a new image, and select the map you've downloaded. The "Coordinate Reference System Selector" dialog will appear again, but we can accept the defaults. Once it appears, we'll begin the georeferencing process (assigning modern geographic coordinates to points on the historic map).

**CAREFUL: To warp a map, we must load it through the georeferencer, not through the "Add Raster Layer" icon from the main QGIS icon stack.**

{% include figure.html class="icon right" src="/assets/images/qgis/add-points-icon.png" %}
Click the "Add Points" icon to begin adding points. Then, click a point on the historic map to which you want to assign coordinates (say, the southern tip of Florida). The dialog box that appears allows you to enter the coordinates manually, but it's often easier to simply click on a corresponding point on our vector image of the counties. Click the "Use map canvas" button, and the georeferencer will automatically minimize to reveal our canvas. Choose the corresponding point on the vector map.

Repeat this process, choosing a handful of points around the perimeter. You need at least 3, but more distributed points provides a much more accurate overlay.

{% include figure.html src="/assets/images/qgis/reference-points-2.png" caption="Just like silly putty."%}

{% include figure.html class="icon right" src="/assets/images/qgis/yellow-gear-icon.png" %}
When you've entered 5-7 points, click the yellow gear icon to adjust the Transformation Settings. For Transformation type, choose "Thin Plate Spline"; for Resampling methods, choose "Cubic Spline". You can read about what these do if you want to remember why you hate math.

Click the folder or dots icon to the right of the "Output Raster" input box and choose a filename and directory to save the warped file. Saving the file makes it easily available for reuse without having to repeat the georeferencing process---super helpful for when you've spent a lot of time aligning many points.

**Make sure the box for "Use 0 for transparency when needed" is checked.**

{% include figure.html class="icon right" src="/assets/images/qgis/green-arrow-icon.png" %}
After you've finished with the transformation settings, click the green arrow icon (right next to the load image icon).

After your map is added to the canvas, you can see we've warped the image to more or less align with our county map!

{% include figure.html src="/assets/images/qgis/warped-map.png" caption="Warping history."%}

If you see an ugly black border, you failed to check the box for "Use 0 for transparency". Bring up the Layer Properties dialog, select the "Transparency" tab on the left, then set (in the upper right) the "Additional No Data" field to be 0 (zero). Click "OK".


## What can we do now?

We've got everything loaded properly, and this is an impressive achievement to have so many different kinds of data on our map in such a short time. Let's futz with the display a bit to make the data more useful.

First, let's rearrange our layers for better visual effects. Within the layers pane, drag the county layer on top of the historic map layer.

{% include figure.html src="/assets/images/qgis/counties-on-historic.png" caption="Layering data."%}

Better already. Now, move the terrain layer above the county. Double click the terrain layer to edit the style properties. Set the Min value to 52, the Max to 255, Blending Mode to "Hard Light", and reduce the contrast to somewhere around -20. Set the Transparency to about 20%.  When done, click "OK". Obviously you can play around with these values according to your own tastes later (there's nothing special about these particular values).

Lastly, move the railway layer to the top, edit its style so that its blending mode is "multiply" and pick a nice bright red color (or whatever you fancy).

{% include figure.html src="/assets/images/qgis/styled-map.png" caption="The end, but only the beginning."%}
