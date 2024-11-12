function send_form(event) {

    event.preventDefault();

    var elements = form.elements;

    var data = {};
    for (var i = 0, element; element = elements[i++];) {        
        if (element.name) {
            data[element.name] = element.value;
        }
    }

    const message = JSON.stringify(data);
    console.log("sent message: " + message);

    ws.send(message);
    document.getElementById('A').value = ''
}

const ws = new WebSocket(`ws://${location.host}/ws`);
console.log("ws opening");
ws.binaryType = "blob";
ws.addEventListener("open", event => {console.log("Websocket connection opened");});
ws.addEventListener("close", event => {console.log("Websocket connection closed");});

ws.onmessage = function (message) {
    {
        console.log("received message: " + message.data);
        const obj = JSON.parse(message.data);
        document.getElementById('A1').innerHTML = obj.A
    }
}

const form = document.getElementById('msgForm');
form.addEventListener("submit", send_form);