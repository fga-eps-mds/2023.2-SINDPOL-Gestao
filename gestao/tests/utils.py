def generate_fake_user():
   
    from faker import Faker
    f = Faker()

    user = {
        'fullName': 'joao',
        'warName': 'null',
        'registration': 'null',
        'birthDate':'2023-01-01',
        'rg': 'null',
        'cpf': 'null',
        'placeOfBirth': 'null',
        'ufNatural': 'null',
        'civilState': 'null',
        'cep': 'null',
        'address': 'null',
        'number': 'null',
        'neighborhood': 'null',
        'city': 'null',
        'complement': 'null',
        'uf':'null',
        'email': 'null',
        'cellphone': 'null',
        'phone': 'null',
        'gender': 'null',
        'motherName': 'null',
        'fatherName': 'null',
        'scolarity': 'null',
        'religion': 'null',
        'bloodType':'null',
        'function': 'null',
        'actualWorkSituation': 'null',
        'admissionDate': '2023-01-01',
        'systemRole': 'null',
        'jobRole': 'null',
        'bodyOfLaw': 'null',
        'lotation': 'null',
        'workPost': 'null',
        'password': 'null',
    }

    return user
