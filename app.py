from flask import Flask, jsonify
import psutil
import time

app = Flask(__name__)

start_time = time.time()


@app.route('/')
def home():
    return jsonify({
        "status": "ok",
        "service": "devops-api"
    })


@app.route('/health')
def health():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    uptime = time.time() - start_time

    return jsonify({
        "cpu": cpu,
        "memory": mem,
        "uptime": round(uptime, 2),
        "status": "healthy" if cpu < 80 and mem < 80 else "unhealthy"
    })


@app.route('/metrics')
def metrics():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent

    response = (
        "# HELP app_cpu_percent CPU usage percentage\n"
        "# TYPE app_cpu_percent gauge\n"
        f"app_cpu_percent {cpu}\n"
        "# HELP app_memory_percent Memory usage percentage\n"
        "# TYPE app_memory_percent gauge\n"
        f"app_memory_percent {mem}\n"
    )

    return response, 200, {"Content-Type": "text/plain"}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)