Представьте, что вам нужно отыскать файл в формате sql среди десятков других, при этом вы знаете некоторые части этого файла (на память или из другого источника).

Программа ожидает строку, которую будет искать (input()).
После того, как строка введена, программа ищет её во всех файлах, выводит имена найденных файлов построчно и выводит количество найденных файлов.
Программа снова ожидает ввод, но теперь поиск происходит только среди отобранных на предыдущем этапе файлов.
Программа снова ожидает ввод.
...
Выход из программы программировать не нужно. Достаточно принудительно ее останавливать, для этого можно нажать Ctrl + C. Для получения списка всех файлов используйте стандартные функции из os и os.path.
