import cv2
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

# Load pre-trained object detection model
module_handle = "https://tfhub.dev/google/openimages_v4/ssd/mobilenet_v2/1"
detector = hub.load(module_handle).signatures['default']

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    
    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)
    
    # Convert frame to RGB (TensorFlow model expects RGB input)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Perform object detection
    converted_frame = tf.convert_to_tensor(rgb_frame)
    result = detector(converted_frame)
    
    # Draw bounding boxes around detected objects
    for i in range(len(result['detection_boxes'].numpy())):
        box = result['detection_boxes'].numpy()[i]
        class_id = int(result['detection_classes'].numpy()[i])
        confidence = result['detection_scores'].numpy()[i]
        
        # Filter out low confidence detections
        if confidence > 0.5:
            h, w, _ = frame.shape
            ymin, xmin, ymax, xmax = box
            startX, startY, endX, endY = int(xmin * w), int(ymin * h), int(xmax * w), int(ymax * h)
            
            # Draw bounding box
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
    
    # Display the output frame
    cv2.imshow('Object Detection', frame)
    
    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam
cap.release()
cv2.destroyAllWindows()
