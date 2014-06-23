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
var map = L.map('map').setView([35.1107,-106.6100], 13);

// add an OpenStreetMap tile layer
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

L.geoJson(geojsonFeature).addTo(map);

omnivore.kml('stuff.kml').addTo(map);

}