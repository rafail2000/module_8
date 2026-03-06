# Module_8

Для установки зависимостей в терминале необходимо набрать следующую команду:
pip install -r requirements.txt

Для миграции базы данных в терминале необходимо набрать следующую команду:
python manage.py migrate

Для наполнения базы данных в терминале необходимо набрать следующие команды:
python manage.py loaddata course_fixture.json
python manage.py loaddata lesson_fixture.json
python manage.py loaddata users_fixture.json
python manage.py loaddata groups_fixture.json
python manage.py loaddata payment_fixture.json

Пользователи:
1 - admin@example.com 
2 - moderator@example.com
Пароли:
1 - 1234
2 - 1234


#Lesson_30.1
Задание 1:
    Создал новый django проект и подключил DRF.
Задание 2:
    Создал модели пользователя, курса и урока.
Задание 3:
    Описал CRUD для модели курса и урока. 

#Lesson_30.2
Задание 1:
    Для модели курса добавлено поле вывода количества уроков с помощью - SerializerMethodField().
Задание 2:
    Добавлена новая модель Payment в приложение user. 
Задание 3:
    Для сериализатора модели курса реализовал поле вывода уроков.
Задание 4:
    Настроил фильтрацию платежей по следующим параметрам:
        менять порядок сортировки по дате оплаты,
        фильтровать по курсу или уроку,
        фильтровать по способу оплаты.

#Lesson_31
Задание 1:
    Реализован CRUD для пользователей, в том числе регистрация пользователей,
    настроен в проекте с использованием JWT-авторизации и закрыт каждый эндпоинт авторизацией. 
Задание 2:
    Создана группа "Модераторы", добавлены проверки для этой группы в курсоры.
Задание 3:
    Описал права пользователей в курсорах для владельцев и модераторов.
    
#Lesson_32.1
Задание 1:
    Реализована валидация ссылки в модели урока.
Задание 2: 
    Добавлена модель подписка с курсорм и сериализатором.
Задание 3:
    Реализована пагинация для всех курсов и уроков.
Задание 4:
    Написаны тесты для проверки моделей CRUD.

#Lesson_32.2
Задание 1:
    Настроил документацию через drf_yags.
Задание 2: 
    Подключил возможность оплаты курсов или уроков через stripe api.

#Lesson_33
Задание 1:
    Настроил проект для работы с Celery.
Задание 2: 
    Добавил отправку сообщений пользователям при обновлении их подписки.
Задание 3: 
    С помощью celery-beat реализовал фоновую задачу деактивации пользователей, если они не заходят, в течение месяца.

#Lesson_34.2
    Для запуска необходимо заполнить .env файл.
    Выполнить в терминале команду:
        docker-compose up --build

#Lesson_35_2
    Для развёртывания приложения на сервер, нужно клонировать приложение в свой репозиторий.
    1. Создать .env файл с зависимостями на основе env_sample.
    2. Заполнить следующие поля в github action:
        DEPLOY_DIR
        DOCKER_HUB_ACCESS_TOKEN
        DOCKER_HUB_USERNAME
        SECRET_KEY
        SERVER_IP
        SSH_KEY
        SSH_USER
    3. Создать свою виртуальную машину, например на yandex.cloud.
    4. Настроить виртуальную машину нужно следующими командами:

        # Add Docker's official GPG key:
        sudo apt update
        sudo apt upgrade
        sudo apt update
        sudo apt install ca-certificates curl
        sudo install -m 0755 -d /etc/apt/keyrings
        sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
        sudo chmod a+r /etc/apt/keyrings/docker.asc
        
        # Add the repository to Apt sources:

        sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
        Types: deb
        URIs: https://download.docker.com/linux/ubuntu
        Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
        Components: stable
        Signed-By: /etc/apt/keyrings/docker.asc
        EOF
        
        sudo apt update
        
        sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
        
        Проверка Docker:
        sudo docker run hello-world
        
    5. Настройка Фаервола:
        sudo ufw allow 22/tcp
        sudo ufw allow 80/tcp
        sudo ufw allow 443/tcp
        sudo ufw enable
        sudo ufw status

    6. Также нужно добавить файл .env на сервер.
        Ввести команду и заполнить данные из .env файла:
            nano ~/.env

    7. Пушить приложение на сервер.

    8. Проверять работоспособность.
        
    