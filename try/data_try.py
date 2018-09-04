# !/usr/bin/env python3
import os
import json
import fire

data_dir = './dataset'
train_file = os.path.join(data_dir, 'me_train.json')

'''
json结构如下：
问题id
    question
        具体内容
    evidences
        答案id-0
            answer
                具体内容（没有答案的为'no_answer'）
            evidence
                具体内容
        答案id-1
            .
            .
            .
        答案id-n


最后我们将整体的格式整理为{question:, one_evidence:, one_answer:,}的格式
'''
def load_train_file(infile):
    with open(infile, encoding='utf8') as f:
        cont = json.load(f)
        print(u'问题数量： ', '{}'.format(len(cont.keys())))
        id = list(cont.keys())[0]
        one_elem = cont[id]
        # print(u'\n第一个问题的格式如下： ', '{}\n{}'.format(id, one_elem))
        print(u'一个问题包含如下项目：', '{}\n{}\n'.format(id, one_elem.keys()))
        question = one_elem['question']
        evidences = one_elem['evidences']
        print(u'问题： ', u'{}\n'.format(question))
        print(u'答案： ', u'{}\n'.format(evidences))
        print(u'子答案列表: ', u'{}\n'.format(evidences.keys()))
        sub_evidience = evidences[list(evidences.keys())[-1]]
        print(u'子答案： ', u'{}\n'.format(sub_evidience))


if __name__ == '__main__':
    # fire.Fire()
    load_train_file('../dataset/me_train.json')