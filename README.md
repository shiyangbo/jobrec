# 大纲（按会上讲的时间顺序）  

## 首先  
论文的内容，它的实现方法。  
一些内容...略  
1. 第1类特征。略    
2. 第2类特征。略  
3. 第3类特征。把jobtile和title,tags做成和论文里相似形式的特征。  
4. 第4类特征。略  

## time窗口的取法  
1. 1--1  
2. 2--1  
3. 2--2  
4. all--1  
5. all--1  

## 正负样本划分  
略  

## 哪些特征  
5 × ( )  
1. 定义similar user   
jobroles + discipline_id + (country) + region + career_level + experience几个 + edu_degree + edu_fieldofstudies  
2. 定义related user  
同论文里的做法。有交集的jobroles  
3. 定义similar job  
除了industry, 下没下架，发布日期3个，其它都要  
4. 定义related job  
同论文里的做法  

=> 取法有两种：针对单个job，针对jobs（针对单个user，针对users）  

加上SU RU SJ RJ  
加上BU BJ  
加上(title长度) (title.word 5 BIN) (tag 8) (jobrole.word )  

## 最后  
1. 改数据库  
engine从innodb改成myMyISAM  
text, char做成全文索引  
注意空值  
2. 接下来就是取样（问：就是抽取特征的意思把。答：嗯）  
3. TreeNet学生版是否是全功能的。  
