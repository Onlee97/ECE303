# Experiment 1B-Resistor Estimation Lab-USB & GPIB
import visa
import numpy as np
import time as time
import matplotlib.pyplot as plt
from addresses import AddressesLastDesk as toolAddr
import enum as Enum


def main():
    # Input values

    awg_address = toolAddr.awg.value  # Waveform Generator Address
    # dmm_address = toolAddr.dmm.value  # Digital Multimeter Address
    V_min = 0  # Lower DMM DC Output Voltage ( Volts )
    V_max = 4.5 # Upper DMM DC Output Voltage ( Volts )
    N_Volts = 51  # Number of voltages between V min and V max
    filename = 'experiment1b.csv'  # File name for data output

    # Define voltage and current vectors
    V = np.linspace(V_min, V_max, N_Volts)
    V1 = np.linspace(V_min, V_max, 10 * N_Volts + 1)
    Imeas = np.zeros(N_Volts)

    # Initiate communications with and open instruments
    rm = visa.ResourceManager()
    awg = rm.open_resource(awg_address)
    # dmm = rm.open_resource(dmm_address)

    # Place waveform generator in High-Z
    awg.write("OUTP:LOAD INF")

    # Conduct Measurements
    count = 0
    for K in V:
        print("Applying %f Volts" % K)
        awg.write("APPL:DC DEF,DEF,%f" % K)
        time.sleep(0.5)
        # Imeas[count] = dmm.query("MEAS:CURR:DC? 1e-1,1e-5")
        print ("here1")
        count = count + 1

        # Calcuate resistor value and estimated current vector
    Rest = V.dot(V) / V.dot(Imeas)
    Iest = V1 / Rest
    print ("here2")

    # Write data to f i l e
    data = np.append(np.transpose([V]), np.transpose([Imeas * 1000]), axis=1)
    np.savetxt(filename, data, delimiter=', ')
    print ("here3")

    # Plot Current vs . Voltage
    plt.plot(V, Imeas * 1000, 'bo ', markersize=4, label='Measured ')
    plt.plot(V1, Iest * 1000, 'r-', linewidth=2, label=' Fitted ')
    plt.grid()
    plt.legend()
    plt.xlabel("Voltage(V)")
    plt.ylabel("Current(mA)")
    plt.title("Estimated Resistance = " + ' {: .0f}'.format(Rest) + r' $\Omega$ ')
    plt.show()  # Make plot visible


if __name__ == "__main__":
    main()
