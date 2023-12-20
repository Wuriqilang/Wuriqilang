---
title: "一、几种最基础的数据结构"
description: 数据结构是一切算法的基础,作为一个以解决问题为目的的工程师,在本文将会列举几种你一定会用到的数据结构,并尽量从实际出发来说明其作用.
date: 2020-05-28 17:33:35
tags: []
categories: [算法]
image: https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/jiegou.jpg
---

数据结构是一切算法的基础,作为一个以解决问题为目的的工程师,在本文将会列举几种你一定会用到的数据结构,并尽量从实际出发来说明其作用.  
至于复杂高级的数据结构,不是我们关注的重点,也不会出现在未来可能出现的面试当中.

# 1.数组 : 你知道它,用它,但未必懂它

数组(Array)是一种**线性表**数据结构.它用一组**连续的内存空间**,来存储一组具有**相同类型的数据**

这句话其实很简单,我们来说明一下几个关键词.

**线性表** : 顾名思义,线性表就是将数据排成像一条线一样的结构.每个线性表上的数据都是前后关系. 除了数组之外,链表、队列、栈等也是线性表结构。

![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1590659062451.jpg)

> 与它相对立的概念是**非线性表**，比如二叉树、堆、图等。在非线性表中，数据之间不是简单的前后关系

![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1590659144195.jpg)

**连续的内存空间和相同类型的数据**：数组的这个特点使其具有了“随机访问”的能力。但是这也样数组的插入、删除变得非常低效。毕竟它是连续的数据，每一次插入和删除都需要对大量数据做移动。

因为是整个系列的第一个数据类型，我认为花一些篇幅来讲讲数据结构在内存中的实现是值得的。

1. 当我们定义一个数组时，计算机会开辟一块空间用于存放数组。
2. 计算机会为每一个内存单元（数组中的每一项）分配一个地址，计算机就可以通过这个地址来访问内存中的数据。

譬如我们新建了一个 int 类型的数组 int[] a = new int[10] ; 这个数组中每一项都是 int 类型，int 类型数据大小为 4 个字节。所以计算机通过计算，开辟了 40 个字节的空间。计算机开辟的这个空间我们称之为内存块，假设这个内存块的首地址为 base_address = 1000

![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1590660142685.jpg)

数据空间开辟好后，计算机访问其中某一个内存单元时，只要计算出其内存地址即可：

```js
a[i]_address = base_address + i * data_type_size;
```

所以当我们需要通过下标来访问呢数组中的某一项时，时间复杂度为 O(1)。这也是数组为什么使用如此广泛的原因。

但当我们需要插入或者删除时，简直是一场灾难。加入一个数组中 5 各项，在第一项插入一个值就需要把**每一项向后移动一位**

当然，当我们不追求数组的顺序时其实是有其他方式降低插入和删除消耗的，我们暂时不用了解。

# 2.链表

- 链表：**通过指针将一组零散的内存数据串联在一起，这样的数据结构就是链表**。其中的内存块我们称之为“**节点**“，节点中除了存储数据之外，还存储了指向与这个节点相连的节点的地址，我们将记录节点地址称之为**指针**

相对于数组，链表显得稍微复杂。
![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1590740821745.jpg)

数组中的数据单元都是连续的，但链表并不需要申请大块的连续的内存空间，哪里有空插哪里，只需要通过指针把这些数据组织起来即可。

链表结构有很多种类型，最常用的就是三种：单链表、双链表、循环链表。

![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1590741026478.jpg)

![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1590741050687.jpg)

![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1590741076134.jpg)

与数组一样，链表也支持数据的查找、插入和删除操作。

- 查找：链表的内存地址并不是连续的，我们无法通过头节点计算出所需的数据地址，需要从头节点开始不断查询到我们所需的内存单元。时间复杂度为 O(n)
- 插入和删除：链表的插入和删除就无需像数组一样进行大量的数据搬迁，只需要考虑相邻节点即可。时间复杂度为 O(1)

![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1590741326297.jpg)

### 链表有什么用？

我们学习一门技术，本质上就是为了解决问题，那么在实践应用中链表解决了什么问题呢？

> 链表能够完美的契合 LRU 缓存淘汰算法。

![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1590889060715.gif)

啥？啥是 LRU？所谓 LRU 淘汰算法就一种提高数据读取性能的技术，在硬件设计与软件开发中使用非常广泛。譬如 CPU 缓存、数据库缓存、浏览器缓存等。缓存大小是有限的，当我们缓存被沾满时，那些数据应该清除，那些数据应该保留？ That is a Question。

LRU 缓存淘汰算法（最近最少使用策略）就是用来进行这项工作的：比如说你有很多书籍，书架放不下了，必须清除一些书籍，你筛选书籍是不是这样的策略呢？那么如何用链表实现 LRU 算法呢？

我的思路是这样的：我们维护一个有序单链表，越靠近链表尾部的结点是越早之前访问的。

1. 当有一个新的数据被访问时，我们从链表头开始顺序遍历链表。
2. 如果此数据之前已经被缓存在链表中了，我们遍历得到这个数据对应的结点，并将其从原来的位置删除，然后再插入到链表的头部。
3. 如果此数据没有在缓存链表中，又可以分为两种情况：如果此时缓存未满，则将此结点直接插入到链表的头部；如果此时缓存已满，则链表尾结点删除，将新的数据结点插入链表的头部。这样我们就用链表实现了一个 LRU 缓存，是不是很简单？

### 链表的实现：

链表基础知识确实也很容易掌握，但写好链表并实现相关的操作很少有人能做到。为了能够不要眼高手低，写出靠谱的链表代码，我们需要注意以下几点：

1. 理解指针或引用的含义
   很多语言并没有**指针**的概念，取而代之的是**引用**，譬如 Java、Python、JS。你将引用理解为指针即可，他们都是存储了对象的内存地址。

**将某个变量赋值给指针，实际上就是将这个变量的地址赋值给指针，或者反过来说，指针中存储了这个变量的内存地址，指向了这个变量，通过指针就能找到这个变量。**

2.警惕指针丢失与内存泄露
写链表的时候很容易出现指针指来指去最后不知道指导哪里去了。为什么会丢失指针呢？

![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1590742103042.jpg)

```c
p->next = x; // 将p的next指针指向x结点；
x->next = p->next; // 将x的结点的next指针指向b结点；
```

如果我们这样写代码，p 的指针已经指向到 x 节点了，再来设置 x 的指针时，等于将 X 的指针指向自己。就导致链表断开，内存泄露，指针丢失。
解决这个问题很简单，只要把代码顺序调换一下即可

```c
x->next = p->next; // 将x的结点的next指针指向b结点；
p->next = x; // 将p的next指针指向x结点；
```

3. 重点留意边界条件处理

我经常用来检查链表代码是否正确的边界条件有这样几个：

- 如果链表为空时，代码是否能正常工作？
- 如果链表只包含一个结点时，代码是否能正常工作？
- 如果链表只包含两个结点时，代码是否能正常工作？
- 代码逻辑在处理头结点和尾结点的时候，是否能正常工作？

啰里啰唆的说了半天，对于我们解决问题为首要目的的工程师来说稍显多余。我们直接来实现一个链表，采用的语言就使用地球上使用人数最多的语言 JS 吧。

### 单项链表的设计：

根据之前的链表原理，链表包括两个类：一个是 Node 类来表示节点，一个是 LinkedList 类表示链表，并且提供链表插入、删除、查找的操作。

- Node 类
  Node 类包括两个属性：element 来保存节点上的数据，next 来保存下一个节点的地址：

```js
function Node(element) {
  this.element = element; //当前节点中存储的内容
  this.next = null; //下一个节点链接
}
```

- LinkedList 类
  LinkedList 类提供了对链表进行操作的方法，包括插入删除节点，查找给定的值等。值得注意的是，它只有一个 属性，那就是使用一个 Node 对象来保存该链表的头节点。

```js
function Node(element) {
  this.element = element; //当前节点中存储的内容
  this.next = null; //下一个节点链接
}

function LinkedList() {
  this.head = new Node("head"); //头节点
  this.find = find; //查找节点
  this.insert = insert; //插入节点
  this.remove = remove; // 删除节点
  this.findPrev = findPrev; // 查找前一个节点
  this.display = display; // 显示链表
  //查找
  function find(item) {
    var currNode = this.head;
    while (currNode.element != item) {
      currNode = currNode.next;
    }
    return currNode;
  }
  //插入
  function insert(newElement, item) {
    var newNode = new Node(newElement);
    var currNode = this.find(item);
    newNode.next = currNode.next;
    currNode.next = newNode;
  }
  //显示
  function display() {
    var currNode = this.head;
    while (!(currNode.next == null)) {
      console.log(currNode.next.element);
      currNode = currNode.next;
    }
  }
  //删除
  function remove(item) {
    //删除节点需要找到需要删除的节点与上一个节点
    var removeNode = this.find(item);
    var prevNode = this.findPrev(removeNode);
    prevNode.next = removeNode.next;
  }
  //查找上一个节点
  function findPrev(node) {
    var prevNode = this.head;
    while (prevNode.next != node) {
      prevNode = prevNode.next;
    }
    return prevNode;
  }
}
```

我们可以调用测试一下：

```js
var demo = new LinkedList();

demo.insert("first", "head");
demo.insert("second", "first");
demo.insert("third", "second");
demo.display();
//first
//second
//third

demo.remove("second");
demo.display();
//first
//third
```

如果你想彻底掌握链表，应对面试中出现的各位问题，那就需要多写多练，熟能生巧。对于双向链表，循环链别的实现，推荐你看这篇文章[链表的 JS 实现](https://www.jianshu.com/p/d20169988bc4)

# 3.栈

作为一名已经开始接触算法与数据结构的工程师，“栈”这个词一定并不陌生，你应该也很清楚的知道其特点：**“先进者后出，后进者先出”** 譬如一摞碟子，就非常符合栈的特点：

![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1590937459099.jpg)

栈是一种操作受限的线性表，它只允许在一端插入和删除数据。那为什么非要用栈呢？数组和链表它不香吗？
事实上，就功能性而言数组和链表确实可以替代栈，但是**特定的数据结构是对特定应用场景的抽象**，数组和链表暴露了太多接口，操作上太灵活就会导致使用不可控，更容易出错。

所以。
**当某个数据集合只涉及在一端插入和删除数据，并且满足后进先出、先进后出的特性，我们就应该首选“栈”这种数据结构。
**

栈可以使用链表实现（链式栈）也可以采用数组实现（顺序栈）。

### 顺序栈的实现

```js
class Stack {
  constructor() {
    this.dataStore = [];
    this.top = 0;
  }
  //出栈
  pop() {
    return this.dataStore[--this.top];
  }
  //入栈
  push(element) {
    this.dataStore[this.top++] = element;
  }
  //查看栈顶元素
  peek() {
    if (this.top > 0) {
      return this.dataStore[this.top - 1];
    } else {
      return "Empty";
    }
  }
  //栈内元素
  length() {
    return this.top;
  }
}
```

```js
var demo = new Stack();
demo.push("first");
demo.push("second");
console.log(demo.peek()); // second
demo.length(); // 2
demo.pop(); // second
console.log(demo.peek()); // first
```

链式栈的实现在这里不做详细说明，毕竟我们以解决问题为首要目的，日常使用中能够实现栈这种数据结构即可。栈的操作都是简单的赋值操作，所以时间复杂度都为 O(1)

### 栈的作用：

那么栈这种数据结构有什么作用？为什么要做这么多的限制？

- 函数调用栈
  操作系统给每个线程分配了一块独立的内存空间，这块内存被组织成“栈”这种结构, 用来存储函数调用时的临时变量。每进入一个函数，就会将临时变量作为一个栈帧入栈，当被调用函数执行完成，返回之后，将这个函数对应的栈帧出栈。
  举个例子就很好理解了：

```c

int main() {
   int a = 1;
   int ret = 0;
   int res = 0;
   ret = add(3, 5);
   res = a + ret;
   printf("%d", res);
   reuturn 0;
}

int add(int x, int y) {
   int sum = 0;
   sum = x + y;
   return sum;
}
```

![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1590942295900.jpg)

- 栈处理表达式求值：

为了方便解释，我将算术表达式简化为只包含加减乘除四则运算，比如：34+13✖9+44-12/3。对于这个四则运算，我们人脑可以很快求解出答案，但是对于计算机来说，理解这个表达式本身就是个挺难的事儿。如果换作你，让你来实现这样一个表达式求值的功能，你会怎么做呢？实际上，编译器就是通过两个栈来实现的。其中一个保存操作数的栈，另一个是保存运算符的栈。我们从左向右遍历表达式，当遇到数字，我们就直接压入操作数栈；当遇到运算符，就与运算符栈的栈顶元素进行比较。如果比运算符栈顶元素的优先级高，就将当前运算符压入栈；如果比运算符栈顶元素的优先级低或者相同，从运算符栈中取栈顶运算符，从操作数栈的栈顶取 2 个操作数，然后进行计算，再把计算完的结果压入操作数栈，继续比较。我将 3+5✖8-6 这个表达式的计算过程画成了一张图，你可以结合图来理解我刚讲的计算过程。

![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1590942557874.jpg)

- 栈处理括号匹配
  除了用栈来实现表达式求值，我们还可以借助栈来检查表达式中的括号是否匹配。我们同样简化一下背景。我们假设表达式中只包含三种括号，圆括号 ()、方括号[]和花括号{}，并且它们可以任意嵌套。比如，{[] ()[{}]}或[{()}([])]等都为合法格式，而{[}()]或[({)]为不合法的格式。那我现在给你一个包含三种括号的表达式字符串，如何检查它是否合法呢？这里也可以用栈来解决。我们用栈来保存未匹配的左括号，从左到右依次扫描字符串。当扫描到左括号时，则将其压入栈中；当扫描到右括号时，从栈顶取出一个左括号。如果能够匹配，比如“(”跟“)”匹配，“[”跟“]”匹配，“{”跟“}”匹配，则继续扫描剩下的字符串。如果扫描的过程中，遇到不能配对的右括号，或者栈中没有数据，则说明为非法格式。当所有的括号都扫描完成之后，如果栈为空，则说明字符串为合法格式；否则，说明有未匹配的左括号，为非法格式。

# 4.队列

队列与栈非常类似,也只支持"入"与"出" .排队买票就是一个队列,先来的人先买,后来的人后买.

![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1590973422823.jpg)

它在许多底层系统,中间件中有着广泛的应用.队列可以通过基于数组或链表的方式实现.我们这里演示基于数组的实现方式.

```js
class Queue {
  constractor() {}
}
```
