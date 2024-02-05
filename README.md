# **Wav2Lip**: *Accurately Lip-syncing Videos In The Wild*


Prerequisites
-------------
- `Python 3.6` 
- ffmpeg: `sudo apt-get install ffmpeg`
- Install necessary packages using `pip install -r requirements.txt`.
- Face detection [pre-trained model](https://www.adrianbulat.com/downloads/python-fan/s3fd-619a316812.pth) should be downloaded to `face_detection/detection/sfd/s3fd.pth`. Alternative [link](https://iiitaphyd-my.sharepoint.com/:u:/g/personal/prajwal_k_research_iiit_ac_in/EZsy6qWuivtDnANIG73iHjIBjMSoojcIV0NULXV-yiuiIg?e=qTasa8) if the above does not work.
https://drive.google.com/file/d/16Lzo9f9TE8Yh7toIlFMcXmlNFQIC7maj/view?usp=drive_link wav2lip_gan.pth file for Getting the weights



Lip-syncing videos using the pre-trained models (Inference)
-------
You can lip-sync any video to any audio:

python inference.py --checkpoint_path <ckpt> --face <video.mp4> --audio <an-audio-source> 


##### Tips for better results:
- Experiment with the `--pads` argument to adjust the detected face bounding box. Often leads to improved results. You might need to increase the bottom padding to include the chin region. E.g. `--pads 0 20 0 0`.
- If you see the mouth position dislocated or some weird artifacts such as two mouths, then it can be because of over-smoothing the face detections. Use the `--nosmooth` argument and give it another try. 
- Experiment with the `--resize_factor` argument, to get a lower-resolution video. Why? The models are trained on faces that were at a lower resolution. You might get better, visually pleasing results for 720p videos than for 1080p videos (in many cases, the latter works well too). 
- The Wav2Lip model without GAN usually needs more experimenting with the above two to get the most ideal results, and sometimes, can give you a better result as well.

####Architecture : Original
