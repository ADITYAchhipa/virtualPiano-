import mediapipe as mp
import cv2
import time
import pygame


cap=cv2.VideoCapture(0)
pygame.mixer.init()
mphands=mp.solutions.hands

hands=mphands.Hands()

mpDraw=mp.solutions.drawing_utils
ctime =0
ptime=0

while True:
    success,img=cap.read()
    img=cv2.flip(img,1)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(img)
    img=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            arr = []
            for id,lm in enumerate(handLms.landmark):
            
              h,w,c=img.shape
              cx,cy=int(lm.x*w),int(lm.y*h)


              arr.append([cx,cy])
            #   cv2.circle(img,(cx,cy),5,(218,212,138),cv2.FILLED)
            if(id==4 or id==8 or id==12 or id==16 or id==20):
                    cv2.circle(img,(cx,cy),5,(218,212,138),cv2.FILLED)

            # for thumb
            if(arr[0][1]<=arr[4][1]):
                    cv2.circle(img,(arr[4][0],arr[4][1]),15,(218,212,138),cv2.FILLED)
                    sound = pygame.mixer.Sound("A.mp3")
                    sound.play()
                # print("done")
            else:
                cv2.circle(img,(arr[4][0],arr[4][1]),5,(218,212,138),cv2.FILLED)

            # for first finger
            if(arr[0][1]<=arr[8][1]):
                sound = pygame.mixer.Sound("B.mp3")
                sound.play()
                cv2.circle(img,(arr[8][0],arr[8][1]),15,(234,243,158),cv2.FILLED)
                print("done")
            else:
                cv2.circle(img,(arr[8][0],arr[8][1]),5,(218,212,138),cv2.FILLED)

            # for 2nd finger
            if(arr[0][1]<=arr[12][1]):
                cv2.circle(img,(arr[12][0],arr[12][1]),15,(255,255,255),cv2.FILLED)
                print("done")
                sound = pygame.mixer.Sound("C.mp3")
                sound.play()
            else:
                cv2.circle(img,(arr[12][0],arr[12][1]),5,(218,212,138),cv2.FILLED)

            #for 3rd finger

            if(arr[0][1]<=arr[16][1]):
                sound = pygame.mixer.Sound("E.mp3")
                sound.play()
                cv2.circle(img,(arr[16][0],arr[16][1]),15,(206,228,135),cv2.FILLED)
                print("done")
            else:
                cv2.circle(img,(arr[16][0],arr[16][1]),5,(218,212,138),cv2.FILLED)
            

            
            # for 4th finger
            if(arr[0][1]<=arr[20][1]):
                sound = pygame.mixer.Sound("G.mp3")
                sound.play()
                cv2.circle(img,(arr[20][0],arr[20][1]),15,(207, 236, 113),cv2.FILLED)
                print("done")
            else:
                cv2.circle(img,(arr[20][0],arr[20][1]),5,(218,212,138),cv2.FILLED)



                # sound = pygame.mixer.Sound("a1.wav")
                # sound.play()

                

              
              
            # mpDraw.draw_landmarks(img,handLms,mphands.HAND_CONNECTIONS)
          


    # calculating frames
    ctime=time.time()
    fps=1/(ctime-ptime)
    ptime=ctime

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)


    cv2.imshow("image",img)
    cv2.waitKey(1)

