input = open("input.txt")
text = input.read().splitlines()
final_list = [i.split(" ") for i in text]

win_dict = {"A": "Y", "B": "Z", "C": "X"}
draw_dict = {"A": "X", "B": "Y", "C": "Z"}
lose_dict = {"A": "Z", "B": "X", "C": "Y"}
point_dict = {"X": 1, "Y": 2, "Z": 3}
points = 0
for x in final_list:
    if draw_dict[x[0]] == x[1]:
        points += 3
    elif win_dict[x[0]] == x[1]:
        points += 6
    points += point_dict[x[1]]
print(points)

points = 0
for x in final_list:
    if x[1] == "Y":
        points += 3
        points += point_dict[draw_dict[x[0]]]
    elif x[1] == "Z":
        points += 6
        points += point_dict[win_dict[x[0]]]
    else:
        points += point_dict[lose_dict[x[0]]]

print(points)
