import numpy as np
import matplotlib.pyplot as plt

data = [
    [ # A*
        [ # map 1
            [ # ground-to-ground
                [64.45997286892673, 23.631545744180546, 39.21733218180744], #lengths
                [7.388905057061257, 7.388905057061257, 8.388905057061258] #time on ground
            ],
            [ # air-to-ground
                [46.241182771401235, 65.06960989614741, 42.969833790618125], #lengths
                [4.242640687119286, 4.242640687119286, 4.242640687119286] #time on ground
            ]
        ],
        [ # map 2
            [ # ground-to-ground
                [62.79898987322333, 17.509860921691395, 40.38890505706125], #lengths
                [8.071067811865476, 7.388905057061257, 7.5604779323150675] #time on ground
            ],
            [ # air-to-ground
                [45.3662673822424, 65.36626738224241, 45.459243911067716], #lengths
                [4.242640687119286, 4.242640687119286, 3.414213562373095] #time on ground
            ]
        ],
        [ # map 3
            [ # ground-to-ground
                [61.43466436361489, 16.681433796945203, 37.85300667219901], #lengths
                [7.706742302257039, 8.024579547452822, 9.024579547452822] #time on ground
            ],
            [ # air-to-ground
                [44.68410462743818, 64.68410462743819, 42.969833790618125], #lengths
                [4.5604779323150675, 4.5604779323150675, 4.5604779323150675] #time on ground
            ]
        ],
        [ # map 4
            [ # ground-to-ground
                [62.116827118419096, 20.535169427003233, 39.2672202345721], #lengths
                [7.388905057061257, 6.5604779323150675, 8.70674230225704] #time on ground
            ],
            [ # air-to-ground
                [44.684104627438174, 64.68410462743819, 42.96983379061812], #lengths
                [4.242640687119286, 4.242640687119286, 4.5604779323150675] #time on ground
            ]
        ],
        [ # map 5
            [ # ground-to-ground
                [17.388905057061258, 14.706742302257041, 19.071067811865476], #lengths
                [7.388905057061257, 7.706742302257039, 8.071067811865476] #time on ground
            ],
            [ # air-to-ground
                [25.656125291633366, 24.384776310850242, 18.192023676495612], #lengths
                [3.414213562373095, 3.414213562373095, 4.242640687119286] #time on ground
            ]
        ]
    ],
    [ # Dijkstra
        [ # map 1
            [ # ground-to-ground
                [61.14553541208295, 19.338288046437587, 36.242640687119284], #lengths
                [61.14553541208295, 19.338288046437587, 36.242640687119284] #time on ground
            ],
            [ # air-to-ground
                [46.24118277140124, 65.06960989614741, 42.96983379061812], #lengths
                [4.242640687119286, 5.242640687119286, 5.242640687119286] #time on ground
            ]
        ],
        [ # map 2
            [ # ground-to-ground
                [62.60623723886871, 16.0956473593183, 37.41421356237309], #lengths
                [62.60623723886871, 16.0956473593183, 37.41421356237309] #time on ground
            ],
            [ # air-to-ground
                [45.3662673822424, 65.36626738224241, 44.287671035813894], #lengths
                [5.242640687119286, 37.242640687119284, 4.242640687119286] #time on ground
            ]
        ],
        [ # map 3
            [ # ground-to-ground
                [59.87418643129983, 14.631545744180544, 35.071067811865476], #lengths
                [59.87418643129983, 14.631545744180544, 35.071067811865476] #time on ground
            ],
            [ # air-to-ground
                [44.68410462743818, 64.68410462743819, 42.969833790618125], #lengths
                [5.5604779323150675, 34.19615242270663, 6.242640687119285] #time on ground
            ]
        ],
        [ # map 4
            [ # ground-to-ground
                [60.459972868926734, 16.58505747976789, 36.342416792648606], #lengths
                [60.459972868926734, 16.58505747976789, 36.342416792648606] #time on ground
            ],
            [ # air-to-ground
                [44.68410462743818, 64.68410462743819, 42.96983379061811], #lengths
                [5.5604779323150675, 5.242640687119286, 4.242640687119286] #time on ground
            ]
        ],
        [ # map 5
            [ # ground-to-ground
                [15.732050807568877, 13.146264369941973, 16.0], #lengths
                [15.732050807568877, 13.146264369941973, 16.0] #time on ground
            ],
            [ # air-to-ground
                [25.65612529163337, 24.384776310850242, 18.192023676495612], #lengths
                [3.82842712474619, 3.82842712474619, 4.242640687119286] #time on ground
            ]
        ]
    ],
    [ # Lazy Theta*
        [ # map 1
            [ # ground-to-ground
                [61.37139321651232, 21.54983443527075, 36.743138350865095], #lengths
                [22.37139321651232, 12.54983443527075, 31.7431383508651] #time on ground
            ],
            [ # air-to-ground
                [42.44174625609426, 59.385801663559064, 39.928594925271256], #lengths
                [5.0, 7.158910531638177, 5.565308279870936] #time on ground
            ]
        ],
        [ # map 2
            [ # ground-to-ground
                [60.08438096044773, 16.58243374944379, 38.126683181409724], #lengths
                [7.557839043551982, 10.25787842910703, 6.9669063302282845] #time on ground
            ],
            [ # air-to-ground
                [40.31768220030615, 58.26556711244772, 40.396063531138594], #lengths
                [4.677030475578647, 5.188102530309008, 3.3166247903554] #time on ground
            ]
        ],
        [ # map 3
            [ # ground-to-ground
                [56.098128311023, 15.239315865334774, 35.27273617373915], #lengths
                [56.098128311023, 14.239315865334774, 31.27273617373915] #time on ground
            ],
            [ # air-to-ground
                [39.92492955535426, 57.56735185849702, 39.319206502675], #lengths
                [6.303936245582252, 9.089581872394266, 5.617029500382142] #time on ground
            ]
        ],
        [ # map 4
            [ # ground-to-ground
                [56.99299219015475, 15.432220400206422, 36.536796308744954], #lengths
                [26.00486614513275, 8.196152422706632, 14.454410447929238] #time on ground
            ],
            [ # air-to-ground
                [39.99106525997432, 57.66722476924946, 39.319206502675], #lengths
                [5.916079783099616, 8.139410298049853, 5.617029500382142] #time on ground
            ]
        ],
        [ # map 5
            [ # ground-to-ground
                [16.224972160321826, 12.696440508742775, 16.0], #lengths
                [16.224972160321826, 12.696440508742775, 16.0] #time on ground
            ],
            [ # air-to-ground
                [23.14085239195441, 23.404231431636596, 16.812239960227117], #lengths
                [3.3166247903554, 3.3166247903554, 4.242640687119285] #time on ground
            ]
        ]
    ]#,
    #[ # GBFS
    #    [ # map 1
    #        [ # ground-to-ground
    #            [69.87005768508878, 24.313708498984763, 42.970562748477136], #lengths
    #            [6.65685424949238, 6.65685424949238, 7.65685424949238] #time on ground
    #        ],
    #        [ # air-to-ground
    #            [47.60550828100967, 67.60550828100963, 44.334159300226545], #lengths
    #            [4.242640687119286, 4.242640687119286, 4.242640687119286] #time on ground
    #        ]
    #    ],
    #    [ # map 2
    #        [ # ground-to-ground
    #            [67.1920236764956, 18.192023676495612, 41.07106781186546], #lengths
    #            [6.65685424949238, 6.65685424949238, 7.65685424949238] #time on ground
    #        ],
    #        [ # air-to-ground
    #            [45.3662673822424, 65.36626738224237, 44.91994573785345], #lengths
    #            [4.242640687119286, 4.242640687119286, 4.242640687119286] #time on ground
    #        ]
    #    ],
    #    [ # map 3
    #        [ # ground-to-ground
    #            [62.60623723886867, 17.36359655174942, 41.170843917394784], #lengths
    #            [7.292528739883945, 7.292528739883945, 8.928203230275509] #time on ground
    #        ],
    #        [ # air-to-ground
    #            [45.3662673822424, 65.36626738224237, 44.72719310349883], #lengths
    #            [4.878315177510849, 4.878315177510849, 5.196152422706632] #time on ground
    #        ]
    #    ],
    #    [ # map 4
    #        [ # ground-to-ground
    #            [67.28427124746187, 20.631545744180546, 45.16671517118376], #lengths
    #            [6.65685424949238, 6.5604779323150675, 8.610365985079726] #time on ground
    #        ],
    #        [ # air-to-ground
    #            [44.68410462743818, 64.68410462743815, 42.96983379061812], #lengths
    #            [4.242640687119286, 4.242640687119286, 4.878315177510849] #time on ground
    #        ]
    #    ],
    #    [ # map 5
    #        [ # ground-to-ground
    #            [18.07106781186548, 15.292528739883945, 19.656854249492383], #lengths
    #            [6.65685424949238, 7.292528739883944, 7.65685424949238] #time on ground
    #        ],
    #        [ # air-to-ground
    #            [26.970562748477146, 24.384776310850242, 18.192023676495612], #lengths
    #            [4.242640687119286, 4.242640687119286, 4.242640687119286] #time on ground
    #        ]
    #    ]
    #]
] # Add other algorithms as needed

# Extract data
n = 30 # number of runs
gn = 15 # number of ground runs
an = 15 # number of air runs
collated_dist = []
collated_ground = []
for i, algorithm in enumerate(data):
    collated_dist += [[]]
    collated_ground += [[]]
    for map in algorithm:
        for type in map: # Type is ground-to-ground or air-to-ground
            for distance in type[0]:
                collated_dist[i].append(distance)
                #Here are your distance numbers
            for grounded in type[1]:
                collated_ground[i].append(grounded)
                #here are your distance near ground numbers

algorithms = ["A *", "Dijkstra", "Lazy Theta *"]
colors = ["#2176b4", "#ed7d17", "#2da42d"]
medianprops = dict(color='black')

bplot = plt.boxplot(collated_dist, labels=algorithms, patch_artist=True, medianprops=medianprops)
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)
plt.legend([bplot["medians"][0], bplot["boxes"][0], bplot["boxes"][1], bplot["boxes"][2]], ["median", "A *", "Dijkstra", "Lazy Theta *"], loc="upper left", fontsize="x-small")
plt.title("Distances of all paths")
plt.ylabel("Distance (m)")
plt.show()

bplot = plt.boxplot(collated_ground, labels=algorithms,  patch_artist=True, medianprops=medianprops)
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)
plt.legend([bplot["medians"][0], bplot["boxes"][0], bplot["boxes"][1], bplot["boxes"][2]], ["median", "A *", "Dijkstra", "Lazy Theta *"], loc="upper left", fontsize="x-small")
plt.title("Distances near ground")
plt.ylabel("Distance (m)")
plt.show()

# extract data
total_avg = [0, 0, 0] #avg of all runs
total_avg_g = [0, 0, 0] #avg ground distance of all runs
total_std = [[], [], []]
total_std_g = [[], [], []]
ground_avg = [0, 0, 0] #avg all ground-to ground
ground_avg_g = [0, 0, 0] #etc.
ground_std = [[], [], []]
ground_std_g = [[], [], []]
air_avg = [0, 0, 0]
air_avg_g = [0, 0, 0]
air_std = [[], [], []]
air_std_g =[[], [], []]
for i, algorithm in enumerate(data):
    for map in algorithm:
        groundlist = map[0]
        airlist = map[1]
        for distance in groundlist[0]:
            total_avg[i] += distance
            total_std[i].append(distance)
            ground_avg[i] += distance
            ground_std[i].append(distance)
        for g in groundlist[1]:
            total_avg_g[i] += g
            total_std_g[i].append(g)
            ground_avg_g[i] += g
            ground_std_g[i].append(g)
        for distance in airlist[0]:
            total_avg[i] += distance
            total_std[i].append(distance)
            air_avg[i] += distance
            air_std_g[i].append(distance)
        for g in airlist[1]:
            total_avg_g[i] += g
            total_std_g[i].append(g)
            air_avg_g[i] += g
            air_std_g[i].append(g)
for i, t in enumerate(total_avg_g):
    total_std_g[i] = np.std(total_std_g[i])
    total_avg_g[i] = t/n
for i, t in enumerate(total_avg):
    total_std[i] = np.std(total_std[i])
    total_avg[i] = (t/n) - total_avg_g[i]
for i, t in enumerate(ground_avg_g):
    ground_std_g[i] = np.std(ground_std_g[i])
    ground_avg_g[i] = t/gn
for i, t in enumerate(ground_avg):
    ground_std[i] = np.std(ground_std[i])
    ground_avg[i] = (t/gn) - ground_avg_g[i]
for i, t in enumerate(air_avg_g):
    air_std_g[i] = np.std(air_std_g[i])
    air_avg_g[i] = t/an
for i, t in enumerate(air_avg):
    air_std[i] = np.std(air_std[i])
    air_avg[i] = (t/an) - air_avg_g[i]

weight_counts = {
    "Near ground": np.array(total_avg_g),
    "Whole length": np.array(total_avg),
}
width = 0.5

bottom = np.zeros(3)

for boolean, weight_count in weight_counts.items():
    p = plt.bar(algorithms, weight_count, width, label=boolean, bottom=bottom)
    bottom += weight_count

plt.title("Average lengths of all paths")
plt.ylabel("Distance (m)")
plt.legend(loc="lower right")

plt.show()

x = algorithms
y = total_avg_g
e = total_std_g

plt.errorbar(x, y, e, linestyle='None', marker='s')

plt.show()

collated_dist_w_0 = []
collated_ground_w_0 = []

for i, algorithm in enumerate(data):
    a = []
    b = []
    for map in algorithm:
        for type in map:
            for distance in type[0]:
                a.append(distance)
            for grounded in type[1]:
                b.append(grounded)
    collated_dist_w_0.append(a)
    collated_ground_w_0.append(b)

x = range(0, len(collated_dist_w_0[0]))

plt.plot(x, collated_dist_w_0[0], "o", label="A *")
plt.plot(x, collated_dist_w_0[1], "o", label="Dijkstra")
plt.plot(x, collated_dist_w_0[2], "o", label="Lazy Theta *")
plt.title("Difference in path length across all runs")
plt.legend(title="Algorithms:", loc="upper right", fontsize="x-small")
plt.ylabel("Distance (m)")
plt.xlabel("Run (1-30)")
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29],["1","","","","","","7","","","","","","13","","","","","","19","","","","","","25"])
plt.show()

plt.plot(x, collated_ground_w_0[0], "o", label="A *")
plt.plot(x, collated_ground_w_0[1], "o", label="Dijkstra")
plt.plot(x, collated_ground_w_0[2], "o", label="Lazy Theta *")
plt.title("Difference in grounded path length across all runs")
plt.legend(title="Algorithms:", loc="upper right", fontsize="x-small")
plt.ylabel("Distance (m)")
plt.xlabel("Run (1-30)")
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29],["1","","","","","","7","","","","","","13","","","","","","19","","","","","","25"])
plt.show()
