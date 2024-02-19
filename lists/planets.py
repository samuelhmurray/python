planet_list = ["Mercury", "Mars"]
planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Uranus", "Neptune"])
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
planet_list.append("Pluto")
del planet_list[8]
rocky_planets=planet_list[0:9]

print(planet_list)
print(rocky_planets)

# Example spacecraft list
spacecraft = [
   ("Cassini", "Saturn"),
   ("Viking", "Mars"),
   ("Savage", "Earth"),
   ("Pinecone", "Neptune"),
   ("hello", "Neptune"),
   ("sam", "Neptune"),
]


for planet in planet_list:
    visited_by = [] 
    for spacecraft_name, visited_planet in spacecraft:
        if visited_planet == planet:
            visited_by.append(spacecraft_name) 
    if visited_by:
        print(f"{planet} is visited by: {', '.join(visited_by)}")
  