#import numpy as np
import matplotlib.pyplot as plt

data = [
    [ # A*
        [ # map 1
            [ # ground-to-ground
                [22.899494936611667, 20, 21, 22, 23], #lengths
                [6.65685424949238] #time on ground
            ],
            [ # air-to-ground
                [], #lengths
                [] #time on ground
            ]
        ],
        [ # map 2
            [ # ground-to-ground
                [], #lengths
                [] #time on ground
            ],
            [ # air-to-ground
                [], #lengths
                [] #time on ground
            ]
        ],
        [ # map 3
            [ # ground-to-ground
                [], #lengths
                [] #time on ground
            ],
            [ # air-to-ground
                [], #lengths
                [] #time on ground
            ]
        ]
    ],
    [ # Dijkstra
        [ # map 1
            [ # ground-to-ground
                [19.82842712474619, 20, 21, 19, 18], #lengths
                [19.82842712474619] #time on ground
            ],
            [ # air-to-ground
                [], #lengths
                [] #time on ground
            ]
        ],
        [ # map 2
            [ # ground-to-ground
                [], #lengths
                [] #time on ground
            ],
            [ # air-to-ground
                [], #lengths
                [] #time on ground
            ]
        ],
        [ # map 3
            [ # ground-to-ground
                [], #lengths
                [] #time on ground
            ],
            [ # air-to-ground
                [], #lengths
                [] #time on ground
            ]
        ]
    ],
    [ # Lazy Theta*
        [ # map 1
            [ # ground-to-ground
                [20.70820393249937, 20, 21, 21, 21], #lengths
                [6.708203932499369] #time on ground
            ],
            [ # air-to-ground
                [], #lengths
                [] #time on ground
            ]
        ],
        [ # map 2
            [ # ground-to-ground
                [], #lengths
                [] #time on ground
            ],
            [ # air-to-ground
                [], #lengths
                [] #time on ground
            ]
        ],
        [ # map 3
            [ # ground-to-ground
                [], #lengths
                [] #time on ground
            ],
            [ # air-to-ground
                [], #lengths
                [] #time on ground
            ]
        ]
    ],
    [ # GBFS
        [ # map 1
            [ # ground-to-ground
                [23.485281374238575, 23, 24, 25, 24], #lengths
                [6.242640687119285] #time on ground
            ],
            [ # air-to-ground
                [], #lengths
                [] #time on ground
            ]
        ],
        [ # map 2
            [ # ground-to-ground
                [], #lengths
                [] #time on ground
            ],
            [ # air-to-ground
                [], #lengths
                [] #time on ground
            ]
        ],
        [ # map 3
            [ # ground-to-ground
                [], #lengths
                [] #time on ground
            ],
            [ # air-to-ground
                [], #lengths
                [] #time on ground
            ]
        ]
    ]
] # Add other algorithms as needed

# Extract data
n = 1 # number of runs
gn = 1 # number of ground runs
an = 0 # number of air runs
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

algorithms = ["A*", "Dijkstra", "LazyThetaStar", "GBFS"]

plt.boxplot(collated_dist)
plt.show()

plt.boxplot(collated_ground)
plt.show()
