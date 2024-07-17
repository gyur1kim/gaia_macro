# -*- coding: utf-8 -*-
import re
import os
import zipfile

FILE_PATH = 'C:/Users/qri/Desktop/gaia_macro/'

# 파일 경로 설정
app_file_js = f'{FILE_PATH}app-1721208887818.js'

# 파일 읽기
with open(app_file_js, 'r', encoding='utf-8') as file:
    content = file.read()


# 정규 표현식을 사용하여 선지 변경
op2_row_list = '[{textValue: "333", filePath: "", imgAlt: ""}, {textValue: "테스트", filePath: "", imgAlt: ""}, {textValue: "옴뇸뇸", filePath: "", imgAlt: ""}, {textValue: "반가워요", filePath: "", imgAlt: ""}]'
op2_answer = '\"5\"'
op2_pattern = r'(name: "0716_op2 66",[\s\S]*?rowList:[\s\S]*?value: )\[[\s\S]*?\](,[\s\S]*?correctAnswer: \{ locked: false)[\s\S]*?(\s*\},)'
op2_replacement = fr'\1{op2_row_list}\2, value: {op2_answer}\3'

# 정규 표현식을 사용하여 텍스트1 변경
text1_value = '\"콤마테스트\"'
text1_pattern = r'(name: "0711_text1 19",[\s\S]*?content:[\s\S]*?theme:[\s\S]*?value:[\s\S]*?value: {[\s\S]*?locked: false)[\s\S]*?(},)'
text1_replacement = fr'\1, value: {text1_value}\2'

# frame
frame_translations = '[{filePath: "",imgAlt: "",text: "여러분, 반갑습니숭구리당당! 저는 진화생물학자 Edward Wilson 박사입니다. 오늘 초대해 주셔서 감사합니다. 오는 길에 이 장소를 찾는데 어려움을 겪었습니다. 다행히도 친절한 학생이 다가와서 여기로 데려다 줬어요. 이런 상황에서 우리가 도움이 필요한 사람을 돕고 싶어 한다는 건 신기한 일입니다. 그럼, 몇 가지 흥미로운 질문이 생깁니다. 우리의 다정함은 어디에서 오는 것이며, 왜 중요한 것일까요?",},]'
frame_explanations = '[{filePath: "",imgAlt: "",text: "뭐뭐하는 데 어려움을 겪다’라는 의미를 나타내는 표현은 have trouble –ing이다. 따라서 2번의 locate를 locating으로 바꿔야 한다.",},]'
frame_correct_answer = '[{answer: "2", filePath: "", imgAlt: "", text: "니냐뇨"},]'
frame_scripts = '[{ english: "", translation: ""}]'
frame_pattern = r'(name: "kgr_240716_frame3 57",[\s\S]*?translations:[\s\S]*?value: )\[[\s\S]*?\](,[\s\S]*?explanations:[\s\S]*?value: )\[[\s\S]*?\](,[\s\S]*?correctAnswer:[\s\S]*?value: )\[[\s\S]*?\](,[\s\S]*?scripts:[\s\S]*?value: )\[[\s\S]*?\](,)'
frame_replacement = fr'\1{frame_translations}\2{frame_explanations}\3{frame_correct_answer}\4{frame_scripts}'

content = re.sub(op2_pattern, op2_replacement, content, flags=re.DOTALL)
content = re.sub(text1_pattern, text1_replacement, content, flags=re.DOTALL)
content = re.sub(frame_pattern, frame_replacement, content, flags=re.DOTALL)

# 파일 저장
with open(app_file_js, 'w', encoding='utf-8') as file:
    file.write(content)

print("파일이 성공적으로 업데이트되었습니다.")

# 여러 JS 파일을 ZIP 파일로 압축
js_files = [
    f"{FILE_PATH}app-1721208887818.js",
    f"{FILE_PATH}GlobalConfig-1721208887818.js",
    f"{FILE_PATH}import-libraries-1721208887818.js",
    f"{FILE_PATH}index.html",
    f"{FILE_PATH}runner-1721208887818.js",
    f"{FILE_PATH}SUIT-Bold.ttf"
]

# 압축 파일 이름
zip_filename = f'{FILE_PATH}test.zip'

# zip 파일 생성 및 파일 추가
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for file in js_files:
        zipf.write(file, arcname=os.path.basename(file))

print(f"{zip_filename} 파일이 성공적으로 생성되었습니다.")
