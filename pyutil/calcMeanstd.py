import numpy as np

# 텍스트 파일 로드
VIOdata = np.loadtxt('/data/lic_lio.log') # 세 번째 열이 per frame VIO time
LIOdata = np.loadtxt('/data/lic_lio_costtime.log') # 두 번째 열이 per frame LIO time이고, 세 번째 열은 평균낸 시간
LIOdata = LIOdata * 1000
# 세 번째 열 데이터 추출 (Python 인덱스는 0부터 시작하므로 인덱스 2가 세 번째 열이 됩니다)
VIOcolumn = VIOdata[:, 2]
LIOcolumn = LIOdata[:, 1]

# 평균 계산
VIOmean = np.mean(VIOcolumn)
LIOmean = np.mean(LIOcolumn)
print('VIO Mean:', VIOmean)
print('LIO Mean:', LIOmean)

# 표준편차 계산
VIOstd_dev = np.std(VIOcolumn)
LIOstd_dev = np.std(LIOcolumn)
print('VIO Standard Deviation:', VIOstd_dev)
print('LIO Standard Deviation:', LIOstd_dev)

print('Total mean: ',VIOmean + LIOmean)
print('Total std: ',VIOstd_dev + LIOstd_dev)