---
title: "HTML相关知识点"
description: "本文将从前端面试题目出发,总结 HTML 必须掌握的知识点."
date: 2020-05-23 21:06:33
categories: ["前端拾遗"]
tags: [HTML]
image: https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/htmlpoint.jpg
---

本文将从前端面试题目出发,总结 HTML 必须掌握的知识点.

### 1.前端开发应该注意那些 SEO

- 知识点：SEO
- 重要程度：★★★

#### SEO 的概念

SEO(Search Engine Optimization) 搜索引擎优化，是一种利用搜索引擎的搜索规则来提高目前网站在有关搜索引擎内的自然排名的方式。

- 合理设置 title，discripition，keywords：搜索对着三项的权重逐个减小。
  - title 强调重点即可，重要关键词不要超过 2 个，不同页面 title 要有所不同
  - descripition 把页面内容高度概括，长度适合，不同页面 descripition 不同
  - keywords 列出关键词即可
- 语义化的 HTML 代码
- 重要的内容放在 HTML 前面
- 重要内容不要使用 JS 输出
- 提高网站访问速度
- 非装饰性图片增加 alt

### 2.从输入 url 到浏览器渲染出页面发生了什么

- 知识点：DNS、页面渲染机制等
- 重要程度：★★★

1. 浏览器将 URL 交给 DNS 域名解析（现查找缓存，然后在 DNS 服务器递归查找）找到真实 IP。
2. 浏览器向服务器发出请求，简历 TCP/IP 连接。
3. 服务器交给后台处理完成后的数据，浏览器接收文件
4. 浏览器对加载的资源进行解析，简历 DOM 树，解析 CSS 后生成 Render 树
5. 渲染页面

### 3.HTML5 有哪些新的特性

HTML5 不再是 SGML 的子集，而是根据现代 WEB 应用的需求发展出了关于图像、多媒体、位置、存储、多任务处理等功能。其主要有以下新特性

####元素

- 新增了一些媒体控制元素 video 和 audio
- 新增了绘画 canvas
- 增加了一些语义化更好的标签 article footer header nav section
- 新增了一些表单控件：canlendar date time email url search
- 移除了一些元素 - 纯表现的元素 big center font 。。。 - 可用性具有负面影响的元素 frame frameset noframes ####数据保存
- 新增 localstorage 长期保存数据
- 新增 sessionStorage 浏览器关闭后自动删除 ####离线 WEB 应用
  页面缓存指的还是有网络状态下，而离线 web 应用指的是在没有网络状态可以运行应用。manifest 文件是核心，记录着哪些资源文件需要离线应用缓存，要使用 manifest，只需要在 html 标签中添加属性

```html
<html manifest="cache.manifest"></html>
```

cache.manifest 的文件格式如下

```vim
    CACHE MANIFEST
    #缓存的文件
    index.html
    test.js
    #不做缓存
    NETWORK
    /images/
    FALLBACK
    offline.html index.html
```

缓存的文件下面是当网络不可用时，文件直接从本地缓存读取，
NETWORK 下面的文件无论是否已经缓存，都要从网络中下载。
FALLBACK 后面，当无法获取到 offline.html，则转到 index.html。

####地理定位
h5 提供了 Geolocation API 访问地理位置，即通过 window.navigator.geolocation 来实现访问。这个对象有三个方法：

```javascript
getCurrentPosition();
watchPosition();
clearWatch();
```

页面第一次使用这个 api 需要获得用户许可, watchPosition 可以对位置变化事件进行监听。

### 4.W3C 标准

- 知识点：W3C 标准
- 重要程度：★★★★★

#### W3C 指定的 WEB 页面标准

- 标签闭合
- 标签小写
- 不乱嵌套
- 使用外链 css 和 js
- 结构行为与表现分离

### 5.html 语义化是什么？

- 重要程度：★★★

  1.利于用户阅读，样式丢失时仍然能让页面呈现清晰的结构。 2.利于 SEO，搜索引擎是根据标签来确定上下文和关键字的权重 3.便于其他设备解析，如盲人阅读器根据语义渲染网页 4.利于开发和维护，语义化代码更佳具有可读性，与 CSS3 关系更和谐
