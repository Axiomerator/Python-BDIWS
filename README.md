# Python BDIWS
一款基于Python的**图像数字盲水印处理系统**。

A **Blind Digital Image Watermarking System** base on Python.

## 图像数字盲水印是什么？
盲水印是人类难以感知到的水印，常规的视觉、听觉等无法察觉到它们。该技术主要应用于音像作品、数字图书等，可以在基本不对原始作品呈现效果作出修改的情况下实现版权防护与传播追踪。

添加数字盲水印的方法基本分为两种：
- 空域方法
- 频域方法

这两种方法添加了冗余信息，在编码和压缩情况不变的情况下，不会使原始图像大小产生变化。

空域是指空间域，我们日常所见的图像就是空域。空域添加数字水印的方法是在空间域直接对图像操作，比如将水印直接叠加在图像上。

另外，我们常说音调的高低，实际上是指声音频率的高低；同样，图像灰度变化强烈的情况，也可以视为图像的频率。频域添加数字水印的方法，是指通过某种变换手段（傅里叶变换，离散余弦变换，小波变换等）将图像变换到频域，在频域对图像添加水印，再通过逆变换，将图像转换为空间域。相对于空域手段，频域手段隐匿性更强，抗攻击性更高。

所谓对水印的攻击，是指破坏水印，包括涂抹，剪切，放缩，旋转，压缩，加噪，滤波等。数字盲水印不仅仅要敏捷性高，也要防御性强。数字盲水印的隐匿性和鲁棒性（抗攻击性）是互斥的。

## Python BDIWS 是什么原理？
程序对图像进行的处理过程的代码源自 guofei9987 老师的 [blind_watermark 项目](https://github.com/guofei9987/blind_watermark)，进行了一定程度的调整与删减。

## 如何使用 Python BDIWS ？ [⚠UNFINISHED⚠]
Python BDIWS 将数字盲水印处理的过程通过简明易懂的GUI实现，降低了使用成本，提高了用户体验。

用户可以根据GUI的提示方便地进行数字盲水印的导入和提取的操作。

目前软件已经实现了部分功能，并拥有了可实现这些功能的GUI界面，软件版本号为 Alpha 0.1 。