import requests

# Отправка GET-запроса
response = requests.get('https://api.github.com')

# Проверка статуса ответа
if response.status_code == 200:
    print("Данные успешно получены:")
    print(response.json())  # Выводим данные в формате JSON
else:
    print("Ошибка при получении данных:", response.status_code)


import pandas as pd

# Чтение данных из CSV файла
df = pd.read_csv('sales_data.csv')

# Вывод первых 5 строк данных
print("Первые 5 строк данных:")
print(df.head())

# Анализ: добавим новый столбец с общей стоимостью продаж
df['Total_Sales'] = df['Quantity'] * df['Price']

# Выводим данные с новым столбцом
print("\nДанные с общей стоимостью продаж:")
print(df)

# Группировка данных по продуктам и подсчет общей суммы продаж
total_sales_by_product = df.groupby('Product')['Total_Sales'].sum().reset_index()

# Печатаем результаты группировки
print("\nОбщая сумма продаж по продуктам:")
print(total_sales_by_product)

# Находим продукт с максимальной суммой продаж
max_sales_product = total_sales_by_product.loc[total_sales_by_product['Total_Sales'].idxmax()]

print(f"\nПродукт с максимальной суммой продаж: {max_sales_product['Product']} "
      f"с суммой {max_sales_product['Total_Sales']:.2f}")



import matplotlib.pyplot as plt

# Данные для визуализации
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

# Создание столбчатой диаграммы
plt.bar(categories, values, color='blue')
plt.title('Пример столбчатой диаграммы')
plt.xlabel('Категории')
plt.ylabel('Значения')
plt.show()  # Отображение графика
