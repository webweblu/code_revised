from ioesim import all as IOE
from ioedev import all as DEV
import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt

def combiner_MMI2X1_3Gen(randomphase=True, new_randomphase=True,
                         DL=4898,
                         # DL0=4898,DL1=4898,DL2=4898,DL3=4898,DL4=4898,DL5=4898,DL6=4898,DL7=4898,
                         # DL9=4898,DL10=4898,
                         # DL11=4898,DL12=4898,DL13=4898,DL14=4898,DL15=4898,DL16=4898,
                         WG=100, MMI2X1_loss=0.3, MMI2X1_imbalance=0,
                         MMI2X1_reflection=20, weight7=1, phase7=0, weight8=1, phase8=0, weight9=1, phase9=0,
                         weight10=1, phase10=0, weight11=1, phase11=0, weight12=1, phase12=0,weight13=1, phase13=0,
                         weight14=1, phase14=0):
                         # weight16=1, phase16=0, weight25=1, phase25=0, weight26=1, phase26=0,
                         # weight27=1, phase27=0, weight28=1, phase28=0, weight29=1, phase29=0, weight30=1, phase30=0,
                         # weight31=1, phase31=0):
    ############## Set Parameters #######################
    if randomphase:
        if new_randomphase:
            randomphase_combiner_MMI2X1 = np.zeros(100, dtype=complex)
            for i in range(100):
                randomphase_combiner_MMI2X1[i] = np.exp(1j * 2 * np.pi * np.random.rand(1))
            filename_random = 'D:\\gs_simulaitondata\\system_3\\randomphase_combiner_MMI2X1_.mat'
            sio.savemat(filename_random, {'data': randomphase_combiner_MMI2X1})
        else:
            filename_random = 'D:\\gs_simulaitondata\\system_3\\randomphase_combiner_MMI2X1_.mat'
            randomdata_combiner_MMI2X1 = sio.loadmat(filename_random)
            randomphase_combiner_MMI2X1 = randomdata_combiner_MMI2X1['data'][0]
    else:
        randomphase_combiner_MMI2X1 = np.ones(100, dtype=complex)

    ########### initialize the system
    combiner_MMI2X1 = IOE.IOESystem()
    combiner_MMI2X1.property_dict['universal']['name'].setValue('comniner_MMI2X1')


    ##### Add devices
    # grating coupler
    # combiner_MMI2X1.addUnit(DEV.GCTE1550())
    # combiner_MMI2X1.subunit_list[0].property_dict['universal']['name'].setValue('GC_' + str(0))
    #
    # combiner_MMI2X1.addOpticalPort()
    # combiner_MMI2X1.optical_port_list[0].property_dict['universal']['name'].setValue('Out_port_0')
    #
    # combiner_MMI2X1.addOCbyName('GC_0', 2, 'Out_port_0')

    #add MMI2X1
    for i in range(0,7):
        combiner_MMI2X1.addUnit(DEV.MMI2X1())
        combiner_MMI2X1.subunit_list[i].property_dict['universal']['name'].setValue('MMI2X1_'+str(i))
        combiner_MMI2X1.subunit_list[i].property_dict['standard']['loss_dB'].setValue(MMI2X1_loss)
        combiner_MMI2X1.subunit_list[i].property_dict['standard']['imbalance_dB'].setValue(MMI2X1_imbalance)
        combiner_MMI2X1.subunit_list[i].property_dict['standard']['reflection_dB'].setValue(MMI2X1_reflection)

    # add modulator_ideal
    for i in range(7, 15):
        combiner_MMI2X1.addUnit(DEV.modulator_ideal())
        combiner_MMI2X1.subunit_list[i].property_dict['universal']['name'].setValue('modulator_ideal_' + str(i))
    combiner_MMI2X1.subunit_list[7].property_dict['standard']['weight'].setValue(weight7)
    combiner_MMI2X1.subunit_list[7].property_dict['standard']['phase'].setValue(phase7)

    combiner_MMI2X1.subunit_list[8].property_dict['standard']['weight'].setValue(weight8)
    combiner_MMI2X1.subunit_list[8].property_dict['standard']['phase'].setValue(phase8)

    combiner_MMI2X1.subunit_list[9].property_dict['standard']['weight'].setValue(weight9)
    combiner_MMI2X1.subunit_list[9].property_dict['standard']['phase'].setValue(phase9)

    combiner_MMI2X1.subunit_list[10].property_dict['standard']['weight'].setValue(weight10)
    combiner_MMI2X1.subunit_list[10].property_dict['standard']['phase'].setValue(phase10)

    combiner_MMI2X1.subunit_list[11].property_dict['standard']['weight'].setValue(weight11)
    combiner_MMI2X1.subunit_list[11].property_dict['standard']['phase'].setValue(phase11)

    combiner_MMI2X1.subunit_list[12].property_dict['standard']['weight'].setValue(weight12)
    combiner_MMI2X1.subunit_list[12].property_dict['standard']['phase'].setValue(phase12)

    combiner_MMI2X1.subunit_list[13].property_dict['standard']['weight'].setValue(weight13)
    combiner_MMI2X1.subunit_list[13].property_dict['standard']['phase'].setValue(phase13)

    combiner_MMI2X1.subunit_list[14].property_dict['standard']['weight'].setValue(weight14)
    combiner_MMI2X1.subunit_list[14].property_dict['standard']['phase'].setValue(phase14)

    # combiner_MMI2X1.subunit_list[24].property_dict['standard']['weight'].setValue(weight24)
    # combiner_MMI2X1.subunit_list[24].property_dict['standard']['phase'].setValue(phase24)
    # combiner_MMI2X1.subunit_list[25].property_dict['standard']['weight'].setValue(weight25)
    # combiner_MMI2X1.subunit_list[25].property_dict['standard']['phase'].setValue(phase25)
    # combiner_MMI2X1.subunit_list[26].property_dict['standard']['weight'].setValue(weight26)
    # combiner_MMI2X1.subunit_list[26].property_dict['standard']['phase'].setValue(phase26)
    # combiner_MMI2X1.subunit_list[27].property_dict['standard']['weight'].setValue(weight27)
    # combiner_MMI2X1.subunit_list[27].property_dict['standard']['phase'].setValue(phase27)
    # combiner_MMI2X1.subunit_list[28].property_dict['standard']['weight'].setValue(weight28)
    # combiner_MMI2X1.subunit_list[28].property_dict['standard']['phase'].setValue(phase28)
    # combiner_MMI2X1.subunit_list[29].property_dict['standard']['weight'].setValue(weight29)
    # combiner_MMI2X1.subunit_list[29].property_dict['standard']['phase'].setValue(phase29)
    # combiner_MMI2X1.subunit_list[30].property_dict['standard']['weight'].setValue(weight30)
    # combiner_MMI2X1.subunit_list[30].property_dict['standard']['phase'].setValue(phase30)
    # combiner_MMI2X1.subunit_list[31].property_dict['standard']['weight'].setValue(weight31)
    # combiner_MMI2X1.subunit_list[31].property_dict['standard']['phase'].setValue(phase31)

    # add delayline
    for i in range(15,23):
        combiner_MMI2X1.addUnit(DEV.WG())
        combiner_MMI2X1.subunit_list[i].property_dict['universal']['name'].setValue('WGDL_'+str(i))
        combiner_MMI2X1.subunit_list[i].property_dict['standard']['length'].setValue(DL)
        # combiner_MMI2X1.subunit_list[i].property_dict['standard']['length'].setValue(DL0)
        # combiner_MMI2X1.subunit_list[i].property_dict['standard']['length'].setValue(DL1)
        # combiner_MMI2X1.subunit_list[i].property_dict['standard']['length'].setValue(DL2)
        # combiner_MMI2X1.subunit_list[i].property_dict['standard']['length'].setValue(DL3)
        # combiner_MMI2X1.subunit_list[i].property_dict['standard']['length'].setValue(DL4)
        # combiner_MMI2X1.subunit_list[i].property_dict['standard']['length'].setValue(DL5)
        # combiner_MMI2X1.subunit_list[i].property_dict['standard']['length'].setValue(DL6)
        # combiner_MMI2X1.subunit_list[i].property_dict['standard']['length'].setValue(DL7)
        # combiner_MMI2X1.subunit_list[i].property_dict['standard']['decay'].setValue(0)
        # combiner_MMI2X1.subunit_list[i].property_dict['standard']['length'].setValue(DL9)
        # combiner_MMI2X1.subunit_list[i].property_dict['standard']['length'].setValue(DL10)
        # combiner_MMI2X1.subunit_list[i].property_dict['standard']['length'].setValue(DL11)
        # combiner_MMI2X1.subunit_list[i].property_dict['standard']['length'].setValue(DL12)
        # combiner_MMI2X1.subunit_list[i].property_dict['standard']['length'].setValue(DL13)
        # combiner_MMI2X1.subunit_list[i].property_dict['standard']['length'].setValue(DL14)
        # combiner_MMI2X1.subunit_list[i].property_dict['standard']['length'].setValue(DL15)
        # combiner_MMI2X1.subunit_list[i].property_dict['standard']['length'].setValue(DL16)

        combiner_MMI2X1.subunit_list[i].property_dict['standard']['random_phase'].setValue(randomphase_combiner_MMI2X1[i - 16])

    # add waveguide
    for i in range(23, 31):
        combiner_MMI2X1.addUnit(DEV.WG())
        combiner_MMI2X1.subunit_list[i].property_dict['universal']['name'].setValue('WG_' + str(i))
        combiner_MMI2X1.subunit_list[i].property_dict['standard']['length'].setValue(WG)
        combiner_MMI2X1.subunit_list[i].property_dict['standard']['decay'].setValue(0)


    #add Terminator
    # for i in range(32,33):
    #     combiner_MMI2X1.addUnit(DEV.term())
    #     combiner_MMI2X1.subunit_list[i].property_dict['universal']['name'].setValue('Term_' + str(i))

    ##### Add output optical ports
    combiner_MMI2X1.addOpticalPort()
    combiner_MMI2X1.optical_port_list[0].property_dict['universal']['name'].setValue('Out_port_0')
    for i in range(1, 9):
        combiner_MMI2X1.addOpticalPort()
        combiner_MMI2X1.optical_port_list[i].property_dict['universal']['name'].setValue('In_port_' + str(i))


    ##### Add connections
    combiner_MMI2X1.addOCbyName('MMI2X1_0', 2, 'Out_port_0')

    combiner_MMI2X1.addOCbyName('MMI2X1_0', 1, 'MMI2X1_1', 2)
    combiner_MMI2X1.addOCbyName('MMI2X1_0', 3, 'MMI2X1_2', 2)

    combiner_MMI2X1.addOCbyName('MMI2X1_1', 1, 'MMI2X1_3', 2)
    combiner_MMI2X1.addOCbyName('MMI2X1_1', 3, 'MMI2X1_4', 2)

    combiner_MMI2X1.addOCbyName('MMI2X1_2', 1, 'MMI2X1_5', 2)
    combiner_MMI2X1.addOCbyName('MMI2X1_2', 3, 'MMI2X1_6', 2)
    #
    # combiner_MMI2X1.addOCbyName('MMI2X1_4', 1, 'MMI2X1_8', 2)
    # combiner_MMI2X1.addOCbyName('MMI2X1_4', 3, 'MMI2X1_9', 2)
    #
    # combiner_MMI2X1.addOCbyName('MMI2X1_5', 1, 'MMI2X1_10', 2)
    # combiner_MMI2X1.addOCbyName('MMI2X1_5', 3, 'MMI2X1_11', 2)
    #
    # combiner_MMI2X1.addOCbyName('MMI2X1_6', 1, 'MMI2X1_12', 2)
    # combiner_MMI2X1.addOCbyName('MMI2X1_6', 3, 'MMI2X1_13', 2)
    #
    # combiner_MMI2X1.addOCbyName('MMI2X1_7', 1, 'MMI2X1_14', 2)
    # combiner_MMI2X1.addOCbyName('MMI2X1_7', 3, 'MMI2X1_15', 2)

    combiner_MMI2X1.addOCbyName('MMI2X1_3', 1, 'modulator_ideal_7', 1)
    combiner_MMI2X1.addOCbyName('MMI2X1_3', 3, 'modulator_ideal_8', 1)

    combiner_MMI2X1.addOCbyName('MMI2X1_4', 1, 'modulator_ideal_9', 1)
    combiner_MMI2X1.addOCbyName('MMI2X1_4', 3, 'modulator_ideal_10', 1)

    combiner_MMI2X1.addOCbyName('MMI2X1_5', 1, 'modulator_ideal_11', 1)
    combiner_MMI2X1.addOCbyName('MMI2X1_5', 3, 'modulator_ideal_12', 1)

    combiner_MMI2X1.addOCbyName('MMI2X1_6', 1, 'modulator_ideal_13', 1)
    combiner_MMI2X1.addOCbyName('MMI2X1_6', 3, 'modulator_ideal_14', 1)

    # combiner_MMI2X1.addOCbyName('MMI2X1_12', 1, 'modulator_ideal_24', 1)
    # combiner_MMI2X1.addOCbyName('MMI2X1_12', 3, 'modulator_ideal_25', 1)
    #
    # combiner_MMI2X1.addOCbyName('MMI2X1_13', 1, 'modulator_ideal_26', 1)
    # combiner_MMI2X1.addOCbyName('MMI2X1_13', 3, 'modulator_ideal_27', 1)
    #
    # combiner_MMI2X1.addOCbyName('MMI2X1_14', 1, 'modulator_ideal_28', 1)
    # combiner_MMI2X1.addOCbyName('MMI2X1_14', 3, 'modulator_ideal_29', 1)
    #
    # combiner_MMI2X1.addOCbyName('MMI2X1_15', 1, 'modulator_ideal_30', 1)
    # combiner_MMI2X1.addOCbyName('MMI2X1_15', 3, 'modulator_ideal_31', 1)

    combiner_MMI2X1.addOCbyName('modulator_ideal_7', 2, 'WGDL_15', 1)
    combiner_MMI2X1.addOCbyName('modulator_ideal_8', 2, 'WGDL_16', 1)
    combiner_MMI2X1.addOCbyName('modulator_ideal_9', 2, 'WGDL_17', 1)
    combiner_MMI2X1.addOCbyName('modulator_ideal_10', 2, 'WGDL_18', 1)
    combiner_MMI2X1.addOCbyName('modulator_ideal_11', 2, 'WGDL_19', 1)
    combiner_MMI2X1.addOCbyName('modulator_ideal_12', 2, 'WGDL_20', 1)
    combiner_MMI2X1.addOCbyName('modulator_ideal_13', 2, 'WGDL_21', 1)
    combiner_MMI2X1.addOCbyName('modulator_ideal_14', 2, 'WGDL_22', 1)
    # combiner_MMI2X1.addOCbyName('modulator_ideal_24', 2, 'WGDL_40', 1)
    # combiner_MMI2X1.addOCbyName('modulator_ideal_25', 2, 'WGDL_41', 1)
    # combiner_MMI2X1.addOCbyName('modulator_ideal_26', 2, 'WGDL_42', 1)
    # combiner_MMI2X1.addOCbyName('modulator_ideal_27', 2, 'WGDL_43', 1)
    # combiner_MMI2X1.addOCbyName('modulator_ideal_28', 2, 'WGDL_44', 1)
    # combiner_MMI2X1.addOCbyName('modulator_ideal_29', 2, 'WGDL_45', 1)
    # combiner_MMI2X1.addOCbyName('modulator_ideal_30', 2, 'WGDL_46', 1)
    # combiner_MMI2X1.addOCbyName('modulator_ideal_31', 2, 'WGDL_47', 1)

    combiner_MMI2X1.addOCbyName('WGDL_15', 2, 'WG_23', 1)
    combiner_MMI2X1.addOCbyName('WGDL_16', 2, 'WG_24', 1)
    combiner_MMI2X1.addOCbyName('WGDL_17', 2, 'WG_25', 1)
    combiner_MMI2X1.addOCbyName('WGDL_18', 2, 'WG_26', 1)
    combiner_MMI2X1.addOCbyName('WGDL_19', 2, 'WG_27', 1)
    combiner_MMI2X1.addOCbyName('WGDL_20', 2, 'WG_28', 1)
    combiner_MMI2X1.addOCbyName('WGDL_21', 2, 'WG_29', 1)
    combiner_MMI2X1.addOCbyName('WGDL_22', 2, 'WG_30', 1)
    # combiner_MMI2X1.addOCbyName('WGDL_40', 2, 'WG_56', 1)
    # combiner_MMI2X1.addOCbyName('WGDL_41', 2, 'WG_57', 1)
    # combiner_MMI2X1.addOCbyName('WGDL_42', 2, 'WG_58', 1)
    # combiner_MMI2X1.addOCbyName('WGDL_43', 2, 'WG_59', 1)
    # combiner_MMI2X1.addOCbyName('WGDL_44', 2, 'WG_60', 1)
    # combiner_MMI2X1.addOCbyName('WGDL_45', 2, 'WG_61', 1)
    # combiner_MMI2X1.addOCbyName('WGDL_46', 2, 'WG_62', 1)
    # combiner_MMI2X1.addOCbyName('WGDL_47', 2, 'WG_63', 1)

    combiner_MMI2X1.addOCbyName('WG_23', 2, 'In_port_1')
    combiner_MMI2X1.addOCbyName('WG_24', 2, 'In_port_2')
    combiner_MMI2X1.addOCbyName('WG_25', 2, 'In_port_3')
    combiner_MMI2X1.addOCbyName('WG_26', 2, 'In_port_4')
    combiner_MMI2X1.addOCbyName('WG_27', 2, 'In_port_5')
    combiner_MMI2X1.addOCbyName('WG_28', 2, 'In_port_6')
    combiner_MMI2X1.addOCbyName('WG_29', 2, 'In_port_7')
    combiner_MMI2X1.addOCbyName('WG_30', 2, 'In_port_8')
    # combiner_MMI2X1.addOCbyName('WG_56', 2, 'In_port_9')
    # combiner_MMI2X1.addOCbyName('WG_57', 2, 'In_port_10')
    # combiner_MMI2X1.addOCbyName('WG_58', 2, 'In_port_11')
    # combiner_MMI2X1.addOCbyName('WG_59', 2, 'In_port_12')
    # combiner_MMI2X1.addOCbyName('WG_60', 2, 'Term_64', 0)
    # combiner_MMI2X1.addOCbyName('WG_61', 2, 'Term_65', 0)
    # combiner_MMI2X1.addOCbyName('WG_62', 2, 'Term_66', 0)
    # combiner_MMI2X1.addOCbyName('WG_63', 2, 'Term_67', 0)

    combiner_MMI2X1.checkAllConnected()

    return combiner_MMI2X1

if __name__ == '__main__':
    ################## Svae the scattering matrices data ###################
    ##### gloable properties

    combiner_MMI2X1_DL = 490
    # combiner_MMI2X1_DL0 = 4898# Delay line length in um
    # combiner_MMI2X1_DL1 = 4898
    # combiner_MMI2X1_DL2 = 4898
    # combiner_MMI2X1_DL3 = 4898
    # combiner_MMI2X1_DL4 = 4898
    # combiner_MMI2X1_DL5 = 4898
    # combiner_MMI2X1_DL6 = 4898
    # combiner_MMI2X1_DL7 = 4898

    combiner_MMI2X1_WG = 490
    combiner_MMI2X1_loss = 0.3
    combiner_MMI2X1_imbalance = 0
    combiner_MMI2X1_reflection = 20

    combiner_MMI2X1_modulator_ideal7_weight = 1  # weight of modulator
    combiner_MMI2X1_modulator_ideal7_phase = 0  # phase of modulator

    combiner_MMI2X1_modulator_ideal8_weight = 1
    combiner_MMI2X1_modulator_ideal8_phase = 0

    combiner_MMI2X1_modulator_ideal9_weight = 1
    combiner_MMI2X1_modulator_ideal9_phase = 0

    combiner_MMI2X1_modulator_ideal10_weight = 1
    combiner_MMI2X1_modulator_ideal10_phase = 0

    combiner_MMI2X1_modulator_ideal11_weight = 1
    combiner_MMI2X1_modulator_ideal11_phase = 0

    combiner_MMI2X1_modulator_ideal12_weight = 1
    combiner_MMI2X1_modulator_ideal12_phase = 0

    combiner_MMI2X1_modulator_ideal13_weight = 1
    combiner_MMI2X1_modulator_ideal13_phase = 0

    combiner_MMI2X1_modulator_ideal14_weight = 1
    combiner_MMI2X1_modulator_ideal14_phase = 0

    # combiner_MMI2X1_modulator_ideal24_weight = 1
    # combiner_MMI2X1_modulator_ideal24_phase = 0
    # combiner_MMI2X1_modulator_ideal25_weight = 1
    # combiner_MMI2X1_modulator_ideal25_phase = 0
    # combiner_MMI2X1_modulator_ideal26_weight = 1
    # combiner_MMI2X1_modulator_ideal26_phase = 0
    # combiner_MMI2X1_modulator_ideal27_weight = 1
    # combiner_MMI2X1_modulator_ideal27_phase = 0
    # combiner_MMI2X1_modulator_ideal28_weight = 1
    # combiner_MMI2X1_modulator_ideal28_phase = 0
    # combiner_MMI2X1_modulator_ideal29_weight = 1
    # combiner_MMI2X1_modulator_ideal29_phase = 0
    # combiner_MMI2X1_modulator_ideal30_weight = 1
    # combiner_MMI2X1_modulator_ideal30_phase = 0
    # combiner_MMI2X1_modulator_ideal31_weight = 1
    # combiner_MMI2X1_modulator_ideal31_phase = 0

    SimPlatform = IOE.SimulationPlatform()
    SimPlatform.FolderPath = 'D:\\gs_simulaitondata\\system_3\\'
    SimPlatform.name = 'combiner_MMI2X1_3'
    SimPlatform.simulationParameters = {'sigfreq': 25e9, 'centerwl': 1.55, 'timestep': 1 / 16, 'modellength': 1280,
                                        'simulationtime': 5000}

    PIC = combiner_MMI2X1_3Gen(randomphase=False, new_randomphase=False,
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
                               phase14=combiner_MMI2X1_modulator_ideal14_phase,)
                               # weight24=combiner_MMI2X1_modulator_ideal24_weight,
                               # phase24=combiner_MMI2X1_modulator_ideal24_phase,
                               # weight25=combiner_MMI2X1_modulator_ideal25_weight,
                               # phase25=combiner_MMI2X1_modulator_ideal25_phase,
                               # weight26=combiner_MMI2X1_modulator_ideal26_weight,
                               # phase26=combiner_MMI2X1_modulator_ideal26_phase,
                               # weight27=combiner_MMI2X1_modulator_ideal27_weight,
                               # phase27=combiner_MMI2X1_modulator_ideal27_phase,
                               # weight28=combiner_MMI2X1_modulator_ideal28_weight,
                               # phase28=combiner_MMI2X1_modulator_ideal28_phase,
                               # weight29=combiner_MMI2X1_modulator_ideal29_weight,
                               # phase29=combiner_MMI2X1_modulator_ideal29_phase,
                               # weight30=combiner_MMI2X1_modulator_ideal30_weight,
                               # phase30=combiner_MMI2X1_modulator_ideal30_phase,
                               # weight31=combiner_MMI2X1_modulator_ideal31_weight,
                               # phase31=combiner_MMI2X1_modulator_ideal31_phase)
    SimPlatform.addPIC(PIC)

    SimPlatform.addOutputPort(port_index=0)
    for i in range(1, 9):
        SimPlatform.addInputPort(port_index=i)



    SimPlatform.Run_Freq(save=True)
    SimPlatform.Visualization_Freq([0], [1,2,3,4])


    # X = SimPlatform.sdata[0,0,:] + SimPlatform.sdata[0,1,:] + SimPlatform.sdata[0,2,:]+SimPlatform.sdata[0,3,:]+SimPlatform.sdata[0,4,:]\
    #         +SimPlatform.sdata[0,5,:]+SimPlatform.sdata[0,6,:]+SimPlatform.sdata[0,7,:]+SimPlatform.sdata[0,8,:]+SimPlatform.sdata[0,9,:]\
    #     +SimPlatform.sdata[0, 10, :]+SimPlatform.sdata[0,11,:]
    # port_12in_data = {'wavelength': (SimPlatform.PIC.smatrix['wavelength']), 'data': X}
    #
    # plt.rcParams["xtick.direction"] = 'in'
    # plt.rcParams["ytick.direction"] = 'in'
    # plt.plot(port_12in_data['wavelength'], abs(port_12in_data['data']))
    #     # plt.plot(port_4in_data['wavelength'], np.angle(port_4in_data['data'][i, :]))
    # plt.xlabel("wavelength/um")
    # plt.ylabel("transmission/dB")
    # plt.show()
    # filename2 = SimPlatform.FolderPath + SimPlatform.name + '_port_12in_data.mat'
    # sio.savemat(filename2, port_12in_data)
    #########################################################################




























