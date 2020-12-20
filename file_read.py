num = 50
hs = open("high_score.txt", "r")
highest_score = hs.readlines()[0]
highest_score = int(highest_score)
if int(float(highest_score)) > number:
    hs.close()
    f = open("high_score.txt", "w")
    f.write(str(highest_score))
    f.close()

print(highest_score)