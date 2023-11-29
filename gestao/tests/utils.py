def generate_fake_user():
    from faker import Faker

    f = Faker("pt-br")
    user = {
        "name": f"{f.name()}",
        "address": f"{f.address()}",
        "neighborhood": "Gama",
        "city": f"{f.city()}",
        "state": f"{f.state()}",
        "zipcode": f"{f.postcode()}",
        "cpf": f"{f.random_number(digits=11)}",
        "rg": f"{f.random_number(digits=7)}",
        "birth_date": f"{f.date_of_birth()}",
        "place_of_birth": f"{f.city()}",
        "blood_type": "A+",
        "gender": "M",
        "father_name": f"{f.name()}",
        "mother_date": f"{f.name()}",
        "position": "null",
        "occupancy": "null",
        "admission_date": f"{f.date_of_birth()}",
        "situation": "active",
        "phone": f"{f.phone_number()}",
        "email": f'{f.email(domain="sindpol.org.br")}',
        "marital_status": "alone",
        "education": "Bachelor Degree",
        "registration": f"{f.random_number(digits=10)}",
        "role": "cop",
        "category": "null",
        "pattern": "null",
        "dispatcher": "null",
        "dispatched_date": f"{f.date_of_birth()}",
        "war_name": f"{f.name()}",
        "password": "admin",
        "rg_consignor": "SSP",
        "rg_date": f"{f.date_of_birth()}",
        "situation_obs": "null",
    }

    return user
