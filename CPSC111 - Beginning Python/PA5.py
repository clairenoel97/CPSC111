#assignment 5

'''
write a program that reads in US locations from an input file
the locations include a road trip origin, destination, and several trip waypoints

input file format

program output
    1. Status messages displayed to the console. These messages simply let the user know what the program is currently computing (e.g. "Reading in road trip origin location from florida_roadtrip.txt...", etc.).
    2. Road trip information and statistics written to an output file. Name your output file <input file base name>_stats.txt. For example, for the provided input file, "florida_roadtrip.txt", the corresponding output file is "florida_roadtrip_stats.txt". The stats to be written to the output file include:
        -Distances in miles between each consecutive road trip stop. See the starter code below for how to get this information.
        -Total number of waypoints on the road trip.
        -Total number of days on the road trip.
        -Total miles traveled on the road trip.
        -Names of the two waypoints with the most distance between them and that distance in miles.
        -Name of the waypoint with the longest stay and its number of days.
        -Average miles between between each stop (including origin, waypoints, and destination).
        -Average number of days spent at each waypoint.
'''
import urllib.request
import webbrowser

API_KEY = "AIzaSyB16_cj_FXLyPvGJf6sble8ex_P6_GENMM"

def format_city_string(city_str):
    '''
    111 students: no need to call this function
    To prepare the city string for the query:
    1. remove comma
    2. replace spaces with +

    (3 pts) Build a string for the waypoints parameter according to the Google Maps Embed API documentation. While iterating through each waypoint in the input file, use the provided format_city_string() function from the starter code and the string concatenation operator to build a string for the waypoints parameter. For the florida_roadtrip.txt files, this string should look like the following (no spaces or newlines):
    '''
    city_str = city_str.replace(",", "")
    city_str = city_str.replace(" ", "+")
    return city_str
def build_query(origin, dest):
    '''
    111 students: no need to call this function
    Builds the query string for the Google Distance Matrix API according to this website:
    https://developers.google.com/maps/documentation/distance-matrix/start
    '''
    query_base = "https://maps.googleapis.com/maps/api/distancematrix/json?origins="
    query = query_base + origin
    query += "&destinations="
    query += dest
    query += "&key="
    query += API_KEY
    return query
def extract_distance(results_str):
    '''
    111 students: no need to call this function
    Extracts the distance in meters from the JSON response.
    '''
    index = results_str.find("distance")
    results_str = results_str[index:]
    index = results_str.find("value")
    results_str = results_str[index:]
    index = results_str.find(":")
    results_str = results_str[index + 2:]
    index = results_str.find(r"\n")
    results_str = results_str[:index]
    dist = int(results_str)
    return dist
def get_distance(city1, city2):
    '''
    111 STUDENTS: THIS IS THE FUNCTION YOU WILL CALL
    Accepts 2 strings representing cities in the U.S.
    Returns the integer distance in meters between city1 and city2
    '''
    city1 = format_city_string(city1)
    city2 = format_city_string(city2)

    query = build_query(city1, city2)

    web_obj = urllib.request.urlopen(query)
    # web_obj.read() returns an array of bytes, need to convert to a string
    results_str = str(web_obj.read())
    web_obj.close()

    dist = extract_distance(results_str)
    return dist

def welcome():
    print("Welcome to the road trip analyzer program, utilizing Google Maps!")
    print("Roadtrip origin, destination, waypoints, and number of days spent at each waypoint will be read in from a file.")
    print("The program write to an output file the distance in miles between each waypoint on the trip and statistics about the trip. Enjoy!\n\n")
def read_file(filename):
    '''
    opens input file
    returns the file that is open
    '''
    input_file = open(filename, "r")
    print("Reading in road trip stop information from %s...\n" %(filename))
    return input_file
def write_file(filename):
    '''
    writes to the chosen file
    data is the information that will be written into the file
    '''
    outfile = open(filename, "w")
    return outfile
def write_to_file(file_to_write, information):
    print(information, file=file_to_write)
def close_file(file_to_close):
    '''
    closes the file
    '''
    file_to_close.close()
def get_origin(input_file, locations):
    origin = input_file.readline()
    locations.append(origin.strip())
    newline = input_file.readline()
    origin = "Roadtrip origin: %s" %(origin.strip())
    print(origin)
    return origin
def get_waypoints(input_file, output_file, days, locations):
    while True:
        location = input_file.readline()
        locations.append(location.strip())
        duration = (input_file.readline())
        newline = input_file.readline()
        if duration == '':
            destination = location
            print("Roadtrip destination: %s" %(destination))
            break
        duration = duration.strip()
        days.append(duration)
        print("Processing waypoint " + location.strip() + " (%s days)..." %(duration))
    return locations, days
def get_all_distances(locations):
    distances_between_points = []
    for location in range(len(locations) - 1):
        #print("location #%d: %s" %(location, locations[location]))
        dist = get_distance(locations[location], locations[location + 1])
        distances_between_points.append(dist)
    return distances_between_points
def convert_distances_to_miles(distances):
    for index in range(len(distances)):
        distances[index] = float(distances[index] / 1609.344)
    return distances
def get_average_of_all_distances(distances, output_file):
    total = 0
    for distance in distances:
        total += distance
    avg = total/len(distances)
    print("Average roadtrip distance between waypoints is: %.2f miles" %(avg), file=output_file)
def get_average_days(days, output_file):
    total = 0
    results = [int(i) for i in days]
    for i in results:
        total += i
    avg = total / len(days)
    print("Average roadtrip days at one waypoint: %.2f days" %(avg), file=output_file)
def get_total_miles_traveled(distances, output_file):
    total = 0
    for i in distances:
        total += i
    print("Total miles traveled on roadtrip: %.2f" %(total), file=output_file)
def waypoints_summary(locations, distances, output_file):
    for i in range(len(locations) - 1):
        print("%s to %s: %.2f miles" %(locations[i], locations[i+1], distances[i]), file=output_file)
def total_number_of_waypoints(locations, output_file):
    print("Number of waypoints on roadtrip: %d" %(len(locations) - 2), file=output_file)
def total_number_of_days(days, output_file):
    results = [int(i) for i in days]
    total = 0
    for i in results:
        total += i
    print("Number of days on roadtrip: %d" %(total), file=output_file

    )
def longest_distance(locations, distance, output_file):
    index = distance.index(max(distance))
    l1 = locations[index]
    l2 = locations[index + 1]
    print("Longest roadtrip distance between waypoints is %s to %s: %.2f" %(l1, l2, max(distance)),file=output_file)
def longest_duration(days, locations, output_file):
    index = days.index(max(days))
    l = locations[index + 1]
    print("Longest roadtrip days at one waypoint is %s: %s days" %(l, max(days)), file=output_file)
def roadtrip_stats(days, locations, distances, output_file):
    print("\n***Roadtrip Stats***", file=output_file)
    total_number_of_waypoints(locations, output_file)
    total_number_of_days(days, output_file)
    get_total_miles_traveled(distances, output_file)
    longest_distance(locations, distances, output_file)
    longest_duration(days, locations, output_file)
    get_average_of_all_distances(distances, output_file)
    get_average_days(days, output_file)
def form_waypoint_string(locations):
    result = [format_city_string(i) for i in locations]
    string = '|'.join(result[1:-1])
    return string

def form_frame(formatted_origin,formatted_destination, formatted_waypoints, api_key):
    base = "https://www.google.com/maps/embed/v1/directions?key="
    base += api_key
    base += "&origin="
    base += formatted_origin
    base += "&destination="
    base += formatted_destination
    base += "&waypoints="
    base += formatted_waypoints
    return base

def making_frame(iframe_string):
    output_file = open("florida_roadtrip.html", "w")
    print(iframe_string, file=output_file)
    output_file.close()

    webbrowser.open("florida_roadtrip.html")

def bonus(locations):
    formatted_origin = format_city_string(locations[0])
    formatted_destination = format_city_string(locations[-1])
    formatted_waypoints = form_waypoint_string(locations)
    url = form_frame(formatted_origin, formatted_destination, formatted_waypoints, API_KEY)
    iframe_string = "<iframe\nwidth='450'\nheight='250'\nframeborder='0'\nstyle='border:0'\nsrc='%s' allowfullscreen>\n</iframe>" %(url)
    making_frame(iframe_string)

def main():
    input_file = "florida_roadtrip.txt"
    output_file = "florida_roadtrip_stats.txt"
    locations = []
    days = []

    welcome()
    in_file = read_file(input_file)
    out_file = write_file(output_file)
    origin = get_origin(in_file, locations)
    get_waypoints(in_file, out_file, days, locations)
    #distance calculations
    distances = get_all_distances(locations)
    convert_distances_to_miles(distances)
    #this is what is written to the outfile
    waypoints_summary(locations, distances, out_file)
    roadtrip_stats(days, locations, distances, out_file)
    #close the file you are writing to
    print("Writing stop stats to %s..." %(output_file))
    print("(Bonus) Launching Google Maps for this roadtrip in the browser...")
    print("Closing files...")
    close_file(out_file)

    bonus(locations)

main()
