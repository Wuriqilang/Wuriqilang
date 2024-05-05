---
title: "1个小时快速学习Go 2024"
description: "这里是值得投资的一个小时系列, 不说废话 , 希望这一个小时能给你带来一些微小而美好的改变"
date: 2024-05-5 00:10:26
categories: ["语言学习"]
tags: [Go]
image: https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2022-07/VzRjXF.jpg
---

这里是 **值得投资的一个小时** 系列, 不说废话 , 希望这一个小时能给你带来一些微小而美好的改变

## 一 背景

### 1.1 什么是 Go

Go ( == Golang) 是 Google 研发的**静态强类型**,**编译型** 语言

### 1.2 为什么要学 Go

- 大势所趋:
  许多大厂(包括我所在的阿里 ☁️ 很多项目已经切换到 Go)
  ![trend](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2022-07/t8nONt.png)

- 时代变化

1. Go 的很多特性更适合云原生场景
2. Go 对于区块链中加密算法很有优势

总之 Go 是一门非常优秀的语言, 它很适合喜欢简洁,高效代码的你. 推荐你将 Go 作为你的**第二语言**

### 1.3 Go 的优点 ( 这部分可以先略过, 后面回过头再看 )

**语言风格**

- 大道至简，比如及其简单但完备的面向对象设计，面向接口，没有继承只有组合；
- 最少特性，一个特性对解决问题有显著效果就没有必要存在；
- 显式表达，比如数据类型必须显式转化，不提供隐式转化能力；
- 最少惊异，减少那些奇怪的特性设计，最大程度减少错误发生概率；

**语言特性**

- 静态语言、静态编译速度快，拥有静态语言的安全与性能；
- 天然支持并发，基于 CPS 并发模型，goroutine 轻量级线程，支持大并发处理；
- 简洁的脚本化语法，如变量赋值 a := 1，兼具静态语言的特性与动态语言的开发效率；
- 提供垃圾回收机制，不需要开发人员管理，通过循环判活，再启用 goroutine 来清理内存；
- 创新的异常处理机制，普通异常通过返回 error 对象处理，严重异常由 panic、recover 处理；
- 函数多返回值，方便接收多值，一些解释性语言已经支持，如 python、js 的 es6 等；
- 支持 defer 延迟调用，从而提供了一种方式来方便资源清理，降低资源泄露的概率；
- 面向接口的 oop，没有对象与继承，强调组合，以类似于 duck-typing 的方式编写面向对象；

你很容易就会发现 Go 是一帮大佬强迫症犯了 , 解决其他语言中各种缺陷的产物.

## 二 安装

这里只介绍 Mac 系统下的安装 ( 其他系统可以查看相关资料 )

### 2.1 下载安装

[下载地址](https://golang.google.cn/)

点击下载, 然后安装, 就这么简单 (windows 系统需要设置环境变量)
![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2022-07/mLy8qS.png)

安装后查看版本

```bash
❯ go version
go version go1.22.2 darwin/amd64
```

### 2.2 环境配置

- GoPROXY

```bash
go env -w GOPROXY=https://goproxy.cn,direct
```

> 注: go1.16后不需要单独配置GOPATH和开启goMod了, 下面的环境配置你只需要知道

- GOPATH 路径（GOPATH 路径是我们的工作区）

```bash
go env -w GOPATH=我们自己的工作区路径
```

- GoMOD

```bash
go env -w GO111MODULE=on
```

- 重要的环境变量

Go 通过环境变量来做项目上的管理和控制，通过命令 go env 可以查看相关变量：

```bash
go env
```

重要的就两条
**GOROOT** ： Go 的安装目录，即可执行文件所在的目录；
**GOPATH** ：GOPATH 是 Go 语言中使用的一个环境变量，它使用绝对路径提供项目的工作目录（也称为工作区）。~[参考文章](https://www.cnblogs.com/ailiailan/p/13454139.html)

因为我们想在全局使用 go 相关的命令,所以需要简单的配置一下环境变量: (适用于 mac, 其他系统请另行百度,大同小异)

1. 打开配置文件 vim ~/.zshrc
2. 在文件底部加上下面的内容
3. 加载配置 source ~/.zshrcx

```zsh
export GOROOT=/usr/local/go  # 告诉系统GO的安装位置
export GOPATH=/Users/[yourname]/go # 告诉系统三方包安装的位置
export PATH=$PATH:$GOPATH/bin # 告诉系统,我可以直接使用三方包提供的指令
```

### 2.2 开发工具

推荐使用 VS Code , 安装 Go 插件即可

## 三 第一个行代码

新建 go 项目目录，并在项目的 src 目录中创建 hello 目录

```bash
# 创建project的目录
$ mkdir gproject

# 进入目录
$ cd gproject/

# 初始化
go mod init gproject
go: creating new go.mod: module gproject
```

在该目录中创建一个 main.go 文件：

```go
package main // import "golang" (此处的注释为go mod init 生成的 module 值)

import "fmt"

func main() {
 fmt.Println("xxx")
}
```

执行或编译后执行：

```bash
# 直接run
$ go run main.go

# 编译成二进制文件
$ go build

# 执行二进制文件
```

## 四 Go 的语法细节(针对初学者)

这部分不建议去看任何其他资料,除了这个网址
<https://tour.go-zh.org>

学习一门新的语言,最主要的是参考其类型定义,然后与自己熟悉的语言做对照.

### 4.1 chapter1 : 变量定义与复制

```go
func main() {
    // chapter1 : 变量定义与复制
    a := 1  // 方式一: 无需关键字,声明并赋值
    fmt.Println(a)
    var b = 2  // 方式二: 关键字声明并赋值
    fmt.Println(b)
    var c int // 方式三: 关键字声明,未赋值(不推荐)
    c = 3
    fmt.Println(c)
    // 方式四: 函数外声明变量,必须使用var关键字
    varD();
  }

  var d = 4
  func varD(){
    fmt.Println(d)
  }
```

### 4.2 chapter2 : 基本类型

整数:
`int` `int8` `int16` `int32` `int64` `uint` `uint8` `uint16` `uint32` `uint64` `uintptr`

- int与unint: 32位系统为32位,64位系统为64位
- `byte` 是 `uint8` 的别名, `rune` 是 `int32` 的别名,

浮点数
`float32` `float64`

复数
`complex64` `complex128`

布尔
`bool`

字符串
`string`

我们可以利用`fmt.printf`获取变量的基本类型

```go
  e:=1
  fmt.Printf(" e 的类型为: %T\n" , e) // e的类型是int
  f:=3.2
  fmt.Printf(" f 的类型为: %T\n" , f) // f的类型是float64
  g:=false
  fmt.Printf(" g 的类型为: %T\n" , g) // g的类型是bool
  h := "str"
  fmt.Printf(" h 的类型为: %T\n" , h) // h的类型是string
```

### 4.3 chapter3 : 运算符

go的运算符与流行的编程语言基本一致

```go
  m := 5
  n := 10

  fmt.Println(m + 5)          // 10
  fmt.Println(n % 3)          // 1
  fmt.Println(m <= n)         // true
  fmt.Println(m & n)          // 位运算 0
   fmt.Println(true && !false) // 与运算 true
```

### 4.4 chapter4 : 分支

```go
  // chapter4: 分支结构
  x := 10
  if x > 10 {
    fmt.Println("x > 10")
  } else if x > 5 {
    fmt.Println("x > 5")
  } else {
    fmt.Println("x 不大于 5")
  }

  // 条件中初始化变量
  if y := 10; y > 5 {
    fmt.Println("y > 5")
  }

  // switch case (可以省略break)
  switch x {
  case 1:
    fmt.Println("x == 1")
  case 2:
    fmt.Println("x == 2")
  case 3:
    fmt.Println("x == 3")
  default:
    fmt.Println("x 不等于 1, 2, 3")
  }
```

### 4.5 chapter5 : 循环

```go
  // chapter5: 循环
  for i := 0; i < 5; i++ {
    fmt.Println(i)
  }

  // 模拟while循环
  i := 0
  for i < 5 {
    fmt.Println(i)
    i++
  }
```

### 4.6 chapter6 : 函数

```go
  // 函数参数类型相同可以只给最后一个
  func add(x, y int) int {
    return x + y
  }

  // 无返回值可以省略返回值类型
  func sub(x, y int) {
    fmt.Println(x - y)
  }

  // 可以返回多个值
  func swap(x, y int) (int, int) {
    return y, x
  }

  // 函数可以作为值
  func complex(x int, y int, transform func(int) int) int {
    return transform(x) + transform(y)
  }

  func main() {
    fmt.Println(add(1, 2))
    sub(1, 2)
    fmt.Println(swap(1, 2))

    plus := func(x int) int {
      return x * 10
    }

    fmt.Println(complex(1, 2, plus))
  }
```

### 4.7 chapter7 : 高级类型 - 数组

go语言中使用切片(slice)类型实现动态数组,其底层还是由数组实现的,但更加常用

```go
  // chapter7: 高级类型 - 数组
  arr := [5]int{1, 2, 3, 4, 5} // 数组空间固定且不可变
  fmt.Println(arr)

  arr2 := make([]int, 0) // 使用切片类型(可变数组) 使用make函数实现
  arr2 = append(arr2, 1, 2, 3, 4, 5)
  fmt.Println(arr2)

  arr3 := []int{1, 2, 3, 4} // 字面值创建切片
  arr3[0] = 5
  fmt.Println(arr3)
```

### 4.8 chapter8 : 高级类型 - Map(键值对)

```go
  myMap := map[string]int{
    "a": 1,
    "b": 2,
    "c": 3,
  }
  fmt.Println(myMap) // map[a:1 b:2 c:3]

  // 不使用初始值可以使用make函数
  myMap2 := make(map[string]int)
  myMap2["a"] = 1
  myMap2["b"] = 2
  fmt.Println(myMap2)
```

### 4.9 chapter9 : 高级类型 - 结构体

```go
  type Point struct {
    X int
    Y int
  }

  // 结构体方法(这里并不生效,因为是按照值拷贝了结构体)
  func (p Point) SetPoint(x, y int) {
    p.X = x
    p.Y = y
  }

  func (p *Point) SetPoint2(x, y int) {
    p.X = x
    p.Y = y
  }

  main() {
    p := Point{1, 2}
    fmt.Println(p) // {1, 2}
    p.X = 3
    fmt.Println(p) // {3, 2}

    //指针
    q := p // 按值进行拷贝
    p.X = 10
    fmt.Println(p) // {20, 2}
    fmt.Println(q) // {3, 2}

    r := &p // 按指针进行拷贝
    p.X = 20
    fmt.Println(p)  // {20, 2}
    fmt.Println(*r) // {20, 2}

    r.Y = 10        // 修改指针中的值,省略*号
    fmt.Println(p)  // {20, 10}
    fmt.Println(*r) // {20, 10}

    p.SetPoint(1, 2)
    fmt.Println(p) // {20, 10}  不生效,因为是值拷贝

    p.SetPoint2(1, 2)
    fmt.Println(p) // {1, 2}
  }
```

### 4.10 chapter10 : 接口

go语言中接口可以为结构规定一组要实现的方法, Go的结构体要实现接口, 只要实现接口中的同名方法即可.

```go
type Shape interface {
  Print() // 无需 func 关键字
}

type Rectangle struct {
}

func (r Rectangle) Print() {
  fmt.Println("Rectangle")
}

type Triangle struct {
}

func (t Triangle) Print() {
  fmt.Println("Triangle")
}

// 接口作为函数参数
func prinShape(s Shape) {
  s.Print()
}

func main() {
  var s Shape
  s = Rectangle{}
  s.Print()

  s = Triangle{}
  s.Print()

  prinShape(Rectangle{})
  prinShape(Triangle{})
}
```

### 4.11 chapter11 : 错误处理

go语言中通常使用`error`类型来处理错误, 许多函数都会返回两个值,一个是正常返回值,另一个是`error`类型, 如果`error`类型不为`nil`, 则表示发生错误, 可以通过`err.Error()`方法获取错误信息.

```go
  // chapter11: 错误处理
  n, err := fmt.Println("hello")
  if err != nil {
    fmt.Println(err.Error()) // 执行正常代码
  } else {
    fmt.Println(n) // 执行异常代码
  }
```

### 4.12 chapter12 : 多线程

```go
func main(){
  go func2()
  func1()

  // 并发
  ch := make(chan string)
  go func3(ch)
  res4 := <-ch  //管道数据读取

  go func4(ch)
  res3 := <-ch //管道数据读取

  fmt.Println(res3, res4) // "func4 func3"
}

func func1() {
  time.Sleep(500 * time.Millisecond) // 用于等待 func2 异步执行完毕
  fmt.Println("func1")
}

func func2() {
  fmt.Println("func2")
}

func func3(ch chan string) {
  ch <- "fun3" //数据写入管道
}

func func4(ch chan string) {
  ch <- "fun4" //数据写入管道
}
```

## 五 如何你决定要深入学习 Go, 下面资料可以参考

只列举我认为必看的文档,持续更新

- go 官网:<https://go-zh.org/>
- 切片的本质: <https://blog.go-zh.org/go-slices-usage-and-internals>
- Go Web 编程:<https://www.bilibili.com/video/BV1Xv411k7Xn/?p=1> (视频教程,杨旭)
- 一个很好的 Go 教程(可以当做查询工具) <https://www.topgoer.com/>
