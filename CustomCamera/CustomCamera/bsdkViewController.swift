//
//  bsdkViewController.swift
//  CustomCamera
//
//  Created by Aparimeya Taneja on 10/14/18.
//  Copyright © 2018 Zero2Launch. All rights reserved.
//

import UIKit
import AVFoundation
import FirebaseStorage
import FirebaseDatabase

class bsdkViewController: UIViewController, AVAudioRecorderDelegate {

    
    var recordingSession:AVAudioSession!
    var audioRecorder:AVAudioRecorder!
    var numberOfRecords = 0
    
     var ref: DatabaseReference!
    @IBOutlet weak var buttonLbel: UIButton!
    @IBAction func rek(_ sender: Any) {
        print(audioRecorder)
        if audioRecorder == nil
        {
            numberOfRecords+=1
            let filename = getDirectory().appendingPathComponent("\(numberOfRecords).m4a")
            
            let settings = [AVFormatIDKey: Int(kAudioFormatMPEG4AAC), AVSampleRateKey: 12000, AVNumberOfChannelsKey: 1, AVEncoderAudioQualityKey: AVAudioQuality.high.rawValue]
            
            do{
                audioRecorder = try AVAudioRecorder(url: filename, settings: settings)
                audioRecorder.delegate = self
                audioRecorder.record()
                
                
                
                buttonLbel.setTitle("Stop Recording", for: .normal)
            }
            catch{
                displayAlert(title: "Oops", message: "Failed")
            }
            
        }
        else
        {
            audioRecorder.stop()
            audioRecorder = nil
            UserDefaults.standard.set(numberOfRecords, forKey: "myNumber")
          
            ref = Database.database().reference()
            let storageRef = Storage.storage().reference()
            let localFile = getDirectory().appendingPathComponent("\(numberOfRecords).m4a")
            print(localFile)
            let fileName = storageRef.child("audio/a\(numberOfRecords).m4a")
           let a = "image/p\(numberOfRecords)"
            let b = fileName.fullPath
            
            let uplink = fileName.putFile(from: localFile)
            buttonLbel.setTitle("Start Recording", for: .normal)
            self.ref.child("n\(numberOfRecords)").setValue(["a": b, "p" : a , "f" : 0 ])
         let x =   Database.database().reference().child("stroke-sense").child("n\(numberOfRecords)")
            


            
            
            let alert = UIAlertController(title: "Computing", message: "", preferredStyle: .alert)
           
            DispatchQueue.main.asyncAfter(deadline: .now() + 3) { // change 2 to desired number of seconds
                
                self.present(alert1, animated: true)

                alert1.addAction(UIAlertAction(title: "Ok", style: .default, handler: {
                    action in
                    self.presentingViewController?.dismiss(animated: true, completion: nil)
                    
                }))
            }
            
            alert.addAction(UIAlertAction(title: "Ok", style: .default, handler: {
                action in
                

                
            }))
           
            
            self.present(alert, animated: true)
            
        }
        
    }
   
    override func viewDidLoad() {
        super.viewDidLoad()

        
        recordingSession = AVAudioSession.sharedInstance()
        
        if let number:Int = UserDefaults.standard.object(forKey: "myNumber") as? Int{
            numberOfRecords = number
        }
        
        AVAudioSession.sharedInstance().requestRecordPermission { (hasPermission) in
            if hasPermission
            {
                print("ACCEPTED")
            }
        }
        
    }
    
    func getDirectory() -> URL {
        let paths = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask)
        let documentDirectory = paths[0]
        return documentDirectory
    }
    
    func displayAlert(title:String, message:String)
    {
        let alert = UIAlertController(title: title, message: message, preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "dismiss", style: .default, handler: nil))
        present(alert,animated: true,completion: nil)
    }
    
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
