from collections import defaultdict
from datetime import datetime
import time

from read_excel import read_excel_data
from option_macro import set_option_template

def set_template_and_props(excel_map, row, type_map):
    index = 0
    total_count = 0
    for sheet_name in excel_map.keys():
        sheet_list = excel_map[sheet_name]
        total_count += len(sheet_list)

    error_list = []
    success_list = []
    else_list = []
    cnt = 0
    start_time = round(time.time())

    # 시트별로 데이터 개수만큼 반복하기
    for sheet_name in excel_map.keys():
        # 시트 데이터 2차원 배열
        sheet_list = excel_map[sheet_name]

        for row, row_data in enumerate(sheet_list):    
            # 범위 지정
            index += 1
            if index < type_map['start_zip_idx']:
                continue
            elif index > type_map['end_zip_idx']:
                break

            if "수학" in sheet_name:                
                problem_number = row_data[1] # 문항 번호
                app_name = row_data[11] # 앱 이름
                subject = 'mat'
            elif "영어" in sheet_name:
                problem_number = row_data[0]
                app_name = row_data[10]
                subject = 'eng'
                
            print("----------------------------------------------------------------------------------------")
            print(f"[시작] || 문항 번호 : {problem_number} || 앱 아이디 : {app_name} || 전체 시트 ({index} / {total_count}) || {sheet_name} ({row + 1} / {len(sheet_list)})")     
            print("----------------------------------------------------------------------------------------")
            create_start_time = round(time.time())

            if "수학(선다형)" in sheet_name.replace(' ',''):
                set_option_template(row_data, app_name, '수학')
            elif "영어(선다형)" in sheet_name.replace(' ',''):
                set_option_template(row_data, app_name, '영어')
            # elif "수학(주관식-단답빈칸)" in sheet_name.replace(' ',''):
            #     short_answer_template.set_data_from_excel(driver, row_data, subject)
            # elif "수학(주관식-새끼문제)" in sheet_name.replace(' ',''):
            #     short_answer_multiple_problem_template.set_data_from_excel(driver, row_data, subject)
            # elif "영어(주관식)" in sheet_name.replace(' ',''):
            #     short_answer_template.set_data_from_excel(driver, row_data, subject)
            # elif "영어(새끼문제)" in sheet_name.replace(' ',''):
            #     short_answer_multiple_problem_template.set_data_from_excel(driver, row_data, subject)
            else:
                print(f"이름({sheet_name})이 일치하는 시트가 존재하지 않습니다.")
                
            distribute_end_time = round(time.time())

            print("----------------------------------------------------------------------------------------")
            print(f"[zip 파일 생성 완료] || 문항 번호 : {problem_number} || 앱 아이디 : {app_name} || 전체 시트 ({index} / {total_count}) || {sheet_name} ({row + 1} / {len(sheet_list)})")
            print("----------------------------------------------------------------------------------------")

            # if type_map["one_or_all"] == 1:
            #     # 업데이트
            #     if type_map["update_or_distribute"] == 1:
            #         one_update(type_map["env"], row_data, subject, error_list, success_list, else_list)
            #     # 배포
            #     else:
            #         one_upload(row_data, subject, error_list, success_list, else_list)
            
            upload_end_time = round(time.time())
            cnt += 1
            print("========================================================================================")
            print(f"- 선택한 범위 : {type_map['start_zip_idx']} ~ {type_map['end_zip_idx']}")
            print(f"- 생성한 문항 개수 : {cnt}개 || 현재 범위 ({index} / {total_count})")
            total_time = upload_end_time-start_time
            print(f"- 총 걸린 시간 : {total_time // 3600}시간 {(total_time % 3600) // 60}분 {total_time % 60}초")
            print(f"- 현재 시간 : {datetime.now()}")
            print("========================================================================================")


def init():
    type_map = defaultdict(dict)

    print("================================================================")
    print()
    zip_input_list = input(">>> 처음 index와 마지막 index를 입력해주세요. (예시 : 1,100) : ").split(',')
    print()
    type_map["start_zip_idx"] = int(zip_input_list[0].strip())
    type_map["end_zip_idx"] = int(zip_input_list[1].strip())
    print("================================================================")
    return type_map


if __name__ == "__main__":
    type_map = init()
    # 엑셀 데이터 불러오기
    excel_map, row = read_excel_data("엑셀_매크로_양식_업데이트.xlsx")
    # 엑셀 데이터로 템플릿에 값 넣기
    set_template_and_props(excel_map, row, type_map)