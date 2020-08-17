# facial-recognition
<h1> Workflow </h1> 
This projects takes the photos in the subfolders of "dataset", and looks for the faces using the pretrained face detection model. It then computes a 128 dimensional embedding of the face using [openFace](http://cmusatyalab.github.io/openface/)
and saves it to the embeddingss.pickle file. An SVM was then trained upon the embeddings to find a relationship between the embeddings and the face of a certain person, and that model is saved in recognizer.pickle. Realtime face-detection occurs
by detecting the face in the OpenCV frame using the face detection model, computing the embedding using openFace, then predicting whose face it is using the saved recognizer. 

<h1> Usage </h1> 
There are two ways to add a new person to be recognized.
1. Manually add a new subfolder to the dataset with the name of the person to be recognized, and add images to that subfolder (**note that the person has to be the only one in the image**). New photos can also be taken within takePhoto.py.

2. A new subfolder can be created within takePhoto.py. takePhoto.py will then also take photos and will add them automatically to the newly created subfolder. 

After a new subfolder is created with images of the new person, run utils.py to perform image augmentation upon the new subfolder. Then, run extract_embeddings.py to get the embeddings of the new pictures. After that, run train_model.py to train the SVM to detect faces. Finally, run detect_video.py, which should provide real-time face recognition. 

<h1> Todo: </h1>
 -[x] Add automatic image capturing script <br>
 -[x] Add image augmentation script so it reflects images over y-axis and generated new images with different lighting <br>
 -[ ] Change extract_embeddings.py so it only looks over the new images <br>
 -[ ] Build model testing framework to get an evaluation metric for the SVM <br>
 -[ ] Fine tune SVM for better accuracy <br>
 -[ ] Expand unknown person dataset <br>
 -[ ] Create a main.py script that can run all the other scripts
 
 <h1> Notes </h1>
A single photo (of which image augmention is run) should be enough for the model to detect that person in that pose with high confidence regardless of the lighting. But, generally the more photos of a person the model has, the better its accuracy. 
 
    
