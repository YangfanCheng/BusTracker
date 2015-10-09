
var map, marker;
function initMap() {
      map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 40.7420, lng: -74.178078},
        zoom: 13
  });
}

function placeMarker(location) {
        marker = new google.maps.Marker({
        position: location, 
        map: map
    });
}

