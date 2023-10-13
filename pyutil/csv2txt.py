import csv

# CSV 파일의 경로
csv_file_path = '/data/lg22/custom_data/tiers_indoor06/pose/indoor05_fastlio_os128.csv'

# 변환된 텍스트를 저장할 파일의 경로
txt_file_path = '/data/lg22/custom_data/tiers_indoor06/pose/indoor05_fastlio_os128.txt'

# CSV 파일을 읽어서 텍스트로 변환하여 저장
with open(csv_file_path, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # 텍스트 데이터를 저장할 문자열
    text_data = ""
    
    for row in csv_reader:
        # 각 행의 열을 스페이스로 구분하여 문자열로 연결
        row_text = ' '.join(row)
        
        # 행을 구분하기 위해 엔터 문자를 추가
        text_data += row_text + '\n'

# 변환된 텍스트를 텍스트 파일에 저장
with open(txt_file_path, 'w') as txt_file:
    txt_file.write(text_data)

print("Succest convert csv to txt. File directory: ", txt_file_path)