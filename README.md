# 编写python程序流程

1. 使用交互式python测试代码

2. 组成python脚本

   将交互模式下测试好的代码放在一个python文件中

3. 封装成函数

   将脚本的输入、输出和某些参数作为函数变量，方便重复调用。

4. 写批处理脚本



## 使用交互式python测试代码

在交互式的python模式下，可以实时方便地查看变量，发现错误。

例如使用`pandas`读取一个excel表格时候，不清楚读出来的表格会是什么样子，

表格地index和columns会是怎样地取，有哪些数据是不需要的等等，这时可以

在交互模式下把读出来的表格立即显示出来。

### 推荐软件

ipython是优化的python交互模式包，界面和功能比原始的交互模式要好些，详细

信息可参考[IPython官网](ipython.org)。

IPython安装：

```bash
$ pip install ipython
```

IPython运行：

```bash
$ ipython
```