function addShroom(id, src, lat, lng) {
  var centerPoint = new google.maps.LatLng(lat, lng);
  shroomCenters[id] = centerPoint;
  var bounds = calculateBounds(centerPoint);

  var srcImage = src;

  var newShroom = new shroomOverlay(bounds, srcImage, map);

  shroomID = id;
  shrooms[id] = newShroom;
  console.log("Shroom " + id + " created");

  map.setCenter(centerPoint);
}

function addTestShroom(lat, lng) {
  addShroom(0, '/media/posts/test.jpeg', lat, lng);
}

function removeShroom(id) {
  shrooms[id].setMap(null);
  console.log("Shroom " + id + " removed");
}

function shroomClicked(id) {
  var src = '/static/images/lsdlarge.jpg';
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
  content += '<div class="newsfeed-item"><img class="newsfeed-photo" src="';
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
          shroomHTML(data.results[d].image, data.results[d].location.description, data.results[d].caption, data.results[d].time_elapsed, 0);
          addShroom(data.results[d].id, data.results[d].image, data.results[d].location.lat, data.results[d].location.lon);
       }
     }
  });

})
