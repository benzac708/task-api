"""Task API — FastAPI service for the k3d GitOps portfolio platform."""

from fastapi import FastAPI
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response
from pydantic import BaseModel

app = FastAPI(title="Task API", version="0.1.6")

REQUESTS = Counter("http_requests_total", "Total HTTP requests", ["method", "path", "status"])
LATENCY = Histogram("http_request_duration_seconds", "Request latency", ["path"])

TASKS: list[dict] = []


class TaskIn(BaseModel):
    title: str
    done: bool = False


@app.get("/healthz")
def healthz():
    REQUESTS.labels("GET", "/healthz", 200).inc()
    return {"status": "ok", "version": "0.1.5"}


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


@app.get("/tasks")
def list_tasks():
    REQUESTS.labels("GET", "/tasks", 200).inc()
    return TASKS


@app.post("/tasks")
def create_task(task: TaskIn):
    item = {"id": len(TASKS) + 1, "title": task.title, "done": task.done}
    TASKS.append(item)
    REQUESTS.labels("POST", "/tasks", 201).inc()
    return item
