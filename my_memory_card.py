from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QButtonGroup, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox
from random import shuffle, randint

class Queee():
    def __init__(self, question, right, wrong1, wrong2, wrong3):
        self.question = question
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def show_ans():
    GroupQue.hide()
    GroupAns.show()
    butt.setText("Следующий вопрос")

def show_que():
    GroupAns.hide()
    GroupQue.show()
    butt.setText("Ответить")
    rg.setExclusive(False)
    ans1.setChecked(False)
    ans2.setChecked(False)
    ans3.setChecked(False)
    ans4.setChecked(False)
    rg.setExclusive(True)

app = QApplication([])
main = QWidget()

main.setWindowTitle('Memory Card')
main.resize(250, 200)

quelist = []

quelist.append(Queee('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'))
quelist.append(Queee('Какого цвета нет на флаге России?', 'Зелёный','Белый','Синий','Красный'))
quelist.append(Queee('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))
que = QLabel('Какой национальности не существует?')
ans1 = QRadioButton('Вар1')
ans2 = QRadioButton('Вар2')
ans3 = QRadioButton('Вар3')
ans4 = QRadioButton('Вар4')
butt = QPushButton('Ответить')

anss = [ans1, ans2, ans3, ans4]   

rg = QButtonGroup()
rg.addButton(ans1)
rg.addButton(ans2)
rg.addButton(ans3)
rg.addButton(ans4)

GroupQue = QGroupBox('Варианты')

laymain = QHBoxLayout()
lay1 = QVBoxLayout()
lay2 = QVBoxLayout()
lay1.addWidget(ans1)
lay1.addWidget(ans2)
lay2.addWidget(ans3)
lay2.addWidget(ans4)
laymain.addLayout(lay1)
laymain.addLayout(lay2)

GroupQue.setLayout(laymain)

GroupAns = QGroupBox('Результат теста')
result = QLabel('Прав ли ты?')
correct = QLabel('Ответ будет потом тут')

ansline1 = QVBoxLayout()
ansline1.addWidget(result, alignment=(Qt.AlignLeft | Qt.AlignTop))
ansline1.addWidget(correct, alignment=(Qt.AlignLeft | Qt.AlignTop))
GroupAns.setLayout(ansline1)

line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()

line1.addWidget(que, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
line2.addWidget(GroupQue)
line2.addWidget(GroupAns)



line3.addStretch(1)
line3.addWidget(butt, stretch=2)
line3.addStretch(1)

cardlay = QVBoxLayout()
cardlay.addLayout(line1, stretch=2)
cardlay.addLayout(line2, stretch=8)
cardlay.addStretch(1)
cardlay.addLayout(line3, stretch=1)
cardlay.addStretch(1)
GroupAns.hide()
cardlay.setSpacing(5)
main.setLayout(cardlay)

def ask(q: Queee):
    shuffle(anss)
    anss[0].setText(q.right)
    anss[1].setText(q.wrong1)
    anss[2].setText(q.wrong2)
    anss[3].setText(q.wrong3)
    que.setText(q.question)
    correct.setText(q.right)
    show_que()

def show_cor(res):
    result.setText(res)
    show_ans()

def checkans():
    if anss[0].isChecked():
        show_cor('Правильно!')
        main.score += 1
        print('Статистика\nВсего вопросов:', main.total, "\nПравильных ответов:", main.score)
    elif anss[1].isChecked() or anss[2].isChecked() or anss[3].isChecked():
        show_cor('Неверно!')
        print('Рейтинг:', (main.score/main.total*100), "%")

def nextque():
    main.total += 1
    print('Статистика\nВсего вопросов:', main.total, "\nПравильных ответов:", main.score)
    main.curque = randint(0, len(quelist)- 1)
    q = quelist[main.curque]
    ask(q)

def click():
    if butt.text() == 'Ответить':
        checkans()
    else:
        nextque()

main.total = 0
main.score = 0

butt.clicked.connect(click)
nextque()

main.show()
app.exec_() 
