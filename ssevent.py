import gevent
from gevent.wsgi import WSGIServer
from gevent.queue import Queue

from flask import Flask, Response

import time, os, sys, threading

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
subscriptions = []

def notify():
    print("I got notified!")
    msg = str(time.time())
    for sub in subscriptions[:]:
        sub.put(msg)

def checkForNewData(n=5):
    while True:
        try:
            gevent.sleep(n)
            notify()
        except GreenletExit:
            print("loop exited!")


# SSE "protocol" is described here: http://mzl.la/UPFyxY
class ServerSentEvent(object):

    def __init__(self, data):
        self.data = data
        self.event = None
        self.id = None
        self.desc_map = {
            self.data : "data",
            self.event : "event",
            self.id : "id"
        }

    def encode(self):
        if not self.data:
            return ""
        lines = ["%s: %s" % (v, k) 
                 for k, v in self.desc_map.iteritems() if k]
        
        return "%s\n\n" % "\n".join(lines)

# Client code consumes like this.
@app.route("/")
def index():
    debug_template = """
     <html>
       <head>
       </head>
       <body>
         <h1>Server sent events</h1>
         <div id="event"></div>
         <script type="text/javascript">

         var eventOutputContainer = document.getElementById("event");
         var evtSrc = new EventSource("/subscribe");

         evtSrc.onmessage = function(e) {
             console.log(e.data);
             eventOutputContainer.innerHTML = e.data;
         };

         </script>
       </body>
     </html>
    """
    return(debug_template)

@app.route("/debug")
def debug():
    return "Currently %d subscriptions" % len(subscriptions)

@app.route("/subscribe")
def subscribe():
    def gen():  # When this function is run, a subscription is added to the queue and 
        q = Queue()
        subscriptions.append(q)
        try:
            while True:
                result = q.get()  # This will block until an item is available, then loop around and wait for the next item to pop into the queue
                ev = ServerSentEvent(str(result))
                yield ev.encode()
        except GeneratorExit: # Or maybe use flask signals
            subscriptions.remove(q)
            print("Generator exited!")
    return Response(gen(), mimetype="text/event-stream")

@app.route("/publish")
def publish():
    #Dummy data - pick up from request for real data    
    gevent.spawn(notify)
    
    return "OK"

if __name__ == "__main__":

    if app.config['HEROKU']:
        app.run(debug=True)
    else:
        if app.config['ETHEREUM']:
            gevent.Greenlet.spawn(checkForNewData)
            
        app.debug = True
        server = WSGIServer(("", 5000), app)
        server.serve_forever()
    # Then visit http://localhost:5000 to subscribe 
    # and send messages by visiting http://localhost:5000/publish