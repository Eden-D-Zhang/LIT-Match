import openai
import json
import requests
from flask import Flask, render_template, request, redirect, url_for
from book import Book, search_book
from api_keys import load_gbooks_key, load_openai_key

app = Flask(__name__)

gbooks_key = load_gbooks_key()
openAI_key = load_openai_key()

# Test

title = "Catching Fire"
author = "Suzanne Collins"

result = search_book(title, author, gbooks_key)

if result:
    print("Book Found:")
    print(f"Title: {result.title}")
    print(f"Authors: {', '.join(result.authors)}")
    print(f"Description: {result.description}")
    print("Image Links:")
    for key, value in result.image_links.items():
        print(f"  {key}: {value}")
else:
    print("No books found.")
