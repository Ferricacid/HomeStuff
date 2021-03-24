# HomeStuff 家庭物品位置记录
 Manage the placement of stuff at home. Designed for family members with different prefences.

# 使用者及其喜好
长辈： 
- 低学习成本（熟悉的工具，精简的规则）
- 方便快速（用手机就能操作）

我（intp）：
- 简洁美观
- 无法忍受错误
- 喜欢分析

### 前期
 大家建一个手机就能轻松访问编辑的云端协作文档（main.xlsx），平时就在这个文档里记录物品摆放位置。
 在记录的过程中，大家会开始对常用的一些位置都有了了解。对于一些名字刁钻的地方，主要管理者（我）拍照后用画图软件简单标出名称。
 因为初期数量少，不容易出现重复命名的情况，有也很容易发现。
 在位置都差不多记上后，建立一个文件（place.xlsx），收录这些区域位置的官方名字以及他们之间的关系。
## 日常
 大家照样在文档中记录位置，懒得找原有行列、或是有新地区的人可以自己新开一行。（这也是为什么不选择data validation）
 还有一个照片文档方便查阅，有闲工夫的人可以去管理这个文档，懒得管的人也不用去管。
 这样一个文档已经能满足日常需求了，光是用excel自带的功能就可以进行查找，搞不清物品名称的话可以去翻翻相册。
## 某些情况
 一个python程序提供一些进阶功能，给主要管理者使用。
 这个程序的功能：
   基本的查找（比在excel里查找舒服一点，可以单独列出所有结果，看到对应照片）
   还有就是查错，每隔一段时间使用者就可以用python程序对excel表格查缺补漏，查出不合理的地方。
 
 # 💫怎么用？
 * 概念
 
   - 物品的具体位置=区域+位置
   
    在示例中区域填的是“客厅”“卫生间”之类的地方，位置是“书柜1”“书柜2”之类的地方。
    区域和位置只是代表一种层级关系，你甚至可以写区域是“老王家”，位置是“羽绒服口袋”
  
 * Excel 文件：
  
   - place文件：里面存放的是各个位置的官方名称，两个columns，一个是所有位置，一个是这些位置所属的区域，反映了两种属性之间的关系。
 
   - Main文件：平时大家用的。
  
 * Py程序
   - 查找：按物品名称查找实例，查看位置布局（可附图），查看位置上的物品
   - 查缺补漏：补全缺失的区域名称
   - 检查物品出现次数，顺便生成词云分析家里物品情况特征
  
 To-do:
 * 排查非官方的区域位置说法
 
