# Emotion-Recognition

# Requirements
- Use Windows 10 with Conda;
- Run `conda create -n tf tensorflow-gpu=2.6.0` to setup env;
- Install `pandas` and `matplotlib` with conda;
- Install `cv2` with `pip install opencv-python`.

# Result
This Network is robust for input images with random noise. The training history is shown below:
![image](https://user-images.githubusercontent.com/69796042/217718455-b567b0cf-9f6b-404a-8bf3-995592442423.jpeg)


## Without denoiser
If we use VGG16 model, but without denoiser:
```
449/449 [==============================] - 4s 10ms/step - loss: 1.0417 - accuracy: 0.6025 - auc: 0.9092
Clean samples clean vgg16 prediction accuracy: 0.6025355458259583
449/449 [==============================] - 4s 9ms/step - loss: 2.0303 - accuracy: 0.2063 - auc: 0.6171
Dirty samples clean vgg16 prediction accuracy: 0.20632487535476685
```
As is shown in the result above, the accuracy of dirty samples is only 20%.

## With denoiser
With the help of the denoiser from this project, we can significantly increase the prediction accuracy: 
```
449/449 [==============================] - 4s 9ms/step - loss: 1.1331 - accuracy: 0.5747 - auc: 0.8917
Clean samples clean hybrid prediction accuracy: 0.5746726393699646
449/449 [==============================] - 5s 10ms/step - loss: 1.1537 - accuracy: 0.5669 - auc: 0.8876
Dirty samples clean hybrid prediction accuracy: 0.5668709874153137
```

As is shon in the result above, the accuracy of dirty samples reached 56.69%, almost the same as the result of the clean samples.
