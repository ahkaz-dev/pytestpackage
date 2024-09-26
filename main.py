def classify_data(data):
    # Определение критериев классификации
    sensitive = ["пароль", "пин код", "паспорт", "биометрические"]
    medium = ["gmail", "номер телефона", "mail", "rambler"]
    low = ["адрес", "ФИО", "имя", "фамилия", "отчество"]

    # Анализ данных
    if any(keyword in data for keyword in sensitive):
        return "Высокий"
    elif any(keyword in data for keyword in medium):
        return "Средний"
    elif any(keyword in data for keyword in low):
        return "Низкий"
    else:
        return "Неизвестный"

while True:
    user_input = input("Введите строку: ").lower()
    
    if user_input == "0" or user_input == "Выход".lower():
        break
    else:
        sensitivity_level = classify_data(user_input)
        print(f"Sensitivity Level: {sensitivity_level}")    