import PyPDF2
import json
import traceback

def read_file(file):
    if file.name.endswith('.pdf'):
        try:
            pdf_reader=PyPDF2.PdfFileReader(file)
            text=""
            for page in pdf_reader.pages:
                text+=page.extract_text()
            return text
        except Exception as e:
            raise Exception(f"Error reading Pdf file: {e}")
    elif file.name.endswith('.txt'):
        try:
            return file.read().decode('utf-8')
        except Exception as e:
            raise Exception(f"Error reading Text file: {e}")
    else:
        raise Exception("Invalid file format. Only Pdf and Txt files are supported")
    

def get_table_data(quiz_data):
    try:
        quiz=json.loads(quiz_data)
        table_data=[]
        for key, value in quiz.items():
            mcq = value["mcq"]
            options = " | ".join(
                [
                    f"{option}: {option_value}"
                    for option, option_value in value["options"].items()
                    ]
                )
            correct = value["correct"]
            table_data.append({"MCQ": mcq, "Choices": options, "Correct": correct})
        return table_data
    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False
