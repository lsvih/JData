# JData for XiaoBo~

### Dependence

This project requires **Python 2.7** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)

You will also need to have software installed to run and execute a [Jupyter Notebook](http://ipython.org/notebook.html)

I don't know what will happen with using **Python 3.x** :)

### First Run

Download the original data from official website, unzip then copy **.csv** files into `original_data` folder.

```bash
python init_data.py
```

Please wait a minute. It will create `data` folder containing cleaned **.csv** files.

### Run

In a terminal or command window, navigate to the top-level project directory `JData` (that contains this README) and run one of the following commands:

```bash
ipython notebook jdata.ipynb
```

or
```bash
jupyter notebook jdata.ipynb
```

This will open the Jupyter Notebook software and project file in your browser.

### Data

The original dataset has the following attributes:

<p>1. 用户数据</p><table class="" border="1"><tbody><tr><td>&nbsp;user_id</td><td>&nbsp;用户<span lang="EN-US">ID</span></td><td>&nbsp;脱敏</td></tr><tr><td>&nbsp;age</td><td>&nbsp;年龄段</td><td>&nbsp;-1表示未知</td></tr><tr><td>&nbsp;sex</td><td>&nbsp;性别</td><td>&nbsp;0表示男，1表示女，2表示保密<br></td></tr><tr><td>&nbsp;user_lv_cd</td><td>&nbsp;用户等级</td><td>&nbsp;有顺序的级别枚举，越高级别数字越大</td></tr><tr><td>&nbsp;user_reg_tm</td><td>&nbsp;用户注册日期</td><td>&nbsp;粒度到天</td></tr></tbody></table><p><br></p><p>2. 商品数据</p><table class="" border="1"><tbody><tr><td>&nbsp;sku_id</td><td>&nbsp;商品编号</td><td>&nbsp;脱敏</td></tr><tr><td>&nbsp;a1</td><td>&nbsp;属性<span lang="EN-US">1</span></td><td>&nbsp;枚举，<span lang="EN-US">-1</span>表示未知</td></tr><tr><td>&nbsp;a2</td><td>&nbsp;属性2</td><td>&nbsp;枚举，<span lang="EN-US">-1</span>表示未知</td></tr><tr><td>&nbsp;a3</td><td>&nbsp;属性3</td><td>&nbsp;枚举，<span lang="EN-US">-1</span>表示未知</td></tr><tr><td>&nbsp;cate</td><td>&nbsp;品类<span lang="EN-US">ID</span></td><td>&nbsp;脱敏</td></tr><tr><td>&nbsp;brand</td><td>&nbsp;品牌<span lang="EN-US">ID</span></td><td>&nbsp;脱敏</td></tr></tbody></table><p><br></p><p>3. 评价数据</p><table class="" border="1"><tbody><tr><td>&nbsp;dt</td><td>&nbsp;截止到时间</td><td>&nbsp;粒度到天</td></tr><tr><td>&nbsp;sku_id</td><td>&nbsp;商品编号</td><td>&nbsp;脱敏</td></tr><tr><td>&nbsp;comment_num</td><td>&nbsp;累计评论数分段</td><td>&nbsp;0表示无评论，1表示有1条评论，<br>&nbsp;2表示有2-10条评论，<br>&nbsp;3表示有11-50条评论，<br>&nbsp;4表示大于50条评论<br></td></tr><tr><td>&nbsp;has_bad_comment</td><td>&nbsp;是否有差评</td><td>&nbsp;0表示无，1表示有<br></td></tr><tr><td>&nbsp;bad_comment_rate</td><td>&nbsp;差评率</td><td>&nbsp;差评数占总评论数的比重</td></tr></tbody></table><p><br></p><p>4. 行为数据</p><table class="" border="1"><tbody><tr><td>&nbsp;user_id</td><td>&nbsp;用户编号</td><td>&nbsp;脱敏</td></tr><tr><td>&nbsp;sku_id</td><td>&nbsp;商品编号</td><td>&nbsp;脱敏</td></tr><tr><td>&nbsp;time</td><td>&nbsp;行为时间</td><td>&nbsp;</td></tr><tr><td>&nbsp;model_id</td><td>&nbsp;点击模块编号，如果是点击</td><td>&nbsp;脱敏</td></tr><tr><td>&nbsp;type</td><td>&nbsp;1.浏览（指浏览商品详情页）；<br>&nbsp;2.加入购物车；3.购物车删除；4.下单；5.关注；6.点击<br></td><td>&nbsp;</td></tr><tr><td>&nbsp;cate</td><td>&nbsp;品类<span lang="EN-US">ID</span></td><td>&nbsp;脱敏</td></tr><tr><td>&nbsp;brand</td><td>&nbsp;品牌<span lang="EN-US">ID</span></td><td>&nbsp;脱敏</td></tr></tbody></table>
