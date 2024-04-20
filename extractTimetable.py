import re

def extract_class_schedule(text):
    schedule = []

    # Pattern for extracting class information
    pattern = r'(\w+):\s*(\d+:\d+\s*(?:to|-)\s*\d+:\d+|\d+\s*to\s*\d+)\s*([A-Z]+)\s*(\d{4})\s*\(([^)]+)\)\s*([A-Z]+[ -]\d{2}(?:,[A-Z]+[ -]\d{2})*)'

    matches = re.finditer(pattern, text)

    for match in matches:
        day = match.group(1)
        time_range = match.group(2)
        class_name = match.group(3)
        class_code = match.group(4)
        lecturer = match.group(5)
        venue = match.group(6)

        # Create a dictionary for each class and add it to the schedule list
        class_info = {
            'day': day,
            'time_range': time_range,
            'class_name': class_name,
            'class_code': class_code,
            'lecturer': lecturer,
            'venue': venue,
        }
        schedule.append(class_info)

    return schedule

timetable_text = """
Monday :7 to 10 BCT 2301 (NANCY CHEMUTAI) EG-28,10 to 1 BIT 2115 (MUTURI) ONLINE,2 to 5 BIT 2118 (NJIRU) LAB B-06
Tuesday:10 to 1 BCT 2302 (KINUTHIA) A-03
Wednesday:7 to 10 SMA 2101 (FELICIAN) EG-30,10 to 1 ICS 2203 (KINYUA) LAB E-02,2 to 5 BCT 2309 (GACHUI) LAB B-07
Thursday:8 to 10 BIT 2118 (NJIRU) A-03,10 to 12 BCT 2302 (KINUTHIA) A-03,2 to 5 BIT 2115 (MUTURI) LAB B-06
Friday:7 to 10 ICS 2105 (KARIS) A-03,10 to 1 ICS 2105 (KARIS) A-05
"""

classes = extract_class_schedule(timetable_text)
for class_info in classes:
    print(class_info)
