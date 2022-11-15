# ASL Sign-Language-Detection-YOLOV5
- A real time software system that will be able to recognize ASL hand-gestures using deep learning techniques.
- This project aims to predict the 'alphabet' gesture of the ASL.
![ASL_Home](https://user-images.githubusercontent.com/96101074/201936672-67f1e866-22f0-44e5-ae2e-f9672765b7b3.png)

“Blindness cuts us off from things, but deafness cuts us off from people." - Helen Keller
Let's comunicate, connect and learn American Sign Language  

# Demo 
- **Real-Time ASL Detection**
![Hello_](https://user-images.githubusercontent.com/96101074/201928579-92855206-76ee-4825-b3bd-13a1cbceb351.gif)
- **ASL Image Prediction**
![D_ASL_predimg](https://user-images.githubusercontent.com/96101074/201934423-7278b270-74f2-4c77-b8fe-6efe21baff46.png)

# Project Overview
- **Dataset :** 
**Training Dataset:** Downloaded from Roboflow. [ASLDataset_YOLOv5_pytorch](https://public.roboflow.com/object-detection/american-sign-language-letters/1/download/yolov5pytorch )
**Testing Dataset:** Clicked sample Img for 'HELLO' word using Opencv lib and annotated with **LabelImg lib**.

- **Model Training:** You Only Look Once Model **(YOLO V5)** model is used for training. Training is done on COLAB NOTEBOOK with GPU. [Notebook](https://github.com/Mahimajain25/Sign-Language-Detection-YOLOV5/blob/main/Sign_language_Generation.ipynb)

- **MOdel Evaluation** Training losses and performance metrics are saved to Tensorboard.

- **Model Detection :** Best weights are used for Real-Time detection and for image prediction.

- **How to run the project ?** write python app.py in terminal.

### **Technologies used**
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Tensorflow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)
![Opencv](https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=white)
![pytorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=PyTorch&logoColor=white)

### **Tools used**
![vscode](https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
## Contact

- linkedin - https://www.linkedin.com/in/mahima-jain-41b540191/
- gmail - mahimaj25@gmail.com

