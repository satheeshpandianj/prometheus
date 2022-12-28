from flask import Flask, request, Response
from prometheus_client import Counter, generate_latest

COUNTER = Counter('app_request', 'App Requests', labelnames=['method', 'path'])

app = Flask(__name__)

@app.route("/")
def hello():
    COUNTER.labels(method=request.method, path=request.path).inc()
    return "Scrape me Satheesh with labels"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), 200, mimetype="text/plain")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)