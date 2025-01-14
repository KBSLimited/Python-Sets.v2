def compare_flight_routes(our_routes, competitor_routes):
    # Find common, unique to our airline, and unique to competitor
    common_destinations = our_routes & competitor_routes
    unique_our_destinations = our_routes - competitor_routes
    unique_competitor_destinations = competitor_routes - our_routes
    
    # Display results
    print(f"Common destinations: {common_destinations}")
    print(f"Destinations unique to our airline: {unique_our_destinations}")
    print(f"Destinations unique to competitor: {unique_competitor_destinations}")

# Example routes
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# Compare routes
compare_flight_routes(our_routes, competitor_routes)