# Инструкция по установке

## Linux:
Перейдите на официальный сайт Git git-scm.com и скачайте последнюю версию установщика для Windows. Нажмите на кнопку "Download" для загрузки.
1. ```git clone git@github.com:Borcheg1/local_scraper.git```
2. ```cd local_scraper ```
3. ```python3 -m venv venv```
4. ```source venv/bin/activate```
5. ```pip install -r requirements.txt```
6. переименовать ```.env_example``` в ```.env``` и заполнить значения переменных
7. запустить **Chrome** через терминал командой ```google-chrome --remote-debugging-port=9222```
8. перейти по адресу ```www.linkedin.com``` и залогиниться
9. запустить скрипт командой ```python3 main.py```
10. следовать инструкциям скрипта

## Windows:
1. **Установка Python 3.10:**</br>
  1.1 Откройте приложение **Microsoft Store**</br>
  1.2 В поиске найдите **Python 3.10**</br>
  1.3 Нажмите **Получить**</br>
  1.4 Дождитесь загрузки и установки приложения</br>
  1.5 Откройте консоль **cmd** и введите ```python --version```, вы должны увидеть версию **Python**</br>

2. **Установка Chrome:**</br>
  2.1 Перейти по ссылке ```https://www.google.com/intl/ru_ru/chrome/```</br>
  2.2 Нажать кнопку **Скачать Chrome**</br>
  2.3 Дождитесь скачивания установщика, запуститите его и следуйте инструкциям</br>

3. **Подготовка Chrome:**</br>
  3.1 Нажмите пкм на ярлык **Chrome**</br>
  3.2 Выберите **Свойства**</br>
  3.3 Во окне **Объект** в конце строки добавьте ```--remote-debugging-port=9222 -- "%1"```</br>
  ![](https://i.ibb.co/xf3Hcj8/image2.png)</br>
  3.4 Нажмите **Применить**</br>
  3.5 Подтвердите, если будут запрашиваться права администратора</br>

4. **Подготовка приложения:**</br>
  4.1 Нажмите кнопку **<> Code** и выберите **Download ZIP**</br>
   ![](https://i.ibb.co/54Q5Y64/image3.png)</br>
  4.2 Разархивируйте в любую папку и перейдите в нее</br>
  4.3 Измените название **.env_example** на **.env**</br>
  4.4 Заполните переменные в **.env** файле</br>
  4.5 Откройте консоль **cmd**</br>
  4.6 С помощью команды **cd** перейдите в папку с проектом, например</br>
    ```cd C:\Users\Desktop\Project\local_scraper```</br>
  4.7 Выполните команду ```python -m venv venv```</br>
  4.8 Выполните команду ```venv\Scripts\activate```</br>
  4.9 Выполните команду ```pip install -r requirements.txt```</br>
  4.10 Дождитесь окончания установки зависимостей</br>
  4.11 Закройте терминал</br>

5. **Запуск приложения:**</br>
  5.1 Запустите подготовленный **Chrome**, не открывайте лишних вкладок</br>
  5.2 Перейдите по адресу ```www.linkedin.com``` и авторизуйтесь</br>
  5.3 Откройте консоль **cmd** и командой **cd** перейдите в папку с проектом, например</br>
    ```cd C:\Users\Desktop\Project\local_scraper```</br>
  5.4 Выполните команду ```python main.py```</br>
  5.5 В окне терминала следуя подсказкам введите **URL** нужной страницы **linkedin**</br>
