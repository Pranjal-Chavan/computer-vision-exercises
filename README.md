# computer-vision-exercises
This repository contains 4 basic hands-on OpenCV tasks for practicing computer vision concepts such as image processing, video playback and drawing using Python.

#Task 1 : Basic drawing and processing image : In this rectangle, circle, line, and text is put on and resizing and cropping of image is done.

#Task 2 : Image Tiling : In this the image is separated in 2*2 grids but as output it gives the same image so no difference is seen, therefore to create a difference a two separated images are flipped and rotated.

#Task 3 : Video playback Overplay : In this on each frame a text is overlayed showing elasped time and remaining time.

#Task 4 : Side by Side Video Player : In this displaying the video side by side synchronized.

#Task5 : This compares YOLOv8's person detection performance on different image sizes (`imgsz`) using the `yolov8n.pt` model. The goal is to observe the trade-offs between **accuracy** and **speed** when using lower vs higher image resolutions. - Use YOLOv8 to detect only persons (`classes=[0]`).
- Test detection using:
  - `imgsz = 320` (low resolution)
  - `imgsz = 640` (high resolution)
- Compare:
  - Detection accuracy (especially on small/distant persons)
  - Processing speed

#Task 6 : - Person detection using `yolov8n.pt`
- Tracks people across video frames
- Detects line-crossing events across 3 custom lines
- Counts how many people crossed from:
  - Line 1 ➝ Line 2 or 3
  - Line 2 ➝ Line 1 or 3
  - Line 3 ➝ Line 1 or 2
- Saves annotated video with live count display
- Modular code with easy customization
