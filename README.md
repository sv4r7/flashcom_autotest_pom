Автотест бизнес пути интернет-магазина Flash Computers

1) В директории base в файле base_class указана локальный путь для сохранения скриншотов.

2) В директории utilities в файле utils указан локальный путь к геко-драйверу.
Нужно указать либо свой путь, либо положить геко-драйвер в директорию проекта, 
предварительно скачав ('https://github.com/mozilla/geckodriver/releases')

3) В файле notebooks_page использован js в статичных методах класса, для дублирования клика,
через execute_script, так как всроенный метод element.click() результата не дал.

4) Тест сделан с учетом специфики MacOs - для выделения текста использовалось сочетание клавиш
'COMMAND + a' - метод input_range_field в файле notebooks_page.py

5) Во время работы над тестами постоянно сталкивался с добавлением новой информации, разработчиками
или удалением информации. Локаторы часто менялись. Так же изменялась цена товара и артикулы.

Тест 1 - Покупка ноутбука - test_buy_notebook
Тест 2 - Проверка попапа - test_check_popup

log test1: 

❯ python -m pytest -s -v test_buy_notebook.py
====================================================== test session starts ============================================
collected 1 item

test_buy_notebook.py::test_buy_notebook Start Test
Current url https://flashcom.ru/
Expected Word Value - Correct Result for Main Page Test Words
Click Catalog Btn
Click Notebooks Link
Click Notebooks Filter
Current url https://flashcom.ru/market/noutbuki/
Expected Word Value - Correct Result for Notebooks Page Test Word
Input Range Field Value
Expected Element Value - Correct Result for Range Field Value
Click Manufacturer Checkbox
Expected Word Value - Correct Result for Manufacturer Test Word
Click Screen Size Checkbox
Expected Word Value - Correct Result for Screen Size Value
Click Processor Checkbox
Expected Word Value - Correct Result for Processor Value
Click Video Card Checkbox
Expected Word Value - Correct Result for Video Card Value
Click Memory Checkbox
Expected Word Value - Correct Result for Memory Value
Click Submit Btn
Current url https://flashcom.ru/market/noutbuki/Lenovo/
filter_priceTo-90000|note_diag-14|3775-Intel%20Core%20i3|1469-
Intel%20UHD%20Graphics|FILTR_OPERATIVNAYA_PAMYAT_GB-8/
Expected Url Value - Correct Result for Filtered Notebook Page Url
Expected Word Value - Correct Result for Vendor Code Value
Expected Word Value - Correct Result for Notebook Price Value
Click Add To Cart Btn
Click Cart Btn
Current url https://flashcom.ru/basket/
Expected Word Value - Correct Result for Basket Test Word Value
Expected Word Value - Correct Result for Basket Vendor Code Value
Expected Word Value - Correct Result for Basket Price Value
Expected Function Value - Correct Result for Basket Overall Price Value
Expected Function Value - Correct Result for Basket Overall Price Value - Value From Site
Click Submit Btn
Current url https://flashcom.ru/order/?CurrentStep=1
Expected Word Value - Correct Result for Ordering Test Word Value
Click Individual Radio Btn
Expected Word Value - Correct Result for Individual Radio Btn Value
Input User Name
Input User Phone
Input User Email
Click Submit Btn
Current url https://flashcom.ru/order/index.php?CurrentStep=2
Expected Word Value - Correct Result for Ordering Test Word Value
Expected Url Value - Correct Result for Ordering Page Logistics
PASSEDFinish Test


======================================================= 1 passed in 9.75s ============================================

log test2:

❯ python -m pytest -s -v test_check_popup.py
====================================================== test session starts ===========================================
collected 1 item

test_check_popup.py::test_check_popup Start Test
Current url https://flashcom.ru/
Click Main Page Login Btn
Expected Word Value - Correct Result for Login Popup Test Word
Click Popup Registration Btn
Expected Word Value - Correct Result for Registration Popup Test Word
Click Popup Login Btn
Login Popup Assertion Error
PASSEDFinish Test


======================================================= 1 passed in 6.05s ============================================