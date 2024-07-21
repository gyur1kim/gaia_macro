import pandas as pd

def read_excel_data(file_name):
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)  

    row = 1

    # 엑셀 파일 읽기
    df_sheet_all = pd.read_excel(io=file_name, 
        sheet_name=None, 
        header=None,
        index_col=None,                                 
        engine='openpyxl',
        dtype=str)    

    # 엑셀 시트 별 리스트 맵
    excel_map = dict()

    # 데이터 개수만큼 반복하기
    for sheet_name in df_sheet_all.keys():
        # 데이터 시트
        df_sheet = df_sheet_all[sheet_name]
        df_sheet = df_sheet.fillna("")        
        df_sheet = df_sheet[2:]
        list_sheet = df_sheet.values.tolist()
        excel_map[sheet_name] = list_sheet

    return excel_map, row