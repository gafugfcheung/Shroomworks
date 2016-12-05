var shrooms = {};
var map;
var shroomID;
const DEFAULT_OPACITY = 0.8;
const ICON_SIZE = 0.06; // 0.0 - 1.0

shroomOverlay.prototype = new google.maps.OverlayView();

// Initialize the map and the custom overlay.

function calculateBounds(point) {
  var zoomLevel = map.getZoom();
  var radius = 100000 * ICON_SIZE;
  for (var i = zoomLevel; i > 0; i--) {
    radius /= 2;
  }
  var pointA = point.destinationPoint(225, radius);
  var pointB = point.destinationPoint(45, radius);
  return new google.maps.LatLngBounds(pointA, pointB);
}

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 11,
    center: {lat: 51, lng: 0},
  });

  map.addListener('zoom_changed', function() {
    for (var i in shrooms) {
      shrooms[i].bounds_ = calculateBounds(shrooms[i].bounds_.getCenter());
    }
  });
}

/** @constructor */
function shroomOverlay(bounds, image, map) {

  // Initialize all properties.
  this.bounds_ = bounds;
  this.image_ = image;
  this.map_ = map;

  // Define a property to hold the image's div. We'll
  // actually create this div upon receipt of the onAdd()
  // method so we'll leave it null for now.
  this.div_ = null;

  // Explicitly call setMap on this overlay.
  this.setMap(map);

}

shroomOverlay.prototype.onAdd = function() {

  /**
   * onAdd is called when the map's panes are ready and the overlay has been
   * added to the map.
   */

  var div = document.createElement('div');
  div.id = shroomID;
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
  img.style.border = '2px solid blue';
  img.style.opacity = DEFAULT_OPACITY;
  img.style.objectFit = "cover";
  div.appendChild(img);

  this.div_ = div;


  // Add the element to the "overlayLayer" pane.
  var panes = this.getPanes();
  panes.overlayMouseTarget.appendChild(div);

  var me = this;
  google.maps.event.addDomListener(img, 'click', function() {
    shroomClicked(div.id);
  });

  google.maps.event.addDomListener(img, 'mouseover', function() {
    img.style.opacity = 1;
  });

  google.maps.event.addDomListener(img, 'mouseout', function() {
    img.style.opacity = DEFAULT_OPACITY;
  });

};

shroomOverlay.prototype.draw = function() {

  // We use the south-west and north-east
  // coordinates of the overlay to peg it to the correct position and size.
  // To do this, we need to retrieve the projection from the overlay.
  var overlayProjection = this.getProjection();

  // Retrieve the south-west and north-east coordinates of this overlay
  // in LatLngs and convert them to pixel coordinates.
  // We'll use these coordinates to resize the div.
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
  // The onRemove() method will be called automatically from the API if
  // we ever set the overlay's map property to 'null'.
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
