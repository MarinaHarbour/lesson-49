import requests
from PIL import Image, ImageFilter

# Получаем ответ от сайта

r = requests.get('https://ru.pinterest.com/#top')
print(f"Код {r.status_code} ресурс работает")

# Скачаем изображение с сайта

image = requests.get('https://i.pinimg.com/564x/aa/3d/82/aa3d8245877e59be5708fd570369a89c.jpg')
with open('new_image.jpg', 'wb') as f:
    f.write(image.content)


# Обработка изображение

image_path = 'new_image.jpg'
img = Image.open(image_path)
new_image = img.resize((500, 500)).filter(ImageFilter.BLUR)
new_image.show()




