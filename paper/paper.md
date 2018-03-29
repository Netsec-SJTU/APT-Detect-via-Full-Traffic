基于全流量的APT检测技术研究

摘要

随着互联网的发展普及，网络对社会的影响越来越大，网络安全问题也越来越突出，并逐渐成为互联网及各项网络服务和应用进一步发展所亟需解决的问题。本课题研究了基于全流量的APT攻击检测技术，通过特征提取、流量分析等手段，实现了APT攻击的检测。

关键词 高级持续性攻击 攻击检测 网络空间安全

Research on APT Inspection Technology Based on Full-flow

Abstract

With the popularization of the Internet, the impact of the Internet on society has become greater and greater. The problem of network security has also become more and more prominent, and it has gradually become an urgent problem for the further development of the Internet and various network services and applications. This topic studies the APT attack detection technology based on full traffic, and implements APT attack detection through feature extraction and traffic analysis.

Key words: APT, Attack Detection, Cyberspace Security
第一章 绪论

1.1 课程的研究背景及意义

APT（高级持续威胁）是一种新兴的攻击类型。攻击者可能会结合网络钓鱼、恶意软件、社会工程、零日攻击和僵尸网络等一系列手段来完成一次APT攻击，这使得攻击相当难以检测。
APT攻击的出现从本质上改变了全球网络空间安全形势。近年来APT攻击已演化为国家网络空间对抗的新方式，它针对诸如政府部门、军事机构、商业企业、高等院校等具有战略战术意义的重要部门，采取多种攻击技术和攻击方式，以获取高价值敏感情报或破坏目标系统。目前已公开的APT攻击，诸如Stuxnet[2]、Duqu[3]、Flame[4]等都对互联网造成了重大危害。因此，研究一项新技术来实现对APT攻击的检测是有意义的。

1.2 国内外研究现状

``TODO``

1.3 课题研究内容

本课题的研究内容为基于全流量的APT检测技术研究，最终目标是使用流量提取、沙箱执行以及特征匹配技术来实现对APT攻击的检测。主要的研究内容分为四个方面

1.3.1 APT攻击技术研究

APT攻击的特征和常用手法。

1.3.2 流量提取技术

从流量中提取文件和HTTP请求流。

1.3.3 沙箱执行技术

利用沙箱执行快速准确的分析二进制可执行文件。

1.3.4 特征匹配技术

利用已知的数据库和机器学习的方式进行特征匹配。

1.4 论文结构安排

``TODO``
第二章 APT攻击技术研究

2.1 APT攻击实例

2.1.1 Stuxnet

``TODO``

2.1.2 Flame

``TODO``

2.1.3 Duqu

``TODO``

2.2 APT攻击技术特征

2.2.1 针对性
APT攻击的攻击手段和攻击方案均针对特定的攻击对象和目的设计。例如，代码植入阶段的钓鱼程序大多是根据特定用户的行为习惯而设计的，且恶意代码的运行环境也都适应于目标主机的操作系统。
 
2.2.2 持续性

APT攻击的实施过程包含多个阶段，攻击者多采用逐层渗透的方式突破高安全等级网络的防御系统，整个攻击过程经常长达数月到数年。
 
2.2.3 伪装性

APT攻击者经常采用多种方式来伪装自己的行为，进而规避检测。例如，攻击者在保持访问阶段和扩展行动阶段分别通过伪造合法签名和模仿正常行为的方式进行伪造

2.2.4 间接性

APT攻击过程中经常使用第三方和中间站作为媒介，而非传统的点到点攻击模式。例如，代码传入阶段的第三方钓鱼网站、初次入侵
阶段的间接执行恶意代码和保持访问阶段的远程访问工具都是 
APT攻击间接性的体现。
 
2.2.5 共享性

APT攻击组织之间互相贩卖漏洞攻击码及搭配的恶意软件在网络中越来越普遍，这表明各攻击组织之间的资源共享性逐步增强。

2.3 本章小结

第三章 攻击检测技术原理

3.1 流量提取技术

3.1.1 HTTP流提取

3.1.2 文件提取

3.2 基于特征匹配的检测

3.2.1 开源waf
3.2.2 攻击工具
3.2.3 APT IoC

3.3 基于沙箱的动态分析

3.4 基于机器学习的攻击检测 

3.4.1 Web请求

3.4.2 Malware

3.4.3 C&C

4. APT攻击检测技术

4.1 黑客攻击识别模型

4.2 已知APT攻击识别模型

4.2.1 各APT攻击特征

4.3 未知APT攻击识别模型

4.4 本章小结

第五章 实验

5.1 常规攻击识别实验

5.1.1 攻击流量重放

5.1.2 攻击工具攻击

5.2 已知攻击识别实验

5.2.1 APT流量重放

5.3 未知攻击识别实验

5.3.1 机器学习实验

5.3 本章小结

第六章 总结与展望

6.1 总结

6.2 展望
参考文献
谢辞

感谢老师在本课题遇到问题时，悉心解答；
感谢等文献作者在入侵检测领域做出的贡献；
感谢父母在本课题研究过程中的关心；
感谢交大与电院给我这次展示与锻炼的机会。

Research on APT Inspection Technology Based on Full-flow
