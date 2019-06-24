# Crowd Flow Tracking


### by [Samarth Negi](https://n-s405.github.io) , [Rishabh Singh]() , [Rahul Rawat]()

_________




## Description 
Project done as the Major Project for College . Combines Image Processing and Machine Learning to create a data analytics tool for market analysis . 

__Crowd flow__ analysis is the process of analysing the movement of people in  a specific area.
This data can be extracted using the surveillance camera footage by the help of Digital image
processing and Machine learning. 
The data extracted can be used for two purposes i.e.
1. Study consumer behaviour  
2. Providing better security

Consumer Behaviour is one of the most important aspect in the industry of retail outlets and
shopping complexes. In the case of retail outlets, the flow of analysis of the targeted audience
is extremely important for the strategic placement of the outlets and the placement of
promotional banners. Whereas in the cases of shopping complexes, the knowledge of consumer
behaviour can be used for the purpose of better crowd management and more importantly, it
can be used for the strategic placement for the various outlets based on the demographic of the
crowd in various areas of the complex. This increases the productivity of every shop and the
thus increases the profits of the overall shopping complex as the more the sale is the higher
rates for the lease can be set.



## Idea Pane / Development To Do List 
- [x] __Implement Depth perception using a camera__ <br/> 
    - [Method 1](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_calib3d/py_depthmap/py_depthmap.html#py-depthmap)<br/> 
    - [Method 2](https://www.youtube.com/watch?v=KNft4RFsK28), the links for which can be found [here](http://visual.cs.ucl.ac.uk/pubs/monoDepth/) and [here](https://github.com/mrharicot/monodepth)<br/>
    - This [Blog](https://albertarmea.com/post/opencv-stereo-camera/)  presents a good example of depth from a stereo camera . <br/>
    - _Figure out if it can be somehow used in the final thing . Avoid ML in this stage_
- [ ] __Tagged Depth Perception__
    - See [this](https://www.pyimagesearch.com/2015/01/19/find-distance-camera-objectmarker-using-python-opencv/)
    - Nice discussion on stackexchange [here](https://photo.stackexchange.com/questions/12434/how-do-i-calculate-the-distance-of-an-object-in-a-photo)
- [x] __Vanilla People Tracking : Just track people in a frame__  -> USED MobileNet + SSD 
    - Use ML . Just find people in a frame 
        - [Haar Cascade Implementation](https://medium.com/@madhawavidanapathirana/https-medium-com-madhawavidanapathirana-real-time-human-detection-in-computer-vision-part-1-2acb851f4e55)
        - [HOG + Linear SVM Implementation](https://www.pyimagesearch.com/2015/11/09/pedestrian-detection-opencv/)
- [ ] __Age , Gender Detector__ 
    - Find things about people in frame . Kinda far fetched due to low accuracy 
    - [This](https://www.vocal.com/video/face-detection-using-viola-jones-algorithm/) explains Viola Jones , alternatively [this](https://www.youtube.com/watch?v=uEJ71VlUmMQ) video 
- [ ] __Gaze Detection__
    - [This](http://www.robots.ox.ac.uk/ActiveVision/Research/Projects/2009bbenfold_headpose/project.html#datasets) is a pretty good starting point to detect people's gaze based on their head position (oxford university) . _also includes the dataset_
- [ ] __A vv Good Implementation of People tracking__
    - [This](https://cvlab.epfl.ch/research/research-surv/research-body-surv-index-php/) uses multiple cameras and a better algorithm . 
    - Read up on how they incorporated DL in their CV pipeline . 
- [ ] __Make an interactive dashboard for the stuff__ 
    - Try something that runs offline like PyGame or PyPlot . 
- [ ] __Add correlation filters ([Kalman?](https://en.wikipedia.org/wiki/Kalman_filter)) to reduce re-entry errors__  
    - Purely to improve accuracy . Attempt in the end . 



## Progress
1. Depth Sensing is done -> using 2 different cameras (Kind of like portrait mode)
2. See flow tracking done here : ![flow tracking](https://github.com/n-s405/Crowd-Flow-Tracking/tree/master/data/flowmain.png) . Done using MobileNet and OpenCV state calculations . With a filter based on MOG image subtraction . 
3. See People Tracking here : ![flow tracking](https://github.com/n-s405/Crowd-Flow-Tracking/tree/master/data/track.png)
Done using CSRT filters 


## Documentation Headers 
- Introduction 
    - Image processing 
        - Python 
        - OpenCV 
        - [Pillow](https://pillow.readthedocs.io/en/stable/)
    - Machine Learning 
        - [TensorFlow](https://www.tensorflow.org/)
        - [Keras](https://keras.io/)
- Main Objective 
- Detecting Humans 
- Clasification of humans 
- Depth perception 


## Requirements 
    Python version number 
    Dependencies etc . 
    Upload an anaconda xml as well . In the data folder . 
