import numpy as np
import random
import os, shutil

from pyAudioAnalysis import audioTrainTest as aT
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score




def train_data_generator():
    test_dir = os.path.join('/home', 'adi', 'HackDuke', 'Audio_Data_Final')
    
    normal_files = os.listdir(os.path.join(test_dir, 'Normal'))
    slurred_files = os.listdir(os.path.join(test_dir, 'Slurred'))

    normal_train_size = 0.75 * len(normal_files)
    slurred_train_size = 0.75 * len(slurred_files)

    

    normal_patients = list()

    for normal_file in normal_files:
	if normal_file[:normal_file.index('_')] not in normal_patients: 
		normal_patients.append(normal_file[:normal_file.index('_')])
       
    for slurred_file in slurred_files:
	if slurred_file[:slurred_file.index('_')] not in slurred_patients:
		slurred_patients.append(slurred_file[:slurred_file.index('_')])



    normal_train_strata_size = int(normal_train_size / (len(normal_patients) + len(slurred_patients)))
    slurred_train_strata_size = int(slurred_train_size  / (len(normal_patients) + len(slurred_patients)))

    random.shuffle(normal_files)
    normal_train_files = list()
  
 
    
    for patient in normal_patients:
       normies = [p for p in normal_files if patient in p]	
       normal_train_files.extend(normies[:normal_train_strata_size])


    random.shuffle(slurred_files)
    slurred_train_files = list()
  
     
    for patient in slurred_patients:
       slurries = [p for p in slurred_files if patient in p]
       slurred_train_files.extend(slurries[:slurred_train_strata_size])


    all_files = list()
    all_files.extend(normal_files)
    all_files.extend(slurred_files)
    
    for f in all_files:
          if f in normal_train_files:
	      	 shutil.copyfile(os.path.join('/home', 'adi', 'HackDuke', 'Audio_Data_Final','Normal',  f), os.path.join('/home', 'adi', 'HackDuke', 'Audio_Train', 'Normal',  f))
          elif f in slurred_train_files:
	         shutil.copyfile(os.path.join('/home', 'adi', 'HackDuke', 'Audio_Data_Final','Slurred',  f), os.path.join('/home', 'adi', 'HackDuke', 'Audio_Train','Slurred',  f))


   

def create_test_dir():
    all_dir = os.path.join('/home', 'adi', 'HackDuke', 'Audio_Data_Final')
    
    train_dir_normal = os.path.join('/home', 'adi', 'HackDuke', 'Audio_Train', 'Normal')
    train_dir_slurred = os.path.join('/home', 'adi', 'HackDuke', 'Audio_Train', 'Slurred')
    
    all_files = os.listdir(os.path.join(all_dir, 'Normal'))
    all_files.extend(os.listdir(os.path.join(all_dir, 'Slurred')))
    all_train_normal = os.listdir(train_dir_normal)
    all_train_slurred = os.listdir(train_dir_slurred)    

    all_files.sort()
    all_train_normal.sort()
    all_train_slurred.sort()
    

    test_files = list()
   
    for f in all_files:
	if f not in all_train_normal and f not in all_train_slurred:
		test_files.append(f)

    
    for test_f in test_files:
	  if 'C' in test_f:
                shutil.copyfile(os.path.join('/home', 'adi', 'HackDuke', 'Audio_Data_Final','Normal',  yeet), os.path.join('/home', 'adi', 'HackDuke', 'Audio_Test', yeet))

          else:
                shutil.copyfile(os.path.join('/home', 'adi', 'HackDuke', 'Audio_Data_Final', 'Slurred', yeet), os.path.join('/home', 'adi', 'HackDuke', 'Audio_Test', yeet))




def train_slur_detector():
	aT.featureAndTrain([os.path.join('/home', 'adi', 'HackDuke', 'Audio_Train','Normal'), os.path.join('/home', 'adi', 'HackDuke', 'Audio_Train','Slurred')], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, 'randomforest', 'rfTemp', False)   
     
	aT.featureAndTrain([os.path.join('/home', 'adi', 'HackDuke', 'Audio_Train','Normal'), os.path.join('/home', 'adi', 'HackDuke', 'Audio_Train','Slurred')], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, 'svm_rbf', 'svmRbfTemp', False)




def test_and_evaluate_slur_detector(test_dir):
        test_files = os.listdir(test_dir)
        final_preds = np.zeros([len(test_files), 2])
        class_preds = np.zeros([len(test_files)])
        labels = np.zeros([len(test_files)])

        correct = 0.0

        for i, test_ex in enumerate(test_files):
                  x_rf, preds_rf, y_rf =  aT.fileClassification(os.path.join(test_dir, test_ex), "rfTemp", "randomforest")         
                  final_preds[i,:] += preds_rf
                  
                  x_svm, preds_svm, y_svm =  aT.fileClassification(os.path.join(test_dir, test_ex), "svmRbfTemp", "svm_rbf")
                  final_preds[i,:] += preds_svm
                       
                  final_preds[i,:] /= 2

                  slurred = 'C' not in test_ex               
                
                  if(slurred):
			labels[i] = 1
                      
           	  class_preds[i] = final_preds[i,1]



        class_preds.astype(np.uint8)
        
        print("labels: ", labels)
        print("preds: ", class_preds)

        print("% Accuracy: ", accuracy_score(labels, np.argmax(final_preds, axis=1)))
        print("F1 score: ", f1_score(labels, np.argmax(final_preds, axis=1)))
        print("AUC score: ", roc_auc_score(labels, class_preds))

                

def test_slur_detector(audio_file):
                  pred = np.array([0.0,0.0])

		  x_rf, preds_rf, y_rf =  aT.fileClassification(audio_file, "rfTemp", "randomforest")         
                  pred += preds_rf
                  
                  x_svm, preds_svm, y_svm =  aT.fileClassification(audio_file, "svmRbfTemp", "svm_rbf")
                  pred += preds_svm
                       
                  return pred/2


#train_data_generator()
#create_test_dir()
#train_slur_detector()
#test_and_evaluate_slur_detector()
print(test_slur_detector(os.path.join( '/home', 'adi', 'HackDuke', 'Audio_Test', 'MC01_Session2_0098.wav')))
