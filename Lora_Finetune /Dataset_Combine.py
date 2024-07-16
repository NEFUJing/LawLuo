import json
import random

#将数据集转换成ChatGLM要求的微调数据集格式
# 文件路径
input_file = 'KINLED _Train.json'
output_file = 'KINLED _Train_Format.json'

# 读取文件并逐行处理
new_data = []
with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)  # 读取整个JSON文件

for entry in data:
    try:
        conversation = {
            'conversations': [
                {'role': 'user', 'content': entry["question"]},
                {'role': 'assistant', 'content': entry["answer"]}
            ]
        }
        new_data.append(conversation)
    except KeyError as e:
        print(f"键错误，缺少{e}，跳过此条目: {entry}")

# 随机选取 6000 条数据
#sampled_data = random.sample(new_data, min(6000, len(new_data)))

# 将新的数据集保存到一个新的 JSON 文件中
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(sampled_data, f, ensure_ascii=False, indent=4)

print("数据转换完成，并保存到 LawConv.json 文件中")
