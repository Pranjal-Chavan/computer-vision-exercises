import cv2 as cv

capture = cv.VideoCapture('Videos/video_ex1.avi')

fps = capture.get(cv.CAP_PROP_FPS)
print(f" Video FPS : {fps}")

output_width = 1920
output_height = 1080

fourcc = cv.VideoWriter_fourcc(*'mpv4')
out = cv.VideoWriter('output/Side by Side.mp4', fourcc, fps, (output_width, output_height))

while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        break

    resized_frame = cv.resize(frame, (output_width//4 , output_height//2))
    left = resized_frame
    right = resized_frame.copy()
    combined = cv.hconcat([left, right])

    cv.imshow("Side by side", combined)
    out.write(combined)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
out.release()
cv.destroyAllWindows()

