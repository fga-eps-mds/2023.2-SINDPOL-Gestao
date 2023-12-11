import io
from datetime import datetime

from docx import Document
from openpyxl import Workbook
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


def generate_report_users_file(all_users_list: list, filter_list: list):
    template_data = {
        "index": [],
        "fullName": [],
        "warName": [],
        "registration": [],
        "rg": [],
        "cpf": [],
        "placeOfBirth": [],
        "ufNatural": [],
        "civilState": [],
        "cep": [],
        "address": [],
        "number": [],
        "neighborhood": [],
        "city": [],
        "complement": [],
        "uf": [],
        "email": [],
        "cellphone": [],
        "phone": [],
        "gender": [],
        "motherName": [],
        "fatherName": [],
        "scolarity": [],
        "religion": [],
        "bloodType": [],
        "actualWorkSituation": [],
        "admissionDate": [],
        "jobRole": [],
        "bodyOfLaw": [],
        "lotation": [],
        "workPost": [],
    }

    for user in all_users_list:
        template_data["index"].append(all_users_list.index(user) + 1)
        template_data["fullName"].append(user.fullName)
        template_data["warName"].append(user.warName)
        template_data["registration"].append(user.registration)
        template_data["rg"].append(user.rg)
        template_data["cpf"].append(user.cpf)
        template_data["placeOfBirth"].append(user.placeOfBirth)
        template_data["ufNatural"].append(user.ufNatural)
        template_data["civilState"].append(user.civilState)
        template_data["cep"].append(user.cep)
        template_data["address"].append(user.address)
        template_data["number"].append(user.number)
        template_data["neighborhood"].append(user.neighborhood)
        template_data["city"].append(user.city)
        template_data["complement"].append(user.complement)
        template_data["uf"].append(user.uf)
        template_data["email"].append(user.email)
        template_data["cellphone"].append(user.cellphone)
        template_data["phone"].append(user.phone)
        template_data["gender"].append(user.gender)
        template_data["motherName"].append(user.motherName)
        template_data["fatherName"].append(user.fatherName)
        template_data["scolarity"].append(user.scolarity)
        template_data["religion"].append(user.religion)
        template_data["bloodType"].append(user.bloodType)
        template_data["actualWorkSituation"].append(user.actualWorkSituation)
        template_data["admissionDate"].append(user.admissionDate)
        template_data["jobRole"].append(user.jobRole)
        template_data["bodyOfLaw"].append(user.bodyOfLaw)
        template_data["lotation"].append(user.lotation)
        template_data["workPost"].append(user.workPost)

    if len(filter_list) == 0:
        users_data = template_data
    else:
        users_data = {
            key: value for key, value in template_data.items() if key in filter_list
        }

    wb = Workbook()
    active_spreadsheet = wb.active

    columns = list(users_data.keys())
    active_spreadsheet.append(columns)

    for line in zip(*users_data.values()):
        active_spreadsheet.append(line)

    file_stream = io.BytesIO()
    wb.save(file_stream)
    file_stream.seek(0)

    return file_stream
