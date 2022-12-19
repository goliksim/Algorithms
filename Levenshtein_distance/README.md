# Расстояние Левенштейна
**Расстояние Левенштейна**, или редакционное расстояние, — метрика cходства между двумя строковыми последовательностями. Чем больше расстояние,
тем более различны строки.</br>
</br>Итак, вычислим расстояние между двумя строками методом Вагнера — Фишера: составим матрицу D и каждый её элемент вычислим по рекуррентной формуле:</br></br>
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSudmaZRJO9iIt93BpqP3FMcDIM_taJk3Muh-o804hUidmUTtc7DrVghABIRDdfGvEAx_k&usqp=CAU?raw=true"  text-align="middle" width="400" >
</br></br>Первые три строчки рекуррентной формулы помогут нам заполнить только первый столбец и первую строку таблицы.</br>
</br>Для всех остальных ячеек мы будем пользоваться четвёртой строкой — той, что с минимумом. </br>Простыми словами, 
мы пытаемся прийти в ячейку из соседних, минимально повышая дистанцию. Именно эта часть позволяет оценить минимальное количество операций, 
чтобы превратить одно слово в другое.</br>
Заполняем таким образом матрицу до самого конца. </br></br>
<img src="https://habrastorage.org/r/w1560/getpro/habr/upload_files/a5c/779/438/a5c7794382b6437808927b6d06cda6dc.png?raw=true"  text-align="middle" width="400" >
</br></br>Расстояние Левенштейна в этой мартице — нижняя правая ячейка.
