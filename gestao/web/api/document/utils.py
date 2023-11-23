import io
from datetime import datetime

from docx import Document
from python_docx_replace import docx_replace

from gestao.db.models.user import User


def generate_affiliation_file(user: User):
    input_path = "./files/affiliation_template.docx"
    now = datetime.now()
    month_switch = {
        1: "janeiro",
        2: "fevereiro",
        3: "março",
        4: "abril",
        5: "maio",
        6: "junho",
        7: "julho",
        8: "agosto",
        9: "setembro",
        10: "outubro",
        11: "novembro",
        12: "dezembro",
    }
    date_string = f"{now.day} de {month_switch.get(now.month)} de {now.year}"
    doc = Document(input_path)
    docx_replace(
        doc,
        **{
            "cpf": user.cpf[:3] + '.' + user.cpf[3:6] + '.' + user.cpf[6:9] + '-' + user.cpf[9:],
            "name": user.name,
            "date": date_string,
        },
    )

    file_stream = io.BytesIO()
    doc.save(file_stream)
    file_stream.seek(0)

    return file_stream


def convert_file(file_stream):
    import subprocess
    import os

    docx_name = "tmp_file.docx"
    pdf_name = "tmp_file.pdf"
    
    with open(docx_name, "wb") as tmp_file:
        tmp_file.write(file_stream.getvalue())
    
    subprocess.call(["libreoffice", "--headless", "--convert-to", "pdf", docx_name])

    with open(pdf_name, "rb") as file_out:
        file_content = file_out.read()
    
    os.remove(docx_name)
    os.remove(pdf_name)
    
    return io.BytesIO(file_content)
