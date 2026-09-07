document.addEventListener("DOMContentLoaded", init);

function init() {
  // Leaflet map initialization
  const map = L.map("map").setView([14.516589, 121.019333], 13);
  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution:
      '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  }).addTo(map);

  //   Fetch the places data from the API - fetch api-get request
  const fetchGetRequest = async (url, func) => {
    try {
      const response = await fetch(url);
      const data = await response.json();
      return func(data);
    } catch (error) {
      console.error("Error fetching data:", error.message);
    }
  };

  // Add all places to the map and define the point style for the markers
  const poinstStyle = {
    stroke: true,
    radius: 8,
    color: "black",
    weight: 2,
    opacity: 1,
    fillColor: "green",
    fillOpacity: 1,
  };

  const selectedPoinstStyle = {
    stroke: true,
    radius: 8,
    color: "black",
    weight: 2,
    opacity: 1,
    fillColor: "yellow",
    fillOpacity: 1,
  };

  // Function to style the clicked marker and reset the previous one
  const styleGeoJSONonClick = (places) => {
    let lastClickedFeature;

    places.on("click", (e) => {
      if (lastClickedFeature) {
        places.resetStyle(lastClickedFeature);
      }
      lastClickedFeature = e.layer;
      e.layer.setStyle(selectedPoinstStyle);
    });
  };

  // GEOJSON layer
  const addAllPlacesToMap = (json) => {
    let places = L.geoJSON(json, {
      pointToLayer: function (feature, latlng) {
        return L.circleMarker(latlng, poinstStyle);
      },
    }).addTo(map);
    // Add click event listener to the places layer to change the color of the clicked marker
    styleGeoJSONonClick(places);
  };

  fetchGetRequest("/api/v1/places/", addAllPlacesToMap);
}
