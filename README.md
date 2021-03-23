# HomeStuff
Manage the placement of stuff at home. Designed for family members with different prefences.
最近刚刚搬家，家里的东西实在是多，感觉最好搞个能记录不常用物品位置的东西。
因为是打算让家庭成员一块使用的，必须考虑到不同人的喜好。
市面上也有一些app可以实现记录物品位置，但是个人觉得不适合全家人使用。😔
有的人（长辈）比较喜欢简单的操作，就比如一个Excel文件，文件里面可能只有两列，一列是“位置”，一列是“这里都有什么”，就完了。（数据库管理员看了发疯）
有的人（我）就比较喜欢写得清楚一点，比如位置要很细致，比如“客厅书架第二排第三列”，物品命名要有足够的区分度，比如“红色的罗技静音鼠标”

同时因为搬家时就是用excel管理打包情况的，发现有如下一些问题：
* 物品记录完成后就忘记了当时记录的是什么名字，比如一台黄色笔记本电脑，在录入时因为太累了就打成“黄色笔电”，再次搜索时可能会按照“笔记本”去找
* Excel不能在单元格里插入图片
* 人类及其容易犯错，比如我妈记录了3个同样编号的箱子......

为了让两边都能愉快使用，目前方案如下：
## 日常
 大家建一个手机就能轻松访问编辑的云端协作文档，平时就在这个文档里记录物品摆放位置。只需要填写其中两列，就是位置和物品，其他通通不需要！！
 还有一个照片文档方便查阅，有闲工夫的人可以去管理这个文档，懒得管的人也不用去管。
## 某些情况
 一个python程序，给完美主义者（我）使用。
 这个程序的功能有两种：
   基本的查找（比在excel里查找舒服一点，可以单独列出所有结果，看到对应照片）
   还有就是查错，每隔一段时间使用者就可以用python程序对excel表格查缺补漏。
 
 # 💫怎么用？
 * 概念
   很简单，物品的具体位置=区域+位置，在示例中区域填的是“客厅”“卫生间”之类的地方，位置是“书柜1”“书柜2”之类的地方。
   区域和位置只是代表一种层级关系，你甚至可以写区域是“老王家”，位置是“羽绒服口袋”
  
 * Excel 文件：
   place文件：里面存放的是各个位置的官方名称，两个columns，一个是所有位置，一个是这些位置所属的区域，反映了两种属性之间的关系。
   用于方便大家填写位置时确认（懒得确认的人可以填表时自己多填一个区域信息，这样照样可以找到东西）
 
   Main文件：平时大家用的，填的时候只要填位置和物品两个格子就行，只要place文件里的位置是独特的，就可以用python程序补全，懒得记官方名称的人也可以轻松看懂。
  
 * Py程序
   查找：按物品名称查找实例，查看位置布局（可附图），查看位置上的物品
   查缺补漏：补全缺失的区域名称
  
 To-do:
 * 显示重复出现的物品
 * 收录非官方的区域位置说法
 * 分析家中物品（？）
 