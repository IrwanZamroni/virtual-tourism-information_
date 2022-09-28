import cv2
import csv
from cvzone.HandTrackingModule import HandDetector
import cvzone
import time


cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)
#success, img = cap.read()

class MCQ():
    def __init__(self, data):

        self.question = data[0]
        self.choice1 = data[1]
        self.choice2 = data[2]
        self.choice3 = data[3]
        self.choice4 = data[4]
        self.answer = int(data[5])

        self.userAns = None

    def update(self, cursor, bboxs):

        for x, bbox in enumerate(bboxs):
            x1, y1, x2, y2 = bbox
            if x1 < cursor[0] < x2 and y1 < cursor[1] < y2:
                self.userAns = x + 1
                print(self.userAns)
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), cv2.FILLED)

imgFront = cv2.imread("bali.png", cv2.IMREAD_UNCHANGED)
imgt = cv2.imread("cek.png", cv2.IMREAD_UNCHANGED)
imgt_1 = cv2.imread("mandal.png", cv2.IMREAD_UNCHANGED)
imgFr = cv2.imread("pantai bali.png", cv2.IMREAD_UNCHANGED)
imgF = cv2.imread("bali.png", cv2.IMREAD_UNCHANGED)
imgFront_1 = cv2.imread("pantai bali.png", cv2.IMREAD_UNCHANGED)
imgF_1 = cv2.imread("pantai bali.png", cv2.IMREAD_UNCHANGED)
imgFront_2 = cv2.imread("manda.png", cv2.IMREAD_UNCHANGED)
imgF_2 = cv2.imread("manda.png", cv2.IMREAD_UNCHANGED)
imgFront_ = cv2.imread("Lombok.png", cv2.IMREAD_UNCHANGED)
imgF_ = cv2.imread("Lombok.png", cv2.IMREAD_UNCHANGED)
imgFront = cv2.resize(imgFront, (80, 50), None, 0.3, 0.3)
imgF = cv2.resize(imgF, (80, 50), None, 0.3, 0.3)
        
imgFr = cv2.resize(imgt, (800, 400), None, 0.3, 0.3)
imgt_1 = cv2.resize(imgt_1, (800, 400), None, 0.3, 0.3)
imgFront_1 = cv2.resize(imgFront_1, (80, 50), None, 0.3, 0.3)
imgF_1 = cv2.resize(imgF_1, (150, 90), None, 0.3, 0.3)
imgFront_2 = cv2.resize(imgFront_2, (80, 50), None, 0.3, 0.3)
imgF_2 = cv2.resize(imgF_2, (150, 90), None, 0.3, 0.3)
imgFront_ = cv2.resize(imgFront_, (400, 400), None, 0.3,0.3)
imgF_ = cv2.resize(imgF_, (400, 400), None, 0.3,0.3)    

# Import csv file data
pathCSV = "Mcqs.csv"
with open(pathCSV, newline='\n') as f:
    reader = csv.reader(f)
    dataAll = list(reader)[1:]

# Create Object for each MCQ
mcqList = []
for q in dataAll:
    mcqList.append(MCQ(q))

print("Total MCQ Objects Created:", len(mcqList))

qNo = 0
qTotal = len(dataAll)

#hf, wf, cf = imgFront.shape
#hf_, wf_, cf_ = imgFront_.shape
#hb, wb, cb = img.shape
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)
    if qNo < qTotal:
        mcq = mcqList[qNo]
         
   
            

    if qNo == 0:
        img, bbox = cvzone.putTextRect(img, mcq.question, [100, 100], 2, 2, offset=50, border=5, colorR=(255, 255, 255),colorT=(0, 0, 0),colorB=(0,0,255))
        #img, bbox1 = cvzone.putTextRect(img, mcq.choice1, [100, 250], 2, 2, offset=50, border=5)
        #img, bbox2 = cvzone.putTextRect(img, mcq.choice2, [400, 250], 2, 2, offset=50, border=5)
       
            
        img, bbox2 = cvzone.putTextRect(img, mcq.choice2, [600, 500], 1, 1, offset=50, border=5,colorR=(255, 255, 255),colorT=(0, 0, 0),colorB=(0,0,255))   
        img, bbox3 = cvzone.putTextRect(img, mcq.choice3, [600, 270], 1, 1, offset=50, border=5,colorR=(255, 255, 255),colorT=(0, 0, 0),colorB=(0,0,255))
        img, bbox4 = cvzone.putTextRect(img, mcq.choice4, [1400, 1500], 1, 1, offset=50, border=5,colorR=(255, 255, 255),colorT=(0, 0, 0),colorB=(0,0,255))
       
        img = cvzone.overlayPNG(img,imgFront_, [50, 200,200])
        img = cvzone.overlayPNG(img, imgFront, [200, 300,300])
        img = cvzone.overlayPNG(img, imgFront_1, [100, 400,400])
        img = cvzone.overlayPNG(img, imgFront_2, [200, 500,400])
        img = cvzone.overlayPNG(img, imgF_1, [565, 220,220])
        img = cvzone.overlayPNG(img, imgF_2, [565, 450,450])

        if hands:
            lmList = hands[0]['lmList']
            cursor = lmList[8]
           
            length, info,img = detector.findDistance(lmList[8], lmList[12],img)
           
            if length < 60:
              
                mcq.update(cursor, [bbox3,bbox2, bbox4])
                  
                
                if mcq.userAns is not None:
                    time.sleep(0.1)
                    #qNo += 1
                    
    for mcq in mcqList:
        if mcq.userAns == 1 :
            b= "Kembali"
            #img, bbox = cvzone.putTextRect(img, d, [400, 400], 1, 1, offset=50, border=5, colorR=(0, 0, 255),colorT=(255, 255, 255),colorB=(255,255,0))
            #img, bbox = cvzone.putTextRect(img, c, [500, 500], 1, 1, offset=50, border=5, colorR=(0, 0, 255),colorT=(255, 255, 255),colorB=(255,255,0))
            img, bbox2 = cvzone.putTextRect(img, mcq.choice2, [1600, 1600], 1, 1, offset=50, border=5)   
            img, bbox3 = cvzone.putTextRect(img, mcq.choice3, [1600, 1400], 1, 1, offset=50, border=5)
            img, bbox4 = cvzone.putTextRect(img, b, [100, 100], 2, 2, offset=50, border=5,colorR=(255, 255, 255),colorT=(0, 0, 0),colorB=(0,0,255))
            #img = cvzone.overlayPNG(img, mcq.imgFront_, [50, 200,200])
            img = cvzone.overlayPNG(img, imgFr, [100, 190,100])
        
            if hands:
                lmList = hands[0]['lmList']
                cursor = lmList[8]
                length, info,img = detector.findDistance(lmList[8], lmList[12],img)
           
                if length < 60:
              
                    mcq.update(cursor, [bbox3,bbox2, bbox4])
                  
                
                    if mcq.userAns is not None:
                        time.sleep(0.1)
                        qNo += 1
            
        if mcq.userAns == 2 :
            b= "Kembali"
            #img, bbox = cvzone.putTextRect(img, d, [400, 400], 1, 1, offset=50, border=5, colorR=(0, 0, 255),colorT=(255, 255, 255),colorB=(255,255,0))
            #img, bbox = cvzone.putTextRect(img, c, [500, 500], 1, 1, offset=50, border=5, colorR=(0, 0, 255),colorT=(255, 255, 255),colorB=(255,255,0))
            img, bbox2 = cvzone.putTextRect(img, mcq.choice2, [1600, 1600], 1, 1, offset=50, border=5)   
            img, bbox3 = cvzone.putTextRect(img, mcq.choice3, [1600, 1400], 1, 1, offset=50, border=5)
            img, bbox4 = cvzone.putTextRect(img, b, [100, 100], 2, 2, offset=50, border=5,colorR=(255, 255, 255),colorT=(0, 0, 0),colorB=(0,0,255))
            #img = cvzone.overlayPNG(img, mcq.imgFront_, [50, 200,200])
            img = cvzone.overlayPNG(img, imgt_1, [100, 190,100])
        
            if hands:
                lmList = hands[0]['lmList']
                cursor = lmList[8]
                length, info,img = detector.findDistance(lmList[8], lmList[12],img)
           
                if length < 60:
              
                    mcq.update(cursor, [bbox3,bbox2, bbox4])
                  
                
                    if mcq.userAns is not None:
                        time.sleep(0.1)
                        qNo += 1

        if mcq.userAns ==3:
            img, bbox = cvzone.putTextRect(img, mcq.question, [100, 100], 2, 2, offset=50, border=5, colorR=(255, 255, 255),colorT=(0, 0, 0),colorB=(0,0,255))
        #img, bbox1 = cvzone.putTextRect(img, mcq.choice1, [100, 250], 2, 2, offset=50, border=5)
        #img, bbox2 = cvzone.putTextRect(img, mcq.choice2, [400, 250], 2, 2, offset=50, border=5)
       
            
            img, bbox2 = cvzone.putTextRect(img, mcq.choice2, [600, 500], 1, 1, offset=50, border=5,colorR=(255, 255, 255),colorT=(0, 0, 0),colorB=(0,0,255))   
            img, bbox3 = cvzone.putTextRect(img, mcq.choice3, [600, 270], 1, 1, offset=50, border=5,colorR=(255, 255, 255),colorT=(0, 0, 0),colorB=(0,0,255))
            img, bbox4 = cvzone.putTextRect(img, mcq.choice4, [1400, 1500], 1, 1, offset=50, border=5,colorR=(255, 255, 255),colorT=(0, 0, 0),colorB=(0,0,255))
       
            img = cvzone.overlayPNG(img, imgFront_, [50, 200,200])
            img = cvzone.overlayPNG(img, imgFront, [200, 300,300])
            img = cvzone.overlayPNG(img, imgFront_1, [100, 400,400])
            img = cvzone.overlayPNG(img, imgFront_2, [200, 500,400])
            img = cvzone.overlayPNG(img, imgF_1, [565, 220,220])
            img = cvzone.overlayPNG(img, imgF_2, [565, 450,450])

            if hands:
                lmList = hands[0]['lmList']
                cursor = lmList[8]
                length, info,img = detector.findDistance(lmList[8], lmList[12],img)
           
                if length < 60:
              
                    mcq.update(cursor, [bbox3,bbox2, bbox4])
                  
                
                    if mcq.userAns is not None:
                        time.sleep(0.1)
                        qNo += 1
           
    cv2.imshow("Img", img)
    cv2.waitKey(1)



    