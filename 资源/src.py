"""by: djdlhpjy@outlook.com"""

# imports:
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QMessageBox, QTextEdit, \
    QDialog
import pyperclip
import sys

def run():
    # window
    app = QApplication(sys.argv)
    w = QMainWindow()
    w.resize(500, 350)
    w.setMinimumSize(1279, 424)
    w.setMaximumSize(1279, 424)
    w.setWindowTitle("营销号生成器")
    w.setStyleSheet("QMainWindow{border-image:url(resources/bg.jpg)}")

    # output
    out_label = QTextEdit(w)
    out_label.setPlaceholderText(
        "　　桃子核不能吞下去是怎么回事呢？桃子核相信大家都很熟悉，但是桃子核不能吞下去\n是怎么回事呢，下面就让小编带大家一起了解吧。\n　　桃子核不能吞下去，其实就是桃核太大了，吞下去容易噎着，大家可能会很惊讶桃子\n核怎么会不能吞下去呢？但事实就是这样，小编也感到非常惊讶。\n　　这就是关于桃子核不能吞下去的事情了，大家有什么想法呢，欢迎在评论区告诉小编\n一起讨论哦！")
    out_label.setStyleSheet("background:rgba(0,0,0,0);"
                            "font-size:16pt;"
                            "color:black")
    out_label.resize(635, 245)
    out_label.move(560, 55)
    out_label.setLineWrapMode(1)

    # main_body
    main_body = QLineEdit(w)
    main_body.move(87, 84)
    main_body.resize(450, 33)
    main_body.setPlaceholderText("桃子核")
    main_body.setStyleSheet("font-size:14pt")

    # event
    event = QLineEdit(w)
    event.move(87, 158)
    event.resize(450, 33)
    event.setPlaceholderText("不能吞下去")
    event.setStyleSheet("font-size:14pt")

    # saying
    saying = QLineEdit(w)
    saying.move(87, 236)
    saying.resize(450, 33)
    saying.setPlaceholderText("桃核太大了，吞下去容易噎着")
    saying.setStyleSheet("font-size:14pt")

    error1 = QLabel(w)
    error1.setStyleSheet("border-image:url(resources/error.png)")
    error1.move(90, 120)
    error1.resize(125, 42)
    if len(main_body.text()) == 0:
        error1.hide()

    error2 = QLabel(w)
    error2.setStyleSheet("border-image:url(resources/error.png)")
    error2.move(90, 190)
    error2.resize(125, 42)
    if len(event.text()) == 0:
        error2.hide()

    error3 = QLabel(w)
    error3.setStyleSheet("border-image:url(resources/error.png);")
    error3.move(90, 268)
    error3.resize(125, 42)
    if len(saying.text()) == 0:
        error3.hide()

    def out():
        if len(main_body.text()) != 0 and len(event.text()) != 0 and len(saying.text()) != 0:
            error1.hide()
            error2.hide()
            error3.hide()
            msg = '　　' + main_body.text() + event.text() + '是怎么回事呢？' + main_body.text() + '相信大家都很熟悉，但是' + main_body.text() + event.text() + '是怎么回事呢，下面就让小编带大家一起了解吧。\n　　' + main_body.text() + event.text() + '，其实就是' + saying.text() + '，大家可能会很惊讶' + main_body.text() + '怎么会' + event.text() + '呢？但事实就是这样，小编也感到非常惊讶。\n　　这就是关于' + \
                  main_body.text() + event.text() + '的事情了，大家有什么想法呢，欢迎在评论区告诉小编一起讨论哦！'
            out_label.setText(msg)
        else:
            if len(main_body.text()) == 0:
                error1.show()
            if len(event.text()) == 0:
                error2.show()
            if len(saying.text()) == 0:
                error3.show()

    def copy():
        if len(out_label.toPlainText()) == 0:
            x = QMessageBox()
            x.information(w, "", "请先生成")
        else:
            pyperclip.copy(out_label.toPlainText())
            x = QMessageBox()
            x.information(w, "", "复制成功")

    # button1
    button = QPushButton(w)
    button.move(92, 287)
    button.resize(58, 37)
    button.setStyleSheet("background:rgba(0,0,0,0)")
    button.clicked.connect(out)

    # button2
    button2 = QPushButton(w)
    button2.move(230, 286)
    button2.resize(105, 37)
    button2.setText("复制到剪贴板")
    button2.setStyleSheet("background:rgba(0,0,0,0);"
                          "font-size:15pt;"
                          "color:white")
    button2.clicked.connect(copy)

    # end_block
    w.show()
    sys.exit(app.exec_())
