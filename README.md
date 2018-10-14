# StrokeSense
StrokeSense is a Python-based iOS application for stroke detection.

## About
Although strokes are the 2nd most common cause of death around the world (10.8% of all deaths result from strokes), more than 73% of people do not know how to identify if someone is suffering from a stroke. StrokeSense takes a novel, machine learning based approach to determining whether someone is having a stroke by analyzing their speech patterns and facial appearance. It offers a cheap and efficient way for everyone from emergency professionals to concerned relatives to ensure that stroke patients can get the appropriate medical health.

Our audio and face segmentation models have predictive accuracies (Areas Under the ROC Curve) of .997 and .940 respectively.

(Area Under the ROC Curve, or AUC, is a metric used to quantify a classifier's discriminatory power. The AUC ranges from 0.5 to 1.0, where 0.5 corresponds to random prediction and 1.0 corresponds to perfect accuracy).

![alt text](https://github.com/vatsalag99/StrokeSense/blob/master/banner-fast.jpg)

## Software
We use the following software in our application:
* Python (SciKit-Learn and NumPy)
* Google's AutoML Face Detection API
* Swift
* Google Firebase

## Usage
### Installation
`$ git clone https://github.com/vatsalag99/StrokeSense.git`
Make sure you untar the rfTemp.tar.bz2 and delete the compressed version of the file. 

### Setup
```python
import StrokeSense
```

## Future Plans and Scalabiliy
Within our 24 hour hack at HackDuke, we were able to get very impressive results on stroke detection through the FAST approach used by first responders. However, we believe that this architecture has the potential to expand across the broad field of emergency medicine.

The future of this platform is two-fold, the first being a further implementation of emergency response through the effective integration of Electronic Health Records (EHRs) with patients that are at severe risk for a given disease and the second, an alternative integration in third world countries.

We also forsee an integration of an online learning models by partnering with healthcare providers through recieving feedback on StrokeSense's performance (i.e. whether it diagnosed the patient correct or there was a false positive).
