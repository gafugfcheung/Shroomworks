const METABOXWIDTH = 360;

function addShroom(id, src, lat, lng) {
  var centerPoint = new google.maps.LatLng(lat, lng);
  shroomCenters[id] = centerPoint;
  var bounds = calculateBounds(centerPoint);

  var newShroom = new shroomOverlay(bounds, src, map);

  shrooms[id] = newShroom;
}

function addTestShroom(lat, lng) {
  addShroom(0, '/media/posts/test.jpeg', lat, lng);
}

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

  document.getElementById("fullscreen").style.display = "block";

  var img = document.getElementById("fullscreen-photo");
  img.src = src;

  var map_img = document.getElementById("fullscreen-meta-map");

  map_img.src = "http://maps.googleapis.com/maps/api/staticmap?size=330x240&zoom=5&markers=" + shroomCenters[id].lat() + "," + shroomCenters[id].lng() + "&key=AIzaSyDsSnbEKYUrxxht13XLL-tKBQnx93KfRqw";

  updateFullScreenSize();

}

function updateFullScreenSize() {
  var img = document.getElementById("fullscreen-photo");
  var wrapper = document.getElementById("fullscreen-photo-wrapper");
  var metabox = document.getElementById("fullscreen-meta");

  var imgWidth = img.naturalWidth;
  var imgHeight = img.naturalHeight;
  var windowWidth = window.innerWidth;
  var windowHeight = window.innerHeight;

  if (imgWidth > 0.9 * windowWidth - METABOXWIDTH) {
    var newWidth = 0.9 * windowWidth - METABOXWIDTH;
    imgHeight = imgHeight * newWidth / imgWidth;
    imgWidth = newWidth;
  }

  if (imgHeight > 0.9 * windowHeight) {
    imgWidth = imgWidth * 0.9 * windowHeight / imgHeight;
    imgHeight = 0.9 * windowHeight;
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

function shroomHTML(src, location, title, time, likes) {

  var content = "";
  content += '<div class="newsfeed-item" onClick="IDtoFullScreen(';
  content += srcToID[src];
  content += ')"><img class="newsfeed-photo" src="';
  content += src;
  content += '"><div class="newsfeed-item-topbar"><div class="newsfeed-item-location newsfeed-item-minor">';
  content += location;
  content += '</div><div class="newsfeed-item-title">';
  content += title;
  content += '</div><div class="newsfeed-item-time newsfeed-item-minor">';
  content += time;
  content += '</div></div><div class="newsfeed-item-bottombar"><div class="newsfeed-item-likes">';
  content += likes;
  content += '</div></div></div>';

  addToNewsFeed(content);

}

$(document).ready(function() {
  console.log('Document ready');
  console.log('Getting user information');
  $.ajax({
    url: '/api/get_profile_self',
    type: "GET",
    data: {'csrfmiddlewaretoken': '{{ csrf_token }}'},
    success : function(data) {
        document.getElementById('navbar-username').innerHTML = data.first_name;
        document.getElementById('navbar-profile-pic').src = data.image;
     }
  });

  console.log('Getting posts list');
    $.ajax({
      url: '/api/posts',
      type: "GET",
      data: {'csrfmiddlewaretoken': '{{ csrf_token }}'},
      success : function(data) {
        for(var d in data.results) {
          dataResults[d] = data.results[d];
          srcToID[data.results[d].image] = data.results[d].id;
          shroomHTML(data.results[d].image, data.results[d].location.description, data.results[d].caption, data.results[d].time_elapsed, 0);
        }
      }
    });

})
