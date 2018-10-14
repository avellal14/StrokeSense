//
//  PreviewViewController.swift
//  CustomCamera
//
//  Created by DUYET on 6/8/17.
//  Copyright © 2017 Zero2Launch. All rights reserved.
//

import UIKit
import FirebaseStorage

class PreviewViewController: UIViewController {
    
 
    var numberOfPhotos = 0
   
    @IBOutlet weak var photo: UIImageView!
    var image:UIImage?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        photo.image = image
        
        if let number:Int = UserDefaults.standard.object(forKey: "myNumber2") as? Int{
            numberOfPhotos = number
        }
      
        
        
        // Do any additional setup after loading the view.
    }

    @IBAction func saveBtn_TouchUpInside(_ sender: Any) {
        guard let imageToSave = image else {
            return
        }
        
        UIImageWriteToSavedPhotosAlbum(imageToSave, nil, nil, nil)
        let storageRef = Storage.storage().reference()
      
        
        if let pic = UIImageJPEGRepresentation(imageToSave, 0.6){
         numberOfPhotos += 1
             UserDefaults.standard.set(numberOfPhotos, forKey: "myNumber2")
          
          let uplink = storageRef.child("image/p\(numberOfPhotos).jpg").putData(pic)
           
        }
        print(imageToSave.size)
       
        let vc = self.storyboard?.instantiateViewController(withIdentifier: "recaud") as! bsdkViewController
        self.present(vc, animated: true, completion: nil)
    }
    @IBAction func closeBtn_TouchUpInside(_ sender: Any) {
        dismiss(animated: true, completion: nil)
    }
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */
   
}
