import cv2
import numpy as np

def compute_stereo_rectification(camera_matrix1, distortion_coeffs1, camera_matrix2, distortion_coeffs2, image_size, R, T):
    R1, R2, P1, P2, Q, _, _ = cv2.stereoRectify(camera_matrix1, distortion_coeffs1, camera_matrix2, distortion_coeffs2, image_size, R, T,  flags=cv2.CALIB_ZERO_DISPARITY, alpha=-1)
    return R1, R2, P1, P2, Q

# 카메라 매트릭스 및 왜곡 계수 설정
camera_matrix1 = np.array([[717.48487592, 0, 625.20936079], [0, 715.5205414, 358.65265012], [0, 0, 1]])
distortion_coeffs1 = np.array([-0.32589524, 0.09047102, -0.00042549, 0.00210588, 0.0])
camera_matrix2 = np.array([[718.34717159, 0, 624.16894738], [0, 717.58060798, 350.42240018], [0, 0, 1]])
distortion_coeffs2 = np.array([-0.34289874, 0.11711671, 0.00002237, -0.00019816, 0.0])

# 이미지 크기 설정
image_size = (1280, 720) # width / height

# 회전 행렬 및 이동 벡터 설정
R = np.array([[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1]], dtype=np.float64)
T = np.array([-0.11891386, -0.0008921, 0.00109607], dtype=np.float64)


R1, R2, P1, P2, Q = compute_stereo_rectification(camera_matrix1, distortion_coeffs1, camera_matrix2, distortion_coeffs2, image_size, R, T)

# 결과 출력
print("Rectification R1:")
print(R1)
print("Rectification R2:")
print(R2)
print("Projection P1:")
print(P1)
print("Projection P2:")
print(P2)
print("Disparity-to-depth mapping matrix Q:")
print(Q)
