from gps_class import GPSVis

vis = GPSVis(
    data_path=1,                                    # <--- data file with GSM positions (change only this row)
    locations="data-locations.csv",                 # restaurants and residences
    map_path="data-map.png",                        # Map downloaded from OSM (https://www.openstreetmap.org/export)
    points=(52.5914, 13.2385, 52.4262, 13.5441)     # Two coordinates of the map (upper left, lower right)
)

vis.create_image(color=(0, 0, 255), width=5)  # Set the color and the width of the GNSS tracks.
vis.plot_map(output='save')

# print()

# import random
# for i in range(5):
#     liste = ["R-A", "R-B", "R-C", "R-D", "P-E", "P-F", "P-G", "P-H"]
#     random.shuffle(liste)
#     for j in range(7):
#         if(random.random() > 0.5):
#             print(liste[j], end=" ")
#     print()
    