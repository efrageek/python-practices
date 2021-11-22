def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname:": "Facundo", "lastname": "Garcia"}

    super_list = [
        {"firstname:": "Facundo", "lastname": "Garcia"},
        {"firstname:": "Facundo", "lastname": "Garcia"},
        {"firstname:": "Facundo", "lastname": "Garcia"},
        {"firstname:": "Facundo", "lastname": "Garcia"},
        {"firstname:": "Facundo", "lastname": "Garcia"}
    ]

    super_dict = {
        "natural_numbers": [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
        "saludos": ["hola", "Hello", "hey"]
    }

    for key, value in super_dict.items():
        print(key, "-", value)


if __name__ == "__main__":
    run()