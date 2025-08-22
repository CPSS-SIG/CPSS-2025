# Take the information from paper_author_information.csv and add to program

import csv

global sessions
sessions = {"Oral presentations 1": [4, 12, 22, 23],
           "Oral presentations 2": [3, 5, 13], 
           "In-Person Poster Session": [8, 14, 17, 19, 21, 25],
           "Oral presentations 3": [10, 18],  
           }
assert sum(map(len, sessions.values())) == 15



global info
info = {}
with open("paper_author_information.csv", encoding="utf-8") as f:
    r = csv.reader(f, delimiter=",", quotechar='"')
    next(r) # skip header
    for row in r:
        paper_no = int(row[0])
        info[paper_no] = (row[1], row[2]) # title, authors

# Modify lower part of program.html
with open("mainprogram.html", encoding="utf-8") as f:
    program_html = f.read()

new_program_html = ""

def add_session_info(new_program_html):
    for session in sessions:
        new_program_html += "<br/>\n\n<h2>" + session + "</h2>\n"
        if len(sessions[session]) == 0:
            new_program_html += "<i>Info on papers will be added soon.</i><br/><br/>\n\n"
        print(info)
        for paper_no in sessions[session]:
            print(paper_no)
            title = info[paper_no][0]
            authors = info[paper_no][1]
            new_program_html += title + "<br/>\n"
            new_program_html += "<i>" + authors + "</i><br/><br/>\n\n"
    return new_program_html



for row in program_html.split("\n"):
    if row != "</table>": # hack to find end of program overview table
        new_program_html += row + "\n"
    else:
        new_program_html += row + "\n\n"
        new_program_html = add_session_info(new_program_html)

with open("program.html", "w", encoding="utf-8") as f:
    f.write(new_program_html)
