import gc
import uasyncio as asyncio
import time
import json
import asyncio
import microdot

app = microdot.Microdot()

import microdot
import microdot.microdot
import microdot.utemplate
import microdot.websocket

microdot.microdot.Response.default_content_type = 'text/html'
microdot.microdot.Response.socket_read_timeout =0


@app.get('/')
async def index(request):
    return microdot.utemplate.Template('index.html').render()


@app.route("/static/<path:path>")
def static(request, path):
    if ".." in path:
        # directory traversal is not allowed
        return "Not found", 404
    return microdot.microdot.send_file("static/" + path)

@app.route('/current_time')
@microdot.websocket.with_websocket
async def get_time(request, ws):
    while True:
        data = {}
        data['time']=time.time_ns()
        await ws.send(json.dumps(data))
        await asyncio.sleep(.5)


async def main():
    # start the server in a background task
    server = asyncio.create_task(app.start_server())

    # ... do other asynchronous work here ...

    # cleanup before ending the application
    await server

asyncio.run(main())