var SOCKET_ADDRESS = "ws://127.0.0.1:8888/socket"  // needs to be modified in production

$(document).ready(function () {
    var ws = new WebSocket(SOCKET_ADDRESS);
    ws.onmessage = function(event) {
        data =  jQuery.parseJSON(event.data)
        // this is a hack !!!!
        location.reload();

        // console.log(data)
        /* should we remove exisiting points? or should it allow multiple */
        // coordinates = data['house_coordinates'].split(",")
        // content = '<a href="/villager"><div class="map-highlight" style="left:'+ coordinates[0] +'px; top:'+coordinates[1]+'px">'
        // content += '<area shape="circle" coords="' + data['house_coordinates'] +'" alt=""/>'
        // content += '</div></a>'

        
    // $('#housemap').append(content);
    }
});
            