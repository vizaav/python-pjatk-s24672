import requests
import json
import xml.etree.ElementTree as ET


def get_random_user_data():
    url = 'https://randomuser.me/api/'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        with open('random_user_data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        root = ET.Element("randomUser")
        user = ET.SubElement(root, "user")
        for key, value in data['results'][0].items():
            ET.SubElement(user, key).text = str(value)
        tree = ET.ElementTree(root)
        tree.write('random_user_data.xml')

        print("Dane użytkownika zostały zapisane w formacie JSON i XML.")
    else:
        print("Wystąpił błąd podczas pobierania danych.")


get_random_user_data()
