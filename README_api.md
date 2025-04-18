# Documentation for translation Flask API

This project provides API for translating Microsoft Word (`.docx`) documents using Argos Translate. It accepts a `.docx` file and translates its content from one language to another, preserving formatting and special elements.

## setup instruction
- go to project root directory in your terminal
- activate virtual environment and run "pip install -r requirements.txt"
- go to project root directory and run "flask run"

- run "docker-compose up --build" (if you want to run in docker)

## run testcase
- run "python test_app.py"

## API docoumentation
- Method: POST
- Endpoint : localhost:8000/translate
- Content-Type: multipart/form-data
- form-data parameters:{
    "file": .docx file,
    "source_lang": "en",
    "target_lang": "fr"
}
- Response: File download (.docx) -translated file will save to the sample_docs directory

