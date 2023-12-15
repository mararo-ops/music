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

def delete_artwork_by_title():
    title = input("\nEnter the unique title of the artwork to delete: ")

    artwork = session.query(Artwork).filter(Artwork.unique_title.ilike(title)).first()
    if artwork:
        session.delete(artwork)
        session.commit()
        print(f"\nArtwork '{title}' deleted successfully.")
    else:
        print(f"\nArtwork '{title}' not found.")


def update_artwork():
    title = input("\nEnter the unique title of the artwork to update: ")

    artwork = session.query(Artwork).filter(Artwork.unique_title.ilike(title)).first()
    if artwork:
        print(f"\nCurrent details of '{title}':")
        print(f"Year of making: {artwork.year_of_making}")
        print(f"Style of art: {artwork.style_of_art}")
        print(f"Price: {artwork.price}")

        new_year_of_making = int(input("\nEnter new year of making (press Enter to keep current): ") or artwork.year_of_making)
        new_style_of_art = input("Enter new style of art (press Enter to keep current): ") or artwork.style_of_art
        new_price = int(input("Enter new price (press Enter to keep current): ") or artwork.price)

        artwork.year_of_making = new_year_of_making
        artwork.style_of_art = new_style_of_art
        artwork.price = new_price

        session.commit()
        print(f"\nArtwork '{title}' updated successfully.")
    else:
        print(f"\nArtwork '{title}' not found.")
