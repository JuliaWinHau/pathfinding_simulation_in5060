# Test runs setup 1
for each map, six runs, three where start and goal are both on the ground, varying goal location, and three where one of them is in the air.

Running Algorithm: AStar 
Running Algorithm: Dijkstra 
Running Algorithm: LazyThetaStar 
Running Algorithm: GBFS 

start_position for all runs (7, 7, 1)

Obstacle z heights are sliglthy randomised for long x axis maps.

# Runs map 1 - Block map, skyscraper style

- Run 1, map 1 Block map, skyscraper style long xaxis, ground start to ground target, goal_position=(62, 18, 2)
Distances
(0, 64.45997286892673)
(1, 61.14553541208295)
(2, 61.37139321651232)
(3, 69.87005768508878)
Groundeds
(0, 7.388905057061257)
(1, 61.14553541208295)
(2, 22.37139321651232)
(3, 6.65685424949238)

- Run 2, map 1 Block map, skyscraper style long xaxis, ground start to ground target, goal_position=(20, 18, 2)
Distances
(0, 23.631545744180546)
(1, 19.338288046437587)
(2, 21.54983443527075)
(3, 24.313708498984763)
Groundeds
(0, 7.388905057061257)
(1, 19.338288046437587)
(2, 12.54983443527075)
(3, 6.65685424949238)


- Run 3, map 1 Block map, skyscraper style long xaxis, ground start to ground target, goal_position=(40, 2, 1)
Distances
(0, 39.21733218180744)
(1, 36.242640687119284)
(2, 36.743138350865095)
(3, 42.970562748477136)
Groundeds
(0, 8.388905057061258)
(1, 36.242640687119284)
(2, 31.7431383508651)
(3, 7.65685424949238)


- Run 4, map 1 Block map, skyscraper style long xaxis, ground start to air target far apart, goal_position=(40, 19, 20)
Distances
(0, 46.241182771401235)
(1, 46.24118277140124)
(2, 42.44174625609426)
(3, 47.60550828100967)
Groundeds
(0, 4.242640687119286)
(1, 4.242640687119286)
(2, 5.0)
(3, 4.242640687119286)

- Run 5, map 1 Block map, skyscraper style long xaxis, ground start to air target far apart, goal_position=(60, 19, 20)
Distances
(0, 65.06960989614741)
(1, 65.06960989614741)
(2, 59.385801663559064)
(3, 67.60550828100963)
Groundeds
(0, 4.242640687119286)
(1, 5.242640687119286)
(2, 7.158910531638177)
(3, 4.242640687119286)

- Run 6, map 1 Block map, skyscraper style long xaxis, ground start to air target far apart, goal_position=(40, 3, 22)
Distances
(0, 42.969833790618125)
(1, 42.96983379061812)
(2, 39.928594925271256)
(3, 44.334159300226545)
Groundeds
(0, 4.242640687119286)
(1, 5.242640687119286)
(2, 5.565308279870936)
(3, 4.242640687119286)

# Runs map 2
- Run 1, map 2 Block map, suburban style, smaller blocks long xaxis, ground start to ground target, goal_position=(62, 18, 2)
Distances
(0, 62.79898987322333)
(1, 62.60623723886871)
(2, 60.08438096044773)
(3, 67.1920236764956)
Groundeds
(0, 8.071067811865476)
(1, 62.60623723886871)
(2, 7.557839043551982)
(3, 6.65685424949238)

- Run 2, map 2 Block map, suburban style, smaller blocks long xaxis, ground start to ground target,goal_position=(15, 18, 2)
Distances
(0, 17.509860921691395)
(1, 16.0956473593183)
(2, 16.58243374944379)
(3, 18.192023676495612)
Groundeds
(0, 7.388905057061257)
(1, 16.0956473593183)
(2, 10.25787842910703)
(3, 6.65685424949238)

- Run 3, map 2 Block map, suburban style, smaller blocks long xaxis, ground start to ground target,goal_position=(40, 2, 1)
Distances
(0, 40.38890505706125)
(1, 37.41421356237309)
(2, 38.126683181409724)
(3, 41.07106781186546)
Groundeds
(0, 7.5604779323150675)
(1, 37.41421356237309)
(2, 6.9669063302282845)
(3, 7.65685424949238)

- Run 4, map 2 Block map, suburban style, smaller blocks long xaxis, ground start to air target, goal_position=(40, 19, 20)
Distances
(0, 45.3662673822424)
(1, 45.3662673822424)
(2, 40.31768220030615)
(3, 45.3662673822424)
Groundeds
(0, 4.242640687119286)
(1, 5.242640687119286)
(2, 4.677030475578647)
(3, 4.242640687119286)

- Run 5, map 2 Block map, suburban style, smaller blocks long xaxis, ground start to air target, goal_position=(60, 19, 20)
Distances
(0, 65.36626738224241)
(1, 65.36626738224241)
(2, 58.26556711244772)
(3, 65.36626738224237)
Groundeds
(0, 4.242640687119286)
(1, 37.242640687119284)
(2, 5.188102530309008)
(3, 4.242640687119286)

- Run 6, map 2 Block map, suburban style, smaller blocks long xaxis, ground start to air target, goal_position=(40, 3, 22)
Distances
(0, 45.459243911067716)
(1, 44.287671035813894)
(2, 40.396063531138594)
(3, 44.91994573785345)
Groundeds
(0, 3.414213562373095)
(1, 4.242640687119286)
(2, 3.3166247903554)
(3, 4.242640687119286)

# Runs map 3 - Random scattered obstacles, all heights, sparse
- Run 1, map 3 Random scattered obstacles, all heights, sparse, long xaxis, ground start to ground target, goal_position=(62, 18, 2)
Distances
(0, 61.43466436361489)
(1, 59.87418643129983)
(2, 56.098128311023)
(3, 62.60623723886867)
Groundeds
(0, 7.706742302257039)
(1, 59.87418643129983)
(2, 56.098128311023)
(3, 7.292528739883945)

- Run 2, map 3 Random scattered obstacles, all heights, sparse, long xaxis, ground start to ground target, goal_position=(15, 18, 2)
Distances
(0, 16.681433796945203)
(1, 14.631545744180544)
(2, 15.239315865334774)
(3, 17.36359655174942)
Groundeds
(0, 8.024579547452822)
(1, 14.631545744180544)
(2, 14.239315865334774)
(3, 7.292528739883945)

- Run 3, map 3 Random scattered obstacles, all heights, sparse, long xaxis, ground start to ground target, goal_position=(40, 2, 1)
Distances
(0, 37.85300667219901)
(1, 35.071067811865476)
(2, 35.27273617373915)
(3, 41.170843917394784)
Groundeds
(0, 9.024579547452822)
(1, 35.071067811865476)
(2, 31.27273617373915)
(3, 8.928203230275509)

- Run 4, map 3 Random scattered obstacles, all heights, sparse, long xaxis, ground start to air target, goal_position=(40, 19, 20)
Distances
(0, 44.68410462743818)
(1, 44.68410462743818)
(2, 39.92492955535426)
(3, 45.3662673822424)
Groundeds
(0, 4.5604779323150675)
(1, 5.5604779323150675)
(2, 6.303936245582252)
(3, 4.878315177510849)

- Run 5, map 3 Random scattered obstacles, all heights, sparse, long xaxis, ground start to air target, goal_position=(60, 19, 20)
Distances
(0, 64.68410462743819)
(1, 64.68410462743819)
(2, 57.56735185849702)
(3, 65.36626738224237)
Groundeds
(0, 4.5604779323150675)
(1, 34.19615242270663)
(2, 9.089581872394266)
(3, 4.878315177510849)

- Run 6, map 3 Random scattered obstacles, all heights, sparse, long xaxis, ground start to air target, goal_position=(40, 3, 22)
Distances
(0, 42.969833790618125)
(1, 42.969833790618125)
(2, 39.319206502675)
(3, 44.72719310349883)
Groundeds
(0, 4.5604779323150675)
(1, 6.242640687119285)
(2, 5.617029500382142)
(3, 5.196152422706632)

# Runs map 4 - Random scattered obstacles, limited heights, very dense,
- Run 1, map 4, Random scattered obstacles, limited heights, very dense, long xaxis, ground start to ground targert, goal_position=(62, 18, 2)
Distances
(0, 62.116827118419096)
(1, 60.459972868926734)
(2, 56.99299219015475)
(3, 67.28427124746187)
Groundeds
(0, 7.388905057061257)
(1, 60.459972868926734)
(2, 26.00486614513275)
(3, 6.65685424949238)

- Run 2, map 4, Random scattered obstacles, limited heights, very dense, long xaxis, ground start to ground targert, goal_position=(15, 18, 2)
Distances
(0, 20.535169427003233)
(1, 16.58505747976789)
(2, 15.432220400206422)
(3, 20.631545744180546)
Groundeds
(0, 6.5604779323150675)
(1, 16.58505747976789)
(2, 8.196152422706632)
(3, 6.5604779323150675)

- Run 3, map 4, Random scattered obstacles, limited heights, very dense, long xaxis, ground start to ground targert, goal_position=(40, 2, 1)
Distances
(0, 39.2672202345721)
(1, 36.342416792648606)
(2, 36.536796308744954)
(3, 45.16671517118376)
Groundeds
(0, 8.70674230225704)
(1, 36.342416792648606)
(2, 14.454410447929238)
(3, 8.610365985079726)

- Run 4, map 4, Random scattered obstacles, limited heights, very dense, long xaxis, ground start to air targert, goal_position=(40, 19, 20)
Distances
(0, 44.684104627438174)
(1, 44.68410462743818)
(2, 39.99106525997432)
(3, 44.68410462743818)
Groundeds
(0, 4.242640687119286)
(1, 5.5604779323150675)
(2, 5.916079783099616)
(3, 4.242640687119286)

- Run 5, map 4, Random scattered obstacles, limited heights, very dense, long xaxis, ground start to air targert, goal_position=(60, 19, 20)
Distances
(0, 64.68410462743819)
(1, 64.68410462743819)
(2, 57.66722476924946)
(3, 64.68410462743815)
Groundeds
(0, 4.242640687119286)
(1, 5.242640687119286)
(2, 8.139410298049853)
(3, 4.242640687119286)

- Run 6, map 4, Random scattered obstacles, limited heights, very dense, long xaxis, ground start to air targert, goal_position=(40, 3, 22)
Distances
(0, 42.96983379061812)
(1, 42.96983379061811)
(2, 39.319206502675)
(3, 42.96983379061812)
Groundeds
(0, 4.5604779323150675)
(1, 4.242640687119286)
(2, 5.617029500382142)
(3, 4.878315177510849)

# Runs map 5 - Grid-like small blocks, short x axis
- Run 1, map 5 Grid-like small blocks, short x axis, ground start to ground goal, goal_position=(12, 18, 2)
Distances
(0, 17.388905057061258)
(1, 15.732050807568877)
(2, 16.224972160321826)
(3, 18.07106781186548)
Groundeds
(0, 7.388905057061257)
(1, 15.732050807568877)
(2, 16.224972160321826)
(3, 6.65685424949238)

- Run 2, map 5 Grid-like small blocks, short x axis, ground start to ground goal, goal_position=(4, 18, 2)
Distances
(0, 14.706742302257041)
(1, 13.146264369941973)
(2, 12.696440508742775)
(3, 15.292528739883945)
Groundeds
(0, 7.706742302257039)
(1, 13.146264369941973)
(2, 12.696440508742775)
(3, 7.292528739883944)

- Run 3, map 5 Grid-like small blocks, short x axis, ground start to ground goal, goal_position=(23, 7, 1)
Distances
(0, 19.071067811865476)
(1, 16.0)
(2, 16.0)
(3, 19.656854249492383)
Groundeds
(0, 8.071067811865476)
(1, 16.0)
(2, 16.0)
(3, 7.65685424949238)

- Run 4, map 5 Grid-like small blocks, short x axis, ground start to air goal, goal_position=(10, 19, 20)
Distances
(0, 25.656125291633366)
(1, 25.65612529163337)
(2, 23.14085239195441)
(3, 26.970562748477146)
Groundeds
(0, 3.414213562373095)
(1, 3.82842712474619)
(2, 3.3166247903554)
(3, 4.242640687119286)

- Run 5, map 5 Grid-like small blocks, short x axis, ground start to air goal, goal_position=(6, 19, 20)
Distances
(0, 24.384776310850242)
(1, 24.384776310850242)
(2, 23.404231431636596)
(3, 24.384776310850242)
Groundeds
(0, 3.414213562373095)
(1, 3.82842712474619)
(2, 3.3166247903554)
(3, 4.242640687119286)

- Run 6, map 5 Grid-like small blocks, short x axis, ground start to air goal, goal_position=(18, 3, 12)
Distances
(0, 18.192023676495612)
(1, 18.192023676495612)
(2, 16.812239960227117)
(3, 18.192023676495612)
Groundeds
(0, 4.242640687119286)
(1, 4.242640687119286)
(2, 4.242640687119285)
(3, 4.242640687119286)

----
... base targets
(62, 18, 2)
(15, 18, 2)
(40, 2, 1)
(40, 19, 20)
(60, 19, 20)
(40, 3, 22)
