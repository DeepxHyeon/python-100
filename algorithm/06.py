'''
병합정렬(0(nlongn))
분할, 정복

입력값 = [5, 10, 66, 77, 54, 32, 11, 15]
전체인덱스 = 7
중간값 = 7//2 # 7//2 = 3, 7/2 = 3.5
입력값[:중간값+1]
입력값[중간값+1:]

[5, 10, 66, 77, 54, 32, 11, 15]
[5, 10, 66, 77], [54, 32, 11, 15]
[5, 10], [66, 77], [54, 32], [11, 15]
[5], [10], [66], [77], [54], [32], [11], [15]
[5, 10], [66, 77], [54, 32], [11, 15]
[5, 10, 66, 77], [11, 15, 32, 54]
[5, 10, 11, 15, 32, 54, 66, 77]
'''

def 병합정렬(입력리스트):
    입력리스트의길이 = len(입력리스트)
    결과값 = []
    if 입력리스트의길이 <= 1:
        return 입력리스트
    중간값 = 입력리스트의길이 //2
    그룹_하나 = 병합정렬(입력리스트[:중간값])
    그룹_둘 = 병합정렬(입력리스트[중간값:])
    while 그룹_하나 and 그룹_둘:
        if 그룹_하나[0] < 그룹_둘[0]:
            결과값.append(그룹_하나.pop(0))
        else:
            결과값.append(그룹_둘.pop(0))
    while 그룹_하나:
        결과값.append(그룹_하나.pop(0))
    while 그룹_둘:
        결과값.append(그룹_둘.pop(0))
    #'그룹_하나 : {}, 그룹_둘 : {}\n'.format(그룹_하나, 그룹_둘)
    return 결과값

print(병합정렬([5, 10, 66, 77, 54, 32, 11, 15]))