from ioesim import all as IOE
from ioedev import all as DEV
from gs23_3gen import GS23_3Gen
from combiner_MMI2X1_6 import combiner_MMI2X1_3Gen
import matplotlib.pyplot as plt
import numpy as np


def get_fitness(position):
    # print(position)
    fitness = np.zeros(np.size(position, 0))
    # 计算每个个体适应值
    for number in range(0, np.size(position, 0)):
        combiner_MMI2X1_modulator_ideal = position[number]
        ################## Svae the scattering matrices data ###################
        ##set parameters of GS46_3
        GS23_3_cen_wl = 1.55
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
        # combiner_MMI2X1_DL0 = 0  # Delay line length in um
        # combiner_MMI2X1_DL1 = 0
        # combiner_MMI2X1_DL2 = 0
        # combiner_MMI2X1_DL3 = 0
        # combiner_MMI2X1_DL4 = 0
        # combiner_MMI2X1_DL5 = 0
        # combiner_MMI2X1_DL6 = 0
        # combiner_MMI2X1_DL7 = 0

        combiner_MMI2X1_WG = 100
        combiner_MMI2X1_loss = 0.3
        combiner_MMI2X1_imbalance = 0
        combiner_MMI2X1_reflection = 20

        combiner_MMI2X1_modulator_ideal7_weight = combiner_MMI2X1_modulator_ideal[0]  # weight of modulator
        combiner_MMI2X1_modulator_ideal7_phase = combiner_MMI2X1_modulator_ideal[1]  # phase of modulator

        combiner_MMI2X1_modulator_ideal8_weight = combiner_MMI2X1_modulator_ideal[2]
        combiner_MMI2X1_modulator_ideal8_phase = combiner_MMI2X1_modulator_ideal[3]

        combiner_MMI2X1_modulator_ideal9_weight = combiner_MMI2X1_modulator_ideal[4]
        combiner_MMI2X1_modulator_ideal9_phase = combiner_MMI2X1_modulator_ideal[5]

        combiner_MMI2X1_modulator_ideal10_weight = combiner_MMI2X1_modulator_ideal[6]
        combiner_MMI2X1_modulator_ideal10_phase = combiner_MMI2X1_modulator_ideal[7]

        combiner_MMI2X1_modulator_ideal11_weight = combiner_MMI2X1_modulator_ideal[8]
        combiner_MMI2X1_modulator_ideal11_phase = combiner_MMI2X1_modulator_ideal[9]

        combiner_MMI2X1_modulator_ideal12_weight = combiner_MMI2X1_modulator_ideal[10]
        combiner_MMI2X1_modulator_ideal12_phase = combiner_MMI2X1_modulator_ideal[11]

        combiner_MMI2X1_modulator_ideal13_weight = combiner_MMI2X1_modulator_ideal[12]
        combiner_MMI2X1_modulator_ideal13_phase = combiner_MMI2X1_modulator_ideal[13]

        combiner_MMI2X1_modulator_ideal14_weight = combiner_MMI2X1_modulator_ideal[14]
        combiner_MMI2X1_modulator_ideal14_phase = combiner_MMI2X1_modulator_ideal[15]



        SimPlatform = IOE.SimulationPlatform()
        SimPlatform.FolderPath = 'D:\\gs_simulaitondata\\system_6\\'
        SimPlatform.name = 'system6_MMI2X1'

        # system6_MMI2X1Gen
        system6_MMI2X1 = IOE.IOESystem()
        system6_MMI2X1.property_dict['universal']['name'].setValue('system3_MMI2X1_2')

        PIC1 = GS23_3Gen(randomphase=True, new_randomphase=False, cen_wl=GS23_3_cen_wl,
                             DL1=GS23_3_DL1, DL2=GS23_3_DL2, DL3=GS23_3_DL3, DL4=GS23_3_DL4, DL5=GS23_3_DL5,
                             DL6=GS23_3_DL6, DL7=GS23_3_DL7, DL8=GS23_3_DL8, DL9=GS23_3_DL9, DL10=GS23_3_DL10,
                             DL11=GS23_3_DL11, DL12=GS23_3_DL12,
                             DL13=GS23_3_DL13, DL14=GS23_3_DL14, DL15=GS23_3_DL15, DL16=GS23_3_DL16,
                             DL_Decay=GS23_3_DL_Decay,
                             DC21_ratio=GS23_3_DC21_ratio, DC22_ratio=GS23_3_DC22_ratio, DC23_ratio=GS23_3_DC23_ratio,
                             DC20_ratio=GS23_3_DC20_ratio,
                             DC24_ratio=GS23_3_DC24_ratio, DC17_ratio=GS23_3_DC17_ratio, DC18_ratio=GS23_3_DC18_ratio,
                             DC19_ratio=GS23_3_DC19_ratio,
                             DC25_ratio=GS23_3_DC25_ratio, DC26_ratio=GS23_3_DC26_ratio, DC27_ratio=GS23_3_DC27_ratio,
                             DC28_ratio=GS23_3_DC28_ratio,
                             DC29_ratio=GS23_3_DC29_ratio,
                             DC30_ratio=GS23_3_DC30_ratio, DC31_ratio=GS23_3_DC31_ratio, DC32_ratio=GS23_3_DC32_ratio)
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

        system6_MMI2X1.addConnection(system6_MMI2X1.subunit_list[0].optical_port_list[8],
                                         system6_MMI2X1.optical_port_list[0])
        system6_MMI2X1.addConnection(system6_MMI2X1.subunit_list[0].optical_port_list[9],
                                         system6_MMI2X1.optical_port_list[1])
        system6_MMI2X1.addConnection(system6_MMI2X1.subunit_list[0].optical_port_list[10],
                                         system6_MMI2X1.optical_port_list[2])
        system6_MMI2X1.addConnection(system6_MMI2X1.subunit_list[0].optical_port_list[11],
                                         system6_MMI2X1.optical_port_list[3])
        system6_MMI2X1.addConnection(system6_MMI2X1.subunit_list[1].optical_port_list[0],
                                         system6_MMI2X1.optical_port_list[4])

        system6_MMI2X1.checkAllConnected()

        #  PIC
        PIC = system6_MMI2X1
        SimPlatform.addPIC(PIC)

        for i in range(4):
            SimPlatform.addInputPort(port_index=i)
        SimPlatform.addOutputPort(port_index=4)

        SimPlatform.simulationParameters = {'sigfreq': 25e9, 'centerwl': 1.55, 'timestep': 1 / 64, 'modellength': 1280,
                                            'simulationtime': 5000}

        SimPlatform.Run_Freq(save=True)
        # SimPlatform.Visualization_Freq([4], [0])
        # SimPlatform.Visualization_Freq([4], [1])
        # SimPlatform.Visualization_Freq([4], [2])
        # SimPlatform.Visualization_Freq([4], [3])

        w = np.linspace(1.55643326, 1.54361971, 1280)
        data_label = np.loadtxt('D:\\gs_simulaitondata\\system_3\\RING_2.smatrix')  # 理想波形
        portindex = 0
        X = SimPlatform.sdata[portindex, 0, :] + SimPlatform.sdata[portindex, 1, :] + SimPlatform.sdata[portindex, 2,:] + SimPlatform.sdata[portindex, 3, :]
        port0_4in_data = {'wavelength': w, 'data': X}

        # plt.plot(w, abs(port0_4in_data['data']) ** 2, label="train")  # 训练波形
        # plt.plot(w, abs(data_label) ** 2, label="goal")
        # plt.legend()
        # plt.show()
        fitness[number] = np.sum((abs(port0_4in_data['data']) ** 2 - abs(data_label) ** 2)**2)
        print(fitness)
    return fitness




