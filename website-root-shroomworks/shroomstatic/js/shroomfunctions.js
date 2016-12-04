var markers = {};
const TOTAL_MARKERS = 100;

// TODO: Get ID and coords from DB and loop into the array

for (var id = 0; id < TOTAL_MARKERS; id++) {
  var random_lat = (Math.random()-0.5) * 170;
  var random_lng = (Math.random()-0.5) * 360;
  markers[id] = {lat: random_lat, lng: random_lng};
}

function markerClicked(shroom_id) {
  document.getElementById("newsfeed").innerHTML = shroomHTML(shroom_id) + document.getElementById("newsfeed").innerHTML;
}

function shroomHTML(shroom_id) {
  var result = '';
  result += '<div class="news-item"><div id="news-image">';
  if (shroom_id % 2 == 0) {
    result += '<img class="news-image" src="{% static "images/Cockfosters.jpg" %}">';
  } else {
    result += '<img class="news-image" src="{% static "images/moorgate.jpg" %}">';
  }
  result += '</div><div id="news-description">';
  result += 'ID: ' + shroom_id + '<br>';
  result += 'Latitude: ' + markers[shroom_id].lat + '<br>';
  result += 'Longitude: ' + markers[shroom_id].lng + '<br>';
  if (shroom_id % 2 == 0) {
    result += 'This is a Picadilly line train terminating at Cockfosters.';
  } else {
    result += 'This station is Moorgate. Change here for Circle, Hammersmith & City and Metropolitan line, and National Rail Services.';
  }
  result += '</div></div>';
  return result;
}
/*
function getLocation() {
  if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(showPosition, showError);
  }
  else {
      document.getElementById("position").innerHTML = "Geolocation is not supported by this browser.";
  }

  function showError(error) {
      switch(error.code) {
          case error.PERMISSION_DENIED:
              document.getElementById("position").innerHTML = "User denied the request for Geolocation."
              break;
          case error.POSITION_UNAVAILABLE:
              document.getElementById("position").innerHTML = "Location information is unavailable."
              break;
          case error.TIMEOUT:
              document.getElementById("position").innerHTML = "The request to get user location timed out."
              break;
          case error.UNKNOWN_ERROR:
              document.getElementById("position").innerHTML = "An unknown error occurred."
              break;
      }
  }
}
*/
