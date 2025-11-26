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
    pass


@app.post("/get_flood_report")
def get_flood_report(req: FloodRequest, report=None):
    # Call your run_agent logic here
    run_agent(req.lat, req.lon, req.usgs_site_id, keys={
        "STORMGLASS_KEY": os.getenv("STORMGLASS_KEY"),
        "WEATHER_KEY": os.getenv("WEATHER_KEY"),
        "GOOGLE_FLOOD_KEY": os.getenv("GOOGLE_FLOOD_KEY")
    })
    return {"report": report}

# Include all helper functions from the template above (run_agent, normalizers, etc.)
