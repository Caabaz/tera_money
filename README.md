# tera_money
<hr>
Tera online<br>
Программа для подсчета прибыли(как в среднем, так и случайной)<br> от производства драгоценных камней - изумрудов и бриллантов.<br>
Для рассчета необходимо указать текущие цены на камни на аукционе или цены,<br> по которым вы собираетесь их продавать.<br>
Так же необходимо указать сколько стамины вы собираетесь потратить,<br> что вы будете производить(конечный продукт) и какой тип прибыли вы предполагаете.<br>
Типы прибыли - "Общая" и "С перспективой".<br>
Общая подразумевает, что вы собираетесь продать все, что смогли получить от крафта.<br>
С перспективой подразумевает, что вы оставите остатки промежуточных камней для дальнейшего их продвижения.<br>
Прибыль в этом случае от промежуточных камней расчитывается как какая то часть от конечного продукта.<br>
Например, цена 1 рубина - это 1\100 от цены бриллианта.<br>
<hr>
**Пока для обоих типов прибыли необходимо вводить все цены.<br> В будущем, если будет идти расчет прибыли с перспективой,<br> ячейки цен промежуточных камней будут заблокированы**
<hr>
** Не добавлена система вывода одной случайной попытки крафта**
<hr>
** Неизвестно точное значение крита **
<hr>
class Craft - хранит в себе одну попытку крафта(количество камней, цена расходников)
<hr>
make_brilliant() - моделирует крафт бриллиантов, до упора тратит стамину.
<hr>
make_diamonds() - моделирует крафт изумрудов, до упора тратит стамину.
<hr>
summary() - в основном отвечает за число итераций для статистики и вывода информации в лог.
