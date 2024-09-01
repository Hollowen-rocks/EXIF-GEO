import piexif

def get_geolocation(image_path):
    exif_data = piexif.load(image_path)
    gps_info = exif_data.get("GPS", {})
    
    if gps_info:
        lat = gps_info.get(piexif.GPSIFD.GPSLatitude)
        lat_ref = gps_info.get(piexif.GPSIFD.GPSLatitudeRef)
        lon = gps_info.get(piexif.GPSIFD.GPSLongitude)
        lon_ref = gps_info.get(piexif.GPSIFD.GPSLongitudeRef)
        
        if lat and lon:
            lat = lat[0] / lat[1] + lat[2] / (lat[1] * 60) + lat[3] / (lat[1] * 3600)
            lon = lon[0] / lon[1] + lon[2] / (lon[1] * 60) + lon[3] / (lon[1] * 3600)
            
            if lat_ref == "S":
                lat = -lat
            if lon_ref == "W":
                lon = -lon
            
            return lat, lon
    return None

image_path = r"PATH HERE" 
location = get_geolocation(image_path)
print("Latitude and Longitude:", location)
