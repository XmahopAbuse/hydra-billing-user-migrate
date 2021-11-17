# Миграция абонентов в биллинг Hydra
Т.к разработчики никак не могут доделать api, выкладываю свою версию, где часть нереализованных функций сделана oracle процедурами

## Установка
1. Ввести данные от БД в файле ```/initial_db/hydra_db.py```
2. Ввести данные от учетной записи (от кого будет производиться добавления) в файле Token.py для инициализация JWT токена
3. Скачать oracle instant client и положить в папку с скриптом
## Примеры
### Инициализация cx_Oracle
```python
import os
import cx_Oracle

dir = os.path.dirname(__file__)
INSTANT_CLIENT_PATH = dir + '/instantclient_19_10' # папка с oracle instant client будет искаться в папке со скриптами
cx_Oracle.init_oracle_client(lib_dir=INSTANT_CLIENT_PATH)
```

### Создания экземпляра БД

```python
hydra_db = hydra_db.HydraDB().connect()
```

## Создание физического лица
CreatePerson возвращает словарь с ключами "person_id" и "message". При успешном создании в person_id вернется id созданного физического лица

```python
created_person = create_person.CreatePerson(first_name="Иван",
                 second_name="Иванович",
                 last_name=person.get_person_last_name(),
                 sex_id=1138 
                 d_birth=helpers.convert_with_time(datetime), # datetime object
                 doc_serial="4200",
                 doc_number='"123123",
                 doc_date=helpers.convert_with_time(datetime), #datetime object
                 doc_authority="УФМС г. Москвы")
created_person = created_person.create()
person_id = created_person['person_id'] # вернет id созданного объекта
```

| Поле | Описание |
| ------ | ------ |
| first_name | Имя |
| second_name | Отчество |
| sex_id| Идентификатор пола, 1138 если мужской, 2138 если женский |
| d_birth | Дата рождения. Должна быть экземпляром класса datetime. Передается в функцию обработчик ```convert_with_time``` для конвертирования в строку, которую примет Гидра|
| doc_serial | Серия паспорта |
| doc_number | Номер паспорта|
|  doc_date | Дата выдачи паспорта | 
| doc_authority | Кем выдан паспорт |

## Привязка адресов к клиенту (регистрации, проживания, номер телефона)

### Привязка номера телефона
```python
phone = create_phone.CreatePhone(person_id, number)
created_phone = phone.create()
```
| Поле | Описание |
| ------ | ------ |
|  person_id | Идентификатор физического лица | 
| number | номер телефона в любом удобном формате |

### Привязка адреса проживания
```python
person_address = create_person_pass_address.CreateAddress(person_id, address, address_type = 1016)
person_address.create()
```
| Поле | Описание |
| ------ | ------ |
|  person_id | Идентификатор физического лица | 
| address | Адрес |
|address_type| 1016 - по номенклатуре тип "адрес проживания" |

### Привязка адреса регистрации
```python
person_address_pass = create_person_pass_address.CreateAddress(person_id,address, address_type = 5016)
person_address_pass.create()
```
| Поле | Описание |
| ------ | ------ |
|  person_id | Идентификатор физического лица | 
| address | Адрес |
|address_type| 5016 - по номенклатуре тип "адрес регистрации" |

## Создание абонента, привязанного к физ. лицу
CreateCustomer вернет id созданного аккаунта при успехе
```python
created_customer = create_customer.CreateCustomer(person_id,
                                                  code,
                                                  d_created)
created_customer = created_customer.create()
customer_id = created_customer['customer_id']
```

| Поле | Описание |
| ------ | ------ |
|  person_id | Идентификатор физического лица | 
| code | Код абонента (может быть логином или id из вашего старого биллинга) |
|d_created| Дата создания |

## Создание счета для абонента
```python 
created_account = create_account.CreateAccount(user_id,customer_id)
created_account = created_account.create()
account_id = created_account['account_id']
```
| Поле | Описание |
| ------ | ------ |
|  user_id | Идентификатор лицевого счета, по которому абонент будет пополнять баланс.  | 
| code | Идентификатор аккаунта |
|d_created| Дата создания |
