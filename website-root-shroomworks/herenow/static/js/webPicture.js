function startCamera() {
  getLocation();
  run_webcam();
}

// gps functions
function getMiniMap(position) {
  var mapUrl = "https://maps.googleapis.com/maps/api/staticmap?center=LATITUDE,LONGITUDE&zoom=14&size=400x300&markers=color:blue|LATITUDE,LONGITUDE&key=AIzaSyCoGpZQdMzmoahBt27dvZDWNlPdeCagig8";
  var lat = position.coords.latitude;
  var lon = position.coords.longitude;
  mapUrl = mapUrl.replace('LATITUDE', lat);
  mapUrl = mapUrl.replace('LATITUDE', lat);
  mapUrl = mapUrl.replace('LONGITUDE', lon);
  mapUrl = mapUrl.replace('LONGITUDE', lon);
  document.getElementById("minimap").src = mapUrl;
}

function getLocation() {
  if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(showPosition, showError);
  }
  else {
      document.getElementById("position").innerHTML = "Geolocation is not supported by this browser.";
  }

  function showPosition(position) {
      document.getElementById("lat").value = position.coords.latitude;
      document.getElementById("lon").value = position.coords.longitude;
      getMiniMap(position);
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

// camera functions
function run_webcam() {
  // Get access to the camera!
  if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
      document.getElementById('video').src = window.URL.createObjectURL(stream);
      document.getElementById('video').play();
      localStream = stream;
    });
  }
}

function stopCamera() {
  document.getElementById('video').pause();
  document.getElementById('video').src = '';
  localStream.getTracks()[0].stop();
}

// Trigger photo take
function snap() {
  document.getElementById('canvas').getContext('2d').drawImage(document.getElementById('video'), 0, 0, 400, 300);
  document.getElementById('take_pic').style.display = 'none';
  document.getElementById('show_pic').style.display = 'block';
  document.getElementById('image_b64').value = document.getElementById('canvas').toDataURL("image/png");
  console.log(document.getElementById('image_b64').value);
};

function retakePicture() {
  document.getElementById('take_pic').style.display = 'block';
  document.getElementById('show_pic').style.display = 'none';
}

function createPost() {
  var formData = JSON.stringify($("#create_post_form").serializeObject());
  var csrftoken = getCookie('csrftoken');
  $.ajax({
    url: '/api/create_post',
    type: "POST",
    contentType: 'application/json; charset=utf-8',
    data: formData,
    beforeSend: function(jqXHR, settings) {
      jqXHR.setRequestHeader("x-csrftoken", csrftoken);
    },
    success : function() {
      console.log("post success!")
    }
  });
}

// Get the webpic_modal
var webpic_modal = document.getElementById('webpic_modal');
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the webpic_modal
function take_pic() {
  startCamera();
  webpic_modal.style.display = "block";
}

// When the user clicks on <span> (x), close the webpic_modal
span.onclick = function() {
  stopCamera();
  webpic_modal.style.display = "none";
}

// When the user clicks anywhere outside of the webpic_modal, close it
window.onclick = function(event) {
  if (event.target == webpic_modal) {
      webpic_modal.style.display = "none";
  }
}
