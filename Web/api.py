import requests

BASE_URL = 'http://127.0.0.1:8000/api/'
session = requests.Session()


def check_connection(func):
    def wrapper(*args, **kwargs):
        res_dict = {'is_ok': False,
                    'response': ''}
        try:
            headers = get_headers()
            response = func(headers=headers, *args, **kwargs)
            res_dict['response'] = response
            res_dict['is_ok'] = True
        except:
            res_dict['response'] = 'Подключение не установлено!'
        finally:
            return res_dict

    return wrapper


def get_csrf_token():
    response = session.get(f"{BASE_URL}drf-auth/login/")
    csrf_token = response.cookies.get('csrftoken')
    return csrf_token


def get_headers():
    csrf_token = session.cookies.get('csrftoken')
    headers = {
        'user-agent': 'my-app/0.0.1',
        'X-CSRFToken': csrf_token,
    }
    return headers


def authenticate(login, password):
    res_dict = {'is_ok': False,
                'response': '',
                'user': ''}
    try:
        get_csrf_token()
        headers = get_headers()
        url = f"{BASE_URL}drf-auth/login/"
        data = {
            'username': login,
            'password': password,
        }
        response = session.post(url, data=data, headers=headers)

        if response.status_code == 200:
            try:
                res_dict['response'] = response.json()
                res_dict['is_ok'] = True
                res_dict['user'] = 'employee'
            except:
                    res_dict['response'] = 'Некорректные данные!'
        else:
            res = get_all_resources('company/get_current')
            if res['is_ok']:
                if res['response'].status_code == 200:
                    res_dict['response'] = res['response'].json()
                    res_dict['is_ok'] = True
                    res_dict['user'] = 'client'
                else:
                    res_dict['response'] = 'Некорректные данные!'
            else:
                res_dict['response'] = 'Ошибка!'
    except:
        res_dict['response'] = 'Подключение не установлено!'
    finally:
        return res_dict


@check_connection
def get_all_resources(endpoint, headers):
    response = session.get(f"{BASE_URL}{endpoint}/", headers=headers)
    return response


@check_connection
def get_resource(endpoint, resource_id, headers):
    response = session.get(f"{BASE_URL}{endpoint}/{resource_id}/", headers=headers)
    return response


@check_connection
def create_resource(endpoint, data, headers):
    response = session.post(f"{BASE_URL}{endpoint}/", json=data, headers=headers)
    return response


@check_connection
def update_resource(endpoint, resource_id, data, headers):
    response = session.put(f"{BASE_URL}{endpoint}/{resource_id}/", json=data, headers=headers)
    return response


@check_connection
def delete_resource(endpoint, resource_id, headers):
    response = session.delete(f"{BASE_URL}{endpoint}/{resource_id}/", headers=headers)
    return response


@check_connection
def change_pass_resource(headers, old_password, new_password):
    response = session.put(f"{BASE_URL}change_pass/", headers=headers, data={'old_password': old_password,
                                                                             'new_password': new_password})
    return response

if __name__ == '__main__':
    print(get_all_resources('work_status'))