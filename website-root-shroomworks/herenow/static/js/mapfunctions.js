var shrooms = {};
var shroomCenters = {};
var map;
var dataResults = {};
var srcToID = {};
const DEFAULT_OPACITY = 1;
const ICON_SIZE = 0.06; // 0.0 - 1.0
const MIN_ZOOM = 5;

shroomOverlay.prototype = new google.maps.OverlayView();

function calculateBounds(point) {
  var zoomLevel = map.getZoom();
  var change = (point.lat() / 75) + 0.375;
  var radius = 100000 * ICON_SIZE / change;
  console.log("Lat: " + point.lat() + ", change: " + change + ", radius: " + radius);
  for (var i = zoomLevel; i > 0; i--) {
    radius /= 2;
  }
  var pointA = point.destinationPoint(225, radius);
  var pointB = point.destinationPoint(45, radius);
  return new google.maps.LatLngBounds(pointA, pointB);
}

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 8,
    minZoom: 2,
    center: {lat: 51.5, lng: 0},
  });

  google.maps.event.addListenerOnce(map, 'idle', function(){
    for(var d in dataResults) {
      addShroom(dataResults[d].id, dataResults[d].image, dataResults[d].location.lat, dataResults[d].location.lon);
    }
  });

  map.addListener('zoom_changed', function() {
    if (map.getZoom() < MIN_ZOOM) {
      console.log("zoom too low");
      map.setZoom(MIN_ZOOM);
    }
    for (var i in shrooms) {
      shrooms[i].bounds_ = calculateBounds(shroomCenters[i]);
    }
  });


}

/** @constructor */
function shroomOverlay(bounds, image, map) {

  this.bounds_ = bounds;
  this.image_ = image;
  this.map_ = map;

  this.div_ = null;

  this.setMap(map);

}

shroomOverlay.prototype.onAdd = function() {


  var div = document.createElement('div');
  div.style.borderStyle = 'none';
  div.style.borderWidth = '0px';
  div.style.position = 'absolute';

  // Create the img element and attach it to the div.
  var img = document.createElement('img');
  img.src = this.image_;
  img.style.width = '100%';
  img.style.height = '100%';
  img.style.position = 'absolute';
  img.style.borderRadius = '100%';
  img.style.border = '3px solid #315FAC';
  img.style.opacity = DEFAULT_OPACITY;
  img.style.objectFit = "cover";
  div.appendChild(img);

  this.div_ = div;


  // Add the element to the "overlayLayer" pane.
  var panes = this.getPanes();
  panes.overlayMouseTarget.appendChild(div);

  var me = this;

  google.maps.event.addDomListener(img, 'click', function() {
    //google.maps.event.trigger(me, 'click');
    var id = srcToID[img.src];
    var src = img.src;
    displayFullScreen(id, src);
  });

  google.maps.event.addDomListener(img, 'mouseover', function() {
    img.style.border = '3px solid #1F2C5D';
  });

  google.maps.event.addDomListener(img, 'mouseout', function() {
  img.style.border = '3px solid #315FAC';
  });

};

shroomOverlay.prototype.draw = function() {

  var overlayProjection = this.getProjection();

  var sw = overlayProjection.fromLatLngToDivPixel(this.bounds_.getSouthWest());
  var ne = overlayProjection.fromLatLngToDivPixel(this.bounds_.getNorthEast());

  // Resize the image's div to fit the indicated dimensions.
  var div = this.div_;
  div.style.left = sw.x + 'px';
  div.style.top = ne.y + 'px';
  div.style.width = (ne.x - sw.x) + 'px';
  div.style.height = (sw.y - ne.y) + 'px';
};

shroomOverlay.prototype.onRemove = function() {
  this.div_.parentNode.removeChild(this.div_);
  this.div_ = null;
};

google.maps.event.addDomListener(window, 'load', initMap);

// necessary math

Number.prototype.toRad = function() {
   return this * Math.PI / 180;
}

Number.prototype.toDeg = function() {
   return this * 180 / Math.PI;
}

google.maps.LatLng.prototype.destinationPoint = function(brng, dist) {
   dist = dist / 6371;
   brng = brng.toRad();

   var lat1 = this.lat().toRad(), lon1 = this.lng().toRad();

   var lat2 = Math.asin(Math.sin(lat1) * Math.cos(dist) +
                        Math.cos(lat1) * Math.sin(dist) * Math.cos(brng));

   var lon2 = lon1 + Math.atan2(Math.sin(brng) * Math.sin(dist) *
                                Math.cos(lat1),
                                Math.cos(dist) - Math.sin(lat1) *
                                Math.sin(lat2));

   if (isNaN(lat2) || isNaN(lon2)) return null;

   return new google.maps.LatLng(lat2.toDeg(), lon2.toDeg());
}
