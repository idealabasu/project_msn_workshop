const ws = new WebSocket(`ws://${location.host}/current_time`);
console.log("ws opening");
ws.binaryType = "blob";
ws.addEventListener("open", event => {console.log("Websocket connection opened");});
ws.addEventListener("close", event => {console.log("Websocket connection closed");});
ws.onmessage = function (message) {
    {
        console.log("message: " + message.data);
        const obj = JSON.parse(message.data);

        document.getElementById('time1').innerHTML = obj.time

    }
}