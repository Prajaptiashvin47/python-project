import cv2
import face_recognition

# Load known face image
known_image = face_recognition.load_image_file("user.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

# Start camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    rgb_frame = frame[:, :, ::-1]  # Convert to RGB
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for encoding in face_encodings:
        match = face_recognition.compare_faces([known_encoding], encoding)
        if match[0]:
            print("Face Recognized! Access Granted.")
    
    cv2.imshow("Face Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()   