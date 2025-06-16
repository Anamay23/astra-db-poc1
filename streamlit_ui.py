import streamlit as st
from quickstart_connect import connect_to_database

# Connect to Astra DB
database = connect_to_database()
collection = database.get_collection("trialcollection1")

st.title("📚 AstraDB Book Search")

# UI Inputs
min_rating = st.slider("Minimum Rating", 0.0, 5.0, step=0.1)
min_pages = st.number_input("Minimum Number of Pages", min_value=0)
language = st.text_input("Language (e.g. English, French)")

# Dynamically extract unique genres
all_documents = collection.find(projection={"genres": True}, limit=1000)
genre_set = set()
for doc in all_documents:
    genres = doc.get("genres", [])
    genre_set.update(genres)

all_genres = sorted(genre_set)

# Display genres as buttons
st.markdown("### Filter by Genre")
cols = st.columns(4)
selected_genre = None
for i, genre in enumerate(all_genres):
    if cols[i % 4].button(genre):
        selected_genre = genre

# Search logic
query = {
    "rating": {"$gte": min_rating},
    "number_of_pages": {"$gte": min_pages},
}
if language:
    query["metadata.language"] = language
if selected_genre:
    query["genres"] = selected_genre

st.markdown("### Search and Results")
if st.button("Search"):
    # Display filters in readable form
    st.markdown("### Applied Filters")
    for key, value in query.items():
        if isinstance(value, dict):
            for op, v in value.items():
                if op == "$gte":
                    st.write(f"**{key} ≥ {v}**")
        else:
            st.write(f"**{key} = {value}**")

    # Fetch and display results
    results = collection.find(query, limit=10, sort={"rating": -1})
    st.markdown("\n\n### Results (Top 10)")
    found = False
    for doc in results:
        st.write(f"**{doc['title']}** by *{doc['author']}* — ⭐ {doc['rating']}")
        found = True

    if not found:
        st.info("No books found matching the criteria.")