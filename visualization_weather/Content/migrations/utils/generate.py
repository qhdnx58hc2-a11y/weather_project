import uuid

from openai import OpenAI

# client = OpenAI(
#     api_key="0ad31a37f185576579a1fd201b610379.mpv5pTFPrxyO2QC3",
#     base_url="https://open.bigmodel.cn/api/paas/v4/"
# )
#
# completion = client.chat.completions.create(
#     model="glm-4-air",
#     messages=[
#         {"role": "system", "content": "关于计算机的考试"},
#         {"role": "user",
#          "content": "生成一道单选题"}
#     ],
#     top_p=0.7,
#     temperature=0.9
# )
#
# print(completion.choices[0].message.content)

def evaluate(content):
    client = OpenAI(
        api_key="0ad31a37f185576579a1fd201b610379.mpv5pTFPrxyO2QC3",
        base_url="https://open.bigmodel.cn/api/paas/v4/"
    )

    completion = client.chat.completions.create(
        model="glm-4-air",
        messages=[
            {"role": "system", "content": content},
            {"role": "user",
             "content": "评估价格多少钱，回复一个价格就可以了"}
        ],
        top_p=0.7,
        temperature=0.9
    )
    # print(completion.choices[0].message.content)
    return completion.choices[0].message.content

if __name__ == "__main__":
    try:
        # 在您的控制台的应用管理处获取
        evaluate("丰田 卡罗拉 2021款 卡罗拉双擎 1.8 无级 精英版 15万公里")
    except Exception as e:
        print("except:", e)
