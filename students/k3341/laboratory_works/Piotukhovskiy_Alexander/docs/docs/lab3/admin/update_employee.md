# Обновить данные сотрудника

### Описание

Этот эндпоинт позволяет обновить информацию о сотруднике, его должности или изменить его трудовой договор.

---

### URL

`PATCH /employees/manage`

---

### Параметры запроса

Запрос принимает JSON-объект в теле запроса. Обязательным является только параметр `employee_id`.

| Параметр          | Тип данных    | Обязательный | Описание                                                                 |
|--------------------|---------------|--------------|--------------------------------------------------------------------------|
| `employee_id`      | `integer`     | Да           | ID сотрудника, данные которого необходимо обновить.                      |
| `first_name`       | `string`      | Нет          | Новое имя сотрудника.                                                    |
| `last_name`        | `string`      | Нет          | Новая фамилия сотрудника.                                                |
| `middle_name`      | `string/null` | Нет          | Новое отчество сотрудника.                                               |
| `passport_number`  | `string`      | Нет          | Новый номер паспорта сотрудника.                                         |
| `position_id`      | `integer`     | Нет          | ID новой должности сотрудника.                                           |
| `contract_type`    | `string`      | Нет          | Новый тип контракта: `FIXED_TERM`, `PERMANENT`, `CIVIL_CONTRACT`.         |
| `start_date`       | `string`      | Нет          | Новая дата начала контракта в формате `YYYY-MM-DD`.                      |
| `end_date`         | `string/null` | Нет          | Новая дата окончания контракта. Не может быть указана для `PERMANENT`.   |

---

### Пример запроса

```http
PATCH /employees/manage
Content-Type: application/json

{
    "employee_id": 10,
    "first_name": "Алексей",
    "last_name": "Смирнов",
    "position_id": 3,
    "contract_type": "PERMANENT",
    "start_date": "2024-01-15"
}
```

---

### Успешный ответ (200)

```json
{
    "id": 2,
    "contract_type": "PERMANENT",
    "employee_id": 10,
    "employee_first_name": "Алексей",
    "employee_last_name": "Смирнов",
    "employee_middle_name": null,
    "start_date": "2024-01-15",
    "end_date": null,
    "position_id": 3,
    "position_name": "Менеджер"
}
```

---

### Ошибки

#### Ошибки валидации данных (422)

Пример ответа:

```json
{
    "detail": "Активный контракт для указанного сотрудника не найден."
}
```

| Код   | Описание                                                         |
|-------|-----------------------------------------------------------------|
| 422   | Ошибки валидации данных. Например, указана некорректная дата или отсутствующий сотрудник. |

#### Сотрудник не найден (404)

Пример ответа:

```json
{
    "detail": "Сотрудник с указанным ID не найден."
}
```

---

### Примечания

- При указании новых данных для контракта (например, `position_id` или `contract_type`) текущий активный контракт сотрудника будет завершен, и будет создан новый.
- Если указаны только данные сотрудника (например, имя или паспорт), изменения вносятся только в запись сотрудника без затрагивания контрактов.
- Для контракта типа `PERMANENT` поле `end_date` должно быть пустым.
- Все даты должны быть корректными, и дата окончания не может быть раньше даты начала.