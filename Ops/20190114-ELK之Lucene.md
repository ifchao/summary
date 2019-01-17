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
- index（索引）: 类似于数据库的表的概念，但是和传统表的概念会有很大的不同。传统关系型数据库或者NoSQL数据的表，在创建时至少要定义表的Scheme，定义表的主键或列等，会有一些明确定义的约束。而Lucene的index，则完全没有约束。
- Document(文档): 类似数据库内的行或者文档数据库内的文档的概念，一个index内会包含多个Document。写入Index的Document会被分配一个唯一的ID，即Sequence Number（更多被叫做Docld）。
- Field（字段）: 一个Document会由一个或者多个Field组成，Field是Lucene中数据索引的最小定义单位。Lucene提供多种不同类型的Field，例如StringField、TextField、LongField或NumericDocValuesField等，Lucene根据Field的类型，来判断该数据要采用哪种类型的索引方式（Invert Index、Store Field、DocValues或N-dimensional等）。
- Term和Term Dictionary：Lucene中索引和搜索的最小单位，一个Field会由一个或多个Term组成，Term是由Field经过Analyzer（分词）产生。Term Dictionary即Term词典，是根据条件查找Term的基本索引。
- Segment: 一个INdex会由一个或多个sub-index构成，sub-index被称为Segment。Lucene的Segment设计思想，与LSM类似但又有些不同，继承了LSM中数据写入的优点，但是在查询上只能提供近实时而非实时查询。

