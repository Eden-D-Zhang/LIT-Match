# Object Class for book information to be populated by Google Books API

import requests
import json
class Book: 
    def __init__(self, id, title, authors, description, image_links):

        """
        Initialize a Book object.

        Parameters:
        - id (str): The Google Books internal ID of the book.
        - title (str): The title of the book.
        - authors (list): List of authors of the book.
        - description (str): A brief description of the book.
        - image_links (dict): Dictionary containing links to book cover images.
        """

        self.id = id
        self.title = title
        self.authors = authors
        self.description = description
        self.image_links = image_links

# Function to search Google Books API, returns first response in Book object
def search_book(title, author, gbooks_key):
    base_url = "https://www.googleapis.com/books/v1/volumes"
    query_params = {
        "q": f"{title}+inauthor:{author}",
        "maxResults": "1",
        "orderBy": "relevance",
        "printType": "books",
        "key": gbooks_key,
    }

    try:
        response = requests.get(base_url, query_params)
        # Check for error
        response.raise_for_status()

        data = response.json()
        items = data.get("items", [])

        if items:
            first_book = items[0]["volumeInfo"]
            id = items[0].get("id")
            title = first_book.get("title", "Title not available")
            authors = first_book.get("authors", ["Author not available"])
            description = first_book.get("description", "description not available")
            image_links = first_book.get("imageLinks", {})

            result = Book(id, title, authors, description, image_links)
            return result
        
        else:
            return None
        
    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        return None
    