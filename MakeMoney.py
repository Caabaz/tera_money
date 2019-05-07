import random
import sys
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QLabel,
                             QApplication, QCheckBox, QPushButton, QComboBox, QErrorMessage, QLineEdit, QTextEdit)
from PyQt5.QtGui import (QPalette, QImage, QBrush, QFont)


class ExampleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.iteration = 1000
        self.statistic = []
        self.statistic2 = []
        self.initUI()
        self.events()

    def initUI(self):
        self.go_button = QPushButton("Расчитать")
        self.combo1 = QComboBox()
        self.combo2 = QComboBox()
        self.combo1.addItems(["Изумруды", "Бриллианты"])
        self.combo2.addItems(["Общая прибыль", "Прибыль с перспективой"])
        self.lbl_auk = QLabel("Введите стоимость, по которой будете продавать")
        self.lbl_auk.setFont(QFont("Times", 14, QFont.Bold))
        self.lbl_auk.setStyleSheet("background-color:White;")
        self.lbl_stamina = QLabel("Введите число очков произовдства, которые хотите потратить:")
        self.lbl_stamina.setFont(QFont("Times", 12, QFont.Bold))
        self.lbl_stamina.setStyleSheet("background-color:White;")
        self.lbl_r = QLabel("Рубины:")
        self.lbl_r.setFont(QFont("Times", 14, QFont.Bold))
        self.lbl_r.setStyleSheet("background-color:White;")
        self.lbl_s = QLabel("Сапфиры:")
        self.lbl_s.setFont(QFont("Times", 14, QFont.Bold))
        self.lbl_s.setStyleSheet("background-color:White;")
        self.lbl_d = QLabel("Изумруды:")
        self.lbl_d.setFont(QFont("Times", 14, QFont.Bold))
        self.lbl_d.setStyleSheet("background-color:White;")
        self.lbl_b = QLabel("Бриллианты:")
        self.lbl_b.setFont(QFont("Times", 14, QFont.Bold))
        self.lbl_b.setStyleSheet("background-color:White;")

        self.cost_r = QLineEdit("100")
        self.cost_s = QLineEdit("200")
        self.cost_d = QLineEdit("1000")
        self.cost_b = QLineEdit("10000")
        self.cost_b.setEnabled(False)
        self.have_s = QLineEdit("4030")
        self.logger = QTextEdit()
        self.logger.setFont(QFont("Times", 14))
        self.logger.setReadOnly(True)

        self.check = QCheckBox('Одно случайное измерение')
        self.check.setStyleSheet("background-color:White;")
        self.check.setChecked(not True)

        self.error_dialog = QErrorMessage()

        layout1 = QVBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()
        layout4 = QHBoxLayout()
        layout5 = QHBoxLayout()
        layout6 = QHBoxLayout()
        layout7 = QHBoxLayout()
        layout8 = QHBoxLayout()
        layout9 = QHBoxLayout()
        layout10 = QHBoxLayout()

        layout2.addWidget(self.lbl_r)
        layout2.addStretch(1)
        layout2.addWidget(self.cost_r)
        layout3.addWidget(self.lbl_s)
        layout3.addStretch(1)
        layout3.addWidget(self.cost_s)
        layout4.addWidget(self.lbl_d)
        layout4.addStretch(1)
        layout4.addWidget(self.cost_d)
        layout5.addWidget(self.lbl_b)
        layout5.addStretch(1)
        layout5.addWidget(self.cost_b)
        layout9.addWidget(self.lbl_auk)
        layout9.addStretch(1)

        layout7.addWidget(self.lbl_stamina)
        layout7.addWidget(self.have_s)
        layout8.addWidget(self.combo1)
        layout8.addWidget(self.combo2)
        layout8.addWidget(self.go_button)

        layout10.addWidget(self.check)
        layout10.addStretch(1)

        layout1.addLayout(layout8)
        layout1.addLayout(layout10)
        layout1.addLayout(layout9)
        layout1.addLayout(layout2)
        layout1.addLayout(layout3)
        layout1.addLayout(layout4)
        layout1.addLayout(layout5)
        layout1.addLayout(layout7)

        layout1.addStretch(1)

        layout6.addLayout(layout1)
        layout6.addWidget(self.logger)

        self.setLayout(layout6)
        self.setGeometry(100, 50, 1200, 500)
        #self.setWindowTitle('MoneyCalc')
        self.show()

    def events(self):
        self.go_button.clicked.connect(self.summary)
        self.combo1.activated[str].connect(self.onActivated)
        self.combo2.activated[str].connect(self.onActivated2)

    def onActivated(self):
        if self.combo1.currentIndex() == 0:
            self.cost_b.setEnabled(False)
        if self.combo1.currentIndex() == 1:
            self.cost_b.setEnabled(True)


    def onActivated2(self):
        if self.combo2.currentIndex() == 1:
            self.cost_b.setEnabled(False)
            self.cost_s.setEnabled(False)
            self.cost_r.setEnabled(False)

    def exit_prog(self):
        exit()

    def resizeEvent(self, event):
        palette = QPalette()
        img = QImage('image.jpg')
        scaled = img.scaled(self.size(), Qt.KeepAspectRatioByExpanding)
        palette.setBrush(QPalette.Window, QBrush(scaled))
        self.setPalette(palette)

    def crit(self):
        luck = random.random()
        if luck <= 0.05:
            return True
        else:
            return False

    def make_brilliant(self, exp):
        one = 1.07
        need_stamina = 0
        while need_stamina < int(self.have_s.text()):
            if need_stamina + 5 <= int(self.have_s.text()):
                need_stamina += 5
                exp.cost += 110 * one
                if self.crit():
                    exp.sap += 1
                else:
                    exp.rub += 1
            if (exp.rub >= 2) and (need_stamina + 20 <= int(self.have_s.text())):
                need_stamina += 20
                exp.cost += 20 * one
                if self.crit():
                    exp.diam += 1
                else:
                    exp.sap += 1
                exp.rub -= 2
            if (exp.sap >= 5) and (need_stamina + 85 <= int(self.have_s.text())):
                need_stamina += 85
                exp.cost += 100 * one
                if self.crit():
                    exp.diam += 5
                else:
                    exp.diam += 1
                exp.sap -= 5
            if (exp.diam >= 10) and (need_stamina + 500 <= int(self.have_s.text())):
                need_stamina += 500
                exp.cost += 1000 * one
                if self.crit():
                    exp.bri += 3
                else:
                    exp.bri += 1
                exp.diam -= 10
        return exp

    def make_diamonds(self, exp):
        one = 1.07
        need_stamina = 0
        while need_stamina < int(self.have_s.text()):
            if need_stamina + 5 <= int(self.have_s.text()):
                need_stamina += 5
                exp.cost += 110 * one
                if self.crit():
                    exp.sap += 1
                else:
                    exp.rub += 1
            if (exp.rub >= 2) and (need_stamina + 20 <= int(self.have_s.text())):
                need_stamina += 20
                exp.cost += 20 * one
                if self.crit():
                    exp.diam += 1
                else:
                    exp.sap += 1
                exp.rub -= 2
            if (exp.sap >= 5) and (need_stamina + 85 <= int(self.have_s.text())):
                need_stamina += 85
                exp.cost += 100 * one
                if self.crit():
                    exp.diam += 5
                else:
                    exp.diam += 1
                exp.sap -= 5
            if (need_stamina < int(self.have_s.text())) and (need_stamina + 5 > int(self.have_s.text())):
                break
        return exp

    def is_num(self, string):
        try:
            int(string)
            return True
        except ValueError:
            self.error_dialog.showMessage('Некорректный ввод данных')
            return False

    def summary(self):
        global money_alt, money
        self.logger.clear()
        if not (self.is_num(self.cost_r.text()) and self.is_num(self.cost_s.text()) and
                self.is_num(self.cost_b.text()) and self.is_num(self.cost_d.text()) and
                self.is_num(self.have_s.text())):
            return -1
        self.statistic = []
        self.statistic2 = []
        sum_r = 0
        sum_s = 0
        sum_d = 0
        sum_r2 = 0
        sum_s2 = 0
        sum_d2 = 0
        sum_b = 0
        sum_cost = 0
        sum_cost2 = 0
        if int(self.have_s.text()) <= 2000:
            self.iteration = 2000
        elif int(self.have_s.text()) <= 4080:
            self.iteration = 1000
        elif int(self.have_s.text()) <= 8200:
            self.iteration = 500
        else:
            self.iteration = 100

        if self.check.isChecked():
            self.iteration = 1
        for i in range(self.iteration):
            if self.combo1.currentIndex() == 1:
                self.statistic.append(self.make_brilliant(Craft()))
            if self.combo1.currentIndex() == 0:
                self.statistic2.append(self.make_diamonds(Craft()))
        for i in range(self.iteration):
            if self.combo1.currentIndex() == 1:
                sum_r += self.statistic[i].rub
                sum_s += self.statistic[i].sap
                sum_d += self.statistic[i].diam
                sum_b += self.statistic[i].bri
                sum_cost += self.statistic[i].cost
            if self.combo1.currentIndex() == 0:
                sum_r2 += self.statistic2[i].rub
                sum_s2 += self.statistic2[i].sap
                sum_d2 += self.statistic2[i].diam
                sum_cost2 += self.statistic2[i].cost
        if self.combo1.currentIndex() == 1:
            self.logger.append("Получено:")
            self.logger.append("Рубинов: " + str(round(sum_r / self.iteration, 1)))
            self.logger.append("Сапфиров: " + str(round(sum_s / self.iteration, 1)))
            self.logger.append("Изумрудов: " + str(round(sum_d / self.iteration, 1)))
            self.logger.append("Бриллиантов: " + str(round(sum_b / self.iteration, 1)))
            self.logger.append("Потрачено золота:")
            self.logger.append(str(round(sum_cost / self.iteration, 1)))
            if self.combo2.currentIndex() == 0:
                self.logger.append("Доход:")
                money = (sum_r * int(self.cost_r.text())) / self.iteration +\
                        (sum_s * int(self.cost_s.text())) / self.iteration +\
                        (sum_d * int(self.cost_d.text())) / self.iteration + \
                        (sum_b * int(self.cost_b.text())) / self.iteration
                self.logger.append(str(round(money, 1)))
            if self.combo2.currentIndex() == 1:
                self.logger.append("Доход:")
                money_alt = (sum_r * int(self.cost_b.text())) / (self.iteration * 10 * 5 * 2) + \
                            (sum_s * int(self.cost_b.text())) / (self.iteration * 10 * 5) + \
                            (sum_d * int(self.cost_b.text())) / (self.iteration * 10) + \
                            (sum_b * int(self.cost_b.text())) / self.iteration
                self.logger.append(str(round(money_alt, 1)))
            self.logger.append("Прибыль:")
            if self.combo2.currentIndex() == 0:
                self.logger.append(str(round(money - sum_cost / self.iteration, 1)))
            if self.combo2.currentIndex() == 1:
                self.logger.append(str(round(money_alt - sum_cost / self.iteration, 1)))
        if self.combo1.currentIndex() == 0:
            self.logger.append("Получено:")
            self.logger.append("Рубинов: " + str(round(sum_r2 / self.iteration, 1)))
            self.logger.append("Сапфиров: " + str(round(sum_s2 / self.iteration, 1)))
            self.logger.append("Изумрудов: " + str(round(sum_d2 / self.iteration, 1)))
            self.logger.append("Потрачено золота:")
            self.logger.append(str(round(sum_cost2 / self.iteration, 1)))
            if self.combo2.currentIndex() == 0:
                self.logger.append("Доход:")
                money = (sum_r2 * int(self.cost_r.text())) / self.iteration + \
                        (sum_s2 * int(self.cost_s.text())) / self.iteration + \
                        (sum_d2 * int(self.cost_d.text())) / self.iteration
                self.logger.append(str(round(money, 1)))
            if self.combo2.currentIndex() == 1:
                self.logger.append("Доход(более реальные условия):")
                money_alt = (sum_r2 * int(self.cost_d.text())) / (self.iteration * 5 * 2) + \
                            (sum_s2 * int(self.cost_d.text())) / (self.iteration * 5) + \
                            (sum_d2 * int(self.cost_d.text())) / self.iteration
                self.logger.append(str(round(money_alt, 1)))
            self.logger.append("Прибыль:")
            if self.combo2.currentIndex() == 0:
                self.logger.append(str(round(money - sum_cost2 / self.iteration, 1)))
            if self.combo2.currentIndex() == 1:
                self.logger.append(str(round(money_alt - sum_cost2 / self.iteration, 1)))


class Craft:
    def __init__(self, rubin=0, sapfir=0, diamond=0, brilliat=0, cost=0):
        self.rub = rubin
        self.sap = sapfir
        self.diam = diamond
        self.bri = brilliat
        self.cost = cost


def main():
    app = QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
