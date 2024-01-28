# Инструкция по установке

## Linux:
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
