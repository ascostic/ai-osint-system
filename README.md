#  ai-osint-system

> A personal learning project — building a free, local version of GeoSpy to understand how machines can detect real-world locations from images.

---

##  Why I Built This

You've probably heard of tools like **GeoSpy** — software that can look at a photo and tell you *where in the world it was taken*. It feels like magic, but it's actually engineering.

The problem? Tools like GeoSpy cost money.

So I decided to build my own dummy version — not to compete with GeoSpy, but to **understand how it works from the inside**. This project is my way of learning how machines read hidden data inside photos and turn it into real-world intelligence.

If you're a non-tech person reading this — think of it like this:

> Every photo taken on a phone secretly stores the GPS coordinates of where it was taken. This system reads that hidden data and tells you exactly where the photo was taken — down to the street.

---

##  What This System Does

-  **Reads hidden GPS data** from image files (called EXIF metadata)
-  **Converts raw coordinates** into a readable location
-  **Generates a Google Maps link** so you can see the exact location
-  **Exposes everything as an API** — send an image, get a location back

---

##  Built With

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| FastAPI | Backend API framework |
| ExifRead | Reading hidden image metadata |
| Uvicorn | Running the local server |

Everything runs **100% locally** — no paid APIs, no cloud services.

---

##  How To Run It

**1. Clone the project**
```bash
git clone https://github.com/ascostic/ai-osint-system.git
cd ai-osint-system
```

**2. Create a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Start the server**
```bash
uvicorn api.main:app --reload
```

**5. Send an image and get a location**
```bash
curl -X POST "http://127.0.0.1:8000/extract-gps" \
  -F "file=@your_photo.jpg"
```

**Example response:**
```json
{
  "latitude": 43.467448,
  "longitude": 11.885127,
  "maps_link": "https://maps.google.com/?q=43.467448,11.885127"
}
```

---

##  Project Structure

```
ai-osint-system/
├── api/
│   └── main.py              # FastAPI server and endpoints
├── modules/
│   ├── metadata_extractor.py  # GPS extraction logic
│   ├── similarity_engine.py   # (coming soon)
│   └── osint_automation.py    # (coming soon)
├── data/                    # Temporary file storage
├── requirements.txt
└── README.md
```

## Disclaimer

This project is built **purely for learning purposes**. It only reads metadata that is already stored inside image files. It does not track anyone, access any external database, or perform any surveillance.

---

## About

Built by a MCA student learning backend development and AI engineering — one module at a time.

---

