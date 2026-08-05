async function initMap() {
    const { Map } = await google.maps.importLibrary("maps");
    const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

    const map = new Map(document.getElementById("map"), {
        center: { lat: 9.9325, lng: -84.0807 }, // San José, Costa Rica
        zoom: 8,
        mapId: "27975f66f479a1d75e8ccc9e"
    });

    let marker = null;

    map.addListener("click", (event) => {
        const position = event.latLng;

        // console.log("Latitud:", position.lat());
        // console.log("Longitud:", position.lng());
        
        document.getElementById("latitude_input").value = position.lat()
        document.getElementById("longitude_input").value = position.lng()


        // Elimina el marcador anterior
        if (marker) {
            marker.map = null;
        }

        // Crea un nuevo marcador en el punto seleccionado
        marker = new AdvancedMarkerElement({
            position: position,
            map: map,
        });
    });
}

initMap();