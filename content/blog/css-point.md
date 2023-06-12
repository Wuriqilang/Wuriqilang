---
external: false
title: "CSS知识点"
date: 2020-05-21 10:55:48
description: CSS 作为构建前端页面的三驾马车,随着现代前端技术的飞速发展,已经称为描述页面样式不可或缺的部分. 本文将从前端面试题目出发,总结 CSS 必须掌握的知识点.
---

CSS 作为构建前端页面的三驾马车,随着现代前端技术的飞速发展,已经称为描述页面样式不可或缺的部分. 本文将从前端面试题目出发,总结 CSS 必须掌握的知识点.

## Questions

### 1. css sprite 是什么?有什么优缺点?

- 知识点:css sprite
- 重要程度:★★★
- 概念与背景: css sprite 是一种用于解决页面图片过多导致大量 http 请求的解决方案. css sprite 将多个小图片拼接到一个图片中，通过 background-positon 和元素尺寸调节需要显示的背景图案.
- 优点:
  - 减少 HTTP 请求数,极大的提高页面加载速度
  - 增加图片信息重复度,提高压缩比,减少图片大小
  - 更换风格方便.只需要在少量图片上修改颜色或者样式即可
- 缺点:

  - 图片合并麻烦
  - 维护不便,修改一个图片可能需要重新布局整个图片样式

- 实现 (转自 MDN 教程):
  如果为类名为 toolbtn 的元素附加一张图片

```css
.toolbtn {
  background: url(myfile.png);
  display: inline-block;
  height: 20px;
  width: 20px;
}
```

为设置 background-position 以使每个按钮得到合并后图片中的正确部分，可以在 background 属性中的 url() 后添加 x, y 两个坐标值，或直接使用 background-position 属性。例如：

```css
#btn1 {
  background-position: -20px 0px;
}
#btn2 {
  background-position: -40px 0px;
}
```

这会将 ID 为 btn1 的元素的背景向左移 20px，ID 为 btn2 的元素的背景向左移 40px（假设这两个元素都带有 toolbtn 这个类且应用了上面 background 属性中定义的图片背景）

类似的，你也可以使用下面的代码添加悬停效果：

```css
#btn:hover {
  background-position: <pixels shifted right>px <pixels shifted down>px;
}
```

### 2. display:none 与 visibility:hidden 的区别

- 知识点: display 与 visibility
- 重要程度:★★
- 概念与背景: 本题考察 display 与 visibility 的渲染机制
- display:none; :
  - 会让元素完全从渲染树中消失,渲染时不占任何空间
  - 非继承属性: 子孙节点同样消失,无法通过修改子孙节点属性使子孙节点显示
- visibility:hidden; :
  - 不会让元素从渲染树中消失,渲染时仍然占据控件,只是内容不可见
  - 子孙节点可以通过重新设置 visibility:visible; 使自身显示
  - 修改 display 属性会导致文档重拍,visibility 只会导致内容重新渲染

### 3.CSS 的选择器

- 知识点: CSS 的样式选择器
- 重要程度:★★★★
- 概念与背景: CSS 选择器规定了 CSS 规则会被应用到哪些元素上。CSS 选择器是构建前端页面样式最基础也是最重要的部分

> 备注：暂时没有能够选择 父元素、父元素的同级元素，或 父元素的同级元素的子元素 的选择器或者组合器。

这里列举部分常见 CSS 元素选择器的使用方法

```html
<div id="box" class="myBox">
  <p title="value">This is a P tag</p>
  <button class="myBtn">Click</button>

  <p>This is a P tag2</p>
</div>
```

```css
/* 类选择器 */
.myBox {
  backgournd-color: red;
}
/* id选择器 */
#box {
  backgournd-color: red;
}
/* 元素选择器 */
p {
  backgournd-color: yellow;
}
/* 组合选择器 */
p,
button {
  backgournd-color: yellow;
} /* 多个元素为平行关系,都获得该样式属性 */
/* 后代选择器 */
.myBox .myBtn {
  background-color: green;
} /* .myBox中的所有.myBtn  用空格隔开 */
/* 子选择器 */
.myBox > .myBtn {
  background-color: green;
} /* .myBox中的所有.myBtn子元素  用>隔开 */
/* 相邻选择器 */
p + .myBtn {
  background-color: green;
} /* p后相邻的.myBtn同级元素*/
/* 同级通配符 */
p ~ btn {
  background: #ff0;
} /* p后所有同级的btn元素  CSS3*/

/* 伪类 */
.myBox:first-child {
  font-style: italic;
} /* mybox的第一个子元素*/
.myBtn:hover {
  background-color: green;
} /* mybox的第一个子元素*/

/* 元素选择器 */
p[title] {
  color: #f00;
} /*具有title属性的P标签*/
p[title="value"] {
  color: #f00;
} /*具有title属性且属性内容为value的P标签*/
```

- 关于选择器的权重：

  - 选择器类型：
    1、ID 　　#id
    2、class 　　.class
    3、标签　　 p
    4、通用　　\*
    5、属性　　[type="text"]
    6、伪类　　：hover
    7、伪元素　　::first-line
    8、子选择器、相邻选择器

  - 权重计算规则：
    1、第一等：代表内联样式，如: style=””，权值为 1000。
    2、第二等：代表 ID 选择器，如：#content，权值为 0100。
    3、第三等：代表类，伪类和属性选择器，如.content，权值为 0010。
    4、第四等：代表类型选择器和伪元素选择器，如 div p，权值为 0001。
    5、通配符、子选择器、相邻选择器等的。如\*、>、+,权值为 0000。
    6、继承的样式没有权值。

- 附：选择器使用方法

![](https://www.xr1228.com/https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1590135976965.png)
![](https://www.xr1228.com/https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1590135990176.png)

### 4.清除浮动有哪些方法？

- 知识点: 清除浮动，BFC
- 重要程度:★★
- 概念与背景: 清除浮动其实就是为了解决父元素内的子元素设置浮动后导致的父元素内部高度为 0 的问题。
  如图：父元素内有两个子元素 BIG、SMALL。当子元素未设置浮动时子元素会自动撑开父元素高度。

![](https://www.xr1228.com/https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1590204347700.png)

当子元素设置 Float 属性后，父元素高度变为 0，且外部元素位置也发生了改变。

![](https://www.xr1228.com/https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1590204463221.png)

#### 清除浮动的方法：

1.  额外标签法：（在最后一个浮动标签后，新加一个标签，给其设置 clear：both；）（不推荐） - 优点：方便，通俗易懂 - 缺点：增加无意义的标签

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
      body {
        font-size: 30px;
      }
      .father {
        background-color: bisque;
        border: red solid 1px;
      }
      .big {
        float: left;
        height: 400px;
        width: 400px;
        background-color: pink;
      }
      .small {
        float: left;
        height: 200px;
        width: 200px;
        background-color: blue;
      }
      .clear {
        clear: both;
      }
      .other {
        height: 200px;
        background-color: green;
      }
    </style>
  </head>
  <body>
    <div class="father">
      <div class="big">BIG</div>
      <div class="small">SMALL</div>
      <div class="clear"></div>
    </div>
    <div class="other"></div>
  </body>
</html>
```

2. 触发 BFC：父级添加 overflow 属性（父元素添加 overflow:hidden）（不推荐）
   这里要说明一下 BFC，
   > BFC（Block formatting context）：块级格式化上下文，BFC 是一个独立的布局环境，其中的元素布局是不受外界的影响，并且在一个 BFC 中，块盒与行盒（行盒由一行中所有的内联元素所组成）都会垂直的沿着其父元素的边框排列。

通俗来讲，BFC 是 HTML 的一种特性，**只要触发了 BFC，一个块级元素就形成了一个封闭空间。这个空间内的子元素排布不会对外部元素发生影响。**
overflow 是触发 BFC 的一个条件，我们利用这个条件就可以让父级形成 BFC。
**触发 BFC 的条件：**
1、float 的值不是 none。
2、position 的值不是 static 或者 relative。
3、display 的值是 inline-block、table-cell、flex、table-caption 或者 inline-flex
4、overflow 的值不是 visible

- 优点：代码简洁
- 缺点：内容增多的时候容易造成不会自动换行导致内容被隐藏掉，无法显示要溢出的元素

```css
.father {
  background-color: bisque;
  border: red solid 1px;
  overflow: hidden;
}
```

1. 使用 after 伪元素清除浮动（推荐）

- 优点：符合闭合浮动思想，结构语义化正确
- 缺点：after 是 css3 提出的伪类，兼容 IE6-7 需要使用 zoom:1 触发 hasLayout

```css
.clearfix:after {
  /*伪元素是行内元素 正常浏览器清除浮动方法*/
  content: "";
  display: block;
  height: 0;
  clear: both;
  visibility: hidden;
}
.clearfix {
  *zoom: 1; /*ie6清除浮动的方式 *号只有IE6-IE7执行，其他浏览器不执行*/
}
```

```html
<body>
  <div class="fahter clearfix">
    <div class="big">big</div>
    <div class="small">small</div>
    <!--<div class="clear">额外标签法</div>-->
  </div>
  <div class="other"></div>
</body>
```

4. 使用 before 和 after 双伪元素清除浮动

- 优点：符合闭合浮动思想，结构语义化正确
- 缺点：after 是 css3 提出的伪类，兼容 IE6-7 需要使用 zoom:1 触发 hasLayout

```css

     .clearfix:after , .clearfix:before{
        content: "";
        display: table;
    }
    .clearfix:after{
        clear: both;
    }
    .clearfix{
        *zoom: 1;
```

### 5. CSS3 有哪些改变？

- 知识点: CSS3 变化
- 重要程度:★★★★

#### CSS3 带来的一些变化：

- 新增了一些选择器
  - p:first-of-type 选择属于其父元素的首个 P 元素
  - p:last-of-type 选择属于其父元素的最后一个 P 元素
  - p:only-of-type 选择属于其父元素的唯一个 P 元素
  - p:only-child 选择属于其父元素的唯一个 P 元素
  - p:nth-child(2) 选择属于其父元素的第二个子元素的 P 元素
  - after：在元素之后添加内容，可以用来清除浮动
  - before：在元素之前添加内容
  - enable，disable，checked
- 增加了对于动画、图形处的处理
  - transition：过度
  - transform：旋转、缩放、移动或倾斜
  - animation：动画
  - gradient：渐变
  - shadow：阴影
  - border-radius：圆角

### 6.浏览器是如何解析 CSS 选择器的？

CSS 选择器是从右向左解析的，如果从左向右解析发现不匹配则需要回溯，会损失许多性能。从右向左解析先找到最右节点，向上寻找其父节点直到找到根元素。
CSS 解析完成后，需要与 Dom Tree 一起分析简历 Render Tree，最后进行绘图。
