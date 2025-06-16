# Astra DB PoC – Book Collection Demo

This project is a simple proof-of-concept exploring how to use [DataStax Astra DB](https://www.datastax.com/astra) with Python and Streamlit to build a basic document-based search app.

## 🔍 What it does

- Connects to a free-tier Astra DB instance using `astrapy`
- Creates a vector-enabled collection of books
- Inserts book data from a JSON file
- Runs filters and vector-based search on the collection
- Displays results through a lightweight Streamlit UI

## 🗂️ Files in this repo

| File                      | Purpose                                                                 |
|---------------------------|-------------------------------------------------------------------------|
| `quickstart_connect.py`   | Connects to Astra DB using environment variables                        |
| `quickstart_create_connection.py` | (Optional) Separate version to manage connection setup             |
| `quickstart_insert_into_collection.py` | Inserts sample documents into the Astra DB collection           |
| `extra_files/quickstart_find.py`      | Basic script to run a few sample queries                                |
| `extra_files/find2.py`                | Extended search script with vector search, filters, and projections     |
| `streamlit_ui.py`         | Interactive web UI to filter and search books using Streamlit           |
| `sample_dataset.json`     | Sample book data used for populating the collection                     |
| `.env`                    | Contains API credentials (excluded from GitHub using `.gitignore`)      |

## 🛠️ Requirements

- Python 3.8+
- Install dependencies using:

```bash
pip install astrapy streamlit python-dotenv
```
### Run the Streamlit app

```bash
streamlit run streamlit_ui.py
```

This will launch a local server where you can try filtering books based on rating, genres, language, and more.
This is just a basic PoC!
