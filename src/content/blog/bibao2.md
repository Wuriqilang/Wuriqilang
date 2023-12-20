---
title: "【JS核心知识点】关于闭包的一切(上)"
date: 2020-05-25 00:44:59
description: 闭包作为前段封装函数，私有化变量的常用手段，几乎是出现在所有面试问题当中。虽然说闭包已经在我们的程序中无处不在，但作为一个日常面向用户写业务代码的程序员，我们总是对闭包一知半解，模棱两可，希望可以通过这篇文章详解关于闭包的一切。.
image: "https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-12/dmlaIz.png"
author: "乌日其浪"
categories: [前端拾遗]
---

闭包作为前段封装函数，私有化变量的常用手段，几乎是出现在所有面试问题当中。虽然说闭包已经在我们的程序中无处不在，但作为一个日常面向用户写业务代码的程序员，我们总是对闭包一知半解，模棱两可，希望可以通过这篇文章详解关于闭包的一切。

> 对于那些有一点 JavaScript 使用经验但从未真正理解闭包概念的人来说，理解闭包甚至可以看作是某种意义上的重生。

## 1.闭包的前置知识：作用域与词法作用域

### 什么是作用域？

作用域并不是 JS 独有的概念，对于任何编程语言来说，只要它能够定义变量、获取变量中的内容，就需要用到作用域的概念。

> 作用域就是一套规则,它明确**程序在哪里以及如何查找变量(标识符).**

通俗的说,作用域就是告诉你的程序,你去哪儿找变量. 我们来看一段代码.

```js
//代码片段1
funciton foo() {
    var a = 'i am a';
    console.log(a);
}
foo(); //程序输出 i am a
//代码片段2
var b = "i am b";
function foo2(){
    console.log(b);
}
foo2(); //代码输出 i am b
```

第一段代码查找变量,在**函数内部**找到了 a,程序就停止查找并且输出 a;
第二段代码先在函数内部查找 b,没有找到就到**全局**中查找,找到了 b,停止查找并且输出 b;
用程序员的黑话来说, 第一段代码在**函数作用域**中找到变量,第二段代码在**全局作用域**中找到变量

聪明如你一定发现,第二段代码先从函数内部进行查找变量,没有找到后在外部查找变量. 仿佛程序沿着一条由内向外的链条来查找变量. 这个链条我们称之为:**作用域链**

### 作用域的嵌套

在 ES6 之前(ES6 为了明确作用域增加了 let,const 关键字),只有函数作用域和全局作用域.全局作用域包含函数作用域,而函数作用域又可以嵌套函数作用域.

![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1590372683410.png)

用代码表示:

![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1590372697520.png)

### 作用域的工作规则

尽管 JS 是一种脚本语言(边编译边运行),但 JS 是有预编译阶段的. 这里我们不讨论复杂且精妙的 JS 编译过程,直接放出结论:

JS 在代码运行前先从上到下进行编译

- 变量声明 : 遇到 var 声明的变量时,如果当前作用域已经存在该变量则忽略,如果不存在则在当前作用域中声明这个变量.
- 变量取值 : 在当前作用域查找变量.如果没有找到则到父级查找,以此类推,直到全局作用域.如果还没有找到就报错: ReferenceError: XX is not defiend;
- 变量赋值 : 同样在当前作用域中查找,如果没有找到则到父级查找,以此类推,直到全局作用域如果还没有找到**,在非严格模式下则创建一个全局变量.**

### 词法作用域

作用域是一种规则,而这种规则有两种运行模式:

- 词法作用域
- 动态作用域

所谓词法作用域,就是在程序员编写程序的时候,根据变量定义的位置就确定了作用域.和大多数编程语言一样,JS 也采用了词法作用域.

> 相对的,动态作用域是不在乎变量定义的位置,仅关注变量时在哪里调用的.。换句话说，作用域链是基于调用栈的，而不是代码中的作用域嵌套。

我们用一段代码来说明一下这两种模式的区别.

```js
var a = 2;
function foo() {
  console.log(a); // 会输出2还是3？
}
function bar() {
  var a = 3;
  foo();
}

bar();
```

- 词法作用域下: foo() 在申明阶段,引用是全局作用域,所以该函数输出为 2
- 动态作用域下(假设 js 是动态作用域): foo() 输出应该是 3

总而言之,词法作用域实在写代码或者定义时候明确的,关注函数在哪里申明.而动态作用域是在运行时确定的,关注函数在哪里调用.

这也对于词法作用域我们总是感觉很别扭,因为人类的大脑其实是习惯了动态作用域来思考问题.
我们用一段伪代码来还原大脑的"作用域"

```js
var 小明的学历 = "文盲";

function 学历() {
  console.log(小明的学历);
}

function 上学() {
  var 小明的学历 = "小学";
  学历();
}
上学();
```

我们人为已经上过学的小明肯定是小学学历,但是在词法作用域看来,小明仍然是一个文盲.

## 2. 为什么要有作用域?

是的,我们已经知道作用域的运行规则,但是为什么要整这么多作用域呢? 大家都全局调用不好吗? 小朋友你是否有很多问号?

![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1590377477309.gif)

这个问题其实不难解答.我们先写出结论:

1. 变量私有化
2. 避免命名冲突

### 变量私有化

```js
function foo(a) {
  var b = 2;
  // 一些代码
  function bar() {
    // ...
  }
  // 更多代码
  var c = 3;
}

bar(); //报错

console.log(a, b, c); //报错
```

很明显,程序报错了. 因为 bar(),a,b,c 都是 foo() 函数内部的变量,这些变量在同一个函数作用域内(foo 的函数作用域) 是可以互相访问的,但是外部函数想要调用他们却不行. 这种设计思想的好处显而易见 —— 变量可以根据需要来接受不同类型的值. 我们不但避免变量名称的重复,同时也能将私有化的变量在函数中隐藏起来,不至于过多的暴露到外部. ("最低权限"设计原则)

<你不懂的 JS> 提到了一个很好的例子:

```js
function doSomething(a) {
  b = a + doSomethingElse(a * 2);

  console.log(b * 3);
}

function doSomethingElse(a) {
  return a - 1;
}

var b;

doSomething(2); // 15
```

这个代码段中，变量 b 和函数 doSomethingElse(..) 很可能是 doSomething(..) 的“私有”细节。允许外围的作用域“访问” b 和 doSomethingElse(..) 不仅没必要而且可能是“危险的”.换一种写法获取更加恰当:

```js
function doSomething(a) {
  function doSomethingElse(a) {
    return a - 1;
  }

  var b;

  b = a + doSomethingElse(a * 2);

  console.log(b * 3);
}

doSomething(2); // 15
```

现在，b 和 doSomethingElse(..) 对任何外界影响都是不可访问的，而是仅仅由 doSomething(..) 控制。

### 避免变量冲突

将变量和函数隐藏在一个作用域内部就很容易避免同名变量之间发生冲突.(不要在浏览器中尝试这段代码,别问我怎么知道的.)

```js
function foo() {
  function bar(a) {
    i = 3; // 在外围的for循环的作用域中改变`i`
    console.log(a + i);
  }

  for (var i = 0; i < 10; i++) {
    bar(i * 2); // 噢，无限循环！
  }
}
foo();
```

bar(..) 内部的赋值 i = 3 地覆盖了在 foo(..) 的 for 循环中声明的 i。这是因为 bar 作为内部函数可以访问外部作用域,i=3 改变了外部函数的 i,导致循环无法停止.
将 i =3; 改为 var i = 3; 就可以有效解决这个问题.

试想一下,你的项目引用了很多外部的库,而这些库没有隐藏内部/私有函数变量,那么就很容易出现类似的冲突.

## 3.函数作用域与块作用域

说实在的,作为一个以解决问题为首要目的的程序员,我已经在努力把这个事情说的简单清晰. 如果你感觉很啰嗦,那就当做"听妈妈的话"吧..... 相信当你仔细读完之后一定会发现 JS 的乐趣.

你已经知道,只要声明一个函数把一段代码包裹起来,就能够建立一个作用域,将内部的变量或者函数声明"隐藏"起来.

```js
var a = 2;
function foo() {
  var a = 3;
  console.log(a); // 3
}
foo();
console.log(a); // 2
```

但这样并不理想. 你看,我们为了将 a 变量隔离, 不但需要声明一个函数 foo(); 还要后面引用它才能达到我们的目的. 事实上声明 foo()其实也是一种命名污染.

> 如果这个函数不需要命名(或者命名了也不会对外部作用域产生影响)并且能自动运行就好了. ^\_^

的确,JavaScript 提供了解决方法: 立即执行函数

```js
var a = 2;

(function foo() {
  // <-- 插入这个
  var a = 3;
  console.log(a); // 3
})(); // <-- 和这个

console.log(a); // 2
```

**当 function..通过(function..)的形式包裹起来后,这个函数不再是一种函数声明,而是变成了一个函数表达式.**

> 简而言之,通过()包裹起来后,原来的函数 foo 从 "定义 foo()"变成了 "执行 foo()里的代码"

这个时候,即使我们在立即执行函数中命名了函数名称 foo, 在全局作用域中也无法调用 foo(). 它不再没有必要的污染外部作用域了.

### 匿名函数

当然你也可以不对函数进行命名

```js
var a = 2;
(function () {
  var a = 3;
  console.log(a); // 3
})();
console.log(a); // 2
```

但是它有几个缺点:

1. 在栈轨迹上匿名函数没有有用的名称可以表示，这可能会使得调试更加困难。
2. 没有名称的情况下，如果这个函数需要为了递归等目的引用它自己，那么就需要很不幸地使用 被废弃的 arguments.callee 引用。另一个需要自引用的例子是，当一个事件处理器函数在被触发后想要把自己解除绑定。
3. 名称经常对提供更易读/易懂的代码很有帮助。一个描述性的名称可以帮助代码自解释。

所以还是建议为自己的立即执行函数进行命名.

### 块级作用域

虽然说函数作用域是最常见的作用域单位,但在 ES6 之前的 JavaScript 在代码书写方面并不符合程序员的思维习惯. ES6 之后引入的 let 和 const 可以帮助我们写出更好的,更简洁且易于维护的代码.

```js
for (var i = 0; i < 10; i++) {
  console.log(i);
}
```

譬如上面这段非常常见代码,我们的本意是希望定义一个 i 在循环内部使用,但实际上却将 i 划入了外部作用域.
再譬如下面这段代码: 我们的本意是将 bar 作为 if 中使用的变量,但它依旧暴露在全局作用域中了.

```js
var foo = true;

if (foo) {
  var bar = foo * 2;
  bar = something(bar);
  console.log(bar);
}
```

那该如何是好呢? JavaScript 并将代码块作为作用域的能力呀.

![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1590390075720.jpg)

但是 ES6 已经很好的解决了这个问题:

### let 与 const

let 和 const 关键字将变量声明附着在它所在的任何块（通常是一个 { .. }）的作用域中。换句话说，let 为它的变量声明隐含地劫持了任意块作用域。我们可以通过简单地引入一个 { .. } 来为 let 创建一个任意的可以绑定的块儿。在这个例子中，我们在 if 语句内部制造了一个明确的块儿，在以后的重构中将整个块儿四处移动可能会更容易，而且不会影响外围的 if 语句的位置和语义。

```js
var foo = true;

if (foo) {
  let bar = foo * 2;
  bar = something(bar);
  console.log(bar);
}

console.log(bar); // ReferenceError bar is not defined
```

> 注:除了 let 与 const 之外,with 结构,try,catch 也是块级作用域.这里不做详细讨论

### 垃圾回收机制

块儿作用域的另一个有用之处是关于闭包和释放内存的垃圾回收。我们将简单地在这里举一个例子.
获取这个例子稍稍有一些复杂,但既然你已经读到这里了,那说明你肯定能看懂.

```js
function process(data) {
	// ****
}

var someReallyBigData = { .. };  //一个巨大的对象

process( someReallyBigData );

var btn = document.getElementById( "my_button" );

btn.addEventListener( "click", function click(evt){
	console.log("button clicked");
}, /*capturingPhase=*/false );
```

当我们执行回调函数 click 时,不需要 someReallyBigData 这个变量. 这意味着从理论来说,在 process(..)执行后我们可以把 someReallyBigData 回收掉来释放内存.

但是 JS 引擎通常会将这个 someReallyBigData 继续保存一段时间,因为 click 在整个作用域上拥有一个闭包,导致 JS 引擎不敢冒然将 someReallyBigData 回收掉.

但是块级作用域可以明确的告诉 JS 引擎可以执行垃圾回收了.

```js
function process(data) {
	// 做些有趣的事
}

// 运行过后，任何定义在这个块中的东西都可以消失了
{
	let someReallyBigData = { .. };

	process( someReallyBigData );
}

var btn = document.getElementById( "my_button" );

btn.addEventListener( "click", function click(evt){
	console.log("button clicked");
}, /*capturingPhase=*/false );
```
