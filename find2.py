from quickstart_connect import connect_to_database
from pprint import pprint

def main() -> None:
    db = connect_to_database()
    collection = db.get_collection("trialcollection1")

    # 1. Semantic + numeric filter: Best-rated dystopian books
    print("\n🔍 Dystopian books rated above 4.0:")
    cursor = collection.find(
        {
            "genres": "Dystopian",
            "rating": {"$gt": 4.0}
        },
        projection={"title": 1, "rating": 1, "genres": 1},
        sort={"rating": -1}
    )
    for doc in cursor:
        pprint(doc)

    # 2. Vector search: Books similar to a thrilling adventure
    print("\n🔍 Vector search: Books like a thrilling adventure in a magical forest")
    result = collection.find(
        {},
        sort={"$vectorize": "A thrilling adventure in a magical forest"},
        limit=2,
        projection={"title": 1, "summary": 1}
    )
    for doc in result:
        pprint(doc)

    # 3. Nested field filtering: Books in Spanish that are not checked out
    print("\n📚 Available books in Spanish:")
    available_spanish_books = collection.find(
        {
            "metadata.language": "Spanish",
            "is_checked_out": False
        },
        projection={"title": 1, "metadata.language": 1}
    )
    for doc in available_spanish_books:
        pprint(doc)

    # 4. Combined vector + numeric filter: Long books set in arctic
    print("\n🌨️ Vector + page filter: Arctic-themed books with > 400 pages")
    arctic_books = collection.find(
        {"number_of_pages": {"$gt": 400}},
        sort={"$vectorize": "a book set in the Arctic"},
        limit=3,
        projection={"title": 1, "author": 1, "number_of_pages": 1}
    )
    for doc in arctic_books:
        pprint(doc)

    # 5. Books that are currently checked out and due soon
    print("\n📆 Books checked out with due dates approaching:")
    checked_out = collection.find(
        {
            "is_checked_out": True,
            "due_date": {"$ne": None}
        },
        projection={"title": 1, "borrower": 1, "due_date": 1}
    )
    for doc in checked_out:
        pprint(doc)


if __name__ == "__main__":
    main()