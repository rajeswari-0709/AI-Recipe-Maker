from ultralytics import YOLO

# Pretrained YOLOv8 model
model = YOLO("yolov8n.pt")


def detect_ingredient(image_path):

    results = model(image_path)

    detected_items = []

    for result in results:

        for box in result.boxes:

            class_id = int(box.cls[0])

            label = result.names[class_id]

            detected_items.append(label)

    detected_items = list(set(detected_items))

    if len(detected_items) == 0:
        return ""

    return ", ".join(detected_items)