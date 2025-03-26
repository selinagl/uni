// Dieses Java-Script File beinhaltet das Script, welches für die Funktionalitäten 
// und Darstellungen der Webmap verantwortlich ist.  

//----------------------------------------
//--- Part 1: Hinzufügen von Basemaps ----
//----------------------------------------

// L.map instanziiert die Webmap. Die Variable 'map' muss mit der DOM ID des div-elements im HTML-Dokument
// übereinstimmen. Center und zoom legen fest, wie die Karte bei Aufruf angezeigt wird. 

var map = L.map('map', {
	center: [ 47.797480, 13.047642], 
	zoom: 14
});

// Basemaps werden mit L.tileLayer instanziiert. Die Attributation ist wichtig, um zu zeigen, woher die Basemap kommt. 
// Minzoom und maxzoom sind praktisch, um das mindest bzw. höchste Zoomlevel für den User zu regeln. 

// Open Street map
var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
var osmAttrib='Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';
var osm = new L.TileLayer(osmUrl, {
	minZoom: 12,
	maxZoom: 19,	
	attribution: osmAttrib
}).addTo(map);

//Thunderforest - Cycle Map
var thunderfUrl = 'https://tile.thunderforest.com/cycle/{z}/{x}/{y}.png?apikey=1fd9b017f3184a68aa7d186d5765e91d';
var thunderf = new L.tileLayer(thunderfUrl, {
	minZoom: 12,
	maxZoom: 19
}).addTo(map);

// Basemap.at - Orthofoto
var basemapDOPURL = 'https://maps.wien.gv.at/basemap/bmaporthofoto30cm/normal/google3857/{z}/{y}/{x}.jpgeg'
var basemapDOP = new L.TileLayer(basemapDOPURL, {	
	minZoom: 12,
	maxZoom: 19,
	attribution:'<a href="http://www.basemap.at">basemap.at</a>'
}).addTo(map);

//----------------------------------------------
//--- Part 2: Hinzufügen der Schloss-Marker ----
//----------------------------------------------

//Punkte aus json-Datei mit L.json auslesen. Anschließendw werden die Marker mit dem Schoss-Icon erstellt und sie erhalten die Funktion onEachBib.

var sub = L.geoJson (schloesser, {
		pointToLayer: function (feature,latlng)	{			
				return L.marker(latlng, {icon: schlossIcon});			
	},
	onEachFeature: onEachBib
}).addTo(map);

//Das Schloss-Icon wird aus dem Verzeichnis geladen. IconSize verändert die Größe des Icons, damit es für den Kartenausschnitt passend ist.
var schlossIcon = L.icon({
iconUrl:  './css/Images/schloss.png',
iconSize: [30, 38]});

//Die Funktion onEachBib wird erstellt. Sie erzeugt ein Popup mit Attributen aus der json-Datei. Die Popups erhalten die Funktion zoomToMarker
function onEachBib (feature, layer) {
	layer.bindPopup(
	'<strong>' + feature.properties.NAME + '</strong>' + ':' + '<br>' +
	feature.properties.TEXT);
	layer.on({
		click: zoomToMarker})
};

//Die Funktion zoomToMarker wird erstellt. Ein Klick auf die zuvor erstellten Popups zoomt jetzt heran.
function zoomToMarker(e) {
	map.setView(e.latlng, 19)};
	
//-----------------------------------------------
//--- Part 3: Weitere Kartenfunktionen einfügen ----
//-----------------------------------------------

//Gruppen für Basemaps und Schloesser werden für die Layer Control erstellt. So kann zwischen den Basemaps gewechselt und der Schloss-Layer ein- und ausgeschaltet werden.	
var hintergrund = {
		'OpenStreetMap': osm,
		'Thundforest-CylceMap': thunderf,
		'Basemap-DOP': basemapDOP
		};
var overlaySchloesser = {
	'Schlösser und Burgen': sub;

//Layer Control wird initalisiert. 
var layerControl = L.control.layers(hintergrund, overlaySchloesser).addTo(map);

//Maßstabsleiste wird ersellt. Es werden nur metrische Einheiten angezeigt. Die Breite der Anzeige und die Position wird festgelegt.
var scale = L.control.scale({
	metric: true,
	imperial: false,
	maxWidth: 200,
	position: 'bottomleft',
}).addTo(map)

//Ein Event für Klick auf die Karte wird erstellt: Ein neuer Marker wird mithilfe der Funktion newMarker hinzugefügt. 
map.on('click', newMarker);

//Funktion newMarker
function newMarker(e) {
	var maker = new L.marker(e.latlng)
	.addTo(map)
	};