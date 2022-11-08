


from logging import root
from pydoc import text
from re import A
from struct import pack
import tkinter as tk
from tkinter import * 
from PIL import ImageTk,Image,ImageDraw,ImageFont
import PIL
import time
import serial
import os
import PIL.Image
import PIL.ImageTk
import glob
import import_ipynb
#import real_time_od
import real_time_od
main_counter = 0

form= tk.Tk()
form.title('Serpent Control Tool v01')
form.geometry('640x480')
form.resizable(False, False)
bg = ImageTk.PhotoImage(file='GUI\Others\dbg.png')
lbl=Label(form,image=bg)
lbl.place(x=0,y=0)
XCoordinatesSendedFlag = 0
YCoordinatesSendedFlag = 0
#ser = serial.Serial('COM7', 9600, timeout = 1)


def object_detection_loop():
    with open("coordinates_x.txt", "r") as t:
        
        coordinates_x = t.read()
        if float(coordinates_x) < 240: ## BURAYA DİĞER KISTASLAR GELECEK
            time.sleep(0.8)
            ser.write(coordinates_x.encode('ascii'))
            ser.flush()
            XCoordinatesSendedFlag = 1 
            print(coordinates_x)
            time.sleep(0.8)
        
    with open("coordinates_y.txt", "r") as s:
        coordinates_y = s.read()
        if int(coordinates_y) < 240: ## BURAYA DİĞER KISTASLAR GELECEK
            time.sleep(0.8)
            ser.write(coordinates_y.encode('ascii'))
            ser.flush()
            print(coordinates_y)
            YCoordinatesSendedFlag = 1 
            time.sleep(0.8)
    if YCoordinatesSendedFlag == 0 and XCoordinatesSendedFlag == 0:
        form.after(2000, object_detection_loop) # run every2000 milliseconds
    




def reset_flags():
    text_file = open("coordinates_x.txt", "a")
    text_file.truncate(0)
    text_file.close()
    text_file = open("coordinates_y.txt", "a")
    text_file.truncate(0)
    text_file.close()
    
    
def start_robot():
    time.sleep(1)
    start_robot_flag=901
    ser.write(str(start_robot_flag).encode('ascii'))
    ser.flush()
    time.sleep(0.5)
    STATUS_ROBOT = tk.Label(form,text='  Working.....',font='Helvetica 11 bold',fg='green')
    STATUS_ROBOT.place(x=195, y=92)
    object_detection_loop()

    
    
    
def stop_robot():
    stop_robot_flag=902
    ser.write(str(stop_robot_flag).encode('ascii'))
    ser.flush()
    time.sleep(1)
    STATUS_ROBOT = tk.Label(form,text='Not Working',font='Helvetica 11 bold',fg='red')
    STATUS_ROBOT.place(x=195, y=92)
    
def start_cv1():
    start_cv1_flag=903
    ser.write(str(start_cv1_flag).encode('ascii'))
    ser.flush()
    time.sleep(1)
    STATUS_CV1 = tk.Label(form,text='  Working.....',font='Helvetica 11 bold',fg='green')
    STATUS_CV1.place(x=195, y=212)
def stop_cv1():
    stop_cv1_flag=904
    ser.write(str(stop_cv1_flag).encode('ascii'))
    ser.flush()
    time.sleep(1)
    STATUS_CV1 = tk.Label(form,text='Not Working',font='Helvetica 11 bold',fg='red')
    STATUS_CV1.place(x=195, y=212)
def start_cv2():
    start_cv2_flag=905
    ser.write(str(start_cv2_flag).encode('ascii'))
    ser.flush()
    time.sleep(1)
    STATUS_CV2 = tk.Label(form,text='  Working.....',font='Helvetica 11 bold',fg='green')
    STATUS_CV2.place(x=195, y=284)
def stop_cv2():
    stop_cv2_flag=906
    ser.write(str(stop_cv2_flag).encode('ascii'))
    ser.flush()
    time.sleep(1)
    STATUS_CV2 = tk.Label(form,text='Not Working',font='Helvetica 11 bold',fg='red')
    STATUS_CV2.place(x=195, y=312)
    
def open_camera():
    #os.system('python real_time_od.ipynb')
    time.sleep(1)
def motor_a_l():
    motor_a_l_flag=911
    ser.write(str(motor_a_l_flag).encode('ascii'))
    ser.flush()

    time.sleep(1)
    
def motor_a_r():
    motor_a_r_flag=912
    ser.write(str(motor_a_r_flag).encode('ascii'))
    ser.flush()
    time.sleep(1)
    
def motor_b_r():
    motor_b_r_flag=913
    ser.write(str(motor_b_r_flag).encode('ascii'))
    ser.flush()
    time.sleep(1)
    
def motor_b_l():
    time.sleep(1)
    motor_b_l_flag=914
    ser.write(str(motor_b_l_flag).encode('ascii'))
    ser.flush()
    
def motor_c_r():
    time.sleep(1)
    motor_c_r_flag=915
    ser.write(str(motor_c_r_flag).encode('ascii'))
    ser.flush()
    time.sleep(1)
    
def motor_c_l():
    
    motor_c_l_flag=916
    ser.write(str(motor_c_l_flag).encode('ascii'))
    ser.flush()
    time.sleep(1)
    
def gripper_l():
    
    gripper_l_flag=917
    ser.write(str(gripper_l_flag).encode('ascii'))
    ser.flush()
    time.sleep(1)

def gripper_r():
    gripper_r_flag=918
    ser.write(str(gripper_r_flag).encode('ascii'))
    ser.flush()
    time.sleep(1)
    
def conveyor_1_r():
    start_cv1_flag=903
    ser.write(str(start_cv1_flag).encode('ascii'))
    ser.flush()
    time.sleep(1)
    
def conveyor_1_l():
    conveyor_1_l_flag=920
    ser.write(str(conveyor_1_l_flag).encode('ascii'))
    ser.flush()
    time.sleep(1)
    
def conveyor_2_r():
    conveyor_2_r_flag=921
    ser.write(str(conveyor_2_r_flag).encode('ascii'))
    ser.flush()
    time.sleep(1)
    
def conveyor_2_l():
    start_cv2_flag=905
    ser.write(str(start_cv2_flag).encode('ascii'))
    ser.flush()
    time.sleep(1)
    pass
def pneumatic_r():
    pneumatic_r_flag=923
    ser.write(str(pneumatic_r_flag).encode('ascii'))
    ser.flush()
    time.sleep(1)
    
def pneumatic_l():
    pneumatic_l_flag=924
    ser.write(str(pneumatic_l_flag).encode('ascii'))
    ser.flush()
    time.sleep(1)
    
def stop_motor():
    stop_motor_flag=923
    ser.write(str(stop_motor_flag).encode('ascii'))
    ser.flush()

    time.sleep(1)


   # Call the infinite_loop() again after 1 sec win.after(1000, infinite_loop)

def run_all():
    conveyor_1_l_flag=920
    ser.write(str(start_cv1_flag).encode('ascii'))
    ser.flush()
    time.sleep(1)
    

def auto_mode():
    auto_mode= Toplevel()
    auto_mode.title("Manual Control Mode")
    auto_mode.resizable(False, False)
    # sets the geometry of toplevel
    L=Label(auto_mode,
          text ="AUTONOMOUS MODE",font='Helvetica 15 bold').pack()
    auto_mode.geometry("340x210")
    START= tk.Button(auto_mode,text='RUN SYSTEM',font='Helvetica 18 bold',fg='green',bg='yellow',width=16,height=3,command=run_all)
    START.place(x=45, y=60)

########################## MANUAL MODE SCRIPTING STARTS ###########3
def manual_mode():
     
    # Toplevel object which will
    # be treated as a new window
    manualMode= Toplevel()

    # sets the title of the
    # Toplevel widget
    manualMode.title("Manual Control Mode")
    manualMode.resizable(False, False)
    # sets the geometry of toplevel
    manualMode.geometry("640x480")
    
    
    # A Label widget to show in toplevel
    L=Label(manualMode,
          text ="MANUAL CONTROL MODE",font='Helvetica 18 bold').pack()
    ############# LEFT ####################33
    MOTOR_A = tk.Label(manualMode,text='MOTOR A',font='Helvetica 14 bold')
    MOTOR_A.place(x=35, y=175)

    MOTOR_A_LEFT = tk.Button(manualMode,text='<',font='Helvetica 18 bold',fg='green',bg='white',width=3,height=1,command=motor_a_l)
    MOTOR_A_LEFT.place(x=145, y=160)
    
    MOTOR_A_RIGHT = tk.Button(manualMode,text='>',font='Helvetica 18 bold',fg='green',bg='white',width=3,height=1,command=motor_a_r)
    MOTOR_A_RIGHT.place(x=205, y=160)
    
    STOP1 = tk.Button(manualMode,text='Stop Move',font='Helvetica 18 bold',fg='red',bg='yellow',width=15,height=1,command=stop_motor)
    STOP1.place(x=315, y=395)

    MOTOR_B = tk.Label(manualMode,text='MOTOR B',font='Helvetica 14 bold')
    MOTOR_B.place(x=35, y=255)

    MOTOR_B_LEFT = tk.Button(manualMode,text='<',font='Helvetica 18 bold',fg='green',bg='white',width=3,height=1,command=motor_b_l)
    MOTOR_B_LEFT.place(x=145, y=240)
    
    MOTOR_B_RIGHT = tk.Button(manualMode,text='>',font='Helvetica 18 bold',fg='green',bg='white',width=3,height=1,command=motor_b_r)
    MOTOR_B_RIGHT.place(x=205, y=240)
    
    MOTOR_C = tk.Label(manualMode,text='MOTOR C',font='Helvetica 14 bold')
    MOTOR_C.place(x=35, y=335)

    MOTOR_C_LEFT = tk.Button(manualMode,text='<',font='Helvetica 18 bold',fg='green',bg='white',width=3,height=1,command=motor_c_l)
    MOTOR_C_LEFT.place(x=145, y=320)
    
    MOTOR_C_RIGHT = tk.Button(manualMode,text='>',font='Helvetica 18 bold',fg='green',bg='white',width=3,height=1,command=motor_c_r)
    MOTOR_C_RIGHT.place(x=205, y=320)
    
    GRIPPER = tk.Label(manualMode,text='GRIPPER',font='Helvetica 14 bold')
    GRIPPER.place(x=35, y=415)

    GRIPPER_LEFT = tk.Button(manualMode,text='<',font='Helvetica 18 bold',fg='green',bg='white',width=3,height=1,command=gripper_l)
    GRIPPER_LEFT.place(x=145, y=400)
    
    GRIPPER_RIGHT = tk.Button(manualMode,text='>',font='Helvetica 18 bold',fg='green',bg='white',width=3,height=1,command=gripper_r)
    GRIPPER_RIGHT.place(x=205, y=400)
    ########################## RIGHT ######################3
    
    PNEUMATIC = tk.Label(manualMode,text='PNEUMATIC',font='Helvetica 14 bold')
    PNEUMATIC.place(x=315, y=175)

    PNEUMATIC_LEFT = tk.Button(manualMode,text='<',font='Helvetica 18 bold',fg='green',bg='white',width=3,height=1,command=pneumatic_l)
    PNEUMATIC_LEFT.place(x=455, y=160)
    
    PNEUMATIC_RIGHT = tk.Button(manualMode,text='>',font='Helvetica 18 bold',fg='green',bg='white',width=3,height=1,command=pneumatic_r)
    PNEUMATIC_RIGHT.place(x=515, y=160)

    MM_CONVEYOR_1 = tk.Label(manualMode,text='CONVEYOR 1',font='Helvetica 14 bold')
    MM_CONVEYOR_1.place(x=315, y=255)

    MM_CONVEYOR_1_LEFT = tk.Button(manualMode,text='<',font='Helvetica 18 bold',fg='green',bg='white',width=3,height=1,command=conveyor_1_l)
    MM_CONVEYOR_1_LEFT.place(x=455, y=240)
    
    MM_CONVEYOR_1_RIGHT = tk.Button(manualMode,text='>',font='Helvetica 18 bold',fg='green',bg='white',width=3,height=1,command=conveyor_1_r)
    MM_CONVEYOR_1_RIGHT.place(x=515, y=240)
    
    MM_CONVEYOR_2 = tk.Label(manualMode,text='CONVEYOR 2',font='Helvetica 14 bold')
    MM_CONVEYOR_2.place(x=315, y=335)
    MM_CONVEYOR_2_LEFT = tk.Button(manualMode,text='<',font='Helvetica 18 bold',fg='green',bg='white',width=3,height=1,command=conveyor_2_l)
    MM_CONVEYOR_2_LEFT.place(x=455, y=320)
    
    MM_CONVEYOR_2_RIGHT = tk.Button(manualMode,text='>',font='Helvetica 18 bold',fg='green',bg='white',width=3,height=1,command=conveyor_2_r)
    MM_CONVEYOR_2_RIGHT.place(x=515, y=320) 



    

########################## MANUAL MODE SCRIPTING STARTS ###########3











op_num = 1
ST_OBJECT_DETECTED_1 = 'Successful'
ST_OBJECT_DETECTED_2 = '--'
ST_OBJECT_GRIPPED_1 = 'Successful'
ST_OBJECT_GRIPPED_2 = '--'
ST_OBJECT_DROPPED_1 = 'Successful'
ST_OBJECT_DROPPED_2 = '--'
ST_READY_1 = 'Yes'
ST_READY_2 = 'No'
    




canvas = Canvas(form, width=800, height=600, highlightthickness=0)
canvas.pack(expand = YES, fill = BOTH)
canvas.create_image(0, 0, image = bg, anchor = NW)
canvas.create_text(121,36 ,
                anchor='w', fill='white', text="COMMANDS",
                font=('Helvetica 18 bold'))





canvas.create_text(55,105 ,
                anchor='w', fill='white', text="ROBOT ",
                font=('Helvetica 15 bold'))

canvas.create_text(55,223 ,
                anchor='w', fill='white', text="CONVEYOR 1 ",
                font=('Helvetica 15 bold'))

canvas.create_text(55,325 ,
                anchor='w', fill='white', text="CONVEYOR 2 ",
                font=('Helvetica 15 bold'))



START_ROBOT = tk.Button(form,text='START',font='Helvetica 18 bold',fg='green',bg='white',width=7,height=2,command=start_robot)
START_ROBOT.place(x=55, y=120)
STOP_ROBOT = tk.Button(form,text='STOP',font='Helvetica 18 bold',fg='red',bg='yellow',width=7,height=2,command=stop_robot)
STOP_ROBOT.place(x=175, y=120)

#CONVEYOR_1 = tk.Label(form,text='Conveyor 1',font='Helvetica 14 bold')
#CONVEYOR_1.place(x=55, y=264)
START_CV_1 = tk.Button(form,text='START',font='Helvetica 18 bold',fg='green',bg='white',width=7,height=1,command=start_cv1)
START_CV_1.place(x=55, y=240)
STOP_CV_1 = tk.Button(form,text='STOP',font='Helvetica 18 bold',fg='red',bg='yellow',width=7,height=1,command=stop_cv1)
STOP_CV_1.place(x=176, y=240)

#CONVEYOR_2 = tk.Label(form,text='Conveyor 2',font='Helvetica 14 bold')
#CONVEYOR_2.place(x=55, y=364)
START_CV_2 = tk.Button(form,text='START',font='Helvetica 18 bold',fg='green',bg='white',width=7,height=1,command=start_cv2)
START_CV_2.place(x=55, y=340)
STOP_CV_2 = tk.Button(form,text='STOP',font='Helvetica 18 bold',fg='red',bg='yellow',width=7,height=1,command=stop_cv2)
STOP_CV_2.place(x=176, y=340)

################################### RIGHT SIDE ########################################################


canvas.create_text(381,36 ,
                anchor='w', fill='white', text="ROBOT STATUS",
                font=('Helvetica 18 bold'))

OPERATION_NUMBER = tk.Label(form,text='Operation Number                       ',font='Helvetica 14 bold')
OPERATION_NUMBER.place(relx =0.53,rely=0.25,anchor='sw')

OBJECT_DETECTED = tk.Label(form,text='Object Detected                           ',font='Helvetica 14 bold')
OBJECT_DETECTED.place(relx =0.53,rely=0.33,anchor='sw')

OBJECT_GRIPPED = tk.Label(form,text='Object Gripped                            ',font='Helvetica 14 bold')
OBJECT_GRIPPED.place(relx =0.53,rely=0.41,anchor='sw')

OBJECT_DROPPED = tk.Label(form,text='Object Dropped                           ',font='Helvetica 14 bold')
OBJECT_DROPPED.place(relx =0.53,rely=0.49,anchor='sw')

READY = tk.Label(form,text='Ready For Operation                  ',font='Helvetica 14 bold')
READY.place(relx =0.53,rely=0.57,anchor='sw')

OPEN_CAMERA = tk.Button(form,text='OPEN CAMERA',font='Helvetica 18 bold',fg='green',bg='white',width=19,height=1,command=open_camera)
OPEN_CAMERA.place(relx =0.53,rely=0.70,anchor='sw')

MAUAL_MODE = tk.Button(form,text='OPEN MANUAL MODE',font='Helvetica 18 bold',fg='green',bg='white',width=19,height=1,command=manual_mode)
MAUAL_MODE.place(relx =0.53,rely=0.82,anchor='sw')

RESET_FLAGS = tk.Button(form,text='Reflesh Flags',font='Helvetica 10 bold',fg='green',bg='white',width=12,height=1,command=reset_flags)
RESET_FLAGS.place(relx =0.53,rely=0.89,anchor='sw')

AUTO_MODE = tk.Button(form,text='AUTO MODE',font='Helvetica 12 bold',fg='green',bg='white',width=22,height=1,command=auto_mode)
AUTO_MODE.place(x=55, y=396)

if (main_counter % 2) == 0:
    ode_flag=0
    odr_flag = 0
    og_flag = 0
    ready_flag = 0
    op_num=0
    status_robot=0
    status_cv1=0
    status_cv2=0
else:
    ode_flag=1
    odr_flag = 1
    og_flag = 1
    ready_flag = 1
    op_num=1
    status_robot=1
    status_cv1=1
    status_cv2=1  
ST_OPERATION_NUMBER = tk.Label(form,text=str(op_num),font='Helvetica 14 bold',fg='green',)
ST_OPERATION_NUMBER.place(relx =0.87,rely=0.25,anchor='sw')


if ode_flag == 1:
    ST_OBJECT_DETECTED =  tk.Label(form,text=ST_OBJECT_DETECTED_1,font='Helvetica 14 bold',fg='green',)
    ST_OBJECT_DETECTED.place(relx =0.80,rely=0.33,anchor='sw')

if og_flag == 1:
    ST_OBJECT_GRIPPED =  tk.Label(form,text=ST_OBJECT_GRIPPED_1,font='Helvetica 14 bold',fg='green',)
    ST_OBJECT_GRIPPED.place(relx =0.80,rely=0.41,anchor='sw')

if odr_flag == 1:
    ST_OBJECT_DROPPED =  tk.Label(form,text=ST_OBJECT_DROPPED_1,font='Helvetica 14 bold',fg='green',)
    ST_OBJECT_DROPPED.place(relx =0.80,rely=0.49,anchor='sw')
else:
    ST_OBJECT_DROPPED =  tk.Label(form,text=ST_OBJECT_DROPPED_2,font='Helvetica 14 bold',fg='red',)
    ST_OBJECT_DROPPED.place(relx =0.87,rely=0.49,anchor='sw')

ST_READY =  tk.Label(form,text=ST_READY_2,font='Helvetica 14 bold',fg='red',)
ST_READY.place(relx =0.87,rely=0.57,anchor='sw') 

def ready_flag_switcher(ready_flag):
 
    if ready_flag == 1:
        ST_READY.config(text=ST_READY_1)
        
    


if status_robot==1:
    STATUS_ROBOT = tk.Label(form,text='  Working.....',font='Helvetica 11 bold',fg='green')
    STATUS_ROBOT.place(x=195, y=92)
else:
    STATUS_ROBOT = tk.Label(form,text='Not Working',font='Helvetica 11 bold',fg='red')
    STATUS_ROBOT.place(x=195, y=92)

if status_cv1==1:
    STATUS_CV1 = tk.Label(form,text='  Working.....',font='Helvetica 11 bold',fg='green')
    STATUS_CV1.place(x=195, y=212)
else:
    STATUS_CV1 = tk.Label(form,text='Not Working',font='Helvetica 11 bold',fg='red')
    STATUS_CV1.place(x=195, y=212)

if status_cv2==1:
    STATUS_CV2 = tk.Label(form,text='  Working.....',font='Helvetica 11 bold',fg='green')
    STATUS_CV2.place(x=195, y=284)
else:
    STATUS_CV2 = tk.Label(form,text='Not Working',font='Helvetica 11 bold',fg='red')
    STATUS_CV2.place(x=195, y=312)

def update_status():
    pass


tk.mainloop()
