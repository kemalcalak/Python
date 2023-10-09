import cv2
import torch
from sahi.utils.yolov8 import download_yolov8s_model
from sahi import AutoDetectionModel
from sahi.predict import get_sliced_prediction

# CUDA kullanılabilir mi?
print(torch.cuda.is_available())

# CUDA cihazlarını listele
print(torch.cuda.device_count())

# Aktif CUDA cihazının adını ve özelliklerini alın
print(torch.cuda.get_device_name(torch.cuda.current_device()))

# CUDA kullanacak şekilde ayarlayın
device = "cuda:1"  # GPU 1'i kullanacak şekilde ayarlandı

yolov8_model_path = "best.pt"
download_yolov8s_model(yolov8_model_path)

# Modeli CUDA cihazına yükleyin
detection_model = AutoDetectionModel.from_pretrained(
    model_type='yolov8',
    model_path=yolov8_model_path,
    confidence_threshold=0.3,
    device=device,  # Yukarıda ayarladığınız CUDA cihazını kullanın
)

videocapture = cv2.VideoCapture("f1.mp4")

output_video_name = "output_tracking.mp4"
frame_width = int(videocapture.get(3))
frame_height = int(videocapture.get(4))
fps = int(videocapture.get(5))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  
output_video = cv2.VideoWriter(output_video_name, fourcc, fps, (frame_width, frame_height))

while(videocapture.isOpened()):
    success, frame = videocapture.read()
    if success == True:
        results = get_sliced_prediction(frame, detection_model, slice_height=256, slice_width=256,
                                       overlap_height_ratio=0.2, overlap_width_ratio=0.2)
        object_prediction_list = results.object_prediction_list

        boxes_list = []
        confs_list = []
        clss_list = []
        for ind, data in enumerate(object_prediction_list):
            boxes = object_prediction_list[ind].bbox.minx, object_prediction_list[ind].bbox.miny,\
                    object_prediction_list[ind].bbox.maxx, object_prediction_list[ind].bbox.maxy
            confs = object_prediction_list[ind].score.value
            clss = object_prediction_list[ind].category.name
            boxes_list.append(boxes)
            confs_list.append(confs)
            clss_list.append(clss)

        for box, conf, cls in zip(boxes_list, confs_list, clss_list):
            x1, y1, x2, y2 = box
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)
            label = str(cls) + ":" + str(format(conf, '.2f'))
            t_size = cv2.getTextSize(label, 0, fontScale=0.6, thickness=1)[0]
            cv2.rectangle(frame, (int(x1), int(y1) - t_size[1] - 3), (int(x1) + t_size[0], int(y1) + 3), (0, 255, 0), -1)
            cv2.putText(frame, label, (int(x1), int(y1) - 2), 0, 0.6, [0, 0, 0], thickness=1, lineType=cv2.LINE_AA)

        output_video.write(frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

output_video.release()
videocapture.release()
cv2.destroyAllWindows()
