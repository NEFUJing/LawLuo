import time
import requests
import json
import re

# 输入你的API密钥
api_key = 'sk-b9mNiwYxacdydc8ua5XDz4GGgFGxq4E2E8cpIhWmftBZYqqo' # api改成你自己的
url = "https://api.moonshot.cn/v1/chat/completions"  # url不变

# 读取JSON文件，更改文件名即可
with open('data.json', 'r', encoding='utf-8') as f:
    legal_terms = json.load(f)

# 生成情景对话函数，更改提示词即可
def generate_scenario(title, classification, contents):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }
    payload = {
        "model": "moonshot-v1-128k",  
        "messages": [
            {"role": "system", "content": "你是一个法律专家。"},
            {"role": "user", "content": f"请阅读以下法律判决文书，根据判决书内容提出三个法律相关的专业问题，然后给出回答。请按照按以下格式生成内容：\n\n问题1: [问题描述]\n\n回答1: [回答描述]\n\n问题2: [问题描述]\n\n回答2: [回答描述]\n\n问题3:根据以下判决书内容\n内容: {contents}，[问题描述]\n\n回答3: [回答描述]\n\n问题4: [问题描述]\n\n回答4: [回答描述]\n\n问题5: [问题描述]\n\n回答5: [回答描述] \n\n\n标题: {title}\n类别: {classification}\n内容: {contents} "}
        ],
        "max_tokens": 1000
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    # 检查API限流错误，因为kimi会限流
    if response.status_code != 200:
        response_data = response.json()
        if "error" in response_data and "rate_limit_reached_error" in response_data["error"]["type"]:
            print(f"API限流错误: {response_data['error']['message']}")
            time.sleep(5)  
            return generate_scenario(title, classification,contents)  
        else:
            print(f"请求失败，状态码：{response.status_code}")
            print(f"错误内容：{response.text}")
            return None
    
    response_data = response.json()
    
    # 检查 'choices' 键并解析情景对话
    if 'choices' in response_data and len(response_data['choices']) > 0:
        content = response_data['choices'][0]['message']['content']
        # 更改相关信息以匹配问题和回答
        questions = re.findall(r'问题\d+: (.+)', content)
        answers = re.findall(r'回答\d+: (.+)', content)
        if len(questions) == 5 and len(answers) == 5:
            return list(zip(questions, answers))
        else:
            print(f"格式错误或找不到足够的问题和答案: {content}")
    else:
        print("响应JSON中没有找到'choices'键或其值不是一个列表。")
    return []

# 生成情景对话
qa_list = []
for entry in legal_terms:
    title = entry['标题']
    classification = entry['文书类型'] #按照字段名字更改
    # num = entry['num'] 
    contents = entry['文书内容'] #按照字段更改
    qa_pairs = generate_scenario(title, classification, contents)
    for question, answer in qa_pairs:
        qa = {
            "question": question.strip(),
            "answer": answer.strip()
        }
        qa_list.append(qa)

# 保存到新文件，更改文件名即可
if qa_list:
    with open('判决文书问答.json', 'w', encoding='utf-8') as f:
        json.dump(qa_list, f, ensure_ascii=False, indent=4)
else:
    print("没有生成任何问答。")
