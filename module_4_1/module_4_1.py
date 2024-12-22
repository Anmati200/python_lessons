from fake_math import divide as div_zero
from true_math import divide as div_inf

# вывод результата, где на ноль делить нельзя
div_zero(23, 0)
div_zero(14, 2)

# вывод результата, где при делении на ноль получаем бесконечность
div_inf(15,0)
div_inf(100, 25)