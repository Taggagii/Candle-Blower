import cv2

cap = cv2.VideoCapture('output.avi')

frame_width, frame_height = int(cap.get(3)), int(cap.get(4))

counter = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    blur = cv2.GaussianBlur(frame, (9, 9), cv2.BORDER_DEFAULT)
    _, thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations = 5)
    img = cv2.cvtColor(dilated, cv2.COLOR_BGR2GRAY)
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours != []:
        for contour, hier in zip(contours, hierarchy[0]):
            counter += 1
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(dilated, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
    STATUS = cv2.imwrite(str(counter) + ".png", dilated)
                    
                
    cv2.imshow("Camera thing", frame)
    if cv2.waitKey(60) == ord("`"):
        break
    
    

cv2.destroyAllWindows()
