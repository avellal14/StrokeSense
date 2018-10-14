import io
import os
import pickle

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score 
from sklearn.externals import joblib

import numpy as np

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=os.path.join('/home', 'adi', 'HackDuke', 'Droopy_Face_Detection', 'google_apps.json')

def detect_landmarks(path):
    """Detects landmarks in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
            content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    lips = [] 
    positions = np.zeros([5, 3])

    j = 0
    for face in faces:
            landmark_list = face.landmarks
            for landmark in landmark_list:
                    landmark_type = (str(landmark).split("\n")[0])
                    if 'LIP' in landmark_type or 'MOUTH' in landmark_type:
                                    lips.append(landmark_type.split(": ")[1])       
                                    count = 0

                                    for p_index, p in enumerate(str(landmark.position).split("\n")):
                                        if ":" in p:
                                          #  print("j: ", j, " p_index: ", p_index)
                                            positions[j][p_index] = (float(p.split(": ")[1]))

                                        else:
                                            p_index -= 1
                                    j += 1    
    #print(positions)        
    return positions

def create_healthy_landmarks(): 
    base_dir = os.path.join(os.path.dirname(__file__), 'Images/Healthy/')
    files = os.listdir(base_dir)

    healthy_landmarks = np.zeros([len(files), 5,3]) 
    y = np.zeros([len(files)])
 

    print("Enumerate files", enumerate(files))
    for i, file in enumerate(files):
            print("Loading new healthy coordinates!", i)
            healthy_landmarks[i, :, :] = detect_landmarks(os.path.join(base_dir, file))           

    return healthy_landmarks, y


def create_droopy_landmarks(): 
    base_dir = os.path.join(os.path.dirname(__file__), 'Images/Droopy/')
    files = os.listdir(base_dir)

    droopy_landmarks = np.zeros([len(files), 5,3]) 
    y = np.ones([len(files)]) 

    for i, file in enumerate(files):
            droopy_landmarks[i, :, :] = detect_landmarks(os.path.join(base_dir, file))
            print("Loading new droopy coordinates! ", i)


    return droopy_landmarks, y



def generate_train_data():

    all_healthy, y_healthy = create_healthy_landmarks()   #all healthy faces 
    all_droopy, y_droopy = create_droopy_landmarks() #droopy faces (n = 108)

    X = np.concatenate((all_healthy, all_droopy), axis=0)
    y = np.concatenate((y_healthy, y_droopy))

    nsamples, nx, ny = X.shape
    X = X.reshape((nsamples, nx*ny))

    np.savetxt('X.csv', X, delimiter=',')
    np.savetxt('y.csv', y, delimiter=',')




def train_and_evaluate_model():

    X = np.genfromtxt(os.path.join(os.path.dirname(__file__), 'X.csv'), delimiter=',')
    y = np.genfromtxt(os.path.join(os.path.dirname(__file__), 'y.csv'), delimiter=',')

    skf = StratifiedKFold(n_splits=3)
    rnd_forest_classifier = RandomForestClassifier(max_depth=2)


    total_accuracy = 0
    total_F1 = 0
    total_auc = 0

    max_auc = 0

    for train_index, test_index in skf.split(X, y):
	probs = rnd_forest_classifier.fit(X[train_index], y[train_index]).predict_proba(X[test_index])
        preds = np.argmax(probs, axis=1)

        y_test = y[test_index]

        total_accuracy += accuracy_score(y_test, preds)
        total_F1 += f1_score(y_test, preds)

        auc = roc_auc_score(y_test, probs[:,1])
        total_auc += auc

        if(auc > max_auc):
		max_auc = auc 	
		joblib.dump(rnd_forest_classifier, 'droopy_rf.sav')
                        
    print('Total Accuracy: ', total_accuracy/3.0)
    print('Total F1: ', total_F1/3.0)
    print('Total AUC: ', total_auc/3.0)


def test_model(img_file):
    	droopy_rf = joblib.load(os.path.join(os.path.dirname(__file__), 'droopy_rf.sav'))
 	feature_vec = detect_landmarks(img_file)
        
        nx, ny = feature_vec.shape
    	feature_vec = feature_vec.reshape((1, nx*ny))     
     
        return droopy_rf.predict_proba(feature_vec)
         	



#generate_train_data()
#train_and_evaluate_model()
#test_model()
