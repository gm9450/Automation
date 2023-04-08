Day1 =  {'provide': '[동] 제공하다, 공급하다, 준비하다', 'develop': '[동] 개발하다, 발달하다, 발전시키다'}

def shorten(Day):
    new_dict = {}
    for key, value in Day1.items():
        # 모든 '['와 ']' 사이의 문자열 추출하여 제거
        while True:
            start = value.find('[')
            end = value.find(']')
            if start != -1 and end != -1:
                value = value[:start] + value[end+1:]
            else:
                break

        while True:
            start = value.find('(')
            end = value.find(')')
            if start != -1 and end != -1:
                value = value[:start] + value[end+1:]
            else:
                break
            
        # 쉼표(,)를 기준으로 값 분리하여 리스트에 저장
        values_list = value.split(',')

        # 리스트의 각 값을 공백 제거 후 저장
        values_list = [val.strip() for val in values_list]

        # 리스트를 딕셔너리의 value로 사용
        new_dict[key] = values_list

    return new_dict
    
new_dict = shorten(Day1)
print(new_dict)