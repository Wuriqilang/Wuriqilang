---
external: false
title: "很基础,但很实用——Meta标签"
description: 今天来说一个很基础但是很实用的 Html 功能，以及很多前端面试中要考察的基础内容 —— meta 标签。
date: 2020-06-02 16:28:17
categories: [前端拾遗]
image: https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/meta.jpg
---

今天来说一个很基础但是很实用的 Html 功能，以及很多前端面试中要考察的基础内容 —— meta 标签。

直接切入正题，meta 标签是非常有用的辅助性标签，所有浏览器都能识别它。meta 标签的内容并不会显示出来，但是会被浏览器识别。浏览器识别 meta 数据是将其识别为“metadata”（中文范围为元数据，但我觉得词不达意，容易造成误解，我们就仍旧沿用其英文名称“metadata”）

> The <meta> tag provides metadata about the HTML document. Metadata will not be displayed on the page, but will be machine parsable.

meta 标签通常被用来定义页面的说明，关键字，修改时间等。meta 标签中的信息给浏览器或搜索引擎以实现一些特定功能。

> Meta elements are typically used to specify page description, keywords, author of the document, last modified, and other metadata.

需要说明的是，meta 标签是通过 name 与 content 来定义 metadata 数据的，所以说 metadata 是一种“名值对”的数据。

meta 有两个属性：

- name：用于描述网页，它是 metadata“名值对”数据中的“名”，name 属性确定需要描述的项目后，content 填入其具体描述。
- http-equiv：equivalent 是“相当于”的意思，http-equiv 相当于 http 文件头，其定义项会加入到 http 请头中，实现一些特定的效果。

那么，meta 有哪些好的应用场景呢？（本文仅会对常用的 meta 属性进行说明与列举，力求以解决问题为主要目的，如果想了解更多，请穿越这座传送门：[html 头部 meta 标签汇总](https://www.jianshu.com/p/8d28e5130ab2)

## 1.移动端适配

```html
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1" />
```

解释一下：

- viewport 是指 web 页面上用户的可见区域。
- width=device-width 是指 css 像素等于设备最佳像素（即占满屏幕），不同设备的 divice-width 是不同的
- initial-scale=1 是指初始缩放比例
- initial-scale=1.0 是指初始化的时候缩放大小是 1，也就是不缩放。
- user-scalable=0 是指禁止用户进行缩放。
- maximum-scale=1.0 是指用户最大缩放大小是 1，其实在禁止用户缩放以后，这一句可以省略。

通常来说我们了解这些就绰绰有余了，但是这里引出了一个重要的概念：CSS 像素。我觉得有责任把这个 meta 的实现原理说清楚，先明确几个概念：

- **设备像素 / 物理像素（physical pixels）**
  是指屏幕的实际物理像素点，比如普通的 1080P 手机是 1920\*1080 的像素分辨率，那么代表它纵向有 1920 个物理像素点，横向有 1080 个物理像素点。
- **CSS 像素（css pixel） / 密度独立像素（density independent pixels - dip）**
  CSS 像素是 web 编程中的概念，是抽象的，不是实际存在的。它是独立于设备用于逻辑上衡量像素的单位，所以又叫密度独立像素。dip 有时候也缩写为 dp 。
  屏幕尺寸
  指屏幕的对角线长度，单位是英寸（inch），1 英寸 = 2.54 厘米。常见屏幕尺寸有 5.0、5.5 和 6.0 等。
- **屏幕像素密度（pixels per inch - ppi）**
  指屏幕上每英寸可以显示的物理像素点的数量。比如 iPhone6 Plus 是 5.5 英寸，分辨率（也就是物理像素）是 1920\*1080 像素，那么它的 ppi = √(19202+10802) / 5.5 ≈ 401ppi 。也就是说它每英寸可以显示 440 个物理像素点。
- **设备像素比**
  指物理像素和密度独立像素的比值。
  window.devicePixelRatio = 物理像素 / dip。
  可以通过 window.devicePixelRatio 获得，该属性被所有 WebKit 浏览器以及 Opera 所支持。

譬如 iphone6（虽然过时了，但是这个例子最经典），他的硬件宽度是 750 个像素，device-width 是 375 像素，所以我们在 css 将宽度定义为 375px 时就占满屏幕了，这就是我们经常听说的“二倍图”
这个时候，前端开发时候如果按照设计图（设计图通常是 PC 端）中给出的尺寸在移动端定义一张图片的宽度，其真实宽度就会放大二倍，从而产生失真。

## 2.网页内容说明

我们可以将网页的主要内容进行定义，提供给搜索引擎，便于 SEO。

```html
//标题
<meta name="title" content="优酷-这世界很酷" />
//关键词
<meta name="keywords" content="视频,视频分享,视频搜索,视频播放" />
//描述
<meta name="description" content="京东JD.COM-专业的综合网上购物商城,销售家电、数码通讯、电脑、家居百货、服装服饰、母婴、图书、食品等数万个品牌优质商品.便捷、诚信的服务，<br>为您提供愉悦的网上购物体验!" />
//作者
<meta name="author" content="Wuriqilang" />
//版权信息
<meta name="copyright" content="本页版权 www.qidian.com 起点中文网所有。All Rights Reserved" />
```

注意这里 title,keywords,descripiton 几个属性对于搜索引擎来说权重是逐渐减小的。
至于这几个属性在搜索引擎中优化 SEO 的原理那就又是一个故事了,以后有空时候可以聊一聊.

## 3.字体编码

字体编码这个属性就像纸质现金,它很重要,在以前最重要,但是随着在线支付的兴起,它仍旧很重要,但是人们不再需要时刻都把它带在身上了.
我们知道字体编码是用来规范 html 文档编码的就行了

```html
<meta charset="UTF-8" />
```

## 4.禁止识别数字为电话号码

```html
<meta name="format-detection" content="telephone=no" />
```

## 5.指定渲染内核(有些国产浏览器会使用双核)

```html
<meta name="renderer" content="webkit" />
```

本文仅会对常用的 meta 属性进行说明与列举，力求以解决问题为主要目的，如果想了解更多，请穿越这座传送门：[html 头部 meta 标签汇总](https://www.jianshu.com/p/8d28e5130ab2)
