number_of_pizza = eval(input("Какое количество пиц желаете заказать? "))
coast__of_pizza = eval(input("Укажите стоимость пиццы: "))
subtotal = number_of_pizza * coast__of_pizza
total = subtotal + subtotal * 0.08
print("Полная стоимость $", subtotal)
print("Налог $", subtotal * 0.08)
print("Счет за пиццу с учетом налога", total, sep=" = ") 
