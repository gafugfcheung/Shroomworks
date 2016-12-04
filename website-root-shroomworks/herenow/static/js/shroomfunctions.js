function addShroom(id, lat, lng, radiusInKm) {
  var centerPoint = new google.maps.LatLng(lat, lng);

  var pointA = centerPoint.destinationPoint(225, radiusInKm);
  var pointB = centerPoint.destinationPoint(45, radiusInKm);
  var bounds = new google.maps.LatLngBounds(pointA, pointB);

  var srcImage = 'static/images/lsdlarge.jpg';

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
  var src = 'static/images/lsdlarge.jpg';
  displayFullScreen(id, src);
}

function displayFullScreen(id, src) {
  document.getElementById("fullscreen").style.display = "block";
  document.getElementById("fullscreen-photo").src = src;
}

function hideFullScreen() {
  document.getElementById("fullscreen").style.display = "none";
}

function addToNewsFeed(newContent) {
  document.getElementById("newsfeed").innerHTML += newContent;
}

function shroomHTML(src, location, title, time, likes) {

  var content = "";
  <div class="newsfeed-item">
    <img class="newsfeed-photo" src="{% static 'images/silverback.jpg' %}">
    <div class="newsfeed-item-topbar">
      <div class="newsfeed-item-location newsfeed-item-minor">Location</div>
      <div class="newsfeed-item-title">Title</div>
      <div class="newsfeed-item-time newsfeed-item-minor">Time</div>
    </div>
    <div class="newsfeed-item-bottombar">
      <div class="newsfeed-item-likes">Likes</div>
    </div>
  </div>

}
