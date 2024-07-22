# -*- coding: utf-8 -*-
import re
import os
import zipfile
import shutil
from collections import defaultdict

from constant_name import *
from convert_to_json import choice_data_to_json, choice_header_data_to_json, explanations_to_json, multi_frame_to_json, soundtrack_script_to_json, translation_to_json

# 경로 관리
PC_NAME = 'GYURI'
MACRO_FOLDER_PATH = f'C:/Users/{PC_NAME}/git repo/miraen/gaia_macro/'
DOWNLOAD_FOLDER_PATH = f'C:/Users/{PC_NAME}/Downloads/'

# 빈 데이터 검사
def check_empty_data(data):
    return data.strip().replace('\n', ' ')

def set_excel_to_component_math_first(row_data):
    comp_map = defaultdict(dict)
    # 메타정보 : 0 ~ 8
    comp_map[METADATA][NUMBER] = check_empty_data(row_data[1])

    # 앱 배포 : 9 ~ 20
    comp_map[APP][ID] = check_empty_data(row_data[10])

    # UX : 21
    comp_map[UX] = check_empty_data(row_data[22])

    # 문제 : 22 ~ 37
    comp_map[PROBLEM_COMPONENT][TEXT0] = check_empty_data(row_data[23])

    comp_map[PROBLEM_COMPONENT][TEXT1] = check_empty_data(row_data[24])
    comp_map[PROBLEM_COMPONENT][IMAGE1] = check_empty_data(row_data[25])
    comp_map[PROBLEM_COMPONENT][IMAGE1_ALT] = check_empty_data(row_data[26])
    comp_map[PROBLEM_COMPONENT][BOX1] = check_empty_data(row_data[27])
    comp_map[PROBLEM_COMPONENT][VIEW1] = check_empty_data(row_data[28])

    comp_map[PROBLEM_COMPONENT][TEXT2] = check_empty_data(row_data[29])
    comp_map[PROBLEM_COMPONENT][IMAGE2] = check_empty_data(row_data[30])
    comp_map[PROBLEM_COMPONENT][IMAGE2_ALT] = check_empty_data(row_data[31])
    comp_map[PROBLEM_COMPONENT][BOX2] = check_empty_data(row_data[32])
    comp_map[PROBLEM_COMPONENT][VIEW2] = check_empty_data(row_data[33])

    comp_map[PROBLEM_COMPONENT][TEXT3] = check_empty_data(row_data[34])
    comp_map[PROBLEM_COMPONENT][IMAGE3] = check_empty_data(row_data[35])
    comp_map[PROBLEM_COMPONENT][IMAGE3_ALT] = check_empty_data(row_data[36])
    comp_map[PROBLEM_COMPONENT][BOX3] = check_empty_data(row_data[37])
    comp_map[PROBLEM_COMPONENT][VIEW3] = check_empty_data(row_data[38])

    # 정답 : 38
    comp_map[ANSWER_COMPONENT][ANSWER1] = check_empty_data(row_data[39])
    
    # 선지: 39 ~ 54
    comp_map[CHOICE_COMPONENT][HEADER] = check_empty_data(row_data[40])

    comp_map[CHOICE_COMPONENT][TEXT1] = check_empty_data(row_data[41])
    comp_map[CHOICE_COMPONENT][IMAGE1] = check_empty_data(row_data[42])
    comp_map[CHOICE_COMPONENT][IMAGE1_ALT] = check_empty_data(row_data[43])

    comp_map[CHOICE_COMPONENT][TEXT2] = check_empty_data(row_data[44])
    comp_map[CHOICE_COMPONENT][IMAGE2] = check_empty_data(row_data[45])
    comp_map[CHOICE_COMPONENT][IMAGE2_ALT] = check_empty_data(row_data[46])

    comp_map[CHOICE_COMPONENT][TEXT3] = check_empty_data(row_data[47])
    comp_map[CHOICE_COMPONENT][IMAGE3] = check_empty_data(row_data[48])
    comp_map[CHOICE_COMPONENT][IMAGE3_ALT] = check_empty_data(row_data[49])
    
    comp_map[CHOICE_COMPONENT][TEXT4] = check_empty_data(row_data[50])
    comp_map[CHOICE_COMPONENT][IMAGE4] = check_empty_data(row_data[51])
    comp_map[CHOICE_COMPONENT][IMAGE4_ALT] = check_empty_data(row_data[52])
    
    comp_map[CHOICE_COMPONENT][TEXT5] = check_empty_data(row_data[53])
    comp_map[CHOICE_COMPONENT][IMAGE5] = check_empty_data(row_data[54])
    comp_map[CHOICE_COMPONENT][IMAGE5_ALT] = check_empty_data(row_data[55])

    # 해설 : 55 ~ 63
    comp_map[EXPLANATION_COMPONENT][TEXT1] = check_empty_data(row_data[56])
    comp_map[EXPLANATION_COMPONENT][IMAGE1] = check_empty_data(row_data[57])
    comp_map[EXPLANATION_COMPONENT][IMAGE1_ALT] = check_empty_data(row_data[58])

    comp_map[EXPLANATION_COMPONENT][TEXT2] = check_empty_data(row_data[59])
    comp_map[EXPLANATION_COMPONENT][IMAGE2] = check_empty_data(row_data[60])
    comp_map[EXPLANATION_COMPONENT][IMAGE2_ALT] = check_empty_data(row_data[61])

    comp_map[EXPLANATION_COMPONENT][TEXT3] = check_empty_data(row_data[62])
    comp_map[EXPLANATION_COMPONENT][IMAGE3] = check_empty_data(row_data[63])
    comp_map[EXPLANATION_COMPONENT][IMAGE3_ALT] = check_empty_data(row_data[64])

    # 이미지 처리
    comp_map[PROBLEM_COMPONENT][IMAGE1] = comp_map[APP][ID] + '/' + comp_map[PROBLEM_COMPONENT][IMAGE1] if comp_map[PROBLEM_COMPONENT][IMAGE1] != '' else ''
    comp_map[PROBLEM_COMPONENT][IMAGE2] = comp_map[APP][ID] + '/' + comp_map[PROBLEM_COMPONENT][IMAGE2] if comp_map[PROBLEM_COMPONENT][IMAGE2] != '' else ''
    comp_map[PROBLEM_COMPONENT][IMAGE3] = comp_map[APP][ID] + '/' + comp_map[PROBLEM_COMPONENT][IMAGE3] if comp_map[PROBLEM_COMPONENT][IMAGE3] != '' else ''
    comp_map[CHOICE_COMPONENT][IMAGE1] = comp_map[APP][ID] + '/' + comp_map[CHOICE_COMPONENT][IMAGE1] if comp_map[CHOICE_COMPONENT][IMAGE1] != '' else ''
    comp_map[CHOICE_COMPONENT][IMAGE2] = comp_map[APP][ID] + '/' + comp_map[CHOICE_COMPONENT][IMAGE2] if comp_map[CHOICE_COMPONENT][IMAGE2] != '' else ''
    comp_map[CHOICE_COMPONENT][IMAGE3] = comp_map[APP][ID] + '/' + comp_map[CHOICE_COMPONENT][IMAGE3] if comp_map[CHOICE_COMPONENT][IMAGE3] != '' else ''
    comp_map[CHOICE_COMPONENT][IMAGE4] = comp_map[APP][ID] + '/' + comp_map[CHOICE_COMPONENT][IMAGE4] if comp_map[CHOICE_COMPONENT][IMAGE4] != '' else ''
    comp_map[CHOICE_COMPONENT][IMAGE5] = comp_map[APP][ID] + '/' + comp_map[CHOICE_COMPONENT][IMAGE5] if comp_map[CHOICE_COMPONENT][IMAGE5] != '' else ''
    comp_map[EXPLANATION_COMPONENT][IMAGE1] = comp_map[APP][ID] + '/' + comp_map[EXPLANATION_COMPONENT][IMAGE1] if comp_map[EXPLANATION_COMPONENT][IMAGE1] != '' else ''
    comp_map[EXPLANATION_COMPONENT][IMAGE2] = comp_map[APP][ID] + '/' + comp_map[EXPLANATION_COMPONENT][IMAGE2] if comp_map[EXPLANATION_COMPONENT][IMAGE2] != '' else ''
    comp_map[EXPLANATION_COMPONENT][IMAGE3] = comp_map[APP][ID] + '/' + comp_map[EXPLANATION_COMPONENT][IMAGE3] if comp_map[EXPLANATION_COMPONENT][IMAGE3] != '' else ''

    return comp_map

def set_excel_to_component_eng(row_data):
    comp_map = defaultdict(dict)
    # 메타정보 : 0 ~ 8
    comp_map[METADATA][NUMBER] = check_empty_data(row_data[0])

    # 앱 배포 : 9 ~ 20
    comp_map[APP][ID] = check_empty_data(row_data[9])

    # UX : 21
    comp_map[UX] = check_empty_data(row_data[21])

    # 지문 : 22 ~ 27

    # 문제 : 28 ~ 
    comp_map[PROBLEM_COMPONENT][TEXT0] = check_empty_data(row_data[28])

    comp_map[PROBLEM_COMPONENT][TEXT1] = check_empty_data(row_data[29])
    comp_map[PROBLEM_COMPONENT][IMAGE1] = check_empty_data(row_data[30])
    comp_map[PROBLEM_COMPONENT][IMAGE1_ALT] = check_empty_data(row_data[31])
    comp_map[PROBLEM_COMPONENT][BOX1] = check_empty_data(row_data[32])
    comp_map[PROBLEM_COMPONENT][BOX_IMAGE1] = check_empty_data(row_data[33])
    comp_map[PROBLEM_COMPONENT][BOX_IMAGE1_ALT] = check_empty_data(row_data[34])
    comp_map[PROBLEM_COMPONENT][VIEW1] = check_empty_data(row_data[35])

    comp_map[PROBLEM_COMPONENT][TEXT2] = check_empty_data(row_data[36])
    comp_map[PROBLEM_COMPONENT][IMAGE2] = check_empty_data(row_data[37])
    comp_map[PROBLEM_COMPONENT][IMAGE2_ALT] = check_empty_data(row_data[38])
    comp_map[PROBLEM_COMPONENT][BOX2] = check_empty_data(row_data[39])
    comp_map[PROBLEM_COMPONENT][BOX_IMAGE2] = check_empty_data(row_data[40])
    comp_map[PROBLEM_COMPONENT][BOX_IMAGE2_ALT] = check_empty_data(row_data[41])
    comp_map[PROBLEM_COMPONENT][VIEW2] = check_empty_data(row_data[42])

    comp_map[PROBLEM_COMPONENT][MUSIC1] = check_empty_data(row_data[43])
    comp_map[PROBLEM_COMPONENT][MUSIC1_SCRIPT_TEXT] = check_empty_data(row_data[44])
    comp_map[PROBLEM_COMPONENT][MUSIC1_SCRIPT_TRANSLATION_TEXT] = check_empty_data(row_data[45])

    # 정답 : 46
    comp_map[ANSWER_COMPONENT][ANSWER1] = check_empty_data(row_data[46])
    
    # 선지: 47 ~ 62
    comp_map[CHOICE_COMPONENT][HEADER] = check_empty_data(row_data[47])

    comp_map[CHOICE_COMPONENT][TEXT1] = check_empty_data(row_data[48])
    comp_map[CHOICE_COMPONENT][IMAGE1] = check_empty_data(row_data[49])
    comp_map[CHOICE_COMPONENT][IMAGE1_ALT] = check_empty_data(row_data[50])

    comp_map[CHOICE_COMPONENT][TEXT2] = check_empty_data(row_data[51])
    comp_map[CHOICE_COMPONENT][IMAGE2] = check_empty_data(row_data[52])
    comp_map[CHOICE_COMPONENT][IMAGE2_ALT] = check_empty_data(row_data[53])

    comp_map[CHOICE_COMPONENT][TEXT3] = check_empty_data(row_data[54])
    comp_map[CHOICE_COMPONENT][IMAGE3] = check_empty_data(row_data[55])
    comp_map[CHOICE_COMPONENT][IMAGE3_ALT] = check_empty_data(row_data[56])
    
    comp_map[CHOICE_COMPONENT][TEXT4] = check_empty_data(row_data[57])
    comp_map[CHOICE_COMPONENT][IMAGE4] = check_empty_data(row_data[58])
    comp_map[CHOICE_COMPONENT][IMAGE4_ALT] = check_empty_data(row_data[59])
    
    comp_map[CHOICE_COMPONENT][TEXT5] = check_empty_data(row_data[60])
    comp_map[CHOICE_COMPONENT][IMAGE5] = check_empty_data(row_data[61])
    comp_map[CHOICE_COMPONENT][IMAGE5_ALT] = check_empty_data(row_data[62])

    # 해석 : 63 ~ 65
    comp_map[TRANSLATION_COMPONENT][TEXT1] = check_empty_data(row_data[63])
    comp_map[TRANSLATION_COMPONENT][IMAGE1] = check_empty_data(row_data[64])
    comp_map[TRANSLATION_COMPONENT][IMAGE1_ALT] = check_empty_data(row_data[65])

    # 해설 : 66
    comp_map[EXPLANATION_COMPONENT][TEXT1] = check_empty_data(row_data[66])

    # 이미지 처리
    comp_map[PROBLEM_COMPONENT][IMAGE1] = comp_map[APP][ID] + '/' + comp_map[PROBLEM_COMPONENT][IMAGE1] if comp_map[PROBLEM_COMPONENT][IMAGE1] != '' else ''
    comp_map[PROBLEM_COMPONENT][IMAGE2] = comp_map[APP][ID] + '/' + comp_map[PROBLEM_COMPONENT][IMAGE2] if comp_map[PROBLEM_COMPONENT][IMAGE2] != '' else ''
    comp_map[PROBLEM_COMPONENT][BOX_IMAGE1] = comp_map[APP][ID] + '/' + comp_map[PROBLEM_COMPONENT][BOX_IMAGE1] if comp_map[PROBLEM_COMPONENT][BOX_IMAGE1] != '' else ''
    comp_map[PROBLEM_COMPONENT][BOX_IMAGE2] = comp_map[APP][ID] + '/' + comp_map[PROBLEM_COMPONENT][BOX_IMAGE2] if comp_map[PROBLEM_COMPONENT][BOX_IMAGE2] != '' else ''
    comp_map[CHOICE_COMPONENT][IMAGE1] = comp_map[APP][ID] + '/' + comp_map[CHOICE_COMPONENT][IMAGE1] if comp_map[CHOICE_COMPONENT][IMAGE1] != '' else ''
    comp_map[CHOICE_COMPONENT][IMAGE2] = comp_map[APP][ID] + '/' + comp_map[CHOICE_COMPONENT][IMAGE2] if comp_map[CHOICE_COMPONENT][IMAGE2] != '' else ''
    comp_map[CHOICE_COMPONENT][IMAGE3] = comp_map[APP][ID] + '/' + comp_map[CHOICE_COMPONENT][IMAGE3] if comp_map[CHOICE_COMPONENT][IMAGE3] != '' else ''
    comp_map[CHOICE_COMPONENT][IMAGE4] = comp_map[APP][ID] + '/' + comp_map[CHOICE_COMPONENT][IMAGE4] if comp_map[CHOICE_COMPONENT][IMAGE4] != '' else ''
    comp_map[CHOICE_COMPONENT][IMAGE5] = comp_map[APP][ID] + '/' + comp_map[CHOICE_COMPONENT][IMAGE5] if comp_map[CHOICE_COMPONENT][IMAGE5] != '' else ''
    comp_map[TRANSLATION_COMPONENT][IMAGE1] = comp_map[APP][ID] + '/' + comp_map[TRANSLATION_COMPONENT][IMAGE1] if comp_map[TRANSLATION_COMPONENT][IMAGE1] != '' else ''

    return comp_map

def convert_backslash(text):
    text = re.sub(r'\\{1,2}', r'\\\\\\\\', text)
    return text

def set_option_template(row_data, app_name, subject):
    if subject == "수학":
        comp_map = set_excel_to_component_math_first(row_data)
    elif subject == "영어":
        comp_map = set_excel_to_component_eng(row_data)


    if "선" in comp_map[UX]:
        # 선다형 폴더 내 파일들(원본)
        FILE_ID = '1721484218170'
        OPTION_FILES_ORIGIN = [
            f'{MACRO_FOLDER_PATH}선다형/app-{FILE_ID}.js',
            f'{MACRO_FOLDER_PATH}선다형/GlobalConfig-{FILE_ID}.js',
            f'{MACRO_FOLDER_PATH}선다형/import-libraries-{FILE_ID}.js',
            f'{MACRO_FOLDER_PATH}선다형/index.html',
            f'{MACRO_FOLDER_PATH}선다형/runner-{FILE_ID}.js',
            f'{MACRO_FOLDER_PATH}선다형/SUIT-Bold.ttf',
            f'{MACRO_FOLDER_PATH}선다형/MathJax_Main-Regular.ttf'
        ]
        # 가이아 컴포넌트명
        FRAME_COMP_NAME = 'kgr_240719_frame2 65'
        TEXT0_COMP_NAME = '0711_text1 59'
        AUDIO_COMP_NAME = 'kgr_240716_audio3 69'
        TEXT1_COMP_NAME = '0711_text1 60'
        IMG1_COMP_NAME = 'kgr_240716_img2 63'
        BOX1_COMP_NAME = '0711_box1 5'
        EX1_COMP_NAME = '0711_ex2 9'
        TEXT2_COMP_NAME = '0711_text1 61'
        IMG2_COMP_NAME = 'kgr_240716_img2 64'
        BOX2_COMP_NAME = '0711_box1 6'
        EX2_COMP_NAME = '0711_ex2 10'
        OP_COMP_NAME = '0719_op 86'
    elif "헤" in comp_map[UX]:
        # 헤더형 폴더 내 파일들(원본)
        FILE_ID = '1721622473009'
        OPTION_FILES_ORIGIN = [
            f'{MACRO_FOLDER_PATH}헤더형/app-{FILE_ID}.js',
            f'{MACRO_FOLDER_PATH}헤더형/GlobalConfig-{FILE_ID}.js',
            f'{MACRO_FOLDER_PATH}헤더형/import-libraries-{FILE_ID}.js',
            f'{MACRO_FOLDER_PATH}헤더형/index.html',
            f'{MACRO_FOLDER_PATH}헤더형/runner-{FILE_ID}.js',
            f'{MACRO_FOLDER_PATH}헤더형/SUIT-Bold.ttf',
            f'{MACRO_FOLDER_PATH}헤더형/MathJax_Main-Regular.ttf'
        ]
        # 가이아 컴포넌트명
        FRAME_COMP_NAME = 'kgr_240719_frame2 55'
        TEXT0_COMP_NAME = '0711_text1 62'
        AUDIO_COMP_NAME = 'kgr_240716_audio3 66'
        TEXT1_COMP_NAME = '0711_text1 63'
        IMG1_COMP_NAME = 'kgr_240716_img2 67'
        BOX1_COMP_NAME = '0711_box1 13'
        EX1_COMP_NAME = '0711_ex2 11'
        TEXT2_COMP_NAME = '0711_text1 64'
        IMG2_COMP_NAME = 'kgr_240716_img2 68'
        BOX2_COMP_NAME = '0711_box1 6'
        EX2_COMP_NAME = '0711_ex2 12'
        OP_COMP_NAME = '0719_ophead 64'

    # WORK PATH의 파일들(복사본)
    OPTION_FILES_IN_WORK_FOLDER = [
        f'{MACRO_FOLDER_PATH}app-{FILE_ID}.js',
        f'{MACRO_FOLDER_PATH}GlobalConfig-{FILE_ID}.js',
        f'{MACRO_FOLDER_PATH}import-libraries-{FILE_ID}.js',
        f'{MACRO_FOLDER_PATH}index.html',
        f'{MACRO_FOLDER_PATH}runner-{FILE_ID}.js',
        f'{MACRO_FOLDER_PATH}SUIT-Bold.ttf'
        f'{MACRO_FOLDER_PATH}MathJax_Main-Regular.ttf'
    ]

    # 수정해야하는 파일 이름
    OP_APP_FILE_NAME = f'{MACRO_FOLDER_PATH}app-{FILE_ID}.js'

    APP_NAME = app_name
    SUBJECT = subject
    if "초" in comp_map[UX]:
        THEME = '초등'
    elif "중" in comp_map[UX]:
        THEME = '중고등'

    # 선다형 폴더에 필요한 파일들 WORK_PATH로 옮기기
    for OPTION_FILE in OPTION_FILES_ORIGIN:
        destination_file = os.path.join(MACRO_FOLDER_PATH, os.path.basename(OPTION_FILE))
        try:
            shutil.copy2(OPTION_FILE, MACRO_FOLDER_PATH)
            print(f"파일이 성공적으로 복사되었습니다: {destination_file}")
        except FileNotFoundError:
            print(f"원본 파일을 찾을 수 없습니다: {OPTION_FILE}")
        except PermissionError:
            print(f"권한이 없습니다: {destination_file}")
        except Exception as e:
            print(f"파일 복사 중 오류가 발생했습니다: {e}")

    # 파일 읽기
    with open(OP_APP_FILE_NAME, 'r', encoding='utf-8') as FILE:
        OP_APP_FILE = FILE.read()

    # 텍스트0 변경
    text0_value = convert_backslash(comp_map[PROBLEM_COMPONENT][TEXT0])
    text0_pattern = fr'("name":"{TEXT0_COMP_NAME}"[\s\S]*?"content":{{[\s\S]*?"value":{{"locked":false)[\s\S]*?(}},)'
    text0_replacement = fr'\1,"value":"{text0_value}"\2'

    # 오디오0 변경
    audio_value = comp_map[APP][ID] + '/' + comp_map[PROBLEM_COMPONENT].get('음원1','') if comp_map[PROBLEM_COMPONENT].get('음원1','') != '' else ''
    audio_pattern = fr'("name":"{AUDIO_COMP_NAME}"[\s\S]*?"content":{{[\s\S]*?"filePath":{{[\s\S]*?false)[\s\S]*?(}},)'
    audio_replacement = fr'\1,"value":"{audio_value}"\2'

    # 텍스트1 변경
    text1_value = convert_backslash(comp_map[PROBLEM_COMPONENT][TEXT1])
    text1_pattern = fr'("name":"{TEXT1_COMP_NAME}"[\s\S]*?"content":{{[\s\S]*?"value":{{"locked":false)[\s\S]*?(}},)'
    text1_replacement = fr'\1,"value":"{text1_value}"\2'

    # 이미지1 변경
    img1_filePath = comp_map[PROBLEM_COMPONENT][IMAGE1]
    img1_imgAlt = comp_map[PROBLEM_COMPONENT][IMAGE1_ALT]
    img1_pattern = fr'("name":"{IMG1_COMP_NAME}"[\s\S]*?"content":{{[\s\S]*?"filePath":{{[\s\S]*?false)[\s\S]*?(}},[\s\S]*?imgAlt":{{[\s\S]*?false)[\s\S]*?(}},?[\s\S]*?)'
    img1_replacement = fr'\1,"value":"{img1_filePath}"\2,"value":"{img1_imgAlt}"\3'

    # 박스1 변경
    box1_value = convert_backslash(comp_map[PROBLEM_COMPONENT][BOX1])
    box1_pattern = fr'("name":"{BOX1_COMP_NAME}"[\s\S]*?"content":{{[\s\S]*?"value":{{"locked":false)[\s\S]*?(}})'
    box1_replacement = fr'\1,"value":"{box1_value}"\2'

    # 보기박스1 변경
    ex1_value = convert_backslash(comp_map[PROBLEM_COMPONENT][VIEW1])
    ex1_pattern = fr'("name":"{EX1_COMP_NAME}"[\s\S]*?"content":{{[\s\S]*?"value":{{"locked":false)[\s\S]*?(}})'
    ex1_replacement = fr'\1,"value":"{ex1_value}"\2'

    # 텍스트2 변경
    text2_value = convert_backslash(comp_map[PROBLEM_COMPONENT][TEXT2])
    text2_pattern = fr'("name":"{TEXT2_COMP_NAME}"[\s\S]*?"content":[\s\S]*?"value":{{"locked":false)[\s\S]*?(}},)'
    text2_replacement = fr'\1,"value":"{text2_value}"\2'

    # 이미지2 변경
    img2_filePath = comp_map[PROBLEM_COMPONENT][IMAGE2]
    img2_imgAlt = comp_map[PROBLEM_COMPONENT][IMAGE2_ALT]
    img2_pattern = fr'("name":"{IMG2_COMP_NAME}"[\s\S]*?"content":{{[\s\S]*?"filePath":{{[\s\S]*?false)[\s\S]*?(}},[\s\S]*?imgAlt":{{[\s\S]*?false)[\s\S]*?(}},?[\s\S]*?)'
    img2_replacement = fr'\1,"value":"{img2_filePath}"\2,"value":"{img2_imgAlt}"\3'

    # 박스2 변경
    box2_value = convert_backslash(comp_map[PROBLEM_COMPONENT][BOX2])
    box2_pattern = fr'("name":"{BOX2_COMP_NAME}"[\s\S]*?"content":[\s\S]*?"value":{{"locked":false)[\s\S]*?(}})'
    box2_replacement = fr'\1,"value":"{box2_value}"\2'

    # 보기박스2 변경
    ex2_value = convert_backslash(comp_map[PROBLEM_COMPONENT][VIEW2])
    ex2_pattern = fr'("name":"{EX2_COMP_NAME}"[\s\S]*?"content":{{[\s\S]*?"value":{{"locked":false)[\s\S]*?(}})'
    ex2_replacement = fr'\1,"value":"{ex2_value}"\2'

    # 선지 변경
    if comp_map[CHOICE_COMPONENT][TEXT1] != '':
        OP_TYPE = 'text'
    else:
        OP_TYPE = 'image'
    op_answer = comp_map[ANSWER_COMPONENT][ANSWER1].replace(' ', '')
    if "선" in comp_map[UX]:
        op_row_list = convert_backslash(choice_data_to_json(comp_map))
        op_pattern = fr'("name":"{OP_COMP_NAME}"[\s\S]*?"content":[\s\S]*?"optionType":[\s\S]*?"value":)[\s\S]*?(}},[\s\S]*?"rowList":{{[\s\S]*?"value":)\[[\s\S]*?\](}},[\s\S]*?"correctAnswer":{{[\s\S]*?false)[\s\S]*?(}},)'
        op_replacement = fr'\1"{OP_TYPE}"\2{op_row_list}\3,"value":"{op_answer}"\4'
    elif "헤" in comp_map[UX]:
        op_row_list = convert_backslash(choice_header_data_to_json(comp_map))
        op_pattern = fr'("name":"{OP_COMP_NAME}"[\s\S]*?"content":[\s\S]*?"optionType":[\s\S]*?"value":)[\s\S]*?(}},[\s\S]*?"rowList":{{[\s\S]*?"value":)\[[\s\S]*?\](}},"className"[\s\S]*?"correctAnswer":{{[\s\S]*?false)[\s\S]*?(}},)'
        op_replacement = fr'\1"{OP_TYPE}"\2{op_row_list}\3,"value":"{op_answer}"\4'
        
    # frame 변경
    frame_correct_answer = convert_backslash(multi_frame_to_json(comp_map))
    frame_explanations = convert_backslash(explanations_to_json(comp_map))
    if SUBJECT == '영어':
        frame_scripts = soundtrack_script_to_json(comp_map)
        frame_translations = translation_to_json(comp_map)
    else:
        frame_scripts = r'[{ "english": "", "translation": ""}]'
        frame_translations = r'[{"filePath": "","imgAlt": "","text": "",},]'
    frame_pattern = fr'(name":"{FRAME_COMP_NAME}"[\s\S]*?"content":[\s\S]*?"translations":[\s\S]*?"value":)\[[\s\S]*?\](}}[\s\S]*?"explanations":[\s\S]*?"value":)\[[\s\S]*?\](}},[\s\S]*?correctAnswer":[\s\S]*?"value":)\[[\s\S]*?\](}}[\s\S]*?"scripts":[\s\S]*?value":)\[[\s\S]*?\](}})'
    frame_replacement = fr'\1{frame_translations}\2{frame_explanations}\3{frame_correct_answer}\4{frame_scripts}\5'

    # 과목 바꾸기
    subject_pattern = r'("subject":{"locked":false,"value":)[\s\S]*?(})'
    subject_replacement = fr'\1"{SUBJECT}"\2'
    theme_pattern = r'("theme":{"locked":false,"value":)[\s\S]*?(})'
    theme_replacement = fr'\1"{THEME}"\2'

    # 과목/학년 변경
    OP_APP_FILE = re.sub(subject_pattern, subject_replacement, OP_APP_FILE, flags=re.DOTALL)
    OP_APP_FILE = re.sub(theme_pattern, theme_replacement, OP_APP_FILE, flags=re.DOTALL)

    # 문제 영역 데이터 입력
    OP_APP_FILE = re.sub(text0_pattern, text0_replacement, OP_APP_FILE, flags=re.DOTALL)
    OP_APP_FILE = re.sub(audio_pattern, audio_replacement, OP_APP_FILE, flags=re.DOTALL)
    OP_APP_FILE = re.sub(text1_pattern, text1_replacement, OP_APP_FILE, flags=re.DOTALL)
    OP_APP_FILE = re.sub(img1_pattern, img1_replacement, OP_APP_FILE, flags=re.DOTALL)
    OP_APP_FILE = re.sub(box1_pattern, box1_replacement, OP_APP_FILE, flags=re.DOTALL)
    OP_APP_FILE = re.sub(ex1_pattern, ex1_replacement, OP_APP_FILE, flags=re.DOTALL)
    OP_APP_FILE = re.sub(text2_pattern, text2_replacement, OP_APP_FILE, flags=re.DOTALL)
    OP_APP_FILE = re.sub(img2_pattern, img2_replacement, OP_APP_FILE, flags=re.DOTALL)
    OP_APP_FILE = re.sub(box2_pattern, box2_replacement, OP_APP_FILE, flags=re.DOTALL)
    OP_APP_FILE = re.sub(ex2_pattern, ex2_replacement, OP_APP_FILE, flags=re.DOTALL)

    # 프레임 영역 데이터 입력
    OP_APP_FILE = re.sub(frame_pattern, frame_replacement, OP_APP_FILE, flags=re.DOTALL)

    # 선다형 영역 데이터 입력
    OP_APP_FILE = re.sub(op_pattern, op_replacement, OP_APP_FILE, flags=re.DOTALL)

    # 파일 저장
    with open(OP_APP_FILE_NAME, 'w', encoding='utf-8') as FILE:
        FILE.write(OP_APP_FILE)

    print("파일이 성공적으로 업데이트되었습니다.")

    # 압축 파일 이름
    zip_filename = f'{DOWNLOAD_FOLDER_PATH}{APP_NAME}.zip'

    # zip 파일 생성 및 파일 추가
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for FILE in OPTION_FILES_IN_WORK_FOLDER:
            zipf.write(FILE, arcname=os.path.basename(FILE))

    print(f"문제 {APP_NAME} 생성 성공")

    # WORK_PATH에 복사한 파일들 삭제
    for OPTION_FILE in OPTION_FILES_IN_WORK_FOLDER:
        try:
            os.remove(OPTION_FILE)
            print(f"파일이 성공적으로 삭제되었습니다: {OPTION_FILE}")
        except FileNotFoundError:
            print(f"파일을 찾을 수 없습니다: {OPTION_FILE}")
        except PermissionError:
            print(f"파일 삭제 권한이 없습니다: {OPTION_FILE}")
        except Exception as e:
            print(f"파일 삭제 중 오류가 발생했습니다: {e}")
    return True