# Documentation for translation Flask API

This project provides API for translating Microsoft Word (`.docx`) documents using Argos Translate. It accepts a `.docx` file and translates its content from one language to another, preserving formatting and special elements.

## setup instruction
- go to project root directory in your terminal
- activate virtual environment and run
  ```bash
  pip install -r requirements.txt"
  ```
- go to project root directory and run
  ```bash
  flask run"
  ```
**If you want to run in Docker**

```bash
docker-compose up --build
```

## run testcase
**run**
```bash
 python test_app.py
```

## API documentation
### Method: POST
```http
 Endpoint: localhost:8000/translate
```
 ** Content-Type: multipart/form-data **
 ```json
 form-data parameters:{
    "file": .docx file,
    "source_lang": "en",
    "target_lang": "fr"
}
```
```json
 Response: File download (.docx) -translated file will save to the sample_docs directory
```

