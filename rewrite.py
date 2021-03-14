#step 9-13
from collections import OrderedDict
glossary = OrderedDict()

glossary['Кортеж'] = 'Неизменяемый список'
glossary['Список'] = 'Набор значений разделенных запятыми'
glossary['Множество'] = 'Содержит только уникальные элементы'

for key, value in glossary.items():
    print(key + ' - ' + value)