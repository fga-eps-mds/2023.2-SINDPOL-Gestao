def generate_fake_user():
   
    from faker import Faker
    f = Faker()

    user = {
        'fullName': f'{f.name()}',
        'warName': f'{f.name()}',
        'registration': f'{f.random_number(digits=10)}',
        'birthDate': f'{f.date_of_birth()}',
        'rg': f'{f.random_number(digits=7)}',
        'cpf': f'{f.random_number(digits=11)}',
        'placeOfBirth': f'{f.city()}',
        'ufNatural': f'{f.state()}',
        'civilState': 'alone',
        'cep': f'{f.postcode()}',
        'address': f'{f.address()}',
        'number': '1',
        'neighborhood': 'null',
        'city': f'{f.city()}',
        'complement': 'null',
        'uf': f'{f.state()}',
        'email': f'{f.email(domain="sindpol.org.br")}',
        'cellphone': f'{f.phone_number()}',
        'phone': f'{f.phone_number()}',
        'gender': 'M',
        'motherName': f'{f.name()}',
        'fatherName': f'{f.name()}',
        'scolarity': 'Bachelor Degree',
        'religion': 'null',
        'bloodType': 'A+',
        'function': 'null',
        'actualWorkSituation': 'null',
        'admissionDate': f'{f.date_of_birth()}',
        'systemRole': 'null',
        'jobRole': 'null',
        'bodyOfLaw': 'null',
        'lotation': 'null',
        'workPost': 'null',
        'password': 'admin',
    }

    return user
