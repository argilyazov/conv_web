#### Описание системы: ####
_Гланвый экран:_ на нем присутствуют кнопки выбора формата при нажатии на которые нам предложат выбрать формат конвертации файла. 
После выбора файла нас переносит на страницу редактирования файла.
_Редактирование файла:_ на этой странице отображается состояние загруженной таблицы и состояние итоговой страницы которая будет скачана в итоге.
Что бы заполнить исходные ячейки мы можем нажимать на столбцы загруженной таблицы, 
что бы заполнить ячейки итоговой таблицы мы нажимаем на столбцы итоговой таблицы, рядом расположены кнопки очистки полей. В поле команды мы можем выбрать 1 из 3х команд, что бы исполнить команду
нужно нажать кнопку применить, после нажатия меняется итоговая таблица(разъединить-разъединяет столбец, переименовать-переименование столбца, соединить-соединяет столбцы).
Кнопка сохранить нам позволяет сохранить измененный файл в директорию на выбор. Кнопка "выбрать другой файл" переносит нас на главный экран приложения.
В выплывающем(!) списке "вид пустых ячеек" можно выбрать как будут заполняться пустые ячейки таблицы.

Базовый функционал описанный выше прмиеним ко всем видам конвертации.
При конвертации из excel-json и excel-markdown возможно копирование текста напрямую с поля "итоговый результат" не сохраняя итоговый файл.
При конвертации из excel-json в выплывающем(!) списке "вид json файла" можно выбрать формат json файла.

_Алгоритм работы:_ после загрузки файла происходит преобразование таблицы в 3 фрейма: оригинальный(отображает неизмененную таблицу),
промежуточный(хранит состояние измененных столбцов) и итоговый(отображает конечный результат и как будет выгядеть таблица в скачанном файле).


#### Места отказа системы: ####
+ 1. Попытка выполнить команду разъединить  при отсутстующих исходных ячейках или при их количестве больше одного или при количестве итоговых ячеек меньше 2х
+ 2. Попытка выполнить команду объединить при отсутстующих итоговых ячейках или при их количестве больше одного или при количестве исходных ячеек меньше 2х
+ 3. Попытка выполнить команду переименовать при отсутстующих итоговых или иходных ячейках либо при их количестве большем одного
+ 4. Поптыка загрузить слишком большой файл
+ 5. Попытка загрузить файл неподходящего расширения
+ 6. Попытка загрузить ексель файла без страниц с определенными названиями (нужный формат, исходный формат)
+ 7. Попытка загрузить файла с одинаковыми полями хедера
+ 8. Попытка загрузить файла с пустыми ячейками
+ 9. Попытка загрузить ексель файла с пустым хедером
+ 10. Попытка скачать файл и вручную указать неверное расширение

#### Ограничение системы: #### 
ограничение на загрузку файла X мб; если при загрузке выбрать не верный формат происходит краш системы;

1. Ограничить объем загружаемого файла
2. Выкидывать предупреждения с соответсвующим сообщением при местах отказа 1,2,3,5,6
