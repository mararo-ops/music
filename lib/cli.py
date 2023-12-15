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

def add_artwork():
    print("\nEnter artwork details:")
    artist_name = input("Artist's Name: ").strip().lower()
    year_of_making = int(input("Year of Making: "))
    unique_title = input("Unique Title: ")
    style_of_art = input("Style of Art: ")
    price = int(input("Price: "))

    artist = session.query(Artist).filter(Artist.name.ilike(artist_name)).first()
    if artist:
        new_artwork = Artwork(artist_id=artist.id, year_of_making=year_of_making, unique_title=unique_title,
                              style_of_art=style_of_art, price=price)
        session.add(new_artwork)
        session.commit()
        print(f"\nAdded artwork: {unique_title} by {artist_name}")
    else:
        print(f"\nArtist {artist_name} not found.")
