// this function is largely based on the Google Maps API documentation
function initMap() {
    // initialises map and sets co-ordinates for its central zoom location
    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 13,
        center: {
            lat: 51.49360,
            lng: -0.19204
        }
    });

    var labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    // sets location to be occupied by a map marker
    var locations = [
        {
            lat: 51.49360,
            lng: -0.19204
        }
    ];

    // takes the first letter of the labels string and positions the marker in the selected location
    var marker = locations.map(function (location, i) {
        return new google.maps.Marker({
            position: location,
            label: labels[i % labels.length]
        });
    });

    var markerCluster = new MarkerClusterer(map, marker,
        { imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m' }
    );
}