function addShroom(id, lat, lng, radiusInKm) {
  var centerPoint = new google.maps.LatLng(lat, lng);

  var pointA = centerPoint.destinationPoint(225, radiusInKm);
  var pointB = centerPoint.destinationPoint(45, radiusInKm);
  var bounds = new google.maps.LatLngBounds(pointA, pointB);

  var srcImage = 'images/lsdlarge.jpg';

  var newShroom = new shroomOverlay(bounds, srcImage, map);

  shroomID = id;
  shrooms[id] = newShroom;
  console.log("Shroom " + id + " created");

  map.setCenter(centerPoint);
}

function removeShroom(id) {
  shrooms[id].setMap(null);
  console.log("Shroom " + id + " removed");
}

function shroomClicked(id) {
  var src = 'images/lsdlarge.jpg';
  displayFullScreen(id, src);
}

function displayFullScreen(id, src) {
  document.getElementById("fullscreen").style.display = "block";
  document.getElementById("fullscreen-photo").src = src;
}

function hideFullScreen() {
  document.getElementById("fullscreen").style.display = "none";
}
