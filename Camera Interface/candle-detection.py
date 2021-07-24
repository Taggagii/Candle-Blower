import cv2

cap = cv2.VideoCapture('output.avi')

frame_width, frame_height = int(cap.get(3)), int(cap.get(4))

while cap.isOpened():
	ret, frame = cap.read()
	if not ret:
		break
	
	blur = cv2.GaussianBlur(frame, (9, 9), cv2.BORDER_DEFAULT)
	_, thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)
	dilated = cv2.dilate(thresh, None, iterations = 5)
	contours, heirs = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	if contours != []:
        for contour, hier in zip(contours, hiers[0]):
            (x, y, w, h) = cv2.boundingRect(contour)
            if cv2.rectangle(previous, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(previous, "Status: Candle", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255, 3))
            
	
	cv2.imshow("Camera thing", dilated)
	if cv2.waitKey(60) == ord("`"):
		break

cv2.destroyAllWindows()
