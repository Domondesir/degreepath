entered=input("Enter the courses you have completed seperated by commas: ")
completed_list=entered.split(",")
completed=set()
for code in completed_list:
    code=code.strip().upper()
    if code!="":
        completed.add(code)

courses = [
{
    "code": "COP2500",
    "name": "Concepts in Comp. Sci",
    "prerequisites": []
},
{
    "code": "COP3223C",
    "name": "Intro to Prog. with C",
    "prerequisites": ["COP2500"]
    #or CS placement test
},
{
    "code": "CDA3103C",
    "name": "Computer Logic and Organization",
    "prerequisites": ["COP3223C"]
},
{
    "code": "COP3330",
    "name": "Object-Oriented Programming",
    "prerequisites": ["COP2500"]
},
{
    "code": "COP3502C",
    "name": "Computer Science I",
    "prerequisites": ["COP3223C", "MAC1105C"]
},
{
    "code": "COP3503C",
    "name": "Computer Science II",
    "prerequisites": ["COP3502C", "COP3330", "COT3100C"]
}
]

def get_missing_prerequisites(course, completed):
        missing=[]
        for prerequisite in course["prerequisites"]:
            if prerequisite not in completed:
                missing.append(prerequisite)
        return missing

eligible_courses=[]

for course in courses:
    if course["code"] in completed:
        continue
    missing=get_missing_prerequisites(course, completed)
    if missing==[]:
        eligible_courses.append(course)
        print(course["code"],"-",course["name"], "-> eligible: yes")
    else:
        print(course["code"],"-",course["name"], "-> eligible: no")
        print("Missing prerequisites:", missing)

print("\nCourses you can take next:")
for course in eligible_courses:
    print(course["code"],"-",course["name"])
if eligible_courses==[]:
    print("No eligible courses found.")