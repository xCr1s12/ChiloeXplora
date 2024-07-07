var map = L.map('map').setView([-42.6378, -74.1091], 14);

// Agregar capa base
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Variable global para el marcador y el control de la ruta
var marker;
var routingControl;
var polygon;

// Función para agregar una ruta
function addRoute(start, end) {
    if (routingControl) {
        map.removeControl(routingControl);
    }
    routingControl = L.Routing.control({
        waypoints: [
            L.latLng(start[0], start[1]),
            L.latLng(end[0], end[1])
        ],
        routeWhileDragging: true
    }).addTo(map);
}

// Botones y sus eventos
document.querySelectorAll('.btn').forEach((button, index) => {
    button.addEventListener('click', () => {
        // Elimina el marcador si existe
        if (marker) {
            map.removeLayer(marker);
        }
        if (polygon) {
            map.removeLayer(cucaoPolygon)
        }
        

        // Define el punto de destino para centrar el mapa y ajustar el zoom
        var end;
        switch (index) {
            case 0:
                addRoute([-42.4806, -73.7635], [-42.6378, -74.1091]); // Ruta Castro - Cucao
                end = [-42.6378, -74.1091];
                break;
            case 1:
                addRoute([-41.8698, -73.8203], [-42.6378, -74.1091]); // Ruta Ancud - Cucao
                end = [-42.6378, -74.1091];
                break;
            case 2:
                addRoute([-41.83148, -73.51242], [-42.6378, -74.1091]); // Ruta Canal de Chacao - Cucao
                end = [-42.6378, -74.1091];
                break;
        }

        // Centra el mapa en el punto de destino y ajusta el nivel de zoom
        if (end) {
            setTimeout(() => {
                map.setView(end, 9);
            }, 500); // Agrega un pequeño retraso para asegurar que la vista se ajuste correctamente
        }
        // mensaje de advertencia
        var mensajeAdvertencia = document.getElementById('mensaje_advertencia');
        mensajeAdvertencia.style.display = 'block' ; 

        setTimeout(() => {
            mensajeAdvertencia.style.display = 'none';
        }, 5000);
    });
});

// Ejemplo de cómo agregar un marcador
marker = L.marker([-42.6378, -74.1091]).addTo(map)
    .bindPopup("Centro de Cucao").openPopup();

// Definir las coordenadas del polígono que encierra Cucao
var polygon = [
    [-42.6406,-74.1104],
    [-42.6389,-74.1118],
    [-42.6389,-74.1118],
    [-42.6338,-74.1058],
    [-42.6307,-74.1036],
    [-42.6336,-74.0996],
    [-42.6356,-74.1030],
    [-42.6392,-74.1065]
];

// Crear y agregar el polígono al mapa
var cucaoPolygon = L.polygon(polygon, {
    color: 'blue',
    fillColor: '#30a5ff',
    fillOpacity: 0.5
}).addTo(map).bindPopup("Pueblo de Cucao");

// Obtener el botón y el campo de texto
const botonCopiar = document.getElementById('copiarRuta');
const campoTexto = document.getElementById('rutaParaCopiar');

// Evento click para el botón de copiar
botonCopiar.addEventListener('click', () => {
    // Obtener la URL actual del navegador (o la ruta que desees compartir)
    const ruta = window.location.href; // Puedes reemplazar con la ruta específica que deseas compartir

    // Mostrar la ruta en el campo de texto
    campoTexto.value = ruta;

    // Seleccionar el texto en el campo de texto
    campoTexto.select();
    campoTexto.setSelectionRange(0, 99999); // Para dispositivos móviles

    // Copiar el texto seleccionado al portapapeles
    document.execCommand('copy');

    // Informar al usuario que se copió la ruta
    alert('¡La ruta se ha copiado al portapapeles!');
});