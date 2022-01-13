from collections import Counter
import numpy as np
from nltk import ngrams


# 단순 카운트 함수
def simple_count(tokens, n): # 토큰화 된 candidate 문장, n-gram에서의 n 이 두 가지를 인자로 받음.
    return Counter(ngrams(tokens, n)) #문장에서 n-gram을 카운트

candidate = "It is a guide to action which ensures that the military always obeys the commands of the party."
tokens = candidate.split() #단어 토큰화
result = simple_count(tokens, 1) #토큰화 된 문장, 유니그램의 개수를 구하고자 한다면 n=1

candidate = 'the the the the the the the'
tokens = candidate.split() #단어 토큰화
result = simple_count(tokens, 1)

def count_clip(candidate, reference_list, n):
    cnt_ca = simple_count(candidate, n)
    # Ca 문장에서 n-gram 카운트
    temp = dict()

    for ref in reference_list: # 다수의 Ref 문장에 대해서 이하 반복
        cnt_ref = simple_count(ref, n)
        # Ref 문장에서 n-gram 카운트

        ''' 
            정밀도의 분자를 계산하기 위해 Ref와 매칭하며 카운트하는 과정에서
            Ca의 유니그램이 이미 Ref에서 매칭된 적이 있었는지를 고려해야 한다.
            우선, 유니그램이 하나의 Ref에서 최대 몇 번 등장했는지를 카운트한다. 
        '''
        for n_gram in cnt_ref: # 모든 Ref에 대해서 비교 후 특정 n-gram이 하나의 Ref에 가장 많이 등장한 횟수를 저장함
            if n_gram in temp:
                temp[n_gram] = max(cnt_ref[n_gram], temp[n_gram]) # max_ref_count
            else:
                temp[n_gram] = cnt_ref[n_gram]

    return {
        n_gram: min(cnt_ca.get(n_gram, 0), temp.get(n_gram, 0)) for n_gram in cnt_ca
        # count_clip=min(count, max_ref_count)
        # 위의 get은 찾고자 하는 n-gram이 없으면 0을 반환한다.
    }

def modified_precision(candidate, reference_list, n):
    clip = count_clip(candidate, reference_list, n)

    total_clip = sum(clip.values()) # 분자

    ct = simple_count(candidate, n)
    total_ct = sum(ct.values()) #분모

    if total_ct==0: # n-gram의 n이 커졌을 때 분모가 0이 되는 것을 방지
        total_ct=1

    return (total_clip / total_ct) # 보정된 정밀도
    # count_clip의 합을 분자로 하고 단순 count의 합을 분모로 하면 보정된 정밀도

def closest_ref_length(candidate, reference_list): # Ca 길이와 가장 근접한 Ref의 길이를 리턴하는 함수
    ca_len = len(candidate) # ca 길이
    ref_lens = (len(ref) for ref in reference_list) # Ref들의 길이
    
    # 파이썬 lambda함수 특징인듯, 첫번째 조건에서 같은 경우 -> 두번째 조건으로 넘어감
    '''
    print(min([14,16,12], key=lambda ref_len: (abs(ref_len - 13), ref_len)))
    result : 12
    print(min([14,16,12], key=lambda ref_len: abs(ref_len - 13)))
    result : 14
    '''
    closest_ref_len = min(ref_lens, key=lambda ref_len: (abs(ref_len - ca_len), ref_len))
    # 길이 차이를 최소화하는 Ref를 찾아서 Ref의 길이를 리턴
    return closest_ref_len

def brevity_penalty(candidate, reference_list):
    ca_len = len(candidate)
    ref_len = closest_ref_length(candidate, reference_list)

    if ca_len > ref_len:
        return 1
    elif ca_len == 0 :
    # candidate가 비어있다면 BP = 0 → BLEU = 0.0
        return 0
    else:
        return np.exp(1 - ref_len/ca_len)

def bleu_score(candidate, reference_list, weights=[0.25, 0.25, 0.25, 0.25]):
    bp = brevity_penalty(candidate, reference_list) # 브레버티 패널티, BP

    # p1, p2, p3, ..., pn
    p_n = [modified_precision(candidate, reference_list, n=n) for n, _ in enumerate(weights,start=1)]
    score = np.sum([w_i * np.log(p_i) if p_i != 0 else 0 for w_i, p_i in zip(weights, p_n)])
    return bp * np.exp(score)

candidate = 'It is a guide to action which ensures that the military always obeys the commands of the party'
references = [
    'It is a guide to action that ensures that the military will forever heed Party commands',
    'It is the guiding principle which guarantees the military forces always being under the command of the Party',
    'It is the practical guide for the army always to heed the directions of the party'
]

# 이번 챕터에서 구현한 코드로 계산한 BLEU 점수
print(bleu_score(candidate.split(),list(map(lambda ref: ref.split(), references))))

import nltk.translate.bleu_score as bleu
print(bleu.sentence_bleu(list(map(lambda ref: ref.split(), references)),candidate.split()))

print(min([14,16,12], key=lambda ref_len: (abs(ref_len - 13), ref_len)))
print(min([14,16,12], key=lambda ref_len: abs(ref_len - 13)))