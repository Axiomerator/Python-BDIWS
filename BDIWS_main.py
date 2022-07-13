# =============================================================================
# This file contains packaged image processing instructions
# and a concise graphical user interface.
# The project is yet in early development.
# The code does not represent the final condition.
# =============================================================================

# 图像数字盲水印操作包
from BDIWS_mechanics import WaterMark

# GUI支持库
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import Qt as Qtc

# 程序图标
from PySide2.QtGui import QIcon, QPixmap

# 导入文件的支持
from PySide2.QtWidgets import QFileDialog

# 其他辅助用库
import time

# GUI窗口类
class Stats:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.RunProgramButton , self.ui.salaryTableBox
        self.ui = QUiLoader().load('./GUI_Support/BDIWS_GUI_Layout.ui')

        # 连接按钮定义
        # 关于
        self.ui.ActionAbout.triggered.connect(self.AboutMsgBox)

        # 总执行
        self.ui.pushButtonExecute.clicked.connect(self.Execute)
        # 清除所有参数
        self.ui.pushButtonClearPara.clicked.connect(self.ClearPara)

        # 当单选按钮变动时控制控件的启用与禁用
        self.ui.buttonGroupM.buttonClicked.connect(self.OperationChanges)
        self.ui.buttonGroupT.buttonClicked.connect(self.OperationChanges)

        # 原图路径浏览
        self.ui.ButtonPathOriginal.clicked.connect(self.openFile_Original)
        # 水印路径浏览
        self.ui.ButtonPathMonochrome.clicked.connect(self.openFile_Watermark)
        # 清空字符串
        self.ui.ButtonStringClear.clicked.connect(self.stringClear)
        # 粘贴字符串
        self.ui.ButtonStringPaste.clicked.connect(self.stringPaste)

        # 加密图像导出路径浏览
        self.ui.ButtonDirImg.clicked.connect(self.choosePath_Img)
        # 水印提取路径浏览
        self.ui.ButtonDirMonochrome.clicked.connect(self.choosePath_Watermark)
        # 字符串复制
        self.ui.ButtonStringCopy.clicked.connect(self.stringCopy)



    def AboutMsgBox(self):
        AboutContent = '本项目源自guofei9987的blind_watermark项目，\n' \
                       '使用PySide2进行了GUI绘制，\n' \
                       '为用户提供了方便快捷的体验。\n\n' \
                       'Alpha 0.3\n' \
                       'Designed by axiomPlaceholder 2022'

        # 新建自定义弹窗
        self.box = QMessageBox(QMessageBox.Question, '关于 Python BDIWS', AboutContent)
        # 设置图标
        self.box.setIconPixmap(QPixmap("./GUI_Support/aboutPage_icon.png"))
        # 添加按钮，可用中文
        yes = self.box.addButton('关闭', QMessageBox.YesRole)

        # 设置消息框的位置（为显示在中央，无手动设置的必要），大小无法设置
        # self.box.setGeometry(1000, 500, 0, 0)

        # 显示该问答框
        self.box.show()

    def ClearPara(self):
        self.ui.LabelPasswordWm.clear()
        self.ui.LabelPasswordImg.clear()
        self.ui.LabelWmWidth.clear()
        self.ui.LabelWmHeight.clear()
        self.ui.LabelAntiAtt_D1.clear()
        self.ui.LabelAntiAtt_D2.clear()

    # 当单选按钮变动时控制控件的启用与禁用
    def OperationChanges(self):
        if self.ui.TypeAddWatermark.isChecked() and self.ui.TypeMonochrome.isChecked():
            # self.ui.LabelPathOriginal.setEnabled(True)
            # self.ui.ButtonPathOriginal.setEnabled(True)
            self.ui.LabelPathMonochrome.setEnabled(True)
            self.ui.ButtonPathMonochrome.setEnabled(True)
            self.ui.LabelStringOriginal.setEnabled(False)
            self.ui.ButtonStringClear.setEnabled(False)
            self.ui.ButtonStringPaste.setEnabled(False)

            self.ui.LabelDirImgOut.setEnabled(True)
            self.ui.ButtonDirImg.setEnabled(True)
            self.ui.LabelDirMonochrome.setEnabled(False)
            self.ui.ButtonDirMonochrome.setEnabled(False)
            self.ui.LabelStringExtract.setEnabled(False)
            self.ui.ButtonStringCopy.setEnabled(False)

            # 执行区域的按钮控制
            self.ui.LabelWmWidth.setEnabled(False)
            self.ui.LabelWmHeight.setEnabled(False)
            self.ui.LabelWmWidth.setPlaceholderText('被提取水印的宽')
            self.ui.LabelWmHeight.setPlaceholderText('被提取水印的高')

        elif self.ui.TypeAddWatermark.isChecked() and self.ui.TypeString.isChecked():
            # self.ui.LabelPathOriginal.setEnabled(True)
            # self.ui.ButtonPathOriginal.setEnabled(True)
            self.ui.LabelPathMonochrome.setEnabled(False)
            self.ui.ButtonPathMonochrome.setEnabled(False)
            self.ui.LabelStringOriginal.setEnabled(True)
            self.ui.ButtonStringClear.setEnabled(True)
            self.ui.ButtonStringPaste.setEnabled(True)

            self.ui.LabelDirImgOut.setEnabled(True)
            self.ui.ButtonDirImg.setEnabled(True)
            self.ui.LabelDirMonochrome.setEnabled(False)
            self.ui.ButtonDirMonochrome.setEnabled(False)
            self.ui.LabelStringExtract.setEnabled(False)
            self.ui.ButtonStringCopy.setEnabled(False)

            # 执行区域的按钮控制
            self.ui.LabelWmWidth.setEnabled(False)
            self.ui.LabelWmHeight.setEnabled(False)
            self.ui.LabelWmWidth.setPlaceholderText('被提取水印的宽')
            self.ui.LabelWmHeight.setPlaceholderText('被提取水印的高')

        elif self.ui.TypeExtractWatermark.isChecked() and self.ui.TypeMonochrome.isChecked():
            # self.ui.LabelPathOriginal.setEnabled(True)
            # self.ui.ButtonPathOriginal.setEnabled(True)
            self.ui.LabelPathMonochrome.setEnabled(False)
            self.ui.ButtonPathMonochrome.setEnabled(False)
            self.ui.LabelStringOriginal.setEnabled(False)
            self.ui.ButtonStringClear.setEnabled(False)
            self.ui.ButtonStringPaste.setEnabled(False)

            self.ui.LabelDirImgOut.setEnabled(False)
            self.ui.ButtonDirImg.setEnabled(False)
            self.ui.LabelDirMonochrome.setEnabled(True)
            self.ui.ButtonDirMonochrome.setEnabled(True)
            self.ui.LabelStringExtract.setEnabled(False)
            self.ui.ButtonStringCopy.setEnabled(False)

            # 执行区域的按钮控制
            self.ui.LabelWmWidth.setEnabled(True)
            self.ui.LabelWmHeight.setEnabled(True)
            self.ui.LabelWmWidth.setPlaceholderText('被提取水印的宽')
            self.ui.LabelWmHeight.setPlaceholderText('被提取水印的高')

        elif self.ui.TypeExtractWatermark.isChecked() and self.ui.TypeString.isChecked():
            # self.ui.LabelPathOriginal.setEnabled(True)
            # self.ui.ButtonPathOriginal.setEnabled(True)
            self.ui.LabelPathMonochrome.setEnabled(False)
            self.ui.ButtonPathMonochrome.setEnabled(False)
            self.ui.LabelStringOriginal.setEnabled(False)
            self.ui.ButtonStringClear.setEnabled(False)
            self.ui.ButtonStringPaste.setEnabled(False)

            self.ui.LabelDirImgOut.setEnabled(False)
            self.ui.ButtonDirImg.setEnabled(False)
            self.ui.LabelDirMonochrome.setEnabled(False)
            self.ui.ButtonDirMonochrome.setEnabled(False)
            self.ui.LabelStringExtract.setEnabled(True)
            self.ui.ButtonStringCopy.setEnabled(True)

            # 执行区域的按钮控制
            self.ui.LabelWmWidth.setEnabled(True)
            self.ui.LabelWmHeight.setEnabled(False)
            self.ui.LabelWmWidth.setPlaceholderText('字符串长度')
            self.ui.LabelWmHeight.setPlaceholderText('')


    def Execute(self):
        self.ui.InfoScreen.append('')
        timeLabel = '[ ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ' ]'
        self.ui.InfoScreen.append(timeLabel)

        self.ui.InfoScreen.append('程序已启动……')

        # 清空图片预览窗的内容
        self.ui.GraphOriginal.setText('[N/A]')
        self.ui.GraphWatermark.setText('[N/A]')
        self.ui.GraphProcessed.setText('[N/A]')

        if self.ui.TypeAddWatermark.isChecked(): # 水印添加模式
            if self.ui.TypeMonochrome.isChecked(): # 黑白图像水印
                self.ui.InfoScreen.append('工作模式：添加 - 黑白图像')

                # 如果待处理图像路径为空
                if self.ui.LabelPathOriginal.toPlainText() == '':
                    # 如果路径为空：
                    self.ui.GraphOriginal.setText('[错误：路径无效]')
                    self.ui.InfoScreen.append('错误：图片路径无效！')
                    return

                # 如果待加入的水印路径为空
                if self.ui.LabelPathMonochrome.toPlainText() == '':
                    # 如果路径为空：
                    self.ui.GraphWatermark.setText('[错误：路径无效]')
                    self.ui.InfoScreen.append('错误：图片路径无效！')
                    return

                # 如果保存路径为空
                if self.ui.LabelDirImgOut.toPlainText() == '':
                    # 如果路径为空：
                    self.ui.GraphProcessed.setText('[错误：路径无效]')
                    self.ui.InfoScreen.append('错误：保存路径无效！')
                    return

                # 如果密码不合法
                if (not self.ui.LabelPasswordWm.toPlainText().isdigit()) or (not self.ui.LabelPasswordImg.toPlainText().isdigit()):
                    self.ui.InfoScreen.append('错误：密码未填写或不合法！')
                    return

                # 展示原图像
                targetSize = self.ui.GraphOriginal.size()
                pixmap = QPixmap(self.ui.LabelPathOriginal.toPlainText()).scaled(targetSize, aspectMode=Qtc.AspectRatioMode.KeepAspectRatio)
                self.ui.GraphOriginal.setPixmap(pixmap)
                self.ui.GraphOriginal.repaint()

                # 展示待添加的水印
                targetSize = self.ui.GraphWatermark.size()
                pixmap = QPixmap(self.ui.LabelPathMonochrome.toPlainText()).scaled(targetSize, aspectMode=Qtc.AspectRatioMode.KeepAspectRatio)
                self.ui.GraphWatermark.setPixmap(pixmap)
                self.ui.GraphWatermark.repaint()

                # 进行水印加密
                targetFile = self.ui.LabelDirImgOut.toPlainText()+'/watermarked_img.png'
                robustness_inputPara_1 = self.ui.LabelAntiAtt_D1.toPlainText()
                robustness_inputPara_2 = self.ui.LabelAntiAtt_D2.toPlainText()
                # 若留空则以默认值进行
                if not robustness_inputPara_1.isdigit():
                    robustness_actual_1 = 36
                else:
                    robustness_actual_1 = eval(robustness_inputPara_1)
                if not robustness_inputPara_2.isdigit():
                    robustness_actual_2 = 20
                else:
                    robustness_actual_2 = eval(robustness_inputPara_2)

                eg1 = WaterMark(password_wm=eval(self.ui.LabelPasswordWm.toPlainText()), password_img=eval(self.ui.LabelPasswordImg.toPlainText()),
                                d1=robustness_actual_1, d2=robustness_actual_2)
                eg1.read_img(self.ui.LabelPathOriginal.toPlainText())  # 读取原图
                eg1.read_wm(self.ui.LabelPathMonochrome.toPlainText())  # 读取水印
                eg1.embed(targetFile)  # 打上盲水印并输出
                # 展示加密好的图像
                targetSize = self.ui.GraphProcessed.size()
                pixmap = QPixmap(targetFile).scaled(targetSize, aspectMode=Qtc.AspectRatioMode.KeepAspectRatio)
                self.ui.GraphProcessed.setPixmap(pixmap)
                self.ui.GraphProcessed.repaint()
                self.ui.InfoScreen.append('水印加密已完成！')

            if self.ui.TypeString.isChecked(): # 字符串水印
                self.ui.InfoScreen.append('工作模式：添加 - 字符串')

                # 如果待处理图像路径为空
                if self.ui.LabelPathOriginal.toPlainText() == '':
                    # 如果路径为空：
                    self.ui.GraphOriginal.setText('[错误：路径无效]')
                    self.ui.InfoScreen.append('错误：图片路径无效！')
                    return

                # 如果水印为空
                if self.ui.LabelStringOriginal.toPlainText() == '':
                    # 如果字符串为空：
                    self.ui.InfoScreen.append('错误：字符串内容无效！')
                    return

                # 如果保存路径为空
                if self.ui.LabelDirImgOut.toPlainText() == '':
                    # 如果路径为空：
                    self.ui.GraphProcessed.setText('[错误：路径无效]')
                    self.ui.InfoScreen.append('错误：保存路径无效！')
                    return

                # 如果密码不合法
                if (not self.ui.LabelPasswordWm.toPlainText().isdigit()) or (
                not self.ui.LabelPasswordImg.toPlainText().isdigit()):
                    self.ui.InfoScreen.append('错误：密码未填写或不合法！')
                    return

                # 展示原图像
                targetSize = self.ui.GraphOriginal.size()
                pixmap = QPixmap(self.ui.LabelPathOriginal.toPlainText()).scaled(targetSize, aspectMode=Qtc.AspectRatioMode.KeepAspectRatio)
                self.ui.GraphOriginal.setPixmap(pixmap)
                self.ui.GraphOriginal.repaint()

                # 进行水印加密
                targetFile = self.ui.LabelDirImgOut.toPlainText() + '/watermarked_img.png'
                robustness_inputPara_1 = self.ui.LabelAntiAtt_D1.toPlainText()
                robustness_inputPara_2 = self.ui.LabelAntiAtt_D2.toPlainText()
                # 若留空则以默认值进行
                if not robustness_inputPara_1.isdigit():
                    robustness_actual_1 = 36
                else:
                    robustness_actual_1 = eval(robustness_inputPara_1)
                if not robustness_inputPara_2.isdigit():
                    robustness_actual_2 = 20
                else:
                    robustness_actual_2 = eval(robustness_inputPara_2)

                eg1 = WaterMark(password_wm=eval(self.ui.LabelPasswordWm.toPlainText()),
                                password_img=eval(self.ui.LabelPasswordImg.toPlainText()),
                                d1=robustness_actual_1, d2=robustness_actual_2)
                eg1.read_img(self.ui.LabelPathOriginal.toPlainText())  # 读取原图
                wm = self.ui.LabelStringOriginal.toPlainText() # 读取水印
                eg1.read_wm(wm, mode='str') # 读取水印
                eg1.embed(targetFile) # 打上盲水印并输出
                wm_actual_length = len(eg1.wm_bit)
                # 展示加密好的图像
                targetSize = self.ui.GraphProcessed.size()
                pixmap = QPixmap(targetFile).scaled(targetSize, aspectMode=Qtc.AspectRatioMode.KeepAspectRatio)
                self.ui.GraphProcessed.setPixmap(pixmap)
                self.ui.GraphProcessed.repaint()
                self.ui.InfoScreen.append('水印加密已完成！')
                self.ui.InfoScreen.append('水印信息长度为 {placeHolder}'.format(placeHolder=wm_actual_length))
            else:
                self.ui.InfoScreen.append("工作模式错误！")


        elif self.ui.TypeExtractWatermark.isChecked(): # 水印提取模式
            if self.ui.TypeMonochrome.isChecked():
                self.ui.InfoScreen.append('工作模式：提取 - 黑白图像')

                # 如果待处理图像路径为空
                if self.ui.LabelPathOriginal.toPlainText() == '':
                    self.ui.GraphOriginal.setText('[错误：路径无效]')
                    self.ui.InfoScreen.append('错误：图片路径无效！')
                    return
                # 如果水印提取输出路径为空
                if self.ui.LabelDirMonochrome.toPlainText() == '':
                    # 如果路径为空：
                    self.ui.GraphWatermark.setText('[错误：路径无效]')
                    self.ui.InfoScreen.append('错误：保存路径无效！')
                    return
                # 如果没有写水印的长和宽
                if not self.ui.LabelWmWidth.toPlainText().isdigit() or not self.ui.LabelWmHeight.toPlainText().isdigit():
                    self.ui.InfoScreen.append('错误：进行水印提取的必要参数无效！')
                    return
                # 如果密码不合法
                if (not self.ui.LabelPasswordWm.toPlainText().isdigit()) or (not self.ui.LabelPasswordImg.toPlainText().isdigit()):
                    self.ui.InfoScreen.append('错误：密码未填写或不合法！')
                    return

                # 展示包含水印的图像
                targetSize = self.ui.GraphOriginal.size()
                pixmap = QPixmap(self.ui.LabelPathOriginal.toPlainText()).scaled(targetSize, aspectMode=Qtc.AspectRatioMode.KeepAspectRatio)
                self.ui.GraphOriginal.setPixmap(pixmap)
                self.ui.GraphOriginal.repaint()

                # 进行水印提取
                targetFile = self.ui.LabelDirMonochrome.toPlainText() + '/extracted_watermark.png'
                wm_width = eval(self.ui.LabelWmWidth.toPlainText())
                wm_height = eval(self.ui.LabelWmHeight.toPlainText())
                robustness_inputPara_1 = self.ui.LabelAntiAtt_D1.toPlainText()
                robustness_inputPara_2 = self.ui.LabelAntiAtt_D2.toPlainText()
                # 若留空则以默认值进行
                if not robustness_inputPara_1.isdigit():
                    robustness_actual_1 = 36
                else:
                    robustness_actual_1 = eval(robustness_inputPara_1)
                if not robustness_inputPara_2.isdigit():
                    robustness_actual_2 = 20
                else:
                    robustness_actual_2 = eval(robustness_inputPara_2)

                ot1 = WaterMark(password_wm=eval(self.ui.LabelPasswordWm.toPlainText()), password_img=eval(self.ui.LabelPasswordImg.toPlainText()),
                                d1=robustness_actual_1, d2=robustness_actual_2)
                ot1.extract(filename=self.ui.LabelPathOriginal.toPlainText(), wm_shape=(wm_width, wm_height), out_wm_name=targetFile)

                # 展示提取出的水印
                targetSize = self.ui.GraphWatermark.size()
                pixmap = QPixmap(targetFile).scaled(targetSize, aspectMode=Qtc.AspectRatioMode.KeepAspectRatio)
                self.ui.GraphWatermark.setPixmap(pixmap)
                self.ui.GraphWatermark.repaint()
                self.ui.InfoScreen.append('水印提取已完成！')

            elif self.ui.TypeString.isChecked(): # 字符串水印
                self.ui.InfoScreen.append('工作模式：提取 - 字符串')

                # 如果待处理图像路径为空
                if self.ui.LabelPathOriginal.toPlainText() == '':
                    self.ui.GraphOriginal.setText('[错误：路径无效]')
                    self.ui.InfoScreen.append('错误：图片路径无效！')
                    return
                # 如果水印提取输出路径为空
                # if self.ui.LabelDirMonochrome.toPlainText() == '':
                #     # 如果路径为空：
                #     self.ui.GraphWatermark.setText('[错误：路径无效]')
                #     self.ui.InfoScreen.append('错误：保存路径无效！')
                #     return
                # 如果字符串长度不合法
                if not self.ui.LabelWmWidth.toPlainText().isdigit():
                    self.ui.InfoScreen.append('错误：字符串长度信息不合法！')
                    return
                # 如果密码不合法
                if (not self.ui.LabelPasswordWm.toPlainText().isdigit()) or (
                not self.ui.LabelPasswordImg.toPlainText().isdigit()):
                    self.ui.InfoScreen.append('错误：密码未填写或不合法！')
                    return

                # 展示包含水印的图像
                targetSize = self.ui.GraphOriginal.size()
                pixmap = QPixmap(self.ui.LabelPathOriginal.toPlainText()).scaled(targetSize, aspectMode=Qtc.AspectRatioMode.KeepAspectRatio)
                self.ui.GraphOriginal.setPixmap(pixmap)
                self.ui.GraphOriginal.repaint()

                # 进行水印提取
                len_wm = eval(self.ui.LabelWmWidth.toPlainText())
                robustness_inputPara_1 = self.ui.LabelAntiAtt_D1.toPlainText()
                robustness_inputPara_2 = self.ui.LabelAntiAtt_D2.toPlainText()
                # 若留空则以默认值进行
                if not robustness_inputPara_1.isdigit():
                    robustness_actual_1 = 36
                else:
                    robustness_actual_1 = eval(robustness_inputPara_1)
                if not robustness_inputPara_2.isdigit():
                    robustness_actual_2 = 20
                else:
                    robustness_actual_2 = eval(robustness_inputPara_2)

                ot1 = WaterMark(password_wm=eval(self.ui.LabelPasswordWm.toPlainText()),
                                password_img=eval(self.ui.LabelPasswordImg.toPlainText()),
                                d1=robustness_actual_1, d2=robustness_actual_2)
                try:
                    wm_extract = ot1.extract(self.ui.LabelPathOriginal.toPlainText(), wm_shape=len_wm, mode='str')
                    # 展示提取出的水印
                    self.ui.LabelStringExtract.setText(wm_extract)
                except:
                    self.ui.InfoScreen.append('发生未知错误，提取失败！')
                    return

                self.ui.InfoScreen.append('水印提取已完成！')

            else:
                self.ui.InfoScreen.append("工作模式错误！")

        else: # 选项无效
            self.ui.InfoScreen.append("工作模式错误！")



    # 待操作目标
    def openFile_Original(self):
        filePath, _ = QFileDialog.getOpenFileName(
            self.ui,  # 父窗口对象
            "选择待加入水印的原图",  # 标题
            r"./",  # 起始目录
            "图片类型 (*.png *.jpg *.bmp)"  # 选择类型过滤项，过滤内容在括号中
        )
        self.ui.LabelPathOriginal.clear()
        self.ui.LabelPathOriginal.append(filePath)

    def openFile_Watermark(self):
        filePath, _ = QFileDialog.getOpenFileName(
            self.ui,  # 父窗口对象
            "选择要加入的水印",  # 标题
            r"./",  # 起始目录
            "图片类型 (*.png *.jpg *.bmp)"  # 选择类型过滤项，过滤内容在括号中
        )
        self.ui.LabelPathMonochrome.clear()
        self.ui.LabelPathMonochrome.append(filePath)

    def stringPaste(self):
        self.ui.LabelStringOriginal.paste()

    def stringClear(self):
        self.ui.LabelStringOriginal.clear()


    # 待导出目标
    def choosePath_Img(self):
        filePath = QFileDialog.getExistingDirectory(self.ui, "选择导出路径")
        self.ui.LabelDirImgOut.clear()
        self.ui.LabelDirImgOut.append(filePath)

    def choosePath_Watermark(self):
        filePath = QFileDialog.getExistingDirectory(self.ui, "选择导出路径")
        self.ui.LabelDirMonochrome.clear()
        self.ui.LabelDirMonochrome.append(filePath)

    def stringCopy(self):
        self.ui.LabelStringExtract.copy()


# 加载窗口
app = QApplication([])
# 加载图标
app.setWindowIcon(QIcon('./GUI_Support/program_icon.png'))

BDIWS_main_ui = Stats()
BDIWS_main_ui.ui.show()
app.exec_()



# # 加密/提取 纯文字水印的示例
#
# bwm1 = WaterMark(password_img=1, password_wm=1)
# bwm1.read_img('egimg.jpg')
# wm = '版权所有，侵权必究'
# bwm1.read_wm(wm, mode='str')
# bwm1.embed('egimg_text_watermarked.png')
# len_wm = len(bwm1.wm_bit)
# # print('Put down the length of wm_bit {len_wm}'.format(len_wm=len_wm))
#
# bwm1 = WaterMark(password_img=1, password_wm=1)
# wm_extract = bwm1.extract('egimg_text_watermarked.png', wm_shape=len_wm, mode='str')
# print(wm_extract)


# # main operating program
#
# eg1 = WaterMark(password_wm=1, password_img=1)
# eg1 = WaterMark()
#
# eg1.read_img('egimg.jpg')  # 读取原图
#
# eg1.read_wm('watermark.png')  # 读取水印
#
# eg1.embed('egimg_img_watermarked.png')  # 打上盲水印
#
# ot1 = WaterMark(password_wm=1, password_img=1)
#
# ot1.extract(filename='egimg_img_watermarked.png', wm_shape=(100, 100), out_wm_name='output_watermark.png', )
