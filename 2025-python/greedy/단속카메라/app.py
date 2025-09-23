def solution(routes):
    routes.sort(key=lambda x: x[1])

    curr_camera = -30001
    camera_cnt = 0
    for x1, x2 in routes:
        # 진입 지점이 최근 카메라 위치보다 뒤일 경우, 카메라 추가
        if curr_camera < x1:
            curr_camera = x2
            camera_cnt += 1    

    return camera_cnt
