---
external: false
title: "我做过哪些项目？"
description: 本文章下次更新时间 下次更新时
date: 2020-05-10 23:33:14
tags: [值得一读]
image: https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/xiangmu.png
---

> 2014 - 2020 ，两千多个披星戴月，收获良多。对个人负责、参与过的项目进行总结如下。

## 项目一： 设备智能管理系统（桌面应用程序）

- 项目描述：一套以发挥数据潜能为核心的智能制造解决方案。主要用于解决当前工厂生产运营中存在的人力、效率、方法、数据价值相关问题，最终帮助工厂向工业 4.0 转型。

- 个人工作职责：项目负责人，负责项目需求制定、程序开发、资源协调与业务推进。

- 实现技术：BS/CS 混合架构 + .NET Winform + MS SQL Server + LinQ + SpringBoot(部分 ServerAPI)；

![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1589153255940.png)

- 主要模块：设备监控、工艺监控、不良调查
  > ![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1589153107363.png)

> ![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1589153172425.png)

> ![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1589153182823.png)

- 项目难点：

      1. UI 样式 ：Winform作为一款20年前推出的框架，组件UI样式已经显得十分“呆板落伍”。
      - 解决方案：通过对 MetroFramework 框架的定制开发，实现了样式设计的现代化同时兼具Winform拖动组件设计的便捷性。

  ![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1589154078440.png)

      2. 代码执行效率：工业级应用在数据分析过程中要快速处理大量数据（M级），BS架构会极大增加服务器压力，CS架构下用户对于程序卡顿感知较强。

      - 解决方案：数据处理在客户端执行，保证了代码执行效率减少服务器开销。大量使用了多线程方案优化用户体验。

## 项目二： 数据透明化平台（Web）

- 项目描述：一套用于工厂数据可视化、展示固定报表，数据监控的 Web 应用。解决用户复杂的数据处理加工需求，减少重复低效的数据二次处理劳动。固化日报月报，帮助技术部获取实时数据。

- 个人工作职责：全栈开发，主要进行项目的需求检讨与开发。

- 实现技术：AngularJS + SpringBoot + Oracle + Primeng + echarts + d3js

![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1589154673790.png)

## 项目三：基于大数据技术的不良分析平台

- 项目描述：一个基于大数据技术的不良分析平台，将工业生产数据与检测数据进行全面联动，采用特定算法计算影响不良的相关因子，明确不良发生原因。为工厂提供不良监控、自主分析等功能。

- 个人工作职责：项目支援，主要进行项目的前端开发、性能调优。

- 实现技术：AngularJS + SpringBoot + 。。。（保密协议相关）

## 项目四：小程序（篇幅有限，将几款小程序合并一起说明）

- 智造之窗：一款用于企业智能制造项目改进、移动端数据展示、新闻、数据交互的微信小程序。
- i 创+提案平台：一款用于企业改善提案上报、审批、数据展示的微信小程序。
- 全员学习系统：用于单位全员学习、考试、学习情况评比、学习心得展示的钉钉小程序。
- 资产名片：用于企业固定资产管理、二维码标签自动生成、资产审批的微信小程序。
- 绩效时钟：用于单位全员绩效管理、任务分解、任务下发的微信小程序。

- 实现技术：小程序原生框架 + Koa2（Nodejs） + MySQL

![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1589385069512.png)

- 项目难点：
  1. 服务中台：小程序项目具有轻量化、数量多、基本数据(用户信息）一致的特点，为了保障应用的快速开发上线，减少重复代码。将人员信息、项目配置信息、页面配置等进行了服务端中台化。
  2. UI 组件：为保障项目统一性与页面美观，基于 ColorUI 开发了 XRUI 框架。通过 template 与 css 方式在保障项目美观的同时兼顾了框架的易用性与可拓展性。
  3. 移动端数据展示：小程序端因为其特定的框架结构，Echarts 等可视化工具无法直接使用。采用 Canvans 方式对 echarts 进行了定制化（基于 echarts for wx）保障了移动端数据可视化功能的执行效率。

![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1589157404629.png)

## 项目五：房车情报（已下线）

- 项目描述：一个为房车情报官方设计的房车展示、新闻展示、车型数据库网站。

- 个人工作职责：项目负责人，负责项目需求制定、程序开发。

- 实现技术：bootStrap + vue + koa2（nodejs） + mySql + sequelize

- 项目难点：
  1. 静态资源优化：新闻类咨询类网站存在大量静态资源且通常图片尺寸较大。采用 Gzip 压缩、上传压缩、CDN 等方式实现了静态资源的尺寸、访问速度优化。
  2. 首屏加载与 SEO 优化：单页应用存在首屏加载与 SEO 问题，通过首页服务度渲染、组件懒加载、Gzip、h5 语义化标签等方式对其进行了优化。

![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1589157977232.jpeg)

---

### 附：个人简历

![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1589125473530.jpg)

![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1589125514909.jpg)
