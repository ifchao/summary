___
- FileName: 20190114-ELK之Lucene.md
- Author: ihuangch -huangch96@qq.com
- Description: ---
- Create:2019-01-14 18:54:25
___

### Lucene
Lucene是一套用于全文检索和搜索的开放源代码程序库，由Apache软件基金会支持和提供。
Lucene提供了一个简单却强大的应用程序接口，能够做全文索引和搜索，在Java开发环境里
Lucene是一个成熟的免费开放源代码工具；就其本身而论，Lucene是现在并且是这几年，
最受欢迎的免费Java信息检索程序库。

### 基于Lucene的项目
- Apache Nutch: 提供成熟可用的网络爬虫
- Apache SOlr: 基于Lucene核心的高性能搜索服务器，提供JSON/Python/Ruby API
- Elasticsearch: 企业搜索平台，目的是组织数据并使其易于获取
- DocFetcher: 跨平台的本机文件搜索桌面程序
- Lucene.NET: 提供给.Net平台用户的Lucene类库的封装
- Swiftype: 基于Lucene的企业级搜索
- Apache Lucy: 为动态语言提供全文搜索的能力，是Lucene Java 库的C接口


### 基本概念
- index: 类似于数据库的表的概念，但是和传统表的概念会有很大的不同。传统关系型数据库或者NoSQL数据的表，在创建时至少要定义表的Scheme，定义表的主键或列等，会有一些明确定义的约束。而Lucene的index，则完全没有约束。
- Document(文档): 类似数据库内的行或者文档数据库内的文档的概念，一个index内会包含多个Document。写入
