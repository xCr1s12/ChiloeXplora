// creando la variable map (y en ella cargando la librería de Leaflet)
var map = L.map('map').setView([-42.6378, -74.1091], 14);



// Carga los mosaicos
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map); //aquí los estoy añadiendo a la variable "map"

// variable "marker" para hacer un marcador
var marker = L.marker([-42.63784,-74.10968]).addTo(map);
marker.bindPopup("Centro de Cucao.").openPopup(); //texto en el marcador

// agregar los puntos de los poligonos
var polygon = L.polygon([
    [-42.63067,-74.10357],
    [-42.63357,-74.09974],
    [-42.6392,-74.1065],
    [-42.6405,-74.1104],
    [-42.6403,-74.1110],
    [-42.6403,-74.1110],
    [-42.6370,-74.1110],
    [-42.6348,-74.1065]
]).addTo(map);

// texto para poligono
polygon.bindPopup("Pueblo de cucao.");

var popup = L.popup();


map.on('click', onMapClick);

L.Routing.control({
    waypoints: [
      L.latLng(-42.48119,-73.77080),
      L.latLng(-42.6378, -74.1091)
    ] 
  }).addTo(map);