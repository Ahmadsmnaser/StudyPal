import os
from dotenv import load_dotenv
from langchain_community.document_loaders import UnstructuredFileLoader, DirectoryLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


load_dotenv()

working_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(working_dir)
data_dir = f"{parent_dir}/data"
vector_db_dir = f"{working_dir}/vector_db"
chapters_vector_db_dir = f"{vector_db_dir}/chapters_vector_db"

embedding = HuggingFaceEmbeddings()
text_splitter = CharacterTextSplitter(chunk_size=2000, chunk_overlap=500)


# vectorize the whole book 
def vectorize_book_and_store_to_db(class_subject_name , vector_db_name):
    book_dir = f"{data_dir}/{class_subject_name}"
    vector_db_path = f"{vector_db_dir}/{vector_db_name}"
    loader = DirectoryLoader(path=book_dir , glob="./*.pdf" , loader_cls=UnstructuredFileLoader )
    documents = loader.load()
    text_chunks = text_splitter.split_documents(documents=documents)
    Chroma.from_documents(documents=text_chunks , embedding=embedding , persist_directory=vector_db_path)
    print(f"vectorization of {class_subject_name} and stored at {vector_db_path} is completed")
    return 0


# vectorize each chapter of the book
def vectorize_chapters(class_subject_name):
    book_dir = f"{data_dir}/{class_subject_name}"
    for chapter in os.listdir(book_dir):
        if not chapter.endswith('.pdf'):
            chapter_name = chapter[:-4]
            chapter_path = f"{book_dir}/{chapter}"
            loader = UnstructuredFileLoader(path=chapter_path)
            documents = loader.load()
            text_chunks = text_splitter.split_documents(documents=documents)
            Chroma.from_documents(documents=text_chunks , embedding=embedding , persist_directory=f"{chapters_vector_db_dir}/{chapter_name}")
            print(f"vectorization of {chapter} and stored at {chapters_vector_db_dir}/{chapter} is completed")
    return 0