# Object Class for book information to be populated by Google Books API

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