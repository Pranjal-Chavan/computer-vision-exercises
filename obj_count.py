import cv2
from ultralytics import YOLO
from collections import defaultdict

def track_entry_exit(video_path, output_path, model_path="yolov8n.pt"):
    model = YOLO(model_path)

    # Define 3 lines
    lines = {
        "1": [(150, 300), (300, 100)],
        "2": [(500, 100), (800, 250)],
        "3": [(500, 500), (770, 320)]
    }

    # Setup video capture and writer
    cap = cv2.VideoCapture(video_path)
    assert cap.isOpened(), "Could not open video."
    w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

    # Person tracking data
    track_history = {}
    entry_exit_counts = defaultdict(int)

    # Line crossing logic
    def crossed_line(p1, p2, line):
        def direction(a, b, c):
            return (c[0] - a[0]) * (b[1] - a[1]) - (b[0] - a[0]) * (c[1] - a[1])
        d1 = direction(line[0], line[1], p1)
        d2 = direction(line[0], line[1], p2)
        return d1 * d2 < 0

    # Run model tracking
    results = model.track(source=video_path, persist=True, classes=[0], stream=True)

    for r in results:
        frame = r.orig_img
        boxes = r.boxes

        if boxes is not None and boxes.id is not None:
            for box, track_id in zip(boxes.xyxy.cpu().numpy(), boxes.id.cpu().numpy()):
                x1, y1, x2, y2 = box
                cx, cy = int((x1 + x2) / 2), int((y1 + y2) / 2)

                if track_id not in track_history:
                    track_history[track_id] = {"points": [], "lines": []}

                track_history[track_id]["points"].append((cx, cy))

                if len(track_history[track_id]["points"]) >= 2:
                    prev = track_history[track_id]["points"][-2]
                    curr = track_history[track_id]["points"][-1]

                    for key, line in lines.items():
                        if key not in track_history[track_id]["lines"] and crossed_line(prev, curr, line):
                            track_history[track_id]["lines"].append(key)

                # Count entry/exit once at least 2 lines crossed
                lines_crossed = track_history[track_id]["lines"]
                if len(lines_crossed) >= 2:
                    entry, exit = lines_crossed[0], lines_crossed[-1]
                    label = f"{entry}_to_{exit}"
                    entry_exit_counts[label] += 1
                    # Prevent overcounting
                    track_history[track_id]["lines"] = [exit]

        # Draw lines and labels
        for key, (pt1, pt2) in lines.items():
            cv2.line(frame, pt1, pt2, (0, 255, 255), 2)
            cv2.putText(frame, f"Line {key}", pt1, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

        # Draw counts on top-left
        y_offset = 30
        for i, (label, count) in enumerate(entry_exit_counts.items()):
            cv2.putText(frame, f"{label}: {count}", (10, y_offset + i * 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        cv2.imshow("Entry/Exit Tracker", frame)
        out.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    print("\n=== Final Entry/Exit Counts ===")
    for label, count in entry_exit_counts.items():
        print(f"{label}: {count}")


# ✅ Call your function
track_entry_exit(
    video_path=r"C:\Users\pranj\OneDrive\Desktop\INTERNSHIP\OPEN_CV\PHOTOS\Object_Tracking.mp4",
    output_path=r"C:\Users\pranj\OneDrive\Desktop\INTERNSHIP\OPEN_CV\PHOTOS\Object_Tracking1234.mp4",
    model_path="yolov8n.pt"
)
