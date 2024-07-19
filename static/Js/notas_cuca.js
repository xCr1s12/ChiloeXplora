document.addEventListener('DOMContentLoaded', (event) => {
    // Inicializar el mapa
    var map = L.map('map').setView([-42.63837, -74.10997], 14);

    // Agregar capa base
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);  

    // Variable global para el marcador y el control de la ruta y también el polígono
    var marker;
    var routingControl;
    var polygon;

    // Definir la función onMapClick
    function onMapClick(e) {
        // Lógica de la función onMapClick
        console.log("You clicked the map at " + e.latlng);
    }

    // Asociar la función onMapClick al evento click del mapa
    map.on('click', onMapClick);

    // Función para agregar una ruta y luego cambiarla
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
                map.removeLayer(polygon);
            }

            // Define el punto de destino para centrar el mapa y ajustar el zoom
            var end;
            switch (index) {
                case 0:
                    addRoute([-42.48127, -73.77064], [-42.63837, -74.10997]); // Ruta Castro - Cucao (Terminado)
                    end = [-42.63837, -74.10997];
                    break;
                case 1:
                    addRoute([-41.87947, -73.79586], [-42.63837, -74.10997]); // Ruta Ancud - Cucao (Terminado)
                    end = [-42.63837, -74.10997];
                    break;
                case 2:
                    addRoute([-41.83148, -73.51242], [-42.63837, -74.10997]); // Ruta Canal de Chacao - Cucao (Terminado)
                    end = [-42.63837, -74.10997];
                    break;
            }

            // Centra el mapa en el punto de destino y ajusta el nivel de zoom
            if (end) {
                setTimeout(() => {
                    map.setView(end, 9);
                }, 500); // Retraso para que cargue todo bien

                // Mostrar mensaje de advertencia
                var mensajeAdvertencia = document.getElementById('mensaje_advertencia');
                mensajeAdvertencia.style.display = 'block';
                setTimeout(() => {
                    mensajeAdvertencia.style.display = 'none';
                }, 5000);
            }
        });
    });

    // Evento para copiar la ruta como enlace y luego poder irse a Google Maps
    const botonCopiar = document.getElementById('copiarRuta');
    botonCopiar.addEventListener('click', () => {
        // Obtener las coordenadas de inicio y fin de la última ruta seleccionada
        var start = routingControl.getWaypoints()[0].latLng;
        var end = routingControl.getWaypoints()[1].latLng;

        // Crear el enlace a Google Maps con las coordenadas
        var googleMapsLink = `https://www.google.com/maps/dir/?api=1&origin=${start.lat},${start.lng}&destination=${end.lat},${end.lng}`;

        // Abrir la página de Google Maps en una nueva pestaña
        window.open(googleMapsLink, '_blank');

        // Mostrar mensaje de confirmación
        alert('Se ha copiado la ruta a Google Maps.');
    });

    // Ejemplo de cómo agregar un marcador
    marker = L.marker([-42.63837, -74.10997]).addTo(map)
        .bindPopup("Centro de Cucao").openPopup();

    // Definir las coordenadas del polígono que encierra Cucao
    var polygonCoords = [
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
    polygon = L.polygon(polygonCoords, {
        color: 'blue',
        fillColor: '#30a5ff',
        fillOpacity: 0.5
    }).addTo(map).bindPopup("Pueblo de Cucao");
});
