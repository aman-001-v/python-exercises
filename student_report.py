students = [
    {"name": "Alice", "marks": 92},
    {"name": "Bob", "marks": 67},
    {"name": "Charlie", "marks": 81},
    {"name": "David", "marks": 45},
]

marks_list = [i["name"] for i in students if i["marks"] >= 80]

marks_dict = {i["name"]:i["marks"] for i in students}

first_letter = {i["name"][0] for i in students}

avg_generator = (i["marks"] for i in students)