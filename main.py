import vk
# import subprocess

oauth_link=("https://oauth.vk.com/authorize?client_id=6223008"
"&display=page"
"&redirect_uri=https://oauth.vk.com/blank.html"
"&scope=messages,wall,notifications,offline"
"&response_type=token"
"&v=5.68")

_my_link=("https://oauth.vk.com/blank.html"
"#access_token=f1c678c565258d7d9087e2e421268c1994336196c9801d99da3ded986757f9e69096a1bb86bd9c446a3e5"
"&expires_in=0"
"&user_id=262386765")

error_example=("https://oauth.vk.com/blank.html"
"#error=access_denied"
"&error_description=The+user+or+authorization+server+denied+the+request.")

print(oauth_link)


# Что мы делаем:
# 1) Открываем в браузере ссылку и авторизуемся
# 2) Получаем токен авторизации и сохраняем его в приложении
# 3) Авторизуемся в vk с помощью токена
# 4) ???
# 5) Что-нибудь поделаем
