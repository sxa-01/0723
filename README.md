## Fire, smoke, and human recognition based on the YOLO model 🔥 🌫️

## Introduction
This project can be used to detect smoke, flames, and people, or further optimized based on this model.

![val_batch1_labels](https://github.com/user-attachments/assets/c7bbb5ac-d7dd-4833-bcb9-4b5428664cde)

## Get Started
- Open "0723/test.py"
- Check if the file path for “best.pt” is correct. The path is usually located in “runs/detect/train/weights/”.
- Check the file path of the test file. There are videos and images in the “test set” that can be used for testing. You can also use your own images or videos for testing.
- Run the code, and the test results will be available in a short time. The test results are saved in “runs/detect/predict.”

### Prerequisites
- Python 3.8+
- Install the Ultralytics YOLO library ———— You can learn how to install it on the official website（ https://docs.ultralytics.com/zh/quickstart/ ）
- Install Pytorch： ```pip3 install torch torchvision torchaudio``` （ URL：https://pytorch.org/get-started/locally/ ）
  
### Data set
- For image data, you can use your own annotated data for training. The data source we used is roboflow (URL: https://universe.roboflow.com/yolo-training-8hmw2/fire-person-dataset).
- This includes 22,169 training sets, 995 validation sets, and 718 test sets.
- Through inspection and training, this dataset has some errors in data annotation, and there may be omissions in the annotation, which may affect the model's learning.
- After training the model, it was found that there were significant differences in the number of training samples for flames, smoke, and people, with fewer samples for people than for fire and smoke.

![val_batch1_labels](https://github.com/user-attachments/assets/71546def-b7b2-437a-a036-12227296d90a)

![val_batch1_pred](https://github.com/user-attachments/assets/85a4c49b-5969-4934-9dec-478662555a18)


### Hint
- When training on your own, you need to modify the data and file paths in the “data.yaml” file.
- In “main_code.py,” you can use any hardware you prefer. Generally, CPUs can run YOLO, but they are slower and more suitable for small-scale testing, so we recommend using a GPU instead.
- GPU usage varies across different systems: Apple systems use MPS, while Windows systems use CUDA.
- Regarding pre-trained model selection: You can choose your own model; the code uses the YOLO8 model.
- Training parameters (epochs, imgsz, batch, etc.) can be adjusted and selected according to your needs.
