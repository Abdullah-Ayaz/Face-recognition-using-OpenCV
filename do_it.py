import cv2
import numpy as np
import face_recognition

#Loading image from the directory and encoding it
img_ab = face_recognition.load_image_file('E:/NUST/FYP_MATERIAL/Face_Recognition/2.jpg')
img_ab = cv2.cvtColor(img_ab,cv2.COLOR_BGR2RGB)

img1_encoding = face_recognition.face_encodings(img_ab)[0]

img_ah = face_recognition.load_image_file("E:/NUST/FYP_MATERIAL/Face_Recognition/Ahmed.jpg")
img_ah = cv2.cvtColor(img_ah,cv2.COLOR_BGR2RGB)
img2_encoding = face_recognition.face_encodings(img_ah)[0]
avg_face_width = 14
focal_length = 600

#defining the distance method to measure distance from the object
def measure_face_distance(face_width_pixels):
    return (avg_face_width * focal_length) / face_width_pixels

#deifing the centroid method to find the center of the bounding box
def centroid(x,w,h,y):
    d1 = (x+w)/2
    d2 = (h+y)/2
    rect_center = (d1-5,d2-40)
    return rect_center

known_face = ["Abdullah","Ahmed"]
known_encodings = [img1_encoding,img2_encoding]
#initialising the camera 
Recording = cv2.VideoCapture(0)
while True:
    #Doing the face encoding of the faces in the video frame 
    ret,R_data = Recording.read()
    
    rgb_frame = cv2.cvtColor(R_data, cv2.COLOR_BGR2RGB)

    video_location = face_recognition.face_locations(rgb_frame)
    video_encoding = face_recognition.face_encodings(rgb_frame,video_location)
    #comparing the known face and the frame face's encodings and deducing the result
    for (h,w,y,x), face_encoding in zip(video_location,video_encoding):
        Face_match = face_recognition.compare_faces(known_encodings,face_encoding)
        name = "unknown"
        distance = measure_face_distance(y)
        centre  = centroid(x,w,h,y)
        print(centre)
        face_distances = face_recognition.face_distance(known_encodings, face_encoding)
        match_index = np.argmin(face_distances)
        if Face_match[match_index]:
            name = known_face[match_index]
    
        cv2.rectangle(R_data,(x,h),(w,y),(0,0,255),4)
        cv2.circle(R_data,(int(centre[0]),int(centre[1])),1,(0,0,255),2)
    
          
        cv2.rectangle(R_data, (x, y - 35), (w, y), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(R_data, name, (x + 6, y - 6), font, 1.0, (255, 255, 255), 1)
        cv2.putText(R_data, f"{distance:.2f} cm", (w, h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    #showing the real time video
    cv2.imshow('SAMPLE',R_data)
    #Terminating the program using the 'q' key on keyboard
    if cv2.waitKey(1) == ord('q'):
        break

Recording.release()
cv2.destroyAllWindows()