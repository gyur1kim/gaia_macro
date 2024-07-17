import re
import os
import zipfile

file_path = 'C:/Users/GYURI/Desktop/0717중영선/'

# 파일 경로 설정
app_file_js = f'{file_path}app-1721208887818.js'

# 변경할 op2값
op2_new_value = '[{textValue: "안녕", filePath: "", imgAlt: ""}, {textValue: "하세요", filePath: "", imgAlt: ""}, {textValue: "만나서", filePath: "", imgAlt: ""}, {textValue: "반가워요", filePath: "", imgAlt: ""}, {textValue: "악", filePath: "", imgAlt: ""}]'

# 파일 읽기
with open(app_file_js, 'r', encoding='utf-8') as file:
    content = file.read()

# 정규 표현식을 사용하여 텍스트 찾기 및 변경
op2Patter = r'(name: "0716_op2 66",[\s\S]*?rowList:[\s\S]*?value: )\[[\s\S]*?\](,)'
replacement = r'\1' + op2_new_value + r'\2'

print(replacement)
new_content = re.sub(op2Patter, replacement, content, flags=re.DOTALL)

# 파일 저장
with open(app_file_js, 'w', encoding='utf-8') as file:
    file.write(new_content)

print("파일이 성공적으로 업데이트되었습니다.")

# 여러 JS 파일을 ZIP 파일로 압축
js_files = [
    f"{file_path}app-1721208887818.js",
    f"{file_path}GlobalConfig-1721208887818.js",
    f"{file_path}import-libraries-1721208887818.js",
    f"{file_path}index.html",
    f"{file_path}runner-1721208887818.js",
    f"{file_path}SUIT-Bold.ttf"
]

# 압축 파일 이름
zip_filename = 'test.zip'

# zip 파일 생성 및 파일 추가
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for file in js_files:
        zipf.write(file, arcname=os.path.basename(file))

print(f"{zip_filename} 파일이 성공적으로 생성되었습니다.")
