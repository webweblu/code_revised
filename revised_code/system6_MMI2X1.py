from ioesim import all as IOE
from ioedev import all as DEV
from gs23_3gen import GS23_3Gen
from combiner_MMI2X1_6 import combiner_MMI2X1_3Gen
import matplotlib.pyplot as plt
import scipy.io as sio
import numpy as np
import math
# GS23_3_DC29_ratio=0.5
# GS23_3_DC30_ratio=0.5
# GS23_3_DC31_ratio=0.5
# GS23_3_DC32_ratio=0.5

def system6_MMI2X1Gen():
    system6_MMI2X1 = IOE.IOESystem()
    system6_MMI2X1.property_dict['universal']['name'].setValue('system3_MMI2X1_2')

    PIC1 = GS23_3Gen(randomphase=True, new_randomphase=False, cen_wl=GS23_3_cen_wl,
                    DL1=GS23_3_DL1, DL2=GS23_3_DL2, DL3=GS23_3_DL3, DL4=GS23_3_DL4, DL5=GS23_3_DL5,
                    DL6=GS23_3_DL6, DL7=GS23_3_DL7,DL8=GS23_3_DL8,DL9=GS23_3_DL9,DL10=GS23_3_DL10,DL11=GS23_3_DL11,DL12=GS23_3_DL12,
                    DL13=GS23_3_DL13,DL14=GS23_3_DL14,DL15=GS23_3_DL15,DL16=GS23_3_DL16,
                    DL_Decay = GS23_3_DL_Decay,
                    DC21_ratio=GS23_3_DC21_ratio, DC22_ratio=GS23_3_DC22_ratio, DC23_ratio=GS23_3_DC23_ratio,DC20_ratio=GS23_3_DC20_ratio,
                    DC24_ratio=GS23_3_DC24_ratio, DC17_ratio=GS23_3_DC17_ratio, DC18_ratio=GS23_3_DC18_ratio,DC19_ratio=GS23_3_DC19_ratio,
                    DC25_ratio=GS23_3_DC25_ratio,DC26_ratio=GS23_3_DC26_ratio,DC27_ratio=GS23_3_DC27_ratio,DC28_ratio=GS23_3_DC28_ratio,
                    DC29_ratio=GS23_3_DC29_ratio,
                    DC30_ratio=GS23_3_DC30_ratio,DC31_ratio=GS23_3_DC31_ratio,DC32_ratio=GS23_3_DC32_ratio )
                    # DC29_ratio=0.5, DC30_ratio=0.5,
                    # DC31_ratio=0.5, DC32_ratio=0.5, DC33_ratio=0.5,
                    # DC34_ratio=0.5, DC35_ratio=0.5, DC36_ratio=0.5,
                    # DC37_ratio=0.5, DC38_ratio=0.5, DC39_ratio=0.5,
                    # DC40_ratio=0.5, DC45_ratio=0.5, DC46_ratio=0.5, DC47_ratio=0.5, DC48_ratio=0.5)
    PIC2 = combiner_MMI2X1_3Gen(randomphase=False, new_randomphase=False,
                               DL=combiner_MMI2X1_DL,
                               # DL0=combiner_MMI2X1_DL0, DL1=combiner_MMI2X1_DL1, DL2=combiner_MMI2X1_DL2,
                               # DL3=combiner_MMI2X1_DL3, DL4=combiner_MMI2X1_DL4,
                               # DL5=combiner_MMI2X1_DL5, DL6=combiner_MMI2X1_DL6, DL7=combiner_MMI2X1_DL7,
                               WG=combiner_MMI2X1_WG,
                               MMI2X1_loss=combiner_MMI2X1_loss, MMI2X1_imbalance=combiner_MMI2X1_imbalance,
                               MMI2X1_reflection=combiner_MMI2X1_reflection,
                               weight7=combiner_MMI2X1_modulator_ideal7_weight,
                               phase7=combiner_MMI2X1_modulator_ideal7_phase,

                               weight8=combiner_MMI2X1_modulator_ideal8_weight,
                               phase8=combiner_MMI2X1_modulator_ideal8_phase,

                               weight9=combiner_MMI2X1_modulator_ideal9_weight,
                               phase9=combiner_MMI2X1_modulator_ideal9_phase,

                               weight10=combiner_MMI2X1_modulator_ideal10_weight,
                               phase10=combiner_MMI2X1_modulator_ideal10_phase,

                               weight11=combiner_MMI2X1_modulator_ideal11_weight,
                               phase11=combiner_MMI2X1_modulator_ideal11_phase,

                               weight12=combiner_MMI2X1_modulator_ideal12_weight,
                               phase12=combiner_MMI2X1_modulator_ideal12_phase,

                               weight13=combiner_MMI2X1_modulator_ideal13_weight,
                               phase13=combiner_MMI2X1_modulator_ideal13_phase,

                               weight14=combiner_MMI2X1_modulator_ideal14_weight,
                               phase14=combiner_MMI2X1_modulator_ideal14_phase, )
    system6_MMI2X1.addUnit(PIC1)
    system6_MMI2X1.addUnit(PIC2)


    for i in range(4):
        system6_MMI2X1.addOpticalPort()
        system6_MMI2X1.optical_port_list[0].property_dict['universal']['name'].setValue('Op_port_' + str(i))
    # system6_MMI2X1.addOpticalPort()
    # system6_MMI2X1.optical_port_list[0].property_dict['universal']['name'].setValue('In_port_0')
    system6_MMI2X1.addOpticalPort()
    system6_MMI2X1.optical_port_list[0].property_dict['universal']['name'].setValue('Out_port_4')

    ##Add connections
    system6_MMI2X1.addConnection(system6_MMI2X1.subunit_list[0].optical_port_list[0],
                                 system6_MMI2X1.subunit_list[1].optical_port_list[1])
    system6_MMI2X1.addConnection(system6_MMI2X1.subunit_list[0].optical_port_list[1],
                                 system6_MMI2X1.subunit_list[1].optical_port_list[2])
    system6_MMI2X1.addConnection(system6_MMI2X1.subunit_list[0].optical_port_list[2],
                                 system6_MMI2X1.subunit_list[1].optical_port_list[3])
    system6_MMI2X1.addConnection(system6_MMI2X1.subunit_list[0].optical_port_list[3],
                                 system6_MMI2X1.subunit_list[1].optical_port_list[4])
    system6_MMI2X1.addConnection(system6_MMI2X1.subunit_list[0].optical_port_list[4],
                                 system6_MMI2X1.subunit_list[1].optical_port_list[5])
    system6_MMI2X1.addConnection(system6_MMI2X1.subunit_list[0].optical_port_list[5],
                                 system6_MMI2X1.subunit_list[1].optical_port_list[6])
    system6_MMI2X1.addConnection(system6_MMI2X1.subunit_list[0].optical_port_list[6],
                                 system6_MMI2X1.subunit_list[1].optical_port_list[7])
    system6_MMI2X1.addConnection(system6_MMI2X1.subunit_list[0].optical_port_list[7],
                                 system6_MMI2X1.subunit_list[1].optical_port_list[8])
    # system6_MMI2X1.addConnection(system6_MMI2X1.subunit_list[1].optical_port_list[9])
    # system6_MMI2X1.addConnection(system6_MMI2X1.subunit_list[0].optical_port_list[9],
    #                              system6_MMI2X1.subunit_list[1].optical_port_list[10])
    # system6_MMI2X1.addConnection(system6_MMI2X1.subunit_list[0].optical_port_list[10],
    #                              system6_MMI2X1.subunit_list[1].optical_port_list[11])
    # system6_MMI2X1.addConnection(system6_MMI2X1.subunit_list[0].optical_port_list[11],
    #                              system6_MMI2X1.subunit_list[1].optical_port_list[12])


    system6_MMI2X1.addConnection(system6_MMI2X1.subunit_list[0].optical_port_list[8], system6_MMI2X1.optical_port_list[0])
    system6_MMI2X1.addConnection(system6_MMI2X1.subunit_list[0].optical_port_list[9], system6_MMI2X1.optical_port_list[1])
    system6_MMI2X1.addConnection(system6_MMI2X1.subunit_list[0].optical_port_list[10], system6_MMI2X1.optical_port_list[2])
    system6_MMI2X1.addConnection(system6_MMI2X1.subunit_list[0].optical_port_list[11], system6_MMI2X1.optical_port_list[3])
    system6_MMI2X1.addConnection(system6_MMI2X1.subunit_list[1].optical_port_list[0], system6_MMI2X1.optical_port_list[4])

    system6_MMI2X1.checkAllConnected()

    return system6_MMI2X1

if __name__ == '__main__':

################## Svae the scattering matrices data ###################
##set parameters of GS46_3
    GS23_3_cen_wl = 1.55
#     changdu =[2000, 2000,2000]
#     lenged = ['r-','b-','g-']
# for i in range(len(changdu)):
#     GS23_3_DL1 = changdu[i]
#     GS23_3_DL2 = changdu[i]
#     GS23_3_DL3 = changdu[i]
#     GS23_3_DL4 = changdu[i]
#     GS23_3_DL5 = changdu[i]
#     GS23_3_DL6 = changdu[i]
#     GS23_3_DL7 = changdu[i]
#     GS23_3_DL8 = changdu[i]
#     GS23_3_DL9 = changdu[i]
#     GS23_3_DL10 = changdu[i]
#     GS23_3_DL11 = changdu[i]
#     GS23_3_DL12 = changdu[i]
#     GS23_3_DL13 = changdu[i]
#     GS23_3_DL14 = changdu[i]
#     GS23_3_DL15 = changdu[i]
#     GS23_3_DL16 = changdu[i]
    GS23_3_DL1 = 500
    GS23_3_DL2 = 500
    GS23_3_DL3 = 500
    GS23_3_DL4 = 500
    GS23_3_DL5 = 500
    GS23_3_DL6 = 500
    GS23_3_DL7 = 500
    GS23_3_DL8 = 500
    GS23_3_DL9 = 500
    GS23_3_DL10 = 500
    GS23_3_DL11 = 500
    GS23_3_DL12 = 500
    GS23_3_DL13 = 500
    GS23_3_DL14 = 500
    GS23_3_DL15 = 500
    GS23_3_DL16 = 500

    # GS46_3_DL17 = 4898
    # GS46_3_DL18 = 4898
    # GS46_3_DL19 = 4898
    # GS46_3_DL20 = 4898
    # GS46_3_DL21 = 4898
    # GS46_3_DL22 = 4898
    # GS46_3_DL23 = 4898
    # GS46_3_DL24 = 4898
    GS23_3_DL_Decay = 2
    GS23_3_DC17_ratio = 0.5
    GS23_3_DC18_ratio = 0.5
    GS23_3_DC19_ratio = 0.5
    GS23_3_DC20_ratio = 0.5
    GS23_3_DC21_ratio = 0.5
    GS23_3_DC22_ratio = 0.5
    GS23_3_DC23_ratio = 0.5
    GS23_3_DC24_ratio = 0.5
    GS23_3_DC25_ratio = 0.5
    GS23_3_DC26_ratio = 0.5
    GS23_3_DC27_ratio = 0.5
    GS23_3_DC28_ratio = 0.5
    GS23_3_DC29_ratio = 0.6
    GS23_3_DC30_ratio = 0.6
    GS23_3_DC31_ratio = 0.6
    GS23_3_DC32_ratio = 0.6
    # gs44_5_DC45_ratio = 0.9
    # gs44_5_DC46_ratio = 0.9
    # gs44_5_DC47_ratio = 0.9
    # gs44_5_DC48_ratio = 0.9

    ##set parameters of combiner_MMI2X1
    combiner_MMI2X1_DL = 500  # Delay line length in um
    # combiner_MMI2X1_DL0 = 4898  # Delay line length in um
    # combiner_MMI2X1_DL1 = 4898
    # combiner_MMI2X1_DL2 = 4898
    # combiner_MMI2X1_DL3 = 4898
    # combiner_MMI2X1_DL4 = 4898
    # combiner_MMI2X1_DL5 = 4898
    # combiner_MMI2X1_DL6 = 4898
    # combiner_MMI2X1_DL7 = 4898

    combiner_MMI2X1_WG = 100
    combiner_MMI2X1_loss = 0.3
    combiner_MMI2X1_imbalance = 0
    combiner_MMI2X1_reflection = 20

    combiner_MMI2X1_modulator_ideal7_weight = 0.7 # weight of modulator
    combiner_MMI2X1_modulator_ideal7_phase =4.16 # phase of modulator

    combiner_MMI2X1_modulator_ideal8_weight = 0.7
    combiner_MMI2X1_modulator_ideal8_phase = 0.4

    combiner_MMI2X1_modulator_ideal9_weight = 0.98
    combiner_MMI2X1_modulator_ideal9_phase = 3.99

    combiner_MMI2X1_modulator_ideal10_weight = 0.99
    combiner_MMI2X1_modulator_ideal10_phase = 1.99

    combiner_MMI2X1_modulator_ideal11_weight = 0.14
    combiner_MMI2X1_modulator_ideal11_phase = 0.01

    combiner_MMI2X1_modulator_ideal12_weight = 0.91
    combiner_MMI2X1_modulator_ideal12_phase = 0.00

    combiner_MMI2X1_modulator_ideal13_weight = 0.99
    combiner_MMI2X1_modulator_ideal13_phase = 2.98

    combiner_MMI2X1_modulator_ideal14_weight = 0.84
    combiner_MMI2X1_modulator_ideal14_phase = 1.37




    # dldata = np.matrix([[0,0],[0,0.1],[0,0.2],[0,0.3],
    #                     [0,0.4],[0,0.5],[0,0.6],
    #                     [0,0.7],[0,0.8],[0,0.9],
    #                     [0,1],[0,1.1],
    #                    ])
    # Ydata = np.zeros((1280, 2))
    # for ii in range(2):
    #     combiner_MMI2X1_modulator_ideal16_phase = dldata[0, ii]
    #     combiner_MMI2X1_modulator_ideal17_phase = dldata[1, ii]
    #     combiner_MMI2X1_modulator_ideal18_phase = dldata[2, ii]
    #     combiner_MMI2X1_modulator_ideal19_phase = dldata[3, ii]
    #     combiner_MMI2X1_modulator_ideal20_phase = dldata[4, ii]
    #     combiner_MMI2X1_modulator_ideal21_phase = dldata[5, ii]
    #     combiner_MMI2X1_modulator_ideal22_phase = dldata[6, ii]
    #     combiner_MMI2X1_modulator_ideal23_phase = dldata[7, ii]
    #     combiner_MMI2X1_modulator_ideal24_phase = dldata[8, ii]
    #     combiner_MMI2X1_modulator_ideal25_phase = dldata[9, ii]
    #     combiner_MMI2X1_modulator_ideal26_phase = dldata[10, ii]
    #     combiner_MMI2X1_modulator_ideal27_phase = dldata[11, ii]
    #     combiner_MMI2X1_modulator_ideal28_phase = dldata[11, ii]
    #     combiner_MMI2X1_modulator_ideal29_phase = dldata[11, ii]
    #     combiner_MMI2X1_modulator_ideal30_phase = dldata[11, ii]
    #     combiner_MMI2X1_modulator_ideal31_phase = dldata[11, ii]
    SimPlatform = IOE.SimulationPlatform()
    SimPlatform.FolderPath = 'D:\\gs_simulaitondata\\system_6\\'
    SimPlatform.name = 'system6_MMI2X1'
    PIC = system6_MMI2X1Gen()
    SimPlatform.addPIC(PIC)

    # for i in range(4):
    #     SimPlatform.addInputPort(port_index=i)
    # SimPlatform.addOutputPort(port_index=4)

    SimPlatform.addInputPort(port_index=0)
    SimPlatform.addInputPort(port_index=1)
    SimPlatform.addInputPort(port_index=2)
    SimPlatform.addInputPort(port_index=3)
    SimPlatform.addOutputPort(port_index=4)
    SimPlatform.simulationParameters = {'sigfreq': 25e9, 'centerwl': 1.55, 'timestep': 1 / 64, 'modellength': 1280,
                                            'simulationtime': 5000}

    SimPlatform.Run_Freq(save=True)
    # SimPlatform.Visualization_Freq([4], [0])
    # SimPlatform.Visualization_Freq([4], [1])
    # SimPlatform.Visualization_Freq([4], [2])
    # SimPlatform.Visualization_Freq([4], [3])
    load_data = 'D:\\gs_simulaitondata\\system_6\\system6_MMI2X1smatrix.mat'
    X = sio.loadmat(load_data)
    w = np.linspace(1.54361971, 1.55643326, 1280)
#拟合输出幅度谱
    legend = []
    #
    data_label = np.loadtxt('D:\\gs_simulaitondata\\system_3\\RING_2.smatrix')
    X = SimPlatform.sdata[0, 0, :] + SimPlatform.sdata[0, 1, :] + SimPlatform.sdata[0, 2, :] + SimPlatform.sdata[0, 3, :]
    print(type(X))
##

    port0_4in_data = {'wavelength': w, 'data': X}
    plt.rcParams["xtick.direction"] = 'in'
    plt.rcParams["ytick.direction"] = 'in'
    plt.plot(w, abs(port0_4in_data['data'])**2)
    # plt.legend(["2000nm"],loc = 'upper right')
    plt.xlabel("wavelength/(um)")
    plt.ylabel("optical power/(mW)")
    plt.plot(w,data_label)
        # plt.plot(w, 20*np.log(abs(port0_4in_data['data'])))
    # np.savetxt('D:\\random_phase_data\\X1_1.5pi',abs(port0_4in_data['data'])**2)

#相位谱分布
    # plt.rcParams["xtick.direction"] = 'in'
    # plt.rcParams["ytick.direction"] = 'in'
    # plt.plot(w, np.angle(X['data'][0, 0, :]+X['data'][0, 1, :]+X['data'][0, 2, :]+X['data'][0, 3, :]))
    # plt.xlabel("wavelength/(um)")
    # plt.ylabel("phase response/(rads)")
#FSR变化-散点图
    # a = np.linspace(2000,2000,6)
    # b = ([1.5,1.45,1.32,1.3,1.2,1.15])
    # plt.rcParams["xtick.direction"] = 'in'
    # plt.rcParams["ytick.direction"] = 'in'
    # plt.scatter(a,b,label = 'FSR')
    # plt.xlabel("WG length/(um)")
    # plt.ylabel("FSR/(nm)")
    # plt.legend()






plt.show()

    #########################################################################



