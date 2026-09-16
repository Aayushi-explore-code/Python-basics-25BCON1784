NUM_SUBJECTS = 3
NAME_INDEX = 0
NAME_WIDTH = 10
TOTAL_WIDTH = 8
AVERAGE_WIDTH = 10
GRADE_WIDTH = 7
REPORT_WIDTH = 40

students = [
    ["Rahul", 78, 88, 92],
    ["Priya", 65, 71, 69],
    ["Amit", 90, 94, 85],
    ["Sneha", 55, 60, 58],
    ["Vikram", 82, 79, 88],
]


def total_marks(student):
    """Return the sum of a student's subject marks."""
    total = 0
    for i in range(1, len(student)):
        total = total + student[i]
    return total


def average_marks(student):
    """Return the student's mean mark across all subjects."""
    return total_marks(student) / NUM_SUBJECTS


def letter_grade(average):
    """Return the letter grade for a numeric average."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def class_mean(students):
    """Return the mean of all student averages."""
    sum_of_averages = 0
    for student in students:
        sum_of_averages = sum_of_averages + average_marks(student)
    return sum_of_averages / len(students)


def count_above_class_average(students, class_average):
    """Return how many students have an average above the class average."""
    count = 0
    for student in students:
        if average_marks(student) > class_average:
            count = count + 1
    return count


def find_topper(students):
    """Return the name and average of the student with the highest average."""
    highest_average = 0
    topper_name = ""
    for student in students:
        average = average_marks(student)
        if average > highest_average:
            highest_average = average
            topper_name = student[NAME_INDEX]
    return topper_name, highest_average


print("=" * REPORT_WIDTH)
print("REPORT".center(REPORT_WIDTH))
print("=" * REPORT_WIDTH)
print(
    f"{'Name':<{NAME_WIDTH}}"
    f"{'Total':>{TOTAL_WIDTH}}"
    f"{'Average':>{AVERAGE_WIDTH}}"
    f"{'Grade':>{GRADE_WIDTH}}"
)
print("-" * REPORT_WIDTH)

for student in students:
    total = total_marks(student)
    average = average_marks(student)
    grade = letter_grade(average)
    print(
        f"{student[NAME_INDEX]:<{NAME_WIDTH}}"
        f"{total:>{TOTAL_WIDTH}}"
        f"{average:>{AVERAGE_WIDTH}.2f}"
        f"{grade:>{GRADE_WIDTH}}"
    )

mean_average = class_mean(students)
topper_name, topper_average = find_topper(students)
above_average_count = count_above_class_average(students, mean_average)

print("-" * REPORT_WIDTH)
print(f"Class average: {mean_average:.2f}")
print(f"Topper:        {topper_name} ({topper_average:.2f})")
print(f"Above average: {above_average_count}")
print("=" * REPORT_WIDTH)
