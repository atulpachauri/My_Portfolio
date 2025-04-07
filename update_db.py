import sqlite3
import sys

default_project = {
    "title": "My New Project",
    "description": "Description of my new project.",
    "url": "https://github.com/MariyaSha",
    "thumbnail": "assets/stock_prediction.png"
}

if len(sys.argv) == 5:
    new_project = {
        "title": sys.argv[1],
        "description": sys.argv[2],
        "url": sys.argv[3],
        "thumbnail": sys.argv[4]
    }
else:
    new_project = default_project

conn = sqlite3.connect('instance/portfolio.db')
c = conn.cursor()

c.execute('INSERT INTO projects (title, description, link, thumbnail) VALUES (:title, :description, :link, :thumbnail)', new_project)
conn.commit()
conn.close()

print("New project added to instance/portfolio.db!")