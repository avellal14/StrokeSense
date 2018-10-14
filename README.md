# StrokeSense
StrokeSense is a Python-based iOS application for stroke detection.

## About
Although strokes are the 2nd most common cause of death around the world (10.8% of all deaths result from strokes), more than 73% of people do not know how to identify if someone is suffering from a stroke. StrokeSense takes a novel, machine learning based approach to determining whether someone is having a stroke by analyzing their speech patterns and facial appearance. It offers a cheap and efficient way for everyone from emergency professionals to concerned relatives to ensure that stroke patients can get the appropriate medical assistance.

StrokeSense uses two machine learning models: one to analyze their speech and another to analyze a person's face. Our system is inspired by the FAST methodology, and we look for two symptoms of patients experiencing a stroke. The first is known as dysarthria, which involves slurred speech. The second, known as palsy, is a condition in which loss of motor control on one side of the body causes facial paralysis and a droopy face.

Our audio analysis model predicts dysarthria with a predictive accuracy of 0.997, and our facial analysis model predicts whether someone is exhibiting palsy with a predictive accuracy of 0.940. (We use Area Under the ROC Curve, or AUC, to quantify our classifiers' discriminatory power. The AUC ranges from 0.5 to 1.0, where 0.5 corresponds to random prediction and 1.0 corresponds to perfect accuracy).

![alt text](https://github.com/vatsalag99/StrokeSense/blob/master/banner-fast.jpg)

## Implementation Details

For our machine learning model architecture, we combined two separate approaches for speech analysis and facial appearance. The speech samples were analyzed using a Radial Basis Function kernel Support Vector Machine (RBF SVM) and a Random Forest. RBF kernels allow us to map infinite dimension inputs to 2 dimensions enabling us to classify and visualize results in an effective and efficient manner. Furthermore, the Random Forest itself is a ensemble method which uses individual decision trees that evaluate different charactersitics of the audio file to determine whether it represents a healthy or stroke patient. Each of these algorithms outputs an individual probability of the patient having a stroke and being healthy, and these probabilities are then averaged to obtain an ensemble prediction of whether the patient is exhibiting dysarthria in their speech. 

Regarding our image analysis model, the program takes an input image of the patient's face and uses the Google AutoML API to determine the landmark features of their face (eyes, lips, nose, etc.). From this, a parser extracts the exact coordinates from each of five lip coordinates and creates a vector of 15 total coordinates. These feature vectors are extracted from both patients who exhibit palsy and those who do not, and we use them to train a Random Forest classifier which predicts whether a patient has palsy based on their lip coordinates.


## Training and Evaluation



![alt text](https://github.com/vatsalag99/StrokeSense/blob/master/ML_Diagram.png)

## Software
We use the following software frameworks in our application:
* Python (SciKit-Learn and NumPy)
* Google's AutoML Face Detection API
* Swift
* Google Firebase

## Usage
### Installation
`$ git clone https://github.com/vatsalag99/StrokeSense.git`
Please make sure you extract the file rfTemp.tar.bz2 and delete the compressed version of it in your local clone of the repository. 

### Setup
```python
import StrokeSense
```

## Future Plans and Scalabiliy
Within our 24 hour hack at HackDuke, we were able to get very impressive results on stroke detection through the FAST approach used by first responders. However, we believe that this architecture has the potential to expand across the broad field of emergency medicine.

The future of this platform is two-fold, the first being a further implementation of emergency response through the effective integration of Electronic Health Records (EHRs) with patients that are at severe risk for a given disease and the second, an alternative integration in third world countries.

We also forsee an integration of an online learning models by partnering with healthcare providers through recieving feedback on StrokeSense's performance (i.e. whether it diagnosed the patient correct or there was a false positive).
