# -*- coding: utf-8 -*-
import re
import os
import zipfile
import shutil

WORK_FOLDER_PATH = 'C:/Users/qri/Desktop/gaia_macro/'
SAVE_FILE_PATH = 'C:/Users/qri/Downloads/'
FILE_ID = '1721484218170'

# 선다형 파일 복사+붙여넣기
OPTION_FILES_ORIGIN = [
    f'{WORK_FOLDER_PATH}선다형/app-{FILE_ID}.js',
    f'{WORK_FOLDER_PATH}선다형/GlobalConfig-{FILE_ID}.js',
    f'{WORK_FOLDER_PATH}선다형/import-libraries-{FILE_ID}.js',
    f'{WORK_FOLDER_PATH}선다형/index.html',
    f'{WORK_FOLDER_PATH}선다형/runner-{FILE_ID}.js',
    f'{WORK_FOLDER_PATH}선다형/SUIT-Bold.ttf',
]

for OPTION_FILE in OPTION_FILES_ORIGIN:
    destination_file = os.path.join(WORK_FOLDER_PATH, os.path.basename(OPTION_FILE))
    
    try:
        # 파일 복사
        shutil.copy2(OPTION_FILE, WORK_FOLDER_PATH)
        print(f"파일이 성공적으로 복사되었습니다: {destination_file}")
    except FileNotFoundError:
        print(f"원본 파일을 찾을 수 없습니다: {OPTION_FILE}")
    except PermissionError:
        print(f"권한이 없습니다: {destination_file}")
    except Exception as e:
        print(f"파일 복사 중 오류가 발생했습니다: {e}")


# 컴포넌트명
FRANE_COMP_NAME = 'kgr_240719_frame2 65'

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

# 파일 경로 설정
OP_APP_FILE_NAME = f'{WORK_FOLDER_PATH}app-{FILE_ID}.js'

# 파일 읽기
with open(OP_APP_FILE_NAME, 'r', encoding='utf-8') as FILE:
    OP_APP_FILE = FILE.read()

# 텍스트0 변경
text0_value = r''
text0_pattern = fr'("?name"?:\s?"{TEXT0_COMP_NAME}"[\s\S]*?content"?:\s?{{[\s\S]*?value"?:\s?{{[\s\S]*?false)[\s\S]*?(}},)'
text0_replacement = fr'\1, "value": "{text0_value}"\2'

# 오디오0 변경
audio0_value = ''
audio0_pattern = fr'("?name"?:\s?"{AUDIO_COMP_NAME}"[\s\S]*?content"?:\s?{{[\s\S]*?filePath"?:\s?{{[\s\S]*?false)[\s\S]*?(}},)'
audio0_replacement = fr'\1, "value": "{audio0_value}"\2'

# 텍스트1 변경
text1_value = r''
text1_pattern = fr'("?name"?:\s?"{TEXT1_COMP_NAME}"[\s\S]*?content"?:\s?{{[\s\S]*?value"?:\s?{{[\s\S]*?false)[\s\S]*?(}},)'
text1_replacement = fr'\1, "value": "{text1_value}"\2'

# 이미지1 변경
img1_filePath = ''
img1_imgAlt = ''
img1_pattern = fr'("?name"?:\s?"{IMG1_COMP_NAME}"[\s\S]*?content"?:\s?{{[\s\S]*?filePath"?:\s?{{[\s\S]*?false)[\s\S]*?(}},[\s\S]*?imgAlt"?:\s?{{[\s\S]*?false)[\s\S]*?(}},?[\s\S]*?}},?)'
img1_replacement = fr'\1, "filePath": "{img1_filePath}" \2, "imgAlt": "{img1_imgAlt}"\3'

# 박스1 변경
box1_value = r''
box1_pattern = fr'("?name"?:\s?"{BOX1_COMP_NAME}"[\s\S]*?content"?:\s?{{[\s\S]*?value"?:\s?{{[\s\S]*?false)[\s\S]*?(}},?[\s\S]*?}},?)'
box1_replacement = fr'\1, "value": "{box1_value}"\2'

# 보기박스1 변경
ex1_value = r''
ex1_pattern = fr'("?name"?:\s?"{EX1_COMP_NAME}"[\s\S]*?content"?:\s?{{[\s\S]*?value"?:\s?{{[\s\S]*?false)[\s\S]*?(}},?[\s\S]*?}},?)'
ex1_replacement = fr'\1, "value": "{ex1_value}"\2'

# 텍스트2 변경
text2_value = r''
text2_pattern = fr'("?name"?:\s?"{TEXT2_COMP_NAME}"[\s\S]*?content"?:\s?{{[\s\S]*?value"?:\s?{{[\s\S]*?false)[\s\S]*?(}},)'
text2_replacement = fr'\1, "value": "{text2_value}"\2'

# 이미지2 변경
img2_filePath = ''
img2_imgAlt = ''
img2_pattern = fr'("?name"?:\s?"{IMG2_COMP_NAME}"[\s\S]*?content"?:\s?{{[\s\S]*?filePath"?:\s?{{[\s\S]*?false)[\s\S]*?(}},[\s\S]*?imgAlt"?:\s?{{[\s\S]*?false)[\s\S]*?(}},?[\s\S]*?}},?)'
img2_replacement = fr'\1, "filePath": "{img2_filePath}" \2, "imgAlt": "{img2_imgAlt}"\3'

# 박스2 변경
box2_value = r''
box2_pattern = fr'("?name"?:\s?"{BOX2_COMP_NAME}"[\s\S]*?content"?:\s?{{[\s\S]*?value"?:\s?{{[\s\S]*?false)[\s\S]*?(}},?[\s\S]*?}},?)'
box2_replacement = fr'\1, "value": "{box2_value}"\2'

# 보기박스2 변경
ex2_value = r''
ex2_pattern = fr'("?name"?:\s?"{EX2_COMP_NAME}"[\s\S]*?content"?:\s?{{[\s\S]*?value"?:\s?{{[\s\S]*?false)[\s\S]*?(}},?[\s\S]*?}},?)'
ex2_replacement = fr'\1, "value": "{ex2_value}"\2'

# 선지 변경
op_row_list = r'[]'
op_answer = '1'
op_pattern = fr'("?name"?:\s?"{OP_COMP_NAME}"[\s\S]*?rowList"?:\s?{{[\s\S]*?value"?:\s?)\[[\s\S]*?\](,?[\s\S]*?}}[\s\S]*?correctAnswer"?:\s?{{[\s\S]*?false)[\s\S]*?(}},)'
op_replacement = fr'\1{op_row_list}\2, "value": {op_answer}\3'

# frame
frame_translations = r'[{"filePath": "","imgAlt": "","text": "여기는 해석이 옵니다.",},]'
frame_explanations = r'[{"filePath": "","imgAlt": "","text": "여기는 해설이 옵니다.",},]'
frame_correct_answer = r'[{"answer": "1", "filePath": "", "imgAlt": "", "text": "5"},]'
frame_scripts = r'[{ "english": "", "translation": ""}]'
frame_pattern = fr'(name"?:\s?"{FRANE_COMP_NAME}",[\s\S]*?translations"?:[\s\S]*?value"?:\s?)\[[\s\S]*?\](,?[\s\S]*?}},[\s\S]*?explanations"?:[\s\S]*?value"?:\s?)\[[\s\S]*?\](,?[\s\S]*?}},[\s\S]*?correctAnswer"?:[\s\S]*?value"?:\s?)\[[\s\S]*?\](,?[\s\S]*?}},[\s\S]*?scripts"?:[\s\S]*?value"?:\s?)\[[\s\S]*?\](,?[\s\S]*?}},)'
frame_replacement = fr'\1{frame_translations}\2{frame_explanations}\3{frame_correct_answer}\4{frame_scripts}\5'

OP_APP_FILE = re.sub(text0_pattern, text0_replacement, OP_APP_FILE, flags=re.DOTALL)
OP_APP_FILE = re.sub(audio0_pattern, audio0_replacement, OP_APP_FILE, flags=re.DOTALL)

OP_APP_FILE = re.sub(text1_pattern, text1_replacement, OP_APP_FILE, flags=re.DOTALL)
OP_APP_FILE = re.sub(img1_pattern, img1_replacement, OP_APP_FILE, flags=re.DOTALL)
OP_APP_FILE = re.sub(box1_pattern, box1_replacement, OP_APP_FILE, flags=re.DOTALL)
OP_APP_FILE = re.sub(ex1_pattern, ex1_replacement, OP_APP_FILE, flags=re.DOTALL)

OP_APP_FILE = re.sub(text2_pattern, text2_replacement, OP_APP_FILE, flags=re.DOTALL)
OP_APP_FILE = re.sub(img2_pattern, img2_replacement, OP_APP_FILE, flags=re.DOTALL)
OP_APP_FILE = re.sub(box2_pattern, box2_replacement, OP_APP_FILE, flags=re.DOTALL)
OP_APP_FILE = re.sub(ex2_pattern, ex2_replacement, OP_APP_FILE, flags=re.DOTALL)

# 프레임
OP_APP_FILE = re.sub(frame_pattern, frame_replacement, OP_APP_FILE, flags=re.DOTALL)

# 선다형
OP_APP_FILE = re.sub(op_pattern, op_replacement, OP_APP_FILE, flags=re.DOTALL)

# 파일 저장
with open(OP_APP_FILE_NAME, 'w', encoding='utf-8') as FILE:
    FILE.write(OP_APP_FILE)

print("파일이 성공적으로 업데이트되었습니다.")

# 여러 JS 파일을 ZIP 파일로 압축
OPTION_FILES_IN_WORK_FOLDER = [
    f'{WORK_FOLDER_PATH}app-{FILE_ID}.js',
    f'{WORK_FOLDER_PATH}GlobalConfig-{FILE_ID}.js',
    f'{WORK_FOLDER_PATH}import-libraries-{FILE_ID}.js',
    f'{WORK_FOLDER_PATH}index.html',
    f'{WORK_FOLDER_PATH}runner-{FILE_ID}.js',
    f'{WORK_FOLDER_PATH}SUIT-Bold.ttf'
]

# 압축 파일 이름
zip_filename = f'{SAVE_FILE_PATH}test.zip'

# zip 파일 생성 및 파일 추가
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for FILE in OPTION_FILES_IN_WORK_FOLDER:
        zipf.write(FILE, arcname=os.path.basename(FILE))

print(f"{zip_filename} 파일이 성공적으로 생성되었습니다.")

# 선다형 파일 삭제하기
for OPTION_FILE in OPTION_FILES_IN_WORK_FOLDER:
    try:
        # 파일 삭제
        os.remove(OPTION_FILE)
        print(f"파일이 성공적으로 삭제되었습니다: {OPTION_FILE}")
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {OPTION_FILE}")
    except PermissionError:
        print(f"파일 삭제 권한이 없습니다: {OPTION_FILE}")
    except Exception as e:
        print(f"파일 삭제 중 오류가 발생했습니다: {e}")