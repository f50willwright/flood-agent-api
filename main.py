from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

# Input schema
class FloodRequest(BaseModel):
    lat: float
    lon: float
    usgs_site_id: str | None = None

def run_agent(lat, lon, usgs_site_id, keys):
    # Placeholder for your logic
    return {"status": "agent executed", "lat": lat, "lon": lon}

# ✅ Health check route
@app.get("/")
def root():
    return {"message": "API is running"}

# ✅ Simple GET route for testing lat/lon
@app.get("/results")
def get_results(lat: float, lon: float):
    return {"lat": lat, "lon": lon}

# ✅ Your POST route
@app.post("/get_flood_report")
def get_flood_report(req: FloodRequest):
    report = run_agent(req.lat, req.lon, req.usgs_site_id, keys={
        "STORMGLASS_KEY": os.getenv("STORMGLASS_KEY"),
        "WEATHER_KEY": os.getenv("WEATHER_KEY"),
        "GOOGLE_FLOOD_KEY": os.getenv("GOOGLE_FLOOD_KEY")
    })
    return {"report": report}
