---
title: 数据库定义与命名规范
description: 本文档参考阿里巴巴MySQL数据库设计与命名规范
date: 2024-03-22
image: "https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2024-03/科技感.png"
author: 乌日其浪
categories: [数据库]
tags: [数据库, 规范]
---

1. **【强制】** 表名,字段名必须使用小写字母或数字,禁止出现数字开头,禁止两个下划线中间只出现数字.数据库字段命名修改的代价很大,字段名称需要慎重考虑.

   - 说明: MySQL在Windows下不区分大小写,但在Linux下区分大小写,因此数据库名\表名\字段名都不允许出现任何大写字.
   - 正例: `aliyun_admin`,`rdc_config`,`level3_name`,
   - 反例: `AliyunAdmin`,`RDCConfig`,`level_3_name`

2. **【强制】** 表达是与否概念的字段,必须使用`is_XXX`的命名方式,数据类型是`tinyint` ( `1` 表示是, `0` 表示否),其他数据类型不使用`is_XXX`的命名方式.

   - 正例: 表达逻辑删除的字段名`is_deleted` , 1表示删除,0表示未删除.

3. **【强制】** 表名不使用复数形式,与实体的概念对应.
4. **【强制】** 禁用保留字,如`desc`,`range`,`match`,`delayed`等.
5. **【强制】** 逐渐索引名为 `pk_字段名`;唯一索引名为`uk_字段名`;普通索引名为`idx_字段名`.
6. **【强制】** 小数类型为`decimal`,禁止使用`float`和`double`.
   - 说明: `float`和`double`在存储的时候,会丢失精度,在计算时,也会丢失精度.
7. **【强制】** `varchar`是可变长字符串,不预先分配存储空间,长度不要超过5000,如果长度超出则使用`text`
8. **【强制】** 表必备的三个字段: `id`, `gmt_create`, `gmt_modified`.
   - 说明: 其中id必须为主键,类型为`bigint`, gmt_create和gmt_modified为datetime类型
9. **【推荐】** 表的命名最好是 "业务名称\_表的作用",如:`alipay_task`,`trade_config`
10. **【推荐】** 库名与应用名尽量一致
