文件夹

- APT apt攻击相关规则
- hash 文件hash

---

APT 规则文件命名

- 根据APT命名文件  ``.`` 使用 ``_`` 代替
- 未知的 用unknown_x
- hash文件中的 命名为 unknown_hash_x

---

meta命名

- ref 参考链接

---

特征命名

- directory // 目录 
- dirver // 驱动
- domain // 第几个用于识别的域名
- hash // 哈希
- file // 文件
- reg // 用于识别的注册表
- service // 服务

---

```
rule identifier : APT
{
    meta:
        ref = ""
    strings:
        $directory = "" nocase wide
        $dirver = "" nocase wide
        $domain = "" nocase wide
        $hash = ""
        $file = "" nocase wide
        $reg = "" nocase wide
        $service = "" nocase wide
    condition:
        all of them
        any of them
}
```