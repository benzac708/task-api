# task-api

FastAPI task service for the k3d GitOps portfolio platform. Deployed via Argo CD
from [task-api-config](https://github.com/benzac708/task-api-config).

- `GET /healthz` — readiness probe
- `GET /metrics` — Prometheus metrics
- `GET /tasks` — list tasks
- `POST /tasks` — create task

See the plan: [devops-portfolio-gitops-vps-plan.md](https://github.com/benzac708/bzdotfiles/blob/main/docs/plans/devops-portfolio-gitops-vps-plan.md)