def distance_sq(left, right):
    """ Returns the square of the distance between left and right. """
    return (
        ((left[0] - right[0]) ** 2) +
        ((left[1] - right[1]) ** 2)
    )

distances_red =[]
distances_green = []
distances_red_green = []

for i in range(0,82):
    green_chromson_pos = []
    with open('C:/Users/niman/Desktop/dibi/35_8gy_24h_p6/EachCell_distance/green/Results'+ str(i) + '_green.csv') as csvfile:
        green = csv.reader(csvfile, delimiter=',')
        for row in green:
            if row[0] == ' ':
                continue
            x = int(row[1])
            y = int(row[2])
            green_chromson_pos.append([x,y])

    red_chromson_pos = []
    with open('C:/Users/niman/Desktop/dibi/35_8gy_24h_p6/EachCell_distance/red/Results'+ str(i) + '_red.csv') as csvfile:
        red = csv.reader(csvfile, delimiter=',')
        for row in red:
            if row[0] == ' ':
                continue
            x = int(row[1])
            y = int(row[2])
            red_chromson_pos.append([x,y])

    green_green_distances = []
    for i in range(len(green_chromson_pos)):
        for j in range(len(green_chromson_pos)):
            if i==j:
                continue
            else:
                green_green_distances.append(distance_sq(green_chromson_pos[i],green_chromson_pos[j]))
    
    try:
        distances_green.append(statistics.median(green_green_distances))
    except statistics.StatisticsError:
        distances_green.append(0)

    red_red_distances = []
    for i in range(len(red_chromson_pos)):
        for j in range(len(red_chromson_pos)):
            if i==j:
                continue
            else:
                red_red_distances.append(distance_sq(red_chromson_pos[i],red_chromson_pos[j]))
    try:
        distances_red.append(statistics.median(red_red_distances))
    except statistics.StatisticsError:
        distances_red.append(0)

    red_green_distances = []
    for i in range(len(green_chromson_pos)):
        for j in range(len(red_chromson_pos)):
            red_green_distances.append(distance_sq(green_chromson_pos[i],red_chromson_pos[j]))
    try:
        distances_red_green.append(statistics.median(red_green_distances))
    except statistics.StatisticsError:
        distances_red_green.append(0)

distances_red_green2 = np.array(distances_red_green)
plt.title("Image : 35_8gy_24h_p6 , Red Green Distances")
plt.hist(distances_red_green, bins=np.arange(distances_red_green.min(), distances_red_green.max()+1))
plt.show()

distances_red2 = np.array(distances_red)
plt.title("Image : 35_8gy_24h_p6 , Red Red Distances")
plt.hist(distances_red_green, bins=np.arange(distances_red_green.min(), distances_red_green.max()+1))
plt.show()

distances_green2 = np.array(distances_green)
plt.title("Image : 35_8gy_24h_p6 , Green Green Distances")
plt.hist(distances_red_green, bins=np.arange(distances_red_green.min(), distances_red_green.max()+1))
plt.show()
