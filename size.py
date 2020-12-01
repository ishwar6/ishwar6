import cv2 as cv
img = cv.imread("media/1929.jpg")


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dim = (width, height)
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

# print(type(img))


#rescaled_image = rescaleFrame(img)
#cv.imshow("1929", rescaled_image)
# print(rescaled_image)
# cv.waitKey(0)


capture = cv.VideoCapture('/Users/ishwarjangid/Movies/a.mp4')
while True:
    isTrue, frame = capture.read()
    frame = rescaleFrame(frame)
    cv.imshow('video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
print(capture, frame)
capture.release()
cv.destroyAllWindows()
