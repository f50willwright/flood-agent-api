
from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class FloodRequest(BaseModel):
    lat: float
    lon: float
    usgs_site_id: str | None = None

@app.post("/get_flood_report")
def get_flood_report(req: FloodRequest):
    url = "https://your-service.onrender.com/get_flood_report"
    payload = {"lat": req.lat, "lon": req.lon, "usgs_site_id": req.usgs_site_id}
    resp = requests.post(url, json=payload)
    return resp.json()

