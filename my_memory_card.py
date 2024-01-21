#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QButtonGroup, QGroupBox,QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox
from random import shuffle
from random import randint
class Question():
    '''содержит вопрос, правильный ответ и три непрпавильных'''
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3




app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')

question = QLabel("Какой национальности не существует?")
btn_ok = QPushButton("Ответить")
#создание виджетов главного окна
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Чулмцы')
rbtn_3 = QRadioButton('Смурфы')
rbtn_4 = QRadioButton('Алеуты')
layout_ans1 = QVBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
 
#расположение виджетов по лэйаутам
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


#панель рузльтатов
AnsGroupBox = QGroupBox('результаты теста')
lb_result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)



main_layout = QVBoxLayout()
layout1= QHBoxLayout()
layout2= QHBoxLayout()
layout3= QHBoxLayout()

layout1.addWidget(question)
layout2.addWidget(RadioGroupBox)
layout2.addWidget(AnsGroupBox)
layout3.addWidget(btn_ok)


main_layout.addLayout(layout_ans1, stretch=2)
main_layout.addLayout(layout_ans2, stretch=8)
main_layout.addStretch(1)
main_layout.addLayout(layout_ans3, stretch=1)
main_layout.addStretch(1)
main_layout.addStretch(5)

def show_result():
    '''показать панель ответов'''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText("следующий вопрос")

def show_question():
    '''показать панель вопросов'''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText('Ответить')

    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def test():
    '''временная функция, которая позволяет нажатием на кнопку вызвать по очереди
    show_result() либо show_question()'''
    if 'Ответить' == btn_ok.text():
        show_result()
    else:
        show_question()

answers = [rbtn_1, rbtn_2, rbtn_3 , rbtn_4]

def ask(q: Question):
    '''функция записывает значения вопроса и ответов в соответствующие виджеты,
    при этом варанты ответов распределяются случайным образом'''
    shuffle(answers)
    
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()



#layout_ans2.addWwidget
main_layout.addLayout(layout1)
main_layout.addLayout(layout2)
main_layout.addLayout(layout3)
main_win.setLayout(main_layout)


question_list = []
question_list.append (Question('не существует национальности', 'Смурфы', 'Аулеты', 'чулмцы', 'энцы'))
question_list.append (Question('кто первый получил 100млн. подписчиков на ютуб', 'Tseries', 'pewdiepie', 'Mr.Beast', 'cocomelon'))
question_list.append (Question('какая из легенд первая получила реликвию в apex legend', 'рейф', 'бладхаунд', 'патфайндер', 'каустик'))
question_list.append (Question('25613415 + 413513534', '1', '14356536243', '625623562', '56262632'))
question_list.append (Question('на каком языке был создан майнкрафт', 'java', 'python', 'c++', 'c#'))
question_list.append (Question('сколько рублей стоит доширак', '50', '15', '30', '25'))
question_list.append (Question('компания разработавшая fortnite', 'epicGames', 'valve','ubisoft','klei'))
question_list.append (Question('сколько ног у сороконожки(ж)', '750', '40', '100','1000'))
question_list.append (Question('вторая по популяронисти ига в epic games', 'rocket league', 'forthite', 'Genshin impact', 'GTA5'))

def next_question():
    '''задает случайный вопрос из списка'''
    main_win.total += 1
    print('Статисктика \n-Всего вопросов:', main_win.total, '\n-Правильных ответов', main_win.score)
    cur_question = randint(0, len(question_list) - 1)

    q = question_list[cur_question]
    ask(q)
    
def click_OK():
    if btn_ok.text() == 'ответить':
        check_answer()
    else:
        next_question()

def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print( main_win.score)
        print('Статистика \n-Всего вопросов', main_win.total, '\n-Правильных ответов:', main_win.score)
        print('Рейтинг:', (main_win.score/main_win.total*100), '%')
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг:', (main_win.score/main_win.total*100), '%')
#ask(q1)



btn_ok.clicked.connect(click_OK)

main_win.score = 0
main_win.total = 0
main_win.show()
app.exec_()