# Reflex test repo

测试一下 reflex (纯 python )写网页, 看起来效果还可以.

见: https://jweb.reflex.run/

网站模板可以直接使用 reflex 官网的仓库, 不要用本仓库, 见: 

https://github.com/reflex-dev/reflex-web

目前发现的问题
- 热更新很慢, 2-3秒网页不多的话, 网页很多就更慢了
- 跟后端失去连接,网页的交互就会失效(比较是通过 websocket 跟后端交互的)
- 生态一般, 唯一比较好用的模板是官方网站,其他模板都比较简单.
- 有不少bug... 比如python代码中删除某个页面后, react 对应的页面还在... 一般这种情况下把 `.web` 删除掉就行

但总的来说,写起来很简单,学习成本低,可以用官方的hosting快速部署,适合小型项目.

不过前端写起来挺像 react 的, 但要用 react 的组件还需要[包装一层](https://reflex.dev/docs/wrapping-react/overview/)

最大的好处是省去了写前端跟后端交互的繁琐代码 boilerplate code (不用手写各种 crud 的api), 写起来很快