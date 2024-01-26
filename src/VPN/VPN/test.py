

# import requests
#
# # Замените эти значения на свои данные
# proxy_username = "hwongjea"
# proxy_password = "wfxvb0auosak"
# proxy_ip = "188.74.210.21"
# proxy_port = 6100
# target_url = "https://www.youtube.com/"
#
# # Создаем объект сессии с использованием прокси
# proxy_url = f"http://{proxy_username}:{proxy_password}@{proxy_ip}:{proxy_port}"
# proxies = {
#     "http": proxy_url,
#     "https": proxy_url,
# }
#
# # Отправляем GET-запрос через прокси
# try:
#     response = requests.get(target_url, proxies=proxies)
#     response.raise_for_status()  # Проверяем, был ли успешный ответ
#     print(response.text)
# except requests.exceptions.RequestException as e:
#     print(f"Ошибка при выполнении запроса: {e}")
# _____________________________________________________________________
#     import requests
#
#     # Замените эти значения на свои данные
#     proxy_ip = "ваш_прокси_ip"
#     proxy_port = ваш_прокси_порт
#
#     target_url = "https://www.example.com"
#
#     # Создаем объект сессии с использованием прокси
#     proxies = {
#         "http": f"http://{proxy_ip}:{proxy_port}",
#         "https": f"https://{proxy_ip}:{proxy_port}",
#     }
#
#     # Отправляем GET-запрос через прокси
#     try:
#         response = requests.get(target_url, proxies=proxies)
#         response.raise_for_status()  # Проверяем, был ли успешный ответ
#         print(response.text)
#     except requests.exceptions.RequestException as e:
#         print(f"Ошибка при выполнении запроса: {e}")
#
