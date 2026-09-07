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

  // function to get near cities based on the clicked place
  var nearCitiesGeoJSONLayer; // Variable to hold the near cities layer
  const addNearCitiesToMap = (geojson) => {
    if (nearCitiesGeoJSONLayer) {
      map.removeLayer(nearCitiesGeoJSONLayer);
    }
    nearCitiesGeoJSONLayer = L.geoJSON(geojson, {
      onEachFeature: function (feature, layer) {
        let cityName = feature.properties.name;
        let proximity = feature.properties.proximity;
        layer.bindPopup(
          `<h4>${cityName}</h4><p>Proximity: ${proximity.toFixed(2)} km</p>`,
        );
      },
    }).addTo(map);
  };

  const addNearCitiesLogic = (id) => {
    let url = `/api/v1/cities/?placeid=${id}`;
    fetchGetRequest(url, addNearCitiesToMap);
  };

  const placeImageElement = document.getElementById("placeimage");
  const menuTitleElement = document.getElementById("menu_title");
  const menuTextElement = document.getElementById("menu_text");

  // Function to handle each feature and bind a popup with the place name
  const onEachFeatureHandler = (feature, layer) => {
    let placeName = feature.properties.place_name;
    layer.bindPopup(`<h4>${placeName}</h4>`);

    let noImageAvailable = "./media/place_images/no_image.jpg";
    layer.on("click", () => {
      let featureImage = feature.properties.image
        ? feature.properties.image
        : noImageAvailable;
      placeImageElement.src = featureImage;
      menuTitleElement.textContent = feature.properties.place_name;
      menuTextElement.textContent = feature.properties.description;

      let featureID = feature.properties.pk;
      addNearCitiesLogic(featureID);
    });
  };

  // GEOJSON layer
  const addAllPlacesToMap = (json) => {
    let places = L.geoJSON(json, {
      pointToLayer: function (feature, latlng) {
        return L.circleMarker(latlng, poinstStyle);
      },
      onEachFeature: function (feature, layer) {
        onEachFeatureHandler(feature, layer);
      },
    }).addTo(map);
    // Add click event listener to the places layer to change the color of the clicked marker
    styleGeoJSONonClick(places);
  };

  fetchGetRequest("/api/v1/places/", addAllPlacesToMap);
}
