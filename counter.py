import cv2
from ultralytics import YOLO

# مسیر فایل ویدئو
video_path = "F:/Mix/Timeless/Programmable Matter/Month 7/traffic.mp4"
output_path = "output_final.mp4"

model = YOLO("yolov8n.pt")
CLASSES_TO_COUNT = [0, 2, 5, 7]

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("❌ خطا در باز کردن فایل!")
    exit()

# تنظیمات ذخیره
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))
LINE_Y = int(frame_height * 0.6)

# --- تغییر مهم: ایجاد پنجره قبل از شروع حلقه ---
cv2.namedWindow("AI Traffic Counter", cv2.WINDOW_NORMAL)
cv2.resizeWindow("AI Traffic Counter", 1024, 768) # تنظیم سایز پنجره

track_history = {}
counted_ids = set()
total_count = 0

print("شروع پردازش... (اگر پنجره سیاه است چند ثانیه صبر کنید)")

while True:
    success, frame = cap.read()
    if not success:
        break

    results = model.track(frame, classes=CLASSES_TO_COUNT, persist=True)
    
    # رسم خط
    cv2.line(frame, (0, LINE_Y), (frame_width, LINE_Y), (0, 255, 0), 3)

    if results[0].boxes.id is not None:
        boxes = results[0].boxes.xywh.cpu()
        track_ids = results[0].boxes.id.int().cpu().tolist()
        class_ids = results[0].boxes.cls.int().cpu().tolist()

        for box, track_id, class_id in zip(boxes, track_ids, class_ids):
            x, y, w, h = box
            x1, y1 = int(x - w/2), int(y - h/2)
            x2, y2 = int(x + w/2), int(y + h/2)
            current_y = int(y + h/2)

            color = (255, 0, 0)
            if class_id == 7: color = (0, 0, 255)   # کامیون قرمز
            elif class_id == 5: color = (255, 0, 255) # اتوبوس بنفش

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.circle(frame, (int(x), current_y), 5, color, -1)
            
            # منطق شمارش
            if track_id in track_history:
                if track_history[track_id] < LINE_Y and current_y >= LINE_Y:
                    if track_id not in counted_ids:
                        total_count += 1
                        counted_ids.add(track_id)
                        cv2.line(frame, (0, LINE_Y), (frame_width, LINE_Y), (0, 0, 255), 5)
            track_history[track_id] = current_y

    cv2.putText(frame, f"Total: {total_count}", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

    out.write(frame)
    
    # نمایش
    cv2.imshow("AI Traffic Counter", frame)
    
    # دکمه خروج
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
print("پایان.")