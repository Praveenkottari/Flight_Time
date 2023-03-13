import math
#import sys,os
from tkinter import *

#os.chdir(sys._MEIPASS)
root=Tk()
root.title("    Edall UAV performance Calculator")
root.geometry("1000x600")
#root.iconbitmap('data\\edall1.ico')
root.iconbitmap('C:\edall\edall.ico')

def Calculation():

    Altitude =float(Altitudeentry.get())
    Prop_Rot = float(Prop_Rotationentry.get())
    prop_dia = float(Prop_Diameterentry.get())
    Prop_pitch = float(Prop_Pitchvalueentry.get())
    Motor_Efficeny = float(Motor_Efficenyentry.get())
    Battery_voltage = float(Voltageentry.get())
    Battery_cap = float(Battery_capacityentry.get())
    Battery_Dischrg = float(Battery_perentry.get())
    Model_TR = float(Model_TRentry.get())
    No_motor = int(No_motorentry.get())

    Temp1 = (((-0.0065) * Altitude)+288.15)
    Temp1 =float(Temp1)

    Density = (((Temp1/288.15)**(4.252205597))*1.225)
    Label(text=f"{Density}",font="arial 13 bold").place(x=300,y=300)

    Thrust_N = ((Density*(math.pi))*(((0.0254*prop_dia)/2)**2)*((Prop_Rot*0.0254*Prop_pitch/60)**2)*(((prop_dia)/(3.29546*Prop_pitch))**1.5))
    Thrust_N = round(Thrust_N,4)
    Label(text=f"{Thrust_N}",font="arial 15 bold").place(x=300,y=350)

    Thrust_kg = (Thrust_N/9.81)
    Thrust_kg=round(Thrust_kg,4)
    Label(text=f"{Thrust_kg}",font="arial 16 bold").place(x=300,y=375)
    

    Elect_power_consumption = ((Model_TRentry*1000)/Motor_Efficeny)
    Elect_power_consumption = round(Elect_power_consumption,4)
    Label(text=f"{Elect_power_consumption}",font ="arial 16 bold").place(x=300,y=425)

    Average_Current =((Elect_power_consumption*No_motor)/Battery_voltage)
    Average_Current= round(Average_Current,4)
    Label(text=f"{Average_Current}",font='arial 16 bold').place(x=800,y=325)

    Flight_time = (((Battery_cap*Battery_Dischrg)/(100000*Average_Current))*60)
    Flight_time=round(Flight_time,4)
    Label(text=f"{Flight_time}",font='arial 16 bold').place(x=800,y=375)


#parameters
heading1 =Label(root,text="Static Thrust Caluclation",font="arial 14 bold")
heading2 =Label(root,text="Flight Time Caluclation",font="arial 14 bold")
param5 =Label(root,text="Altitude(meter):",font="arial 14")
param2 =Label(root,text="Prop Rotation(RPM):",font="arial 14")
param3 =Label(root,text="Prop Diameter(inch):",font="arial 14")
param4 =Label(root,text="Prop Pitch(inch):",font="arial 14")
param6 =Label(root,text="Motor Efficency:",font="arial 14")
param7 =Label(root,text="Battery Voltage(Volt): ",font='arial 14')
param8 =Label(root,text="Average Current Drawn(Amp): ",font='arial 14')
param9 =Label(root,text="Battery capacity (mah): ",font='arial 14')
param10 =Label(root,text="Battery Discharge(%): ",font='arial 14')
param11 =Label(root,text="Thrust Required to \n Lift/cruise(Kg): ",font='arial 14')
param12 =Label(root,text="Number of motors : ",font='arial 14')

param1 =Label(root,text="Density(Kg/m^3):",font="arial 12")
Thrust_N =Label(root,text="Static Thrust(Newton) :",font="arial 16")
Thrust_kg =Label(root,text="Static Thrust(Kg):",font="arial 16")
power_elct_watt = Label(root,text="Electric Power(Watt): ",font="arial 16")
Flight_time =Label(root,text="Flight time(minutes): ",font='arial 16')

heading1.place(x=150,y=5)
heading2.place(x=620,y=5)
param5.place(x=50,y=50)
param2.place(x=50,y=100)
param3.place(x=50,y=150)
param4.place(x=50,y=200)
param6.place(x=50,y=250)
param1.place(x=50,y=300)
param7.place(x=520,y=100)
param8.place(x=520,y=325)
param9.place(x=520,y=150)
param10.place(x=520,y=200)
param11.place(x=520,y=50)
param12.place(x=520,y=250)


Thrust_N.place(x=50,y=350)
Thrust_kg.place(x=50,y=375)
power_elct_watt.place(x=50,y=425)
Flight_time.place(x=520,y=375)


Altitudevalue=StringVar()
Prop_Rotationvalue=StringVar()
Prop_Diametervalue=StringVar()
Prop_Pitchvalue=StringVar()
Motor_Efficenyvalue=StringVar()
Voltagevalue = StringVar()
Batterycapacityvalue = StringVar()
Battery_pervalue = StringVar()
Model_TRvalue =StringVar()
No_motorvalue = StringVar()

#for Dropdown option
#No_motor =StringVar()
#No_motor.set("1")
#drop = OptionMenu(root,No_motor,"1","2","3","4","6","8")
#drop.pack()

Altitudeentry=Entry(root,textvariable=Altitudevalue,font="arial 15",width=15)
Prop_Rotationentry=Entry(root,textvariable=Prop_Rotationvalue,font="arial 15",width=15)
Prop_Diameterentry=Entry(root,textvariable=Prop_Diametervalue,font="arial 15",width=15)
Prop_Pitchvalueentry=Entry(root,textvariable=Prop_Pitchvalue,font="arial 15",width=15)
Motor_Efficenyentry=Entry(root,textvariable=Motor_Efficenyvalue,font="arial 15",width=15)
Voltageentry = Entry(root,textvariable=Voltagevalue,font='arial 15',width=15)
Battery_capacityentry = Entry(root,textvariable=Batterycapacityvalue,font='aerial 15',width=15)
Battery_perentry = Entry(root,textvariable=Battery_pervalue,font='arial 15',width=15)
Model_TRentry = Entry(root,textvariable=Model_TRvalue,font='arial 15',width=15)
No_motorentry= Entry(root,textvariable=No_motorvalue,font='arial 15',width=15)


Altitudeentry.place(x=300,y=50)
Prop_Rotationentry.place(x=300,y=100)
Prop_Diameterentry.place(x=300,y=150)
Prop_Pitchvalueentry.place(x=300,y=200)
Motor_Efficenyentry.place(x=300,y=250)
Voltageentry.place(x=775,y=100)
Battery_capacityentry.place(x=775,y =150)
Battery_perentry.place(x=775,y=200)
Model_TRentry.place(x=775,y=50)
No_motorentry.place(x=775,y=250)


Button(text="Calculate",font="arial 15",bg="grey",bd=15,command=Calculation).place(x=400,y=500)


root.mainloop()
