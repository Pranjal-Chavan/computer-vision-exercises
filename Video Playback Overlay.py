import cv2 as cv

capture = cv.VideoCapture('Videos/video_ex1.avi')

fourcc = cv.VideoWriter_fourcc(*'mp4v')
fps = int(capture.get(cv.CAP_PROP_FPS))
total_frames = int(capture.get(cv.CAP_PROP_FRAME_COUNT))
duration = total_frames / fps
width = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))

print(f"Video FPS:{fps}")
print(f"Total Duration : {duration:0.2f} seconds")

output_path = "video_ex1.avi"

out = cv.VideoWriter('output/sample_video.mp4', fourcc, fps, (width, height))
frame_num = 0
while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        break
    elapsed_time = frame_num / fps
    remaining_time = duration - elapsed_time

    r=text = f"Elapsed : {elapsed_time:0.1f}s | Remaining:{remaining_time :0.1f}s" 
    cv.putText(frame, text, (10,30),cv.FONT_HERSHEY_SIMPLEX, 0.8,(0,0,255), 2)  

    cv.imshow('Video with Overlay', frame)

    if elapsed_time <=10:
          out.write(frame)
    else:
           break
    frame_num+=1
    if cv.waitKey(1) & 0xFF == ord('q') :
         break

capture.release()
out.release()
cv.destroyAllWindows()
