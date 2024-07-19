var map = L.map('map').setView([-42.62863645758797, -74.10592466486328], 17); // inicializando el mapa centrado en "Restauran"

// Agregar capa base (esto va, si o si)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);  

// Variable global para el marcador y el control de la ruta y tambien el poligono para luego quitarlos mediante una funcion más abajito
var marker;
var routingControl;


// marcador que irá centrado en el restaurant
marker = L.marker([-42.62863645758797, -74.10592466486328]).addTo(map)
    .bindPopup("Restaurant: Raices Huilliches").openPopup();
        
//funcion para agregar ruta
function addRoute(start, end) {
    if (routingControl) {
        map.removeControl(routingControl);
    }
    if (marker){
        map.removeLayer(marker);
    }
    routingControl = L.Routing.control({
        waypoints: [
            L.latLng(start[0], start[1]),
            L.latLng(end[0], end[1])
        ],
        routeWhileDragging: true
    }).addTo(map);

    // Ajustando el nivel del zoom del mapa pero con un leve retraso
    setTimeout(() => {
        map.setZoom(15); // reseteando zoom cuando la persona genere la ruta
    }, 500)


    
}

// boton "Generar ruta" evento
document.getElementById('copiarRuta').addEventListener('click', () => {
    var cucao = [-42.63795, -74.10976];
    var paradorDarwing = [-42.62863645758797, -74.10592466486328];
    addRoute(cucao, paradorDarwing);
});


// Evento para copiar la ruta como enlace y luego poder irse a google maps
document.getElementById('obtener_ruta').addEventListener('click', () => {
    if (routingControl) {
        var waypoints = routingControl.getWaypoints();
        var start = waypoints[0].latLng;
        var end = waypoints[1].latLng;

    // Crear el enlace a Google Maps con las coordenadas
    var googleMapsLink = `https://www.google.com/maps/dir/?api=1&origin=${start.lat},${start.lng}&destination=${end.lat},${end.lng}`;

    // Abrir la página de Google Maps en una nueva pestaña
    window.open(googleMapsLink, '_blank');

    // Mostrar mensaje de confirmación
    alert('Se ha copiado la ruta a Google Maps.');
} else {
    alert('Por favor, genera primero una ruta.');
}
});