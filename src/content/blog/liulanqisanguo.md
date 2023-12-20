---
title: "浏览器内核的三国风云"
descripiton: 天下大势,分久必合,合久必分 —— 《三国演义》
date: 2020-07-01 09:02:04
tags: [值得一读]
categories: ["前端拾遗"]
image: https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/liulanqisanguo.PNG
---

> 天下大势,分久必合,合久必分 —— 《三国演义》

作为一名前端开发工程师，总会在各种文档的字里行间中看“内核”，“引擎”等名词，看了许多文章，仍然是对其中一些概念懵懵懂懂，譬如“Chromium 和 Blink 是什么关系？Chromium 和 Chrome 是什么关系？”这直接导致我给同事吹牛时底气不足。

> 犹豫，就会败北。尤其是在吹牛的时候 —— 《只狼：影逝二度》

![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1593566832242.jpg)

## 一、最基本的概念：浏览器，内核，引擎

- 浏览器：用来检索、展示以及传递 Web 信息资源的应用程序。记住：**浏览器是一种产品**。譬如 Chrome，Chromium，FirFox，Safiar，IE，360，QQ 。。。
- 内核：驱动浏览器运行的核心部分。他包括**JS 引擎与渲染引擎**。但是随着 JS 的发展，JS 引擎也愈发显得独立于复杂，浏览器内核就倾向于单指渲染引擎。但就目前而言，多数浏览器内核仍然包括了 JS 引擎与渲染引擎（譬如 Blink 内核），为了便于理解，本文的观点是：**内核包括 JS 引擎与渲染引擎**。譬如 Blink，Webkit，Gecko
- 引擎：
  - JS 引擎：专门处理 JavaScript 脚本的虚拟机（简单来说就是能够运行 JS 的环境）。
  - 渲染引擎（也可以叫排版引擎或图像引擎）：对 HTML 文档进行解析并将其显示在页面上的工具。

浏览器、内核、引擎的关系可以用下图所示：

![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1593573021116.png)

还有一些遗失在前端发展历史进程中或者市场使用率很低的浏览器与内核（IE，EdgeHtml，Netscape ...) 为了文章简洁且具有现实意义，本文就不做讨论了，让我们向参与这些项目的程序员致敬。

![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1593573273158.jpg)

## 二、浏览器的三国大势

视频展示了 2009 年到 2020 年各浏览器的市场占用情况，风云变幻，百家争鸣。[视频来源-bilibli Data_Fun](https://www.bilibili.com/video/BV1iK41157eK?from=search&seid=8186579024934449220)

<div class="aspect-ratio">
<iframe src="https://player.bilibili.com/player.html?aid=498000935&bvid=BV1iK41157eK&cid=187449223&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" sandbox="allow-top-navigation allow-same-origin allow-forms allow-scripts"> </iframe></div>

作为一名以解决问题为核心的工程师，我们不必关心浏览器战争背后的故事，我们知道就目前而言，对于前端开发者来说我们主要需要对 Blink 与 Webkit 内核的浏览器做适配就足够了（该结论写于 2020.7.1）

**未来？**随着 Edge 开始基于 Chromium 开发，浏览器内核的发展呈现逐渐一家独大的趋势。但是我们也应该看到为了应对移动端的发展，各家大厂也在研发新的浏览器，或是更加关注隐私（FireFox Focus），或是针对安卓进行了底层优化，亦或是针对自家生态的定制（微信 x5）。
同时，随着 Http3，WebAssembly，更快的网速，更复杂的 WebApp 交互需求，浏览器的变化仍未定型。身为一名开发工程师，我庆幸自己生活在这样一个时代。

> 有时候，不确定就代表潜力。

## 三、为什么要写这篇文章？

这篇文章似乎有一些标题党，其实我本身并不想讨论关于浏览器大战的细节与历史，这些历史也无法对实际工作产生比较大的作用，我仅仅是通过这篇文章来厘清浏览器、内核、引擎之间的关系。为后续研究浏览器内核渲染机制，乃至 Vue Virtual Dom，nextTick 的作用原理做铺垫。
