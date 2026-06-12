from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import attacks, defense, reports

app = FastAPI(
    title="KubeRedOps Dashboard API",
    description="Kubernetes Threat Simulation & Defense — Phase 4",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(attacks.router,  prefix="/api/attacks",  tags=["Attacks"])
app.include_router(defense.router,  prefix="/api/defense",  tags=["Defense"])
app.include_router(reports.router,  prefix="/api/reports",  tags=["Reports"])

@app.get("/")
def root():
    return {
        "project": "Kubernetes Threat Simulation & Defense",
        "phase": 4,
        "status": "running"
    }
