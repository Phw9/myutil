# -*- coding: utf-8 -*-
import cv2
import numpy as np

def match_sift_features(image1, image2):
    # SIFT 특징점 매칭
    sift = cv2.xfeatures2d.SIFT_create()
    keypoints1, descriptors1 = sift.detectAndCompute(image1, None)
    keypoints2, descriptors2 = sift.detectAndCompute(image2, None)
    
    # 특징점 매칭
    matcher = cv2.BFMatcher()
    matches = matcher.match(descriptors1, descriptors2)
    
    # 매칭된 특징점의 위치 정보 추출
    image_points1 = np.array([keypoints1[match.queryIdx].pt for match in matches], dtype=np.float32)
    image_points2 = np.array([keypoints2[match.trainIdx].pt for match in matches], dtype=np.float32)
    print(len(image_points1), len(image_points2))
    return image_points1, image_points2

def estimate_essential_matrix(image_points1, image_points2, left_camera_matrix, right_camera_matrix, method=cv2.RANSAC, threshold=1.0):
    # 정규화된 좌표로 변환
    image_points1_norm = cv2.undistortPoints(image_points1, left_camera_matrix, left_distortion_coeffs)
    image_points2_norm = cv2.undistortPoints(image_points2, right_camera_matrix, right_distortion_coeffs)
    
    # Essential Matrix 계산
    essential_matrix, _ = cv2.findEssentialMat(image_points1_norm, image_points2_norm, left_camera_matrix, left_distortion_coeffs,
                                               right_camera_matrix, right_distortion_coeffs, method, 0.999, threshold)
    
    return essential_matrix

# 이미지 로드
image1 = cv2.imread("/data/mid360/bag/cvlabDSR/0529/0.png", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("/data/mid360/bag/cvlabDSR/0529/1.png", cv2.IMREAD_GRAYSCALE)

# SIFT 특징점 추출
image_points1, image_points2 = match_sift_features(image1, image2)

# 카메라 매트릭스 설정
left_camera_matrix = np.array([[717.48487592, 0, 625.20936079], [0, 715.5205414, 358.65265012], [0, 0, 1]])
right_camera_matrix = np.array([[718.34717159, 0, 624.16894738], [0, 717.58060798, 350.42240018], [0, 0, 1]])
left_distortion_coeffs = np.array([-0.32589524, 0.09047102, -0.00042549, 0.00210588, 0.0])
right_distortion_coeffs = np.array([-0.34289874, 0.11711671, 0.00002237, -0.00019816, 0.0])

# Essential Matrix 계산
essential_matrix = estimate_essential_matrix(image_points1, image_points2, left_camera_matrix, right_camera_matrix)

# 결과 출력
print("Essential Matrix:")
print(essential_matrix)
