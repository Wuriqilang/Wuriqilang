---
title: "VUE的生命周期函数——详解"
description: 除了数据双向绑定、virtual Dom 等偏向于底层实现的知识点外，vue 的生命周期函数作为应用层层面里最核心的问题，其重要程度随着你的能力提升会不断提高。
date: 2020-06-01 09:38:11
tags: [vue]
categories: [前端拾遗]
image: https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/vuelivecycle.jpg
---

除了数据双向绑定、virtual Dom 等偏向于底层实现的知识点外，vue 的生命周期函数作为应用层层面里最核心的问题，其重要程度随着你的能力提升会不断提高。

## 1.定义

每个 Vue 实例在被创建时都要经过一系列的初始化过程——例如，需要设置数据监听、编译模板、将实例挂载到 DOM 并在数据变化时更新 DOM 等。同时在这个过程中也会运行一些叫做生命周期钩子的函数，这给了用户在不同阶段添加自己的代码的机会。

![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1590975920584.png)

| 生命周期钩子  | 组件状态                                                                                                                    | 最佳实践                                                     |
| ------------- | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| beforeCreate  | 实例初始化之后，this 指向创建的实例，不能访问到 data、computed、watch、methdos 上的方法和数据                               | 常用于初始化非响应式变量                                     |
| created       | 实例创建完成，可访问 data、computed、watch、methods 上的方法和数据，未挂载到 DOM，不能访问\$el 属性，\$ref 属性内容为空数组 | 常用于简单的 ajax 请求，页面的初始化                         |
| beforeMount   | 在挂载开始之前被调用，beforeMount 之前，会找对对应的 template，并编译成 render 函数                                         | -                                                            |
| mounted       | 实例挂载到 DOM 上，此时可以通过 DOM API 获取到 DOM 节点，/$ref 属性可以访问                                                 | 常用于获取 VNode 信息和操作，ajax 请求                       |
| beforeupdate  | 响应式数据更新时调用，发生在虚拟 DOM 打补丁之前                                                                             | 适合在更新之前访问现有的 DOM，比如手动移除已添加的事件监听器 |
| updated       | 虚拟 DOM 重新渲染和补丁之后调用，组件 DOM 已经更新，可以执行依赖于 DOM 的操作                                               | 避免在这个钩子函数中操作数据，可能陷入死循环                 |
| beforeDestroy | 实例销毁之前调用。这一步，实例仍然完全可用，this 仍能获取到实例                                                             | 常用于销毁定时器、解绑全局事件、销毁插件对象等操作           |
| destroyed     | 实例销毁后调用，调用后，Vue 实例指示的所有东西都会解绑定，所有的事件监听器会被移除，所有的子实例也会被销毁                  | -                                                            |

注意：

- created 阶段的 ajax 请求与 mounted 请求的区别：前者页面视图未出现，如果请求信息过多，会导致页面长时间处于白屏状态。

接下来我们从流程和代码两个方面来说明 Vue 的生命周期：

## 2.Vue 生命周期流程

1. 当我们创建一个 Vue 实例，即 new Vue()，首先会执行 init 函数，在 init 函数中会执行第一个 beforeCreated 钩子函数。
   - 执行 beforeCreate 之前，先执行 mergeOptions 函数，得到/$options 选项，并把这个设置成 Vue 实例的一个属性。
   - beforeCreate，设个阶段生成生命周期以及一些数据的初始化。
2. 接下来执行 created：这个阶段数据已经绑定在实例上，但是还没有挂载对象。
3. created 之后，判断 instance（实例）是否含有'el'这个 options 选项。
   - 如果没有，它会调用 vm./$mount(el) 这个方法，然后执行下一步，意味着它会停止编译，生命周期结束。
   - 如果有，判断是否含有 template 属性，如果有的话 Vue 将 template 解析成一个 render function，如果没有 template 选项它将外部的 HTML 作为模板编译。
4. 当 render function 之后才会执行 beforeMounted，

这里说的不明白， 以后重写

## 3. 单个组件的生命周期

```html
<template>
  <div id="single">
    <h3>单个组件的生命周期函数</h3>
    <button @click="singleData+= 1">更新{{singleData}}</button>
    <button @click="handleDestroy">销毁</button>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        singleData: 1,
      };
    },
    //生命周期
    beforeCreate() {
      this.compName = "single"; //定义非响应式变量
      console.log(`--${this.compName}--befroeCreate`);
    },
    created() {
      console.log(`--${this.compName}--created`);
    },
    beforeMount() {
      console.log(`--${this.compName}--beforeMount`);
    },
    mounted() {
      console.log(`--${this.compName}--mounted`);
    },
    beforeUpdate() {
      console.log(`--${this.compName}--beforeUpdate`);
    },
    updated() {
      console.log(`--${this.compName}--updated`);
    },
    beforeDestroy() {
      console.log(`--${this.compName}--beforeDestroy`);
    },
    destroyed() {
      console.log(`--${this.compName}--destroyed`);
    },
    methods: {
      handleDestroy() {
        this.$destroy();
      },
    },
  };
</script>
```

当组件加载与初始化时：

![](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/posts/1590979391076.PNG)

当更新组件时：

> --single--beforeUpdate
> --single--updated

组件销毁时：

> --single--beforeDestroy
> --single--destroyed

从结果我们可以看出：

1. 初始化组件时，仅执行了 beforeCreate/Created/beforeMount/mounted 四个钩子函数
2. 当改变 data 中定义的变量（响应式变量）时，会执行 beforeUpdate/updated 钩子函数
3. 当切换组件（当前组件未缓存）时，会执行 beforeDestory/destroyed 钩子函数
4. **初始化和销毁时的生命钩子函数均只会执行一**次，beforeUpdate/updated 可多次执行

## 4.父子组件之间传值

父组件：

```html
<template>
  <div id="father">
    <button @click="handleDestroy">父组件销毁</button>
    <child compName="child"></child>
  </div>
</template>

<script>
  import child from "../components/Child.vue";
  export default {
    name: "Father",
    components: {
      child,
    },
    //生命周期
    beforeCreate() {
      this.compName = "father"; //定义非响应式变量
      console.log(`--${this.compName}--befroeCreate`);
    },
    created() {
      console.log(`--${this.compName}--created`);
    },
    beforeMount() {
      console.log(`--${this.compName}--beforeMount`);
    },
    mounted() {
      console.log(`--${this.compName}--mounted`);
    },
    beforeUpdate() {
      console.log(`--${this.compName}--beforeUpdate`);
    },
    updated() {
      console.log(`--${this.compName}--updated`);
    },
    beforeDestroy() {
      console.log(`--${this.compName}--beforeDestroy`);
    },
    destroyed() {
      console.log(`--${this.compName}--destroyed`);
    },
    methods: {
      handleDestroy() {
        this.$destroy();
      },
    },
  };
</script>
```

子组件：

```html
<template>
  <div id="child">
    <h3>单个组件的生命周期函数</h3>
    <button @click="singleData+= 1">更新{{singleData}}</button>
    <button @click="handleDestroy">销毁</button>
  </div>
</template>

<script>
  export default {
    name: "child",
    props: {
      compName: String,
    },
    data() {
      return {
        singleData: 1,
      };
    },
    //生命周期
    beforeCreate() {
      //this.compName = 'single';  //定义非响应式变量
      console.log(`--props的值未获取，不知道compName是啥--befroeCreate`);
    },
    created() {
      console.log(`--${this.compName}--created`);
    },
    beforeMount() {
      console.log(`--${this.compName}--beforeMount`);
    },
    mounted() {
      console.log(`--${this.compName}--mounted`);
    },
    beforeUpdate() {
      console.log(`--${this.compName}--beforeUpdate`);
    },
    updated() {
      console.log(`--${this.compName}--updated`);
    },
    beforeDestroy() {
      console.log(`--${this.compName}--beforeDestroy`);
    },
    destroyed() {
      console.log(`--${this.compName}--destroyed`);
    },
    methods: {
      handleDestroy() {
        this.$destroy();
      },
    },
  };
</script>
```

初始化组件时，打印：

> --father--befroeCreate
> --father--created
> --father--beforeMount
> --props 的值未获取，不知道 compName 是啥--befroeCreate
> --child--created
> --child--beforeMount
> --child--mounted
> --father--mounted
> 数据更新时
> child--beforeUpdate
> --child--updated
> 组件销毁时
> --father--beforeDestroy
> --child--beforeDestroy
> --child--destroyed
> --father--destroyed

从打印结果可以看出:

1. 仅当子组件完成挂载后，父组件才会挂载
2. 当子组件完成挂载后，父组件会主动执行一次 beforeUpdate/updated 钩子函数（仅首次）
3. 父子组件在 data 变化中是分别监控的，但是在更新 props 中的数据是关联的（可实践）
4. 销毁父组件时，先将子组件销毁后才会销毁父组件
