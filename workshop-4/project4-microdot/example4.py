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

A = 1

@app.get('/')
async def index(request):
    return microdot.utemplate.Template('index2.html').render()


@app.route("/static/<path:path>")
def static(request, path):
    if ".." in path:
        return "Not found", 404
    return microdot.microdot.send_file("static/" + path)

@app.route('/ws')
@microdot.websocket.with_websocket
async def read_form(request, ws):
    global A
    while True:
        try:
            data = await ws.receive()
            await ws.send(data)
            json_data = json.loads(data)
            A  = float(json_data['A'])
            print(data)
        except Exception as e:
            print(e)


async def main():
    server = asyncio.create_task(app.start_server())
    await server

asyncio.run(main())