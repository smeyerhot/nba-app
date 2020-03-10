import requests 
import singer                                # To use request package in current program 
response = requests.get("https://raw.githubusercontent.com/akabab/starwars-api/master/api/all.json")   


# Use the convenience function to query the API
# tesco_items = retrieve_products("Tesco")

singer.write_schema(stream_name="products", schema=schema,
                    key_properties=[])

# Write a single record to the stream, that adheres to the schema
singer.write_record(stream_name="products", 
                    record={**response[0], "store_name": "Tesco"})

# for shop in requests.get(SHOPS_URL).json()["shops"]:
#     # Write all of the records that you retrieve from the API
#     singer.write_records(
#       stream_name="products", # Use the same stream name that you used in the schema
#       records=({**item, "store_name": item}
#                for item in retrieve_products(shop))
#     )    