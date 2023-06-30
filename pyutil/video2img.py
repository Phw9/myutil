import cv2
# 동영상 파일 열기
# video_path = '/home/phw93/dev/calib/data/calibration.mov'
video_path = '/home/phw/dev/myenv/data/calibration.mov'
cap = cv2.VideoCapture(video_path)

# 프레임 카운트 초기화
frame_count = 0

# 프레임 읽기
while cap.isOpened():
    # 프레임 읽기
    ret, frame = cap.read()

    if ret:
        # 이미지 파일로 저장
        image_path = f'/home/phw/dev/myenv/data/frame_{frame_count}.jpg'
        cv2.imwrite(image_path, frame)

        # 다음 프레임으로 넘어가기
        frame_count += 1
    else:
        break

# 작업 완료 후 해제
cap.release()
