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
            "cpf": user.cpf,
            "name": user.fullName,
            "date": date_string,
        },
    )

    file_stream = io.BytesIO()
    doc.save(file_stream)
    file_stream.seek(0)

    return file_stream
