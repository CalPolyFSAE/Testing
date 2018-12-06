import visa
import time
#from time import time
import datetime
rm = visa.ResourceManager()
print(rm.list_resources())
print(rm)
mMeter = rm.open_resource('USB0::0x1AB1::0x09C4::DM3R193601791::INSTR')

# =============================================================================
# pSupply = rm.open_resource('COM3')
# print(pSupply.session)
# pSupply.baud_rate = 57600
# print(pSupply)
# print("-----------------------")
# print(pSupply.write("VSET 10"))
# print(pSupply.query("VSET?"))
# print(pSupply.write("ISET 0.9"))
# pSupply.close()
# =============================================================================

print("-----------------------")
print(mMeter)
print("-----------------------")
f = open("pyVisaData.txt", "w")
other_start_time = datetime.time
start_time = time.time()
current_time = time.time()
f.write("Min\tTime\tVolt\n")
while((current_time-start_time)<80):
    time.sleep(1.0 - ((time.time() - start_time) % 1.0))
    m = mMeter.query(":MEASure:VOLTage:DC?")
    time_now = time.time()-start_time
    f.write(("{0:4.0f}\t{0:4.0f}\t{1}").format(time_now//60,time_now%60,str(float(m))))
    
    f.write("\n")
    current_time = time.time()
f.close()
print("done")


#f.close
#print(mMeter.query("*IDN?"))


#Power Supply
#print(pSupply.write('OUTPut CH1, OFF'))

#print(pSupply.write('OUTPut CH1, ON'))
#time.sleep(15)

#print(pSupply.query("VOLT?"))

#time.sleep(15)
#print(pSupply.write('SOURce1:VOLTage 15'))
#Multimeter
#print("DC Current = ", inst.query(":MEASure:CURRent:DC?"))