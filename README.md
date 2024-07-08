# LawLuo: A Chinese Law Firm co-run by LLMs

## 1. KINLED (Knowledge-INtensive LEgal Dialogue) Dataset
| Composition | No.Dialouge Entries |
|----------|--------|
|法律概念和术语解释对话    | 3125  |
| 司法解释情景问答     | 4382  |
| 法律判决文书问答     | 533 (estimate)  |
| 带有法律依据的情景问答     | 3026  |
| 法律咨询对话    | 995  |
| 法考问题解答对话     | 985  |

## 一次微调的权重文件 //由于文件过大，请直接使用OSS下载，具体操作方式如下
1.下载OSS至Windows操作系统，详细下载链接请见：https://gpushare.com/docs/data/download/
2.登录OSS //oss login 
3.账号：18965335880  // Paswd：20021226#Dcx
4.执行命令： oss cp oss://Lora_Output.zip /Path/to/you/pc
5.Lora 代码也在里面，如需要请执行命令： oss cp oss://ChatGLM3/ChatGLM3.zip /Path/to/you/pc
6.配置文件请见 Lora.ymal

## 免责声明
1. 本项目中的所有内容与资源**仅限于学术研究用途，严禁应用于任何商业以及其他可能危害社会或造成不良影响的用途**。
2. 本项目中的法律术语及其概念数据来自**中文法律术语汇编**，网址：https://terms.legalhub.cn
3. 本项目中的法律问答数据集由**Kimi**和**ChatGPT**生成，**未经法律权威或专业人士严格验证，可能会存在些许错误内容，请诸位在使用时仔细判断与甄别，严禁应用于真实的法律相关用途或其他用途**。
4. 本项目**不承担任何法律责任**。
