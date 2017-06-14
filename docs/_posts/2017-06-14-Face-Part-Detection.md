---
layout: post
title: Facial Parts Detection
---

# Face-Parts-Detection

## Overview

This framework will enable you to detect facial parts separately. facial parts including: eyes, eyebrows, nose, mouth and jawline.


## Dependencies

``` 
pip install imutils
pip istall -r requirements.txt

```

## Usage
```
python detect_face_parts.py --shape-predictor shape_predictor_68_face_landmarks.dat --image images/example_01.jpg 
```
## Results

![Alt](results/face_overlay.png)
![Alt](results/face5_nose.png)
![Alt](results/face0_mouth.png)
![Alt](results/face6_jaw.png)
![Alt](results/face1_right_eyebrow.png)
![Alt](results/face2_left_eyebrow.png)
![Alt](results/face3_right_eye.png)
![Alt](results/face4_left_eye.png)


#### Credits: My Guru- Adrian Rosebrock