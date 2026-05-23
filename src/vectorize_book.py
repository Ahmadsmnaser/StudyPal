import os
from dotenv import load_dotenv
from vectorize_script import vectorize_book_and_store_to_db, vectorize_chapters


load_dotenv()

CLASS_SUBJECT_NAME = os.getenv("CLASS_SUBJECT_NAME")

# vectorize the whole book 
vectorize_book_and_store_to_db(class_subject_name= CLASS_SUBJECT_NAME , vector_db_name="os_vector_db")

# vectorize each chapter of the book
vectorize_chapters(class_subject_name= CLASS_SUBJECT_NAME)
    