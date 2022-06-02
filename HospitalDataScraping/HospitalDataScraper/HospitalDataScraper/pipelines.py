
import sqlite3 as sq3


class HospitaldatascraperPipeline:

    def __init__(self) -> None:
        self.connection = self.create_connection()
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_connection(self):
        return sq3.connect('hospitalDoctor.db')

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE doctorinfo(doctorName TEXT, speciality TEXT, degree TEXT, doctorDetailsLink TEXT, department TEXT)
        """)

    def insert(self, items):
        self.cursor.executemany(
            """INSERT INTO doctorinfo VALUES(?,?,?,?,?)""", (items) 
        )

    def process_item(self, item, spider):

        items = list(
            zip(item['doctorName'], item['speciality'], item['degree'],
                item['doctorDetailsLink'],item['department'])
        )
        
        self.insert(items)
        self.save()
        return item

    def save(self):
        self.connection.commit()
