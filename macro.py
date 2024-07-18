# -*- coding: utf-8 -*-
import re
import os
import zipfile

FILE_PATH = 'C:/Users/qri/Desktop/gaia_macro/'
FILE_ID = '1721316601086'

# 파일 경로 설정
app_file_js = f'{FILE_PATH}app-{FILE_ID}.js'

# 파일 읽기
with open(app_file_js, 'r', encoding='utf-8') as file:
    content = file.read()

# 텍스트0 변경
text0_value = '1086'
text0_pattern = r'("?name"?:\s?"0711_text1 19"[\s\S]*?content"?:\s?{[\s\S]*?value"?:\s?{[\s\S]*?false)[\s\S]*?(},)'
text0_replacement = fr'\1, "value": "{text0_value}"\2'

# 오디오0 변경
audio0_value = 'APP_ID/오디오파일명.mp4'
audio0_pattern = r'("?name"?:\s?"kgr_240716_audio3 65"[\s\S]*?content"?:\s?{[\s\S]*?filePath"?:\s?{[\s\S]*?false)[\s\S]*?(},)'
audio0_replacement = fr'\1, "value": "{audio0_value}"\2'

# 텍스트1 변경
text1_value = '텍스트1'
text1_pattern = r'("?name"?:\s?"0711_text1 63"[\s\S]*?content"?:\s?{[\s\S]*?value"?:\s?{[\s\S]*?false)[\s\S]*?(},)'
text1_replacement = fr'\1, "value": "{text1_value}"\2'

# 이미지1 변경
img1_filePath = 'APP_ID/어쩌구.jpg'
img1_imgAlt = '대체텍스트'
img1_pattern = r'("?name"?:\s?"kgr_240716_img2 69"[\s\S]*?content"?:\s?{[\s\S]*?filePath"?:\s?{[\s\S]*?false)[\s\S]*?(},[\s\S]*?imgAlt"?:\s?{[\s\S]*?false)[\s\S]*?(},?[\s\S]*?},?)'
img1_replacement = fr'\1, "filePath": "{img1_filePath}" \2, "imgAlt": "{img1_imgAlt}"\3'

# 박스1 변경
box1_value = '박스1'
box1_pattern = r'("?name"?:\s?"0711_box1 13"[\s\S]*?content"?:\s?{[\s\S]*?value"?:\s?{[\s\S]*?false)[\s\S]*?(},?[\s\S]*?},?)'
box1_replacement = fr'\1, "value": "{box1_value}"\2'

# 보기박스1 변경
ex1_value = '보기1086'
ex1_pattern = r'("?name"?:\s?"0711_ex2 11"[\s\S]*?content"?:\s?{[\s\S]*?value"?:\s?{[\s\S]*?false)[\s\S]*?(},?[\s\S]*?},?)'
ex1_replacement = fr'\1, "value": "{ex1_value}"\2'

# 텍스트2 변경
text2_value = ''
text2_pattern = r'("?name"?:\s?"0711_text1 64"[\s\S]*?content"?:\s?{[\s\S]*?value"?:\s?{[\s\S]*?false)[\s\S]*?(},)'
text2_replacement = fr'\1, "value": "{text2_value}"\2'

# 이미지2 변경
img2_filePath = ''
img2_imgAlt = ''
img2_pattern = r'("?name"?:\s?"kgr_240716_img2 70"[\s\S]*?content"?:\s?{[\s\S]*?filePath"?:\s?{[\s\S]*?false)[\s\S]*?(},[\s\S]*?imgAlt"?:\s?{[\s\S]*?false)[\s\S]*?(},?[\s\S]*?},?)'
img2_replacement = fr'\1, "filePath": "{img2_filePath}" \2, "imgAlt": "{img2_imgAlt}"\3'

# 박스2 변경
box2_value = ''
box2_pattern = r'("?name"?:\s?"0711_box1 14"[\s\S]*?content"?:\s?{[\s\S]*?value"?:\s?{[\s\S]*?false)[\s\S]*?(},?[\s\S]*?},?)'
box2_replacement = fr'\1, "value": "{box2_value}"\2'

# 보기박스2 변경
ex2_value = ''
ex2_pattern = r'("?name"?:\s?"0711_ex2 12"[\s\S]*?content"?:\s?{[\s\S]*?value"?:\s?{[\s\S]*?false)[\s\S]*?(},?[\s\S]*?},?)'
ex2_replacement = fr'\1, "value": "{ex2_value}"\2'

# 선지 변경
op_row_list = '[{"textValue": "1", "filePath": "", "imgAlt": ""}, {"textValue": "2", "filePath": "", "imgAlt": ""}, {"textValue": "3", "filePath": "", "imgAlt": ""}, {"textValue": "4", "filePath": "", "imgAlt": ""}, {"textValue": "5", "filePath": "", "imgAlt": ""}]'
op_answer = '5'
op_pattern = r'("?name"?:\s?"0716_op2 66"[\s\S]*?rowList"?:\s?{[\s\S]*?value"?:\s?)\[[\s\S]*?\](,?[\s\S]*?}[\s\S]*?correctAnswer"?:\s?{[\s\S]*?false)[\s\S]*?(},)'
op_replacement = fr'\1{op_row_list}\2, "value": {op_answer}\3'

# frame
frame_translations = '[{"filePath": "","imgAlt": "","text": "여기는 해석이 옵니다.",},]'
frame_explanations = '[{"filePath": "","imgAlt": "","text": "여기는 해설이 옵니다.",},]'
frame_correct_answer = '[{"answer": "5", "filePath": "", "imgAlt": "", "text": "5"},]'
frame_scripts = '[{ "english": "", "translation": ""}]'
frame_pattern = r'(name"?:\s?"kgr_240716_frame3 57",[\s\S]*?translations"?:[\s\S]*?value"?:\s?)\[[\s\S]*?\](,?[\s\S]*?},[\s\S]*?explanations"?:[\s\S]*?value"?:\s?)\[[\s\S]*?\](,?[\s\S]*?},[\s\S]*?correctAnswer"?:[\s\S]*?value"?:\s?)\[[\s\S]*?\](,?[\s\S]*?},[\s\S]*?scripts"?:[\s\S]*?value"?:\s?)\[[\s\S]*?\](,?[\s\S]*?},)'
frame_replacement = fr'\1{frame_translations}\2{frame_explanations}\3{frame_correct_answer}\4{frame_scripts}\5'

content = re.sub(frame_pattern, frame_replacement, content, flags=re.DOTALL)
content = re.sub(text0_pattern, text0_replacement, content, flags=re.DOTALL)
content = re.sub(audio0_pattern, audio0_replacement, content, flags=re.DOTALL)
content = re.sub(text1_pattern, text1_replacement, content, flags=re.DOTALL)
content = re.sub(img1_pattern, img1_replacement, content, flags=re.DOTALL)
content = re.sub(box1_pattern, box1_replacement, content, flags=re.DOTALL)
content = re.sub(ex1_pattern, ex1_replacement, content, flags=re.DOTALL)
content = re.sub(text2_pattern, text2_replacement, content, flags=re.DOTALL)
content = re.sub(img2_pattern, img2_replacement, content, flags=re.DOTALL)
content = re.sub(box2_pattern, box2_replacement, content, flags=re.DOTALL)
content = re.sub(ex2_pattern, ex2_replacement, content, flags=re.DOTALL)
content = re.sub(op_pattern, op_replacement, content, flags=re.DOTALL)

# 파일 저장
with open(app_file_js, 'w', encoding='utf-8') as file:
    file.write(content)

print("파일이 성공적으로 업데이트되었습니다.")

# 여러 JS 파일을 ZIP 파일로 압축
js_files = [
    f"{FILE_PATH}app-{FILE_ID}.js",
    f"{FILE_PATH}GlobalConfig-{FILE_ID}.js",
    f"{FILE_PATH}import-libraries-{FILE_ID}.js",
    f"{FILE_PATH}1086index.html",
    f"{FILE_PATH}runner-{FILE_ID}.js",
    f"{FILE_PATH}SUIT-Bold.ttf"
]

# 압축 파일 이름
zip_filename = f'{FILE_PATH}1086.zip'

# zip 파일 생성 및 파일 추가
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for file in js_files:
        zipf.write(file, arcname=os.path.basename(file))

print(f"{zip_filename} 파일이 성공적으로 생성되었습니다.")
