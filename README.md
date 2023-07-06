# Resume Scanner

Easily extract important information from a resume using the power of OpeanAI functions to structure responses.

## Features

- **PDF Upload**: You can upload a PDF file to the application.
- **Text Extraction**: The application extracts the text from the uploaded PDF.
- **Information Extraction**: Extracts the most useful information from the resume.

## Usage

Upload any resume in PDF format and it will extract the most important information from the resume and display it in a structured format.

## Dependencies

The application depends on several Python libraries, including:

- `python-dotenv` for loading environment variables.
- `streamlit` for creating the application interface.
- `PyPDF2` for reading PDF files.
- `langchain` for text splitting, embeddings, vector stores, and question answering.

Please see the `requirements.txt` file for the exact versions of these dependencies.

## Installation

To install the application, first clone this repository:

```bash
git clone https://github.com/what-the-func/resume-scanner
```

Then, navigate to the project directory and install the dependencies:

```bash
cd resume-scanner
pip install -r requirements.txt
```

Finally, run the application:

```bash
streamlit run app.py
```

## License

This project is licensed under the terms of the MIT license.
