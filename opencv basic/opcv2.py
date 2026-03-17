import cv2

imgpath=input("enter image path here: ")
image=cv2.imread(imgpath)
if image is not None:
    print("image found")
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    inputs=input("enter image is to be show or save : ").lower()
    if inputs=="show":
        cv2.imshow("image",gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif inputs=="save":
        savename=input("enter name to file savingin.jpg : ")
        cv2.imwrite(savename,gray)
        print(f"{savename} saved successfully")


