
countries = [
  {
    "ID": "1",
    "الجذر": "ا ب ت",
    "النوع": "صصص",
    "فَعَلَ": "دَخَلَ",
    "فَعُلَ": ""
  },
  {
    "ID": "2",
    "الجذر": "م ب ع",
    "النوع": "صصص",
    "فَعَلَ": "ذَهَبَ",
    "فَعُلَ": "ذَهُبَ"
  },
  {
    "ID": "3",
    "الجذر": "ه و ي",
    "النوع": "ءصص",
    "فَعَلَ": "أَكَلَ",
    "فَعُلَ": "أُكَلَ"
  }
]

import sqlite3
conn = sqlite3.connect('test.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS countries (ID INT,فَعُلَ TXT, فَعَلَ TXT,الجذر TXT,النوع TXT)")
import json

for country in countries:
   country.values()
   c.execute("insert into countries values (?, ?, ?, ?, ?)", [country['ID'],country['فَعُلَ'], country['فَعَلَ'],country['الجذر'],country['النوع']])
   conn.commit()
if 'دَخَلَ' in country.values():
    print('found ok')
else:
    print('not found')
conn.close()