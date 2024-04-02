with open("students.csv") as file:
    lines=file.readlines()
    print(len(file))
    count=0
    lines.sort()
    for line in lines:
        count=count+1
        name,house = line.rstrip().split(",")
        print(f"{name} is in {house}")
    print(count)
          