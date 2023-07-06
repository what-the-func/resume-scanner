from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from langchain import PromptTemplate
import json

function_descriptions = [
    {
        "name": "scan_resume",
        "description": "Scans a resume and returns relevant information",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Name of the person"
                },
                "email": {
                    "type": "string",
                    "description": "Email of the person"
                },
                "phone": {
                    "type": "string",
                    "description": "Phone number of the person"
                },
                "education": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "school": {
                                "type": "string",
                                "description": "Name of the school"
                            },
                            "degree_or_certificate": {
                                "type": "string",
                                "description": "Degree or certificate"
                            },
                            "time_period": {
                                "type": "string",
                                "description": "Time period of education"
                            },
                        },
                    },
                    "description": "Education of the person",
                },
                "employment": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "company": {
                                "type": "string",
                                "description": "Name of the company"
                            },
                            "title": {
                                "type": "string",
                                "description": "Title of the person"
                            },
                            "time_period": {
                                "type": "string",
                                "description": "Time period of employment"
                            },
                        },
                    },
                    "description": "Employment history of the person",
                },
                "skills": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "description": "Skills of the person"
                    },
                },
            },
            "required": ["name", "email", "skills"]
        }
    }
]

template = """/
Scan the following resume and return the relevant details.
If the data is missing just return N/A
Resume: {resume}
"""


def main():
    load_dotenv()

    llm = ChatOpenAI(model="gpt-3.5-turbo-0613")

    st.write("# Resume Scanner")

    st.write("### Upload Your Resume")

    status = st.empty()

    file = st.file_uploader("PDF, Word Doc", type=["pdf"])

    details = st.empty()

    if file is not None:
        pdf_reader = PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        prompt = PromptTemplate.from_template(template)
        content = prompt.format(resume=text)

        response = llm(
            [HumanMessage(content=content)], functions=function_descriptions)

        data = json.loads(
            response.additional_kwargs["function_call"]["arguments"])

        with details.container():
            st.write("## Details")
            st.write(f"Name: {data['name']}")
            st.write(f"Email: {data['email']}")
            st.write(f"Phone: {data['phone']}")
            st.write("Education:")
            for education in data['education']:
                st.markdown(f"""
                    * {education['school']}
                        - {education['degree_or_certificate']}
                        - {education['time_period']}
                """)
            st.write("Employment:")
            for employment in data['employment']:
                st.markdown(f"""
                    * {employment['company']}
                        - {employment['title']}
                        - {employment['time_period']}
                """)
            st.write("Skills:")
            for skill in data['skills']:
                st.write(f" - {skill}")

        status = status.success("File Uploaded Successfully")


if __name__ == '__main__':
    main()