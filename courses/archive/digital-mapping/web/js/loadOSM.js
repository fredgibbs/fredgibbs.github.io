/**
 * @fileoverview Sample showing capturing a KML file click
 *   and displaying the contents in a side panel instead of
 *   an InfoWindow
 */

/**
 * Initializes the map and calls the function that creates polylines.
 */
function initialize() {

// create a map in the "map" div, set the view to a given place and zoom
var map = L.map('map').setView([35.1107,-106.6100], 6);

// add an OpenStreetMap tile layer
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);


// the line below loads the json object (we called it geojsonFeture) 
// that we defined in nmstuff.geojson file.
L.geoJson(geojsonFeature).addTo(map);


// Another way of loading files is to use the omnivore plug-in for leaflet.

// In this case, we don't need to put our json object into a javascript variable,
// we just specifiy the file we want to load.

// Remember to adjust omnibore.kml or omnivore.geojson or omnivore.csv 
// depending on what you're trying to load 

omnivore.kml('stuff.kml').addTo(map);

}