import asyncio
import microdot

app = microdot.Microdot()

@app.route('/')
async def index(request):
    return 'Hello, world!'

@app.route('/users/active')
async def active_users(request):
    return 'Active users: Susan, Joe, and Bob'


@app.route('/makefile')
async def makefile(request):
    import time
    test_dict = {}
    test_dict['a'] = 1.5
    test_dict['another_key']=[4,3,'a']
    test_dict['time'] = time.time_ns()
    import json
    with open('static/test.json','w') as f:
        f.write(json.dumps(test_dict))
    return 'made'

@app.route("/static/<path:path>")
def static(request, path):
    if ".." in path:
        # directory traversal is not allowed
        return "Not found", 404
    return microdot.microdot.send_file("static/" + path)

async def main():
    # start the server in a background task
    server = asyncio.create_task(app.start_server())

    # ... do other asynchronous work here ...

    # cleanup before ending the application
    await server

asyncio.run(main())