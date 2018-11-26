___
- FileName: Jenkins持续集成集成.md
- Author: ihuangch -huangch96@qq.com
- Description: ---
- Create:2018-11-22 11:45:52
___

### 1.相关概念
#### 1.1 持续集成(Continuous Integration)
大师Mratin Fowler对持续集成是这样定义的：持续集成是一种软件开发实践，即团队开发成员经常集成
他们的工作，通常每个成员至少集成一次，也就意味着每天可能会发生多次集成。每次集成都通过自动化
的构建（包括编译，发布，自动化测试）来验证，从而尽快的发现集成错误。许多团队发现这个过程可以
大大减少集成的问题，让团队能够更快的开发内聚的软件。  
**主要好处:**
- 1、快速发现错误。每完成一点更新，就集成到主干，可以快速发现错误，定位错误也比较容易。  
- 2、防止分支大幅偏离主干。如果不是经常集成，主干又在不断更新，会导致以后集成的难道变大，甚至难以集成。  
**持续集成的目的:**
- 让产品可以快速迭代，同时还能保持高质量。它的核心措施是，代码集成到主干之前，必须通过自动化测试。只要有一个测试用例失败，就不能集成。

<div align="center"> <img src="https://github.com/ihuangch/blog/blob/master/Ops/pic/ci.png" /> </div><br> 

总的来说：就是持续集成就是每天都把代码集成到同一个分支，然后经过编译，测试，打包之后将程序
保存(在一个新的仓库中)。

#### 1.2 持续交付(Continuous Delivery)
持续交付指的是：频繁的将软件的新版本，交付给质量团队或者用户，以供评审。如果评审通过代码就
进入生产阶段。  
持续交付可以看作持续集成的下一步。在持续集成的基础上，将集成后的代码，部署到更贴近真实运行
环境的（类生产环境）中。比如，我们完成单元测试后，可以把代码部署到连接数据库的staging环境中
进行更多的测试。如果代码没有问题，可以继续手动部署到生产环境中。  
持续交付强调的是，不管怎么更新，软件是随时随地的可以交付的。  

<div align="center"> <img src="https://github.com/ihuangch/blog/blob/master/Ops/pic/cd1.png" /> </div><br> 

#### 1.3 持续部署(Continuous Deployment)
持续部署是持续交付的下一步，指的是代码通过评审以后，自动部署到生产环境中。  

<div align="center"> <img src="https://github.com/ihuangch/blog/blob/master/Ops/pic/cd2.png" /> </div><br> 


### 2.Jenkins

