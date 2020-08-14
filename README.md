# facial-recognition
<h1> Workflow </h1> 
This projects takes the photos in the subfolders of "dataset", and looks for the faces using the pretrained face detection model. It then computes a 128 dimensional embedding of the face using [openFace](http://cmusatyalab.github.io/openface/) 
and saves it to the embeddingss.pickle file. An SVM was then trained upon the embeddings to find a relationship between the embeddings and the face of a certain person, and that model is saved in recognizer.pickle. Realtime face-detection occurs
by detecting the face in the OpenCV frame using the face detection model, computing the embedding using openFace, then predicting whose face it is using the saved recognizer. 

<h1> Usage </h1> 
Add a new subfolder to the dataset with the name of the person to be recognized. Add as many images as possible into that subfolder (a minimum of 10 should be a good baseline to identify the person in all settings, for smaller amounts of images it can only identify the person in settings similar to the ones the photos were taken in). 
Then run extract_embeddings.py to save the embeddings of each face. Then run train_model.py to train the recognizer. Then run recognize_video.py which should (hopefully) provide real-time face detection. 

<h1> Todo: </h1>
 - TODO: Add TODO's