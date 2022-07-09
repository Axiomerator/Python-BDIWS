from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit

# 初始化
app = QApplication([])

# 主窗口
window = QMainWindow()
window.resize(500, 400)
window.move(100, 100)
window.setWindowTitle('薪资统计')

# 主窗口控件 文本框
textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("请输入薪资表")
textEdit.move(10,25)
textEdit.resize(300,350)

# 主窗口控件 按钮
button = QPushButton('统计', window)
button.move(380,80)

# 显示主窗口
window.show()

app.exec_()