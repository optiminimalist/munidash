$(function(){

        var greenIcon = new L.Icon({
          iconUrl: 'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png',
          shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
          iconSize: [25, 41],
          iconAnchor: [12, 41],
          popupAnchor: [1, -34],
          tooltipAnchor: [1, -34],
          shadowSize: [41, 41]
        });

        var redIcon = new L.Icon({
          iconUrl: 'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
          shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
          iconSize: [25, 41],
          iconAnchor: [12, 41],
          popupAnchor: [1, -34],
          tooltipAnchor: [1, -34],
          shadowSize: [41, 41]
        });

        var map = L.map('map').setView([37.757921, -122.434762], 13);
        mapLink =
            '<a href="http://openstreetmap.org">OpenStreetMap</a>';
        L.tileLayer(
            'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; ' + mapLink + ' Contributors',
            maxZoom: 18,
            }).addTo(map);

        $.get('/all_vehicles.json', function(data){
            var vehicles = [];

            $.each(data, function(i, d) {
                vehicles.push([d.lat, d.lon, 10]);

                var icon;
                if(d.direction == "INBOUND") {
                    icon = redIcon;
                }
                else if (d.direction == "OUTBOUND") {
                    icon = greenIcon;
                }

                var marker = L.marker([d.lat, d.lon], {icon: icon}).
                bindTooltip(d.route_tag + " " + d.direction, {"permanent": false, "direction": "top"}).
                addTo(map);
            });

            var heat = L.heatLayer(vehicles, {radius: 25}).addTo(map);


        });

});