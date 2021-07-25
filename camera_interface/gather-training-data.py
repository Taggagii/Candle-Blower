import cv2, os

cap = cv2.VideoCapture(0)

frame_width, frame_height = int(cap.get(3)), int(cap.get(4))

OUTPUT_FOLDER = "1"

try:
    counter = max([int(i.replace(".png", "")) for i in os.listdir(OUTPUT_FOLDER)]) + 1
except:
    counter = 0



while cap.isOpened():
    counter += 1
    print(counter)
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
            
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(dilated, (x, y), (x + w, y + h), (0, 255, 0), 2)
    dilated = cv2.resize(dilated, (180, 180))
    STATUS = cv2.imwrite(f"{OUTPUT_FOLDER}/{str(counter)}.png", dilated)
                    
                
    cv2.imshow("Camera thing", dilated)
    if cv2.waitKey(60) == ord("`"):
        break
    
    

cv2.destroyAllWindows()
