# 基于全流量的APT检测技术研究

该repo主要用于存储项目相关代码，目录结构如下

- common 常用库
- document 必要的说明文档
- ml
    - Fwaf
        - 基于机器学习的Web应用Waf
- parser
    - http报文解析
- install 安装脚本
    - ``install*.sh`` 安装脚本
- paper 论文
- server
    - 项目网站
- yara-rules yara规则
    - 具体说明见目录下README.md
- aptd.py 调用脚本

# 实现逻辑

- 读入pcap
    - 访问频率统计
        - (time, srcip, dstip) to DB
    - tcp重组包
        - http解析
            - tcpflow
        - smtp解析
            - tcpflow
        - ftp解析
            - tcpflow
        - log tcp流
            - IoC匹配
    - udp包
        - dns解析
            - dns特征扩展
            - log dns
            - IoC匹配
    - 文件提取
        - elf沙箱执行
            cuckoo
        - 其他文件提取特征
        - IoC匹配

- 数据库写什么
    - 被发现的traffic
    - 被发现的malware
    - ip访问频度


## 安装

- 执行安装脚本安装依赖库
