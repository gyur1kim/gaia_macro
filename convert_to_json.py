from constant_name import *

def convert_text(text):
    text = text.replace("\\", "\\\\")
    text = text.replace("\"", "\\\"")
    return text

# frame 속성에 넣을 값을 json으로 변환
def explanations_to_json(comp_map):    
    json_objects = []

    for num in range(1,4):
        if comp_map[EXPLANATION_COMPONENT].get(f'텍스트{int(num)}','') == '' and comp_map[EXPLANATION_COMPONENT].get(f'이미지{int(num)}','') == '':
            continue
        json_object = '{'
        json_object += '"text": "' + convert_text(comp_map[EXPLANATION_COMPONENT].get(f'텍스트{int(num)}','')) + '", '
        json_object += '"filePath": "' + convert_text(comp_map[EXPLANATION_COMPONENT].get(f'이미지{int(num)}','')) + '", '
        json_object += '"imgAlt": "' + convert_text(comp_map[EXPLANATION_COMPONENT].get(f'이미지{int(num)} 대체텍스트','')) + '"'
        json_object += '}'
        json_objects.append(json_object)

    json_data = '['+ ','.join(json_objects) + ']'
    return json_data

# 선다형 속성에 넣을 값을 json으로 변환
def choice_data_to_json(comp_map):
    json_objects = []
    
    for num in range(1,6):
        if comp_map[CHOICE_COMPONENT][f'텍스트{int(num)}'] == '' and comp_map[CHOICE_COMPONENT][f'이미지{int(num)}'] == '':
            continue
        json_object = '{'
        json_object += '"textValue": "' + convert_text(comp_map[CHOICE_COMPONENT].get(f'텍스트{int(num)}','')) + '", '
        json_object += '"filePath": "' + convert_text(comp_map[CHOICE_COMPONENT].get(f'이미지{int(num)}','')) + '", '
        json_object += '"imgAlt": "' + convert_text(comp_map[CHOICE_COMPONENT].get(f'이미지{int(num)} 대체텍스트','')) + '" '
        json_object += '}'
        json_objects.append(json_object)

    json_data = '['+ ','.join(json_objects) + ']'
    return json_data

def soundtrack_script_to_json(comp_map):
    json_data = '[{' 
    json_data += '"english": "' + convert_text(comp_map[PROBLEM_COMPONENT][MUSIC1_SCRIPT_TEXT]) + '", '
    json_data += '"translation": "' + convert_text(comp_map[PROBLEM_COMPONENT][MUSIC1_SCRIPT_TRANSLATION_TEXT]) +'" '
    json_data += '}]'
    return json_data

def translation_to_json(comp_map):
    json_data = '[{' 
    json_data += '"filePath": "' + convert_text(comp_map[TRANSLATION_COMPONENT][IMAGE1]) + '", '
    json_data += '"imgAlt": "' + convert_text(comp_map[TRANSLATION_COMPONENT][IMAGE1_ALT]) +'", '
    json_data += '"text": "' + convert_text(comp_map[TRANSLATION_COMPONENT][TEXT1]) +'" '    
    json_data += '}]'
    return json_data

def choice_header_data_to_json(comp_map):
    def create_option_list(texts, img_file="", img_alt=""):
        if texts:
            return ", ".join([f'{{"textValue":"{convert_text(text.strip())}","filePath":"","imgAlt":""}}' for text in texts.split("§")])
        return f'{{"textValue":"","filePath":"{convert_text(img_file)}","imgAlt":"{convert_text(img_alt)}"}}'

    json_data = "["

    header_list = comp_map[CHOICE_COMPONENT][HEADER].split("§")
    header_json = ", ".join([f'{{"textValue":"{convert_text(header.strip())}","filePath":"","imgAlt":""}}' for header in header_list])
    json_data += f'{{"rowItemList" : [{header_json}]}}'

    for i in range(1, 6):
        text_key = f'텍스트{i}'
        image_key = f'이미지1{i}'
        image_alt_key = f'이미지{i} 대체텍스트'

        if comp_map[CHOICE_COMPONENT].get(text_key, ""):
            choice_json = create_option_list(comp_map[CHOICE_COMPONENT][text_key])
            json_data += f',{{"rowItemList" : [{choice_json}]}}'
        elif comp_map[CHOICE_COMPONENT].get(image_key, ""):
            choice_json = create_option_list("", comp_map[CHOICE_COMPONENT][image_key], comp_map[CHOICE_COMPONENT].get(image_alt_key, ""))
            json_data += f',{{"rowItemList" : [{choice_json}]}}'

    json_data += "]"
    return json_data

def short_frame_to_json(comp_map):
    json_objects = []
    
    for num in range(1,6):
        if comp_map[INPUT_COMPONENT1][f'정답{num}'] == '':
            continue
        json_object = '{'
        json_object += '"answer": "' + convert_text(comp_map[INPUT_COMPONENT1][f'정답{num}']) + '"'
        json_object += '}'
        json_objects.append(json_object)

    json_data = '['+ ','.join(json_objects) + ']'

    return json_data

def multi_frame_to_json(comp_map):
    correctAnswerList = comp_map[ANSWER_COMPONENT][ANSWER1].split(',')
    json_objects = []

    for answer in correctAnswerList:
        if '1' in answer: num = '1'
        elif '2' in answer: num = '2'
        elif '3' in answer: num = '3'
        elif '4' in answer: num = '4'
        elif '5' in answer: num = '5'
        json_object = '{'
        json_object += '"answer": "' + convert_text(answer.strip()) + '", '
        json_object += '"text": "' + convert_text(comp_map[CHOICE_COMPONENT].get(f'텍스트{num}','')) + '", '
        json_object += '"filePath": "' + convert_text(comp_map[CHOICE_COMPONENT].get(f'이미지{num}','')) + '", '
        json_object += '"imgAlt": "' + convert_text(comp_map[CHOICE_COMPONENT].get(f'이미지{num} 대체텍스트','')) + '" '
        json_object += '}'
        json_objects.append(json_object)

    json_data = '['+ ','.join(json_objects) + ']'
    return json_data

def short_answer_multiple_to_json(comp_map):
    json = '['

    for i in range(5):
        if comp_map[f'입력_컴포넌트{i+1}']['텍스트1'] == '' and comp_map[f'입력_컴포넌트{i+1}'][f'정답1'] == '':
            continue
        json += '{ "valueList": ['
        for j in range(5):
            if comp_map[f'입력_컴포넌트{i+1}'][f'텍스트{j+1}'] == '' and comp_map[f'입력_컴포넌트{i+1}'][f'정답{j+1}'] == '':
                break
            json += '{ "textValue": "' + convert_text(comp_map[f'입력_컴포넌트{i+1}'][f'텍스트{j+1}']) + '", "correctAnswer": "' + convert_text(comp_map[f'입력_컴포넌트{i+1}'][f'정답{j+1}']) + '" },'
        if json.endswith(','):
            json = json[:-1]
        json += ']},'

    
    if json.endswith(','):
        json = json[:-1]
    json += ']'
    
    return json

def short_answer_to_json(comp_map):
    json = '['

    for i in range(5):
        json += '{ "textValue": "' + convert_text(comp_map[INPUT_COMPONENT1][f'텍스트{i+1}']) + '", "correctAnswer": "' + convert_text(comp_map[INPUT_COMPONENT1][f'정답{i+1}']) + '" }'
        if i != 4:
            json += ','
    
    json += ']'
    return json