document.addEventListener("DOMContentLoaded", init);

function init() {
  const map = L.map("map").setView([14.516589, 121.019333], 13);
  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution:
      '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  }).addTo(map);
}
