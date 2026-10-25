
stockholm_store = (59.3293, 18.0686)
gothenburg_store = (57.7089, 11.9746)

stores = {
    "SE001": stockholm_store,
    "SE002": gothenburg_store
}

for store_id, coordinates in stores.items():
    latitude, longitude = coordinates

    print(
        f"Store: {store_id}, "
        f"Latitude: {latitude}, "
        f"Longitude: {longitude}"
    )
