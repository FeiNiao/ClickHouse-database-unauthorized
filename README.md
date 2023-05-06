# ClickHouse-database-unauthorized
ClickHouse是一款开源的列式数据库，ClickHouse存在未授权访问漏洞，攻击者可利用该漏洞获取数据库的敏感信息

# 免责声明
使用本程序请自觉遵守当地法律法规，出现一切后果均与作者无关。

本工具旨在帮助企业快速定位漏洞修复漏洞,仅限授权安全测试使用!

严格遵守《中华人民共和国网络安全法》,禁止未授权非法攻击站点!

由于用户滥用造成的一切后果与作者无关。

切勿用于非法用途，非法使用造成的一切后果由自己承担，与作者无关。

# ClickHouse数据库未授权访问漏洞，攻击者可以利用该漏洞获取数据库的敏感信息

## 食用方法

`
python .\ClickHouseAPI-数据库接口未授权访问.py -f .\host.txt
`
##### 效果图

![image](https://user-images.githubusercontent.com/66779835/236594093-17311314-d25c-4348-9b00-055a99381dda.png)

疑似存在漏洞均以绿色标出，并且返回数据库的库名
![image](https://user-images.githubusercontent.com/66779835/236594123-d8b5924d-0f2c-4967-a280-581064024676.png)


