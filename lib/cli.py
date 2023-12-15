from models import Artist, Artwork
from database import session, create_database  

def add_artist():
    print("\nEnter artist details:")
    name = input("Name: ")
    age = int(input("Age: "))
    birthplace = input("Birthplace: ")
    style_of_work = input("Style of Work: ")

    new_artist = Artist(name=name, age=age, birthplace=birthplace, style_of_work=style_of_work)
    session.add(new_artist)
    session.commit()
    print(f"\nAdded artist: {name}")
