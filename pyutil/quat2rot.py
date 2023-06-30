import numpy as np
from numpy.quaternion import Quaternion

def quaternion_to_rotation(quaternion):
    # 쿼터니언 객체 생성
    quat = Quaternion(quaternion[0], quaternion[1], quaternion[2], quaternion[3])
    
    # 정규화
    quat = quat.normalized()
    
    # 회전 행렬로 변환
    rotation_matrix = np.zeros((3, 3))
    rotation_matrix[0, 0] = 1 - 2 * (quat.y**2 + quat.z**2)
    rotation_matrix[0, 1] = 2 * (quat.x * quat.y - quat.z * quat.w)
    rotation_matrix[0, 2] = 2 * (quat.x * quat.z + quat.y * quat.w)
    rotation_matrix[1, 0] = 2 * (quat.x * quat.y + quat.z * quat.w)
    rotation_matrix[1, 1] = 1 - 2 * (quat.x**2 + quat.z**2)
    rotation_matrix[1, 2] = 2 * (quat.y * quat.z - quat.x * quat.w)
    rotation_matrix[2, 0] = 2 * (quat.x * quat.z - quat.y * quat.w)
    rotation_matrix[2, 1] = 2 * (quat.y * quat.z + quat.x * quat.w)
    rotation_matrix[2, 2] = 1 - 2 * (quat.x**2 + quat.y**2)
    
    return rotation_matrix

# 쿼터니언 값 설정
quaternion = [0.99999644, -0.00055698, 0.00156046, -0.00209196]  # [w, x, y, z] 형태의 쿼터니언 값

# 회전 행렬로 변환
rotation_matrix = quaternion_to_rotation(quaternion)

# 결과 출력
print("Rotation Matrix:")
print(rotation_matrix)
