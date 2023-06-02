import numpy as np

def inverse_SE3(T):
    R = T[:3, :3]  # 회전 행렬 추출
    p = T[:3, 3]  # 위치 벡터 추출

    inv_R = np.transpose(R)  # 회전 행렬의 전치행렬 계산
    inv_p = -np.dot(inv_R, p)  # 위치 벡터의 반대 방향으로 이동한 벡터 계산

    inv_T = np.eye(4)  # 단위 행렬 생성
    inv_T[:3, :3] = inv_R  # 회전 행렬 대입
    inv_T[:3, 3] = inv_p  # 위치 벡터 대입

    return inv_T

def multiply_SE3(T1, T2):
    R1 = T1[:3, :3]  # 첫 번째 행렬의 회전 행렬
    p1 = T1[:3, 3]  # 첫 번째 행렬의 위치 벡터

    R2 = T2[:3, :3]  # 두 번째 행렬의 회전 행렬
    p2 = T2[:3, 3]  # 두 번째 행렬의 위치 벡터

    R = np.dot(R1, R2)  # 회전 행렬 간의 곱셈
    p = np.dot(R1, p2) + p1  # 회전 행렬과 위치 벡터의 곱셈 및 덧셈

    T = np.eye(4)  # 단위 행렬 생성
    T[:3, :3] = R  # 회전 행렬 대입
    T[:3, 3] = p  # 위치 벡터 대입

    return T


imu2sensor = np.array([[1., 0., 0., 6.253],
                       [0., 1., 0., -11.775],
                       [0., 0., 1., 7.645],
                       [0., 0., 0., 1.]])
sensor2imu = inverse_SE3(imu2sensor)
lidar2sensor = np.array([[-1., 0., 0., 0.],
                       [0., -1., 0., 0.],
                       [0., 0., 1., 38.195],
                       [0., 0., 0., 1.]])

print(sensor2imu)
print(multiply_SE3(lidar2sensor,sensor2imu))
