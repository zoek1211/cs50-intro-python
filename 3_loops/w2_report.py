## Short dictionaries

# dictionaries come with key value pairs


def main():
    spacecraft = {"name": "Voyager 1", "distance": 163}
    print(create_report(spacecraft))


def create_report(spacecraft):
    return f"""
    ====== REPORT ======

    Name: {spacecraft["name"]}
    Distance: {spacecraft["distance"]} AU

    =====================
    """

## error handling with get 
def main():   
    spacecraft = {"name": "James Webb Space Telescope"}
    spacecraft["distance"] = 0.01    # add distance key
    spacecraft.update({"distance": 0.01, "orbit": "Sun"})  # update distance key
    print(create_report(spacecraft))

# use get to access key value pairs
def create_report(spacecraft):
    return f"""
    ====== REPORT ======

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Orbit: {spacecraft.get("orbit", "Unknown")}

    =====================
    """

main()