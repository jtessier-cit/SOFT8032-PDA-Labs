def q01a():
    filename = "studentDetails.txt"
    file_obj = open(filename, 'r')


    for line in file_obj:
        print(line.rstrip("\n"))
        student_list = line.split()
        print(student_list)
        student_name = student_list[0]
        student_grade_string = student_list[1:]
        student_grade_list = [int(i) for i in student_grade_string]
        student_average = sum(student_grade_list) / len(student_grade_list)

        print(f"Name: {student_name}")
        print(f"Average: {student_average}\n")

    # close file
    file_obj.close()


def q01b():
    filename = "studentDetails.txt"
    file_obj = open(filename, 'r')

    students = {}

    for line in file_obj:
        # print(line.rstrip("\n"))
        student_list = line.split()
        # print(student_list)
        student_name = student_list[0]
        student_grade_string = student_list[1:]
        student_grade_list = [int(i) for i in student_grade_string]
        student_average = sum(student_grade_list) / len(student_grade_list)
        students[student_name] = student_average

    # close file
    file_obj.close()

    print(students)

    response = "y"
    while not response == "n":
        search_name = input("Enter the name of a student: ")
        if search_name in students:
            print(f"Student: {search_name}")
            print(f"Average: {students[search_name]}")
        else:
            print(f"Student {search_name} not found.")

        response = input("Continue y/n ? ") or 'y'


def q02a():
    def avg_passengers():
        filename = "../dataset/AirPassengers.csv"
        file_obj = open(filename, 'r')

        passengers = []
        for line in file_obj:
            # line = line.strip()
            line_list = line.strip().split(',')
            # print(line_list)
            passengers.append(int(line_list[2]))

        print(passengers)
        return(sum(passengers) / len(passengers))

    print(avg_passengers())

def q02b():

    def avg_passengers():
        filename = "../dataset/AirPassengers.csv"
        file_obj = open(filename, 'r')

        passengers = []
        for line in file_obj:
            # line = line.strip()
            line_list = line.strip().split(',')
            # print(line_list)
            passengers.append(int(line_list[2]))

        # print(passengers)
        return(sum(passengers) / len(passengers))


    def years_exceeded(limit):
        filename = "../dataset/AirPassengers.csv"
        file_obj = open(filename, 'r')

        for line in file_obj:
            line_list = line.strip().split(',')
            passengers = (int(line_list[2]))
            year = (line_list[1])
            if passengers > limit:
                print(f"Year: {year}\t Passengers: {passengers}")

    print(f"Limit: {avg_passengers()}")
    years_exceeded(avg_passengers())

def q02c():

    def get_passengers_dict():
        passengers_dict = {}

        filename = "../dataset/AirPassengers.csv"
        file_obj = open(filename, 'r')

        for line in file_obj:
            line_list = line.strip().split(',')
            passengers_year = line_list[1]
            passengers_num = int(line_list[2])
            passengers_dict[passengers_year] = passengers_num

        # print(passengers_dict)
        return(passengers_dict)


    def get_avg_passengers(pass_dict):
        return (sum(pass_dict.values()) / len(pass_dict))


    def years_exceeded(pass_dict, limit):
        for year, num in pass_dict.items():
            if num > limit:
                print(f"{year} {num}")


    pass_dict = get_passengers_dict()
    pass_avg = get_avg_passengers(pass_dict)

    years_exceeded(pass_dict, pass_avg)


def q03():
    import string

    def cleanWord(word):
        itemToDelete = list(string.punctuation)

        for item in itemToDelete:
            if item in word:
                word = word.replace(item, "")

        return word

    filename = "../dataset/novels/SherlockHolmes.txt"
    file_obj = open(filename, 'r')

    # read contents of file
    file_contents = file_obj.read()
    book_words = file_contents.split()

    # print(len(file_contents))

    upperFreq = 10
    characterLength = 10

    records = {}
    for word in book_words:
        word = cleanWord(word)
        # print(word)

        if len(word) == characterLength:
            if word in records:
                records[word] = records[word]+1
            else:
                records[word] = 1

    # print(len(records))
    for rec in records:
        if records[rec] >= upperFreq:
            print(f"{rec}\t{records[rec]}")

q03()