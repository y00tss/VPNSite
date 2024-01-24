from main.models import Proxy

'''Main is function to get proxy_id and return all data related for connection the proxy including IP, PORT, 
Username and Password In additional this function creates simulation of another user(finger changes) to random OS'''


def get_proxy_http(id: str) -> dict:
    proxy = Proxy.objects.get(pk=int(id))
    ip = proxy.ip
    port = proxy.port
    username = proxy.username
    password = proxy.password

    proxies = f'https://{username}:{password}@{ip}:{port}'

    return proxies


def get_proxy_data(id: dict) -> dict:
    proxy = Proxy.objects.get(pk=int(id))
    ip = proxy.ip
    port = proxy.port
    username = proxy.username
    password = proxy.password

    proxy_data = {
        'ip': ip,
        'port': port,
        'username': username,
        'password': password
    }
    return proxy_data
