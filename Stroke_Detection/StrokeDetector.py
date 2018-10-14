from SlurDetector import test_slur_detector
from DroopyDetector import test_droopy_detector



def having_stroke(audio_file, img_file):
 
	slur_preds = test_slur_detector(audio_file) #[p(no dysarthia), p(dysarthia)]
        img_preds = test_droopy_detector(img_file)  #[p(no droopy face), p(droopy face)]

         
        stroke_preds = 0.33 * slur_preds + 0.66 * img_preds #[p(no stroke), p(stroke)]
        return stroke_preds[1] #return probability that person is experiencing stroke
                  
