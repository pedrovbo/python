import requests


def consulta():
    response = requests.get('https://api.adviceslip.com/advice')
    print(response.status_code)
    print(response.json())
    # for tip in response.json():
    # print(tip['advice'])


consulta()

