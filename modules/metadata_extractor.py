def convert_to_decimal(degrees, minutes, seconds):
    return degrees + (minutes / 60) + (seconds / 3600)
import exifread

def convert_to_decimal(degrees, minutes, seconds):
    return degrees + (minutes / 60) + (seconds / 3600)

def extract_gps(image_path):
    with open(image_path, 'rb') as f:
        tags = exifread.process_file(f)

    if 'GPS GPSLatitude' not in tags:
        return None

    lat_raw = tags['GPS GPSLatitude'].values
    lon_raw = tags['GPS GPSLongitude'].values
    lat_ref = str(tags['GPS GPSLatitudeRef'])
    lon_ref = str(tags['GPS GPSLongitudeRef'])

    lat = convert_to_decimal(
        float(lat_raw[0]),
        float(lat_raw[1]),
        float(lat_raw[2])
    )
    lon = convert_to_decimal(
        float(lon_raw[0]),
        float(lon_raw[1]),
        float(lon_raw[2])
    )

    if lat_ref == 'S':
        lat = -lat
    if lon_ref == 'W':
        lon = -lon

    return {
        "latitude": round(lat, 6),
        "longitude": round(lon, 6),
        "maps_link": f"https://maps.google.com/?q={lat},{lon}"
    }