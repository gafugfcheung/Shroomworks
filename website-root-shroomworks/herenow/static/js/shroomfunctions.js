const METABOXWIDTH = 360;
var currentCenter;

function addShroom(id, src, lat, lng) {
  var centerPoint = new google.maps.LatLng(lat, lng);
  //geocodeLatLng(centerPoint);
  shroomCenters[id] = centerPoint;
  var bounds = calculateBounds(centerPoint);

  var newShroom = new shroomOverlay(bounds, src, map);

  shrooms[id] = newShroom;
}

// function addTestShroom(lat, lng) {
//   addShroom(0, '/media/posts/test.jpeg', lat, lng);
// }

function removeShroom(id) {
  shrooms[id].setMap(null);
  console.log("Shroom " + id + " removed");
}

function shroomClicked(id) {
  console.log("shroom " + id + " clicked");
  var src = shrooms[id].image_;
  console.log("src: " + src);
  displayFullScreen(id, src);
}

function IDtoFullScreen(id) {
  displayFullScreen(id, shrooms[id].image_);
}

function displayFullScreen(id, src) {

  var lat = shroomCenters[id].lat();
  var lng = shroomCenters[id].lng();

  currentCenter = new google.maps.LatLng(lat, lng)

  document.getElementById("fullscreen").style.display = "block";
  var img = document.getElementById("fullscreen-photo");
  img.src = src;

  updateFullScreenSize();

  var newCaption = "";
  var likes = "";

  for (var d in dataResults) {
    if (dataResults[d].id == id) {
      newCaption = dataResults[d].caption;
      likes = dataResults[d].likes;
      break;
    }
  }

  document.getElementById("fullscreen-meta-title").innerHTML = newCaption;
  document.getElementById("fullscreen-meta-like-count").innerHTML = likes + " like(s)";

  var map_img = document.getElementById("fullscreen-meta-map");
  var mapHeight = document.getElementById("fullscreen-meta").clientHeight - 71;
  map_img.src = "http://maps.googleapis.com/maps/api/staticmap?size=340x" + mapHeight + "&zoom=5&markers=" + lat + "," + lng + "&key=AIzaSyDsSnbEKYUrxxht13XLL-tKBQnx93KfRqw";
  map_img.style.height = mapHeight - 30;

}

function minimapClicked() {
  map.setCenter(currentCenter);
  hideFullScreen();
}

function updateFullScreenSize() {

  const PROPORTION = 0.8;

  var img = document.getElementById("fullscreen-photo");
  var wrapper = document.getElementById("fullscreen-photo-wrapper");
  var metabox = document.getElementById("fullscreen-meta");

  var imgWidth = img.naturalWidth;
  var imgHeight = img.naturalHeight;
  var windowWidth = window.innerWidth;
  var windowHeight = window.innerHeight;

  if (imgWidth > PROPORTION * windowWidth - METABOXWIDTH) {
    var newWidth = PROPORTION * windowWidth - METABOXWIDTH;
    imgHeight = imgHeight * newWidth / imgWidth;
    imgWidth = newWidth;
  }

  if (imgHeight > PROPORTION * windowHeight) {
    imgWidth = imgWidth * PROPORTION * windowHeight / imgHeight;
    imgHeight = PROPORTION * windowHeight;
  }

  var wrapperWidth = imgWidth + METABOXWIDTH;

  var left = (windowWidth - wrapperWidth) / 2;
  var top = (windowHeight - imgHeight) / 2;
  wrapper.style.left = left + "px";
  wrapper.style.width = wrapperWidth + "px";
  img.style.width = imgWidth + "px";
  wrapper.style.top = top + "px";
  wrapper.style.height = imgHeight + "px";
  img.style.height = imgHeight + "px";
  metabox.style.height = imgHeight + "px";
}

function hideFullScreen() {
  document.getElementById("fullscreen").style.display = "none";
}

function addToNewsFeed(newContent) {
  document.getElementById("newsfeed").innerHTML += newContent;
}

$(document).ready(function() {
  $.ajax({
    url: '/api/get_profile_self',
    type: "GET",
    success : function(data) {
        document.getElementById('navbar-username').innerHTML = data.first_name;
        document.getElementById('navbar-profile-pic').src = data.image;
     }
  });

  $.ajax({
    url: '/api/posts_preview',
    type: "GET",
    success : function(data) {
      for(var d in data.results) {
        dataResults[d] = data.results[d];
        dataResults[d].likes = Math.floor(Math.random() * Math.random() * 30) + 1;
        srcToID[data.results[d].image] = data.results[d].id;
        createFeedItem(data.results[d].image, data.results[d].location.description, data.results[d].caption, data.results[d].time_elapsed, dataResults[d].likes);
      }
    }
  });
})
