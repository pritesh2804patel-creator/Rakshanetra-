def get_ip_location(ip):
    # Placeholder logic for known IPs
    if ip.startswith("103.21."):
        return {"lat": 28.6139, "lon": 77.2090}  # Delhi
    elif ip.startswith("182.0."):
        return {"lat": 24.8607, "lon": 67.0011}  # Karachi
    elif ip.startswith("202.0."):
        return {"lat": 39.9042, "lon": 116.4074}  # Beijing
    else:
        return {"lat": 23.0, "lon": 82.0}  # Central Bharat (default)
