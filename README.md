# StrokeSense
StrokeSense is a Python-based iOS application for stroke detection.

## About
Although it is the 2nd most common cause of death around the world at 10.8% of all deaths resulting from strokes, more than 73% of people do not know how to identify if someone is suffering from a stroke. StrokeSense takes a novel, machine learning based approach on the dire need for effectively determining whether someone is having a stroke by analyzing speech and appearance.

![alt text](https://github.com/vatsalag99/StrokeSense/blob/master/Stroke_Detection/banner-fast.jpg)

## Software
We use the following software in our application:
* Python (SciKit-Learn and NumPy)
* Google's AutoML Face Detection API
* Swift
* Google Firebase

## Usage
### Installation
`$ git clone https://github.com/vatsalag99/StrokeSense.git`

### Setup
```python
import StrokeSense
```

## Future Plans and Scalabiliy
Within our 24 hour hack at HackDuke, we were able to get very impressive results on stroke detection through the FAST approach used by first responders. However, we believe that this architecture has the potential to expand across the broad field of emergency medicine.

The future of this platform is two-fold, the first being a further implementation of emergency response through the effective integration of Electronic Health Records (EHRs) with patients that are at severe risk for a given disease and the second, an alternative integration in third world countries.

We also forsee an integration of an online learning models by partnering with healthcare providers through recieving feedback on StrokeSense's performance (i.e. whether it diagnosed the patient correct or there was a false positive).
