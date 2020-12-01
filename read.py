
import cv2 as cv
#img = cv.imread("media/1929.jpg")
# print(type(img))
#cv.imshow("1929", img)
capture = cv.VideoCapture('/Users/ishwarjangid/Movies/a.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
# cv.waitKey(0)
