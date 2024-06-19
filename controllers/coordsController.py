import services.database as db

def create(cat, lat, lng):
    
    format_coord = {
        "cat": cat,
        "lat": lat,
        "lng": lng
    }

    db.coord_collection.insert_one(format_coord)

def read():
    return list(db.coord_collection.find())