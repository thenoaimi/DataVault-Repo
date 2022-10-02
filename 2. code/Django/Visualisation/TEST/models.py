# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
class Exp1MetadataSatellite(models.Model):
    level_0 = models.BigIntegerField(blank=True, null=True)
    header = models.TextField(db_column='Header', blank=True, null=True)  # Field name made lowercase.
    file_version = models.TextField(db_column='File Version', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_information = models.TextField(db_column='Patient Information', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    id1 = models.TextField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    age = models.TextField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    sex = models.TextField(db_column='Sex', blank=True, null=True)  # Field name made lowercase.
    analyze_information = models.TextField(db_column='Analyze Information', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    analyzemode = models.TextField(db_column='AnalyzeMode', blank=True, null=True)  # Field name made lowercase.
    pre_time_s_field = models.TextField(db_column='Pre Time[s]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    post_time_s_field = models.TextField(db_column='Post Time[s]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    recovery_time_s_field = models.TextField(db_column='Recovery Time[s]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    base_time_s_field = models.TextField(db_column='Base Time[s]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    fitting_degree = models.TextField(db_column='Fitting Degree', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hpf_hz_field = models.TextField(db_column='HPF[Hz]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lpf_hz_field = models.TextField(db_column='LPF[Hz]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    moving_average_s_field = models.TextField(db_column='Moving Average[s]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    measure_information = models.TextField(db_column='Measure Information', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    mode = models.TextField(db_column='Mode', blank=True, null=True)  # Field name made lowercase.
    wave_nm_field = models.TextField(db_column='Wave[nm]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    wave_length = models.TextField(db_column='Wave Length', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    analog_gain = models.TextField(db_column='Analog Gain', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    digital_gain = models.TextField(db_column='Digital Gain', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sampling_period_s_field = models.TextField(db_column='Sampling Period[s]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    stimtype = models.TextField(db_column='StimType', blank=True, null=True)  # Field name made lowercase.
    stim_time_s_field = models.TextField(db_column='Stim Time[s]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    a = models.TextField(db_column='A', blank=True, null=True)  # Field name made lowercase.
    repeat_count = models.TextField(db_column='Repeat Count', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exception_ch = models.TextField(db_column='Exception Ch', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    time_stamp = models.DateTimeField(blank=True, null=True)
    patient_id = models.BigIntegerField(blank=True, null=True)
    index = models.BigIntegerField(blank=True, null=True)
    experiment_hub_key = models.BigIntegerField(db_column='Experiment_Hub_Key', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Exp1_Metadata_Satellite'


class Exp2MetadataSatellite(models.Model):
    index = models.TextField(blank=True, null=True)
    subject = models.TextField(db_column='Subject', blank=True, null=True)  # Field name made lowercase.
    samplingrate = models.TextField(db_column='SamplingRate', blank=True, null=True)  # Field name made lowercase.
    wavelength_n = models.TextField(db_column='waveLength_N', blank=True, null=True)  # Field name made lowercase.
    wavelengths = models.TextField(db_column='Wavelengths', blank=True, null=True)  # Field name made lowercase.
    source_n = models.TextField(db_column='source_N', blank=True, null=True)  # Field name made lowercase.
    detector_n = models.TextField(db_column='detector_N', blank=True, null=True)  # Field name made lowercase.
    time_point_n = models.TextField(db_column='time_point_N', blank=True, null=True)  # Field name made lowercase.
    source_detector_key = models.TextField(blank=True, null=True)
    source_detector_key_pt2 = models.TextField(db_column='Source_Detector_Key_Pt2', blank=True, null=True)  # Field name made lowercase.
    probeinfo_file = models.TextField(db_column='probeInfo_file', blank=True, null=True)  # Field name made lowercase.
    time_stamp = models.DateTimeField(blank=True, null=True)
    sessiondr_type = models.TextField(db_column='SessionDR_Type', blank=True, null=True)  # Field name made lowercase.
    number_10 = models.TextField(db_column='10', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_11 = models.TextField(db_column='11', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_12 = models.TextField(db_column='12', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_13 = models.TextField(db_column='13', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_14 = models.TextField(db_column='14', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_15 = models.TextField(db_column='15', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_16 = models.TextField(db_column='16', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_17 = models.TextField(db_column='17', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_18 = models.TextField(db_column='18', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_19 = models.TextField(db_column='19', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20 = models.TextField(db_column='20', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_21 = models.TextField(db_column='21', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_22 = models.TextField(db_column='22', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_23 = models.TextField(db_column='23', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_24 = models.TextField(db_column='24', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_25 = models.TextField(db_column='25', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_26 = models.TextField(db_column='26', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_27 = models.TextField(db_column='27', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_28 = models.TextField(db_column='28', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_29 = models.TextField(db_column='29', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_30 = models.TextField(db_column='30', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_31 = models.TextField(db_column='31', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_32 = models.TextField(db_column='32', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_33 = models.TextField(db_column='33', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_34 = models.TextField(db_column='34', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_35 = models.TextField(db_column='35', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_36 = models.TextField(db_column='36', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_37 = models.TextField(db_column='37', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_38 = models.TextField(db_column='38', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_39 = models.TextField(db_column='39', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_40 = models.TextField(db_column='40', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_41 = models.TextField(db_column='41', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_42 = models.TextField(db_column='42', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_43 = models.TextField(db_column='43', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_44 = models.TextField(db_column='44', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_45 = models.TextField(db_column='45', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_46 = models.TextField(db_column='46', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_47 = models.TextField(db_column='47', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_48 = models.TextField(db_column='48', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_49 = models.TextField(db_column='49', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_50 = models.TextField(db_column='50', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_51 = models.TextField(db_column='51', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_52 = models.TextField(db_column='52', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_53 = models.TextField(db_column='53', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_54 = models.TextField(db_column='54', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_55 = models.TextField(db_column='55', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_56 = models.TextField(db_column='56', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_57 = models.TextField(db_column='57', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_58 = models.TextField(db_column='58', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_59 = models.TextField(db_column='59', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_60 = models.TextField(db_column='60', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_61 = models.TextField(db_column='61', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_62 = models.TextField(db_column='62', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_63 = models.TextField(db_column='63', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_64 = models.TextField(db_column='64', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_65 = models.TextField(db_column='65', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_66 = models.TextField(db_column='66', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_67 = models.TextField(db_column='67', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_68 = models.TextField(db_column='68', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_69 = models.TextField(db_column='69', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_70 = models.TextField(db_column='70', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_71 = models.TextField(db_column='71', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_72 = models.TextField(db_column='72', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_73 = models.TextField(db_column='73', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_74 = models.TextField(db_column='74', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_75 = models.TextField(db_column='75', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_76 = models.TextField(db_column='76', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_77 = models.TextField(db_column='77', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_78 = models.TextField(db_column='78', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_79 = models.TextField(db_column='79', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_80 = models.TextField(db_column='80', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_81 = models.TextField(db_column='81', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_82 = models.TextField(db_column='82', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_83 = models.TextField(db_column='83', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_84 = models.TextField(db_column='84', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_85 = models.TextField(db_column='85', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_86 = models.TextField(db_column='86', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_87 = models.TextField(db_column='87', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_88 = models.TextField(db_column='88', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_89 = models.TextField(db_column='89', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_90 = models.TextField(db_column='90', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_91 = models.TextField(db_column='91', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_92 = models.TextField(db_column='92', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_93 = models.TextField(db_column='93', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_94 = models.TextField(db_column='94', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_95 = models.TextField(db_column='95', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_96 = models.TextField(db_column='96', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_97 = models.TextField(db_column='97', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_98 = models.TextField(db_column='98', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_99 = models.TextField(db_column='99', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_100 = models.TextField(db_column='100', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_101 = models.TextField(db_column='101', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_102 = models.TextField(db_column='102', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_103 = models.TextField(db_column='103', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_104 = models.TextField(db_column='104', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_105 = models.TextField(db_column='105', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_106 = models.TextField(db_column='106', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_107 = models.TextField(db_column='107', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_108 = models.TextField(db_column='108', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_109 = models.TextField(db_column='109', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    experiment_hub_key = models.BigIntegerField(db_column='Experiment_Hub_Key', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Exp2_Metadata_Satellite'


class PatientSatellite(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    patient_id = models.TextField(db_column='Patient_ID', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    sex = models.TextField(db_column='SEX', blank=True, null=True)  # Field name made lowercase.
    age = models.TextField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase.
    patient_hub_key = models.BigIntegerField(db_column='Patient_Hub_Key', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Patient_Satellite'


class ProbedataSatellite(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    ch1_698_1_field = models.FloatField(db_column='CH1(698.1)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch1_828_7_field = models.FloatField(db_column='CH1(828.7)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch2_697_1_field = models.FloatField(db_column='CH2(697.1)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch2_828_2_field = models.FloatField(db_column='CH2(828.2)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch3_698_1_field = models.FloatField(db_column='CH3(698.1)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch3_828_7_field = models.FloatField(db_column='CH3(828.7)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch4_698_3_field = models.FloatField(db_column='CH4(698.3)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch4_828_4_field = models.FloatField(db_column='CH4(828.4)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch5_697_1_field = models.FloatField(db_column='CH5(697.1)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch5_828_2_field = models.FloatField(db_column='CH5(828.2)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch6_698_3_field = models.FloatField(db_column='CH6(698.3)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch6_828_4_field = models.FloatField(db_column='CH6(828.4)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch7_698_3_field = models.FloatField(db_column='CH7(698.3)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch7_828_4_field = models.FloatField(db_column='CH7(828.4)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch8_697_5_field = models.FloatField(db_column='CH8(697.5)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch8_828_7_field = models.FloatField(db_column='CH8(828.7)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch9_698_3_field = models.FloatField(db_column='CH9(698.3)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch9_828_4_field = models.FloatField(db_column='CH9(828.4)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch10_697_9_field = models.FloatField(db_column='CH10(697.9)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch10_829_0_field = models.FloatField(db_column='CH10(829.0)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch11_697_5_field = models.FloatField(db_column='CH11(697.5)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch11_828_7_field = models.FloatField(db_column='CH11(828.7)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch12_697_9_field = models.FloatField(db_column='CH12(697.9)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch12_829_0_field = models.FloatField(db_column='CH12(829.0)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch13_698_7_field = models.FloatField(db_column='CH13(698.7)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch13_828_2_field = models.FloatField(db_column='CH13(828.2)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch14_698_2_field = models.FloatField(db_column='CH14(698.2)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch14_827_5_field = models.FloatField(db_column='CH14(827.5)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch15_698_7_field = models.FloatField(db_column='CH15(698.7)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch15_828_2_field = models.FloatField(db_column='CH15(828.2)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch16_697_7_field = models.FloatField(db_column='CH16(697.7)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch16_828_6_field = models.FloatField(db_column='CH16(828.6)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch17_698_2_field = models.FloatField(db_column='CH17(698.2)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch17_827_5_field = models.FloatField(db_column='CH17(827.5)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch18_697_7_field = models.FloatField(db_column='CH18(697.7)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch18_828_6_field = models.FloatField(db_column='CH18(828.6)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch19_697_7_field = models.FloatField(db_column='CH19(697.7)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch19_828_6_field = models.FloatField(db_column='CH19(828.6)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch20_698_4_field = models.FloatField(db_column='CH20(698.4)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch20_828_9_field = models.FloatField(db_column='CH20(828.9)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch21_697_7_field = models.FloatField(db_column='CH21(697.7)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch21_828_6_field = models.FloatField(db_column='CH21(828.6)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch22_697_1_field = models.FloatField(db_column='CH22(697.1)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch22_828_8_field = models.FloatField(db_column='CH22(828.8)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch23_698_4_field = models.FloatField(db_column='CH23(698.4)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch23_828_9_field = models.FloatField(db_column='CH23(828.9)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch24_697_1_field = models.FloatField(db_column='CH24(697.1)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch24_828_8_field = models.FloatField(db_column='CH24(828.8)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    mark = models.BigIntegerField(db_column='Mark', blank=True, null=True)  # Field name made lowercase.
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    bodymovement = models.BigIntegerField(db_column='BodyMovement', blank=True, null=True)  # Field name made lowercase.
    removalmark = models.BigIntegerField(db_column='RemovalMark', blank=True, null=True)  # Field name made lowercase.
    prescan = models.BigIntegerField(db_column='PreScan', blank=True, null=True)  # Field name made lowercase.
    patient_id = models.BigIntegerField(blank=True, null=True)
    time_stamp = models.DateTimeField()
    stimuli_type = models.TextField(db_column='Stimuli_Type', blank=True, null=True)  # Field name made lowercase.
    probedata_hub_key = models.BigIntegerField(db_column='ProbeData_Hub_Key', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProbeData_Satellite'
        unique_together = (('probedata_hub_key', 'time_stamp'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DatasourcesFnirsLink(models.Model):
    datasourcesfnirs_hub_key = models.AutoField(primary_key=True)
    loaddatetime = models.DateTimeField()
    recordsource = models.CharField(max_length=10)
    index = models.BigIntegerField(blank=True, null=True)
    datasources_hub_key = models.ForeignKey('DatasourcesHub', models.DO_NOTHING, db_column='datasources_hub_key', blank=True, null=True)
    fnirs_hub_key = models.ForeignKey('FnirsHub', models.DO_NOTHING, db_column='fnirs_hub_key', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datasources_fnirs_link'


class DatasourcesHub(models.Model):
    datasources_hub_key = models.AutoField(primary_key=True)
    datasources_businesskey = models.CharField(max_length=5, blank=True, null=True)
    loaddatetime = models.DateTimeField(blank=True, null=True)
    recordsource = models.CharField(max_length=10, blank=True, null=True)
    datasource_name = models.CharField(max_length=10, blank=True, null=True)
    index = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datasources_hub'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ExperimentHub(models.Model):
    experiment_hub_key = models.AutoField(primary_key=True)
    experiment_businesskey = models.CharField(max_length=5, blank=True, null=True)
    loaddatetime = models.DateTimeField(blank=True, null=True)
    recordsource = models.CharField(max_length=10, blank=True, null=True)
    experiment_type = models.CharField(max_length=15, blank=True, null=True)
    index = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'experiment_hub'


class ExperimentalSessionSatellite(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    time_stamp = models.DateTimeField(blank=True, null=True)
    sessions_hub_key = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'experimental_session_satellite'


class FnirsDeoxySatellite(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    probe1_deoxy_field = models.BigIntegerField(db_column='Probe1(Deoxy)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch1 = models.FloatField(db_column='CH1', blank=True, null=True)  # Field name made lowercase.
    ch2 = models.FloatField(db_column='CH2', blank=True, null=True)  # Field name made lowercase.
    ch3 = models.FloatField(db_column='CH3', blank=True, null=True)  # Field name made lowercase.
    ch4 = models.FloatField(db_column='CH4', blank=True, null=True)  # Field name made lowercase.
    ch5 = models.FloatField(db_column='CH5', blank=True, null=True)  # Field name made lowercase.
    ch6 = models.FloatField(db_column='CH6', blank=True, null=True)  # Field name made lowercase.
    ch7 = models.FloatField(db_column='CH7', blank=True, null=True)  # Field name made lowercase.
    ch8 = models.FloatField(db_column='CH8', blank=True, null=True)  # Field name made lowercase.
    ch9 = models.FloatField(db_column='CH9', blank=True, null=True)  # Field name made lowercase.
    ch10 = models.FloatField(db_column='CH10', blank=True, null=True)  # Field name made lowercase.
    ch11 = models.FloatField(db_column='CH11', blank=True, null=True)  # Field name made lowercase.
    ch12 = models.FloatField(db_column='CH12', blank=True, null=True)  # Field name made lowercase.
    ch13 = models.FloatField(db_column='CH13', blank=True, null=True)  # Field name made lowercase.
    ch14 = models.FloatField(db_column='CH14', blank=True, null=True)  # Field name made lowercase.
    ch15 = models.FloatField(db_column='CH15', blank=True, null=True)  # Field name made lowercase.
    ch16 = models.FloatField(db_column='CH16', blank=True, null=True)  # Field name made lowercase.
    ch17 = models.FloatField(db_column='CH17', blank=True, null=True)  # Field name made lowercase.
    ch18 = models.FloatField(db_column='CH18', blank=True, null=True)  # Field name made lowercase.
    ch19 = models.FloatField(db_column='CH19', blank=True, null=True)  # Field name made lowercase.
    ch20 = models.FloatField(db_column='CH20', blank=True, null=True)  # Field name made lowercase.
    ch21 = models.FloatField(db_column='CH21', blank=True, null=True)  # Field name made lowercase.
    ch22 = models.FloatField(db_column='CH22', blank=True, null=True)  # Field name made lowercase.
    ch23 = models.FloatField(db_column='CH23', blank=True, null=True)  # Field name made lowercase.
    ch24 = models.FloatField(db_column='CH24', blank=True, null=True)  # Field name made lowercase.
    mark = models.BigIntegerField(db_column='Mark', blank=True, null=True)  # Field name made lowercase.
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    bodymovement = models.FloatField(db_column='BodyMovement', blank=True, null=True)  # Field name made lowercase.
    removalmark = models.FloatField(db_column='RemovalMark', blank=True, null=True)  # Field name made lowercase.
    prescan = models.FloatField(db_column='PreScan', blank=True, null=True)  # Field name made lowercase.
    time_stamp = models.DateTimeField(blank=True, null=True)
    fnirs_type = models.TextField(db_column='fNIRS_type', blank=True, null=True)  # Field name made lowercase.
    patient_id = models.BigIntegerField(db_column='Patient_ID', blank=True, null=True)  # Field name made lowercase.
    fnirs_hub_key = models.BigIntegerField(db_column='fNIRS_Hub_Key', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fNIRS_Deoxy_Satellite'


class FnirsExp2Sess1DatSatellite(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    field_0_0000000_0_0000000_0_0000000_0_0000000_0_0000000_0_00000 = models.TextField(db_column='-0.0000000 -0.0000000 -0.0000000 -0.0000000 -0.0000000 -0.00000', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    patient_identifier = models.BigIntegerField(db_column='Patient identifier', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_field = models.TextField(db_column='\x02', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    time_stamp = models.DateTimeField(db_column='Time stamp', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fnirs_hub_key = models.BigIntegerField(db_column='fNIRS_Hub_Key', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fNIRS_Exp2Sess1Dat_Satellite'


class FnirsExp2Sess2DatSatellite(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    field_0_0000000_0_0000000_0_0000000_0_0000000_0_0000000_0_00000 = models.TextField(db_column='-0.0000000 -0.0000000 -0.0000000 -0.0000000 -0.0000000 -0.00000', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    patient_identifier = models.BigIntegerField(db_column='Patient identifier', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    time_stamp = models.DateTimeField(db_column='Time stamp', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fnirs_hub_key = models.BigIntegerField(db_column='fNIRS_Hub_Key', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fNIRS_Exp2Sess2Dat_Satellite'


class FnirsOxySatellite(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    probe1_oxy_field = models.BigIntegerField(db_column='Probe1(Oxy)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ch1 = models.FloatField(db_column='CH1', blank=True, null=True)  # Field name made lowercase.
    ch2 = models.FloatField(db_column='CH2', blank=True, null=True)  # Field name made lowercase.
    ch3 = models.FloatField(db_column='CH3', blank=True, null=True)  # Field name made lowercase.
    ch4 = models.FloatField(db_column='CH4', blank=True, null=True)  # Field name made lowercase.
    ch5 = models.FloatField(db_column='CH5', blank=True, null=True)  # Field name made lowercase.
    ch6 = models.FloatField(db_column='CH6', blank=True, null=True)  # Field name made lowercase.
    ch7 = models.FloatField(db_column='CH7', blank=True, null=True)  # Field name made lowercase.
    ch8 = models.FloatField(db_column='CH8', blank=True, null=True)  # Field name made lowercase.
    ch9 = models.FloatField(db_column='CH9', blank=True, null=True)  # Field name made lowercase.
    ch10 = models.FloatField(db_column='CH10', blank=True, null=True)  # Field name made lowercase.
    ch11 = models.FloatField(db_column='CH11', blank=True, null=True)  # Field name made lowercase.
    ch12 = models.FloatField(db_column='CH12', blank=True, null=True)  # Field name made lowercase.
    ch13 = models.FloatField(db_column='CH13', blank=True, null=True)  # Field name made lowercase.
    ch14 = models.FloatField(db_column='CH14', blank=True, null=True)  # Field name made lowercase.
    ch15 = models.FloatField(db_column='CH15', blank=True, null=True)  # Field name made lowercase.
    ch16 = models.FloatField(db_column='CH16', blank=True, null=True)  # Field name made lowercase.
    ch17 = models.FloatField(db_column='CH17', blank=True, null=True)  # Field name made lowercase.
    ch18 = models.FloatField(db_column='CH18', blank=True, null=True)  # Field name made lowercase.
    ch19 = models.FloatField(db_column='CH19', blank=True, null=True)  # Field name made lowercase.
    ch20 = models.FloatField(db_column='CH20', blank=True, null=True)  # Field name made lowercase.
    ch21 = models.FloatField(db_column='CH21', blank=True, null=True)  # Field name made lowercase.
    ch22 = models.FloatField(db_column='CH22', blank=True, null=True)  # Field name made lowercase.
    ch23 = models.FloatField(db_column='CH23', blank=True, null=True)  # Field name made lowercase.
    ch24 = models.FloatField(db_column='CH24', blank=True, null=True)  # Field name made lowercase.
    mark = models.BigIntegerField(db_column='Mark', blank=True, null=True)  # Field name made lowercase.
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    bodymovement = models.FloatField(db_column='BodyMovement', blank=True, null=True)  # Field name made lowercase.
    removalmark = models.FloatField(db_column='RemovalMark', blank=True, null=True)  # Field name made lowercase.
    prescan = models.FloatField(db_column='PreScan', blank=True, null=True)  # Field name made lowercase.
    time_stamp = models.DateTimeField(blank=True, null=True)
    fnirs_type = models.TextField(db_column='fNIRS_type', blank=True, null=True)  # Field name made lowercase.
    patient_id = models.BigIntegerField(db_column='Patient_ID', blank=True, null=True)  # Field name made lowercase.
    fnirs_hub_key = models.BigIntegerField(db_column='fNIRS_Hub_Key', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fNIRS_Oxy_Satellite'


class FnirsHub(models.Model):
    fnirs_hub_key = models.AutoField(primary_key=True)
    fnirs_businesskey = models.CharField(max_length=5, blank=True, null=True)
    loaddatetime = models.DateTimeField(blank=True, null=True)
    recordsource = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    index = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fnirs_hub'


class Image(models.Model):
    data = models.BinaryField(blank=True, null=True)
    datatype = models.TextField()  # This field type is a guess.
    sessionid = models.BigIntegerField()
    patientid = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'image'
        unique_together = (('patientid', 'datatype', 'sessionid'),)


class PatientExperimentLink(models.Model):
    patientexperiment_hub_key = models.AutoField(primary_key=True)
    loaddatetime = models.DateTimeField()
    recordsource = models.CharField(max_length=10)
    index = models.BigIntegerField(blank=True, null=True)
    patient_hub_key = models.ForeignKey('PatientHub', models.DO_NOTHING, db_column='patient_hub_key', blank=True, null=True)
    experiment_hub_key = models.ForeignKey(ExperimentHub, models.DO_NOTHING, db_column='experiment_hub_key', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_experiment_link'


class PatientHub(models.Model):
    patient_hub_key = models.AutoField(primary_key=True)
    patient_businesskey = models.CharField(max_length=5, blank=True, null=True)
    loaddatetime = models.DateTimeField(blank=True, null=True)
    recordsource = models.CharField(max_length=10, blank=True, null=True)
    index = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_hub'


class PatientdataSourcesLink(models.Model):
    patientdatasources_hub_key = models.AutoField(primary_key=True)
    loaddatetime = models.DateTimeField()
    recordsource = models.CharField(max_length=10)
    index = models.BigIntegerField(blank=True, null=True)
    patient_hub_key = models.ForeignKey(PatientHub, models.DO_NOTHING, db_column='patient_hub_key', blank=True, null=True)
    datasources_hub_key = models.ForeignKey(DatasourcesHub, models.DO_NOTHING, db_column='datasources_hub_key', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patientdata_sources_link'


class ProbedataExperimentLink(models.Model):
    probedataexperiment_hub_key = models.AutoField(primary_key=True)
    loaddatetime = models.DateTimeField()
    recordsource = models.CharField(max_length=10)
    index = models.BigIntegerField(blank=True, null=True)
    experiment_hub_key = models.ForeignKey(ExperimentHub, models.DO_NOTHING, db_column='experiment_hub_key', blank=True, null=True)
    probedata_hub_key = models.ForeignKey('ProbedataHub', models.DO_NOTHING, db_column='probedata_hub_key', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'probedata_experiment_link'


class ProbedataHub(models.Model):
    probedata_hub_key = models.AutoField(primary_key=True)
    probedata_businesskey = models.CharField(max_length=5, blank=True, null=True)
    loaddatetime = models.DateTimeField(blank=True, null=True)
    recordsource = models.CharField(max_length=10, blank=True, null=True)
    index = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'probedata_hub'


class ProbedataSessionsLink(models.Model):
    probedatasession_hub_key = models.AutoField(primary_key=True)
    loaddatetime = models.DateTimeField()
    recordsource = models.CharField(max_length=10)
    index = models.BigIntegerField(blank=True, null=True)
    sessions_hub_key = models.ForeignKey('SessionsHub', models.DO_NOTHING, db_column='sessions_hub_key', blank=True, null=True)
    probedata_hub_key = models.ForeignKey(ProbedataHub, models.DO_NOTHING, db_column='probedata_hub_key', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'probedata_sessions_link'


class SessionsDatasourcesLink(models.Model):
    sessiondatasources_hub_key = models.AutoField(primary_key=True)
    loaddatetime = models.DateTimeField()
    recordsource = models.CharField(max_length=10)
    index = models.BigIntegerField(blank=True, null=True)
    sessions_hub_key = models.ForeignKey('SessionsHub', models.DO_NOTHING, db_column='sessions_hub_key', blank=True, null=True)
    datasources_hub_key = models.ForeignKey(DatasourcesHub, models.DO_NOTHING, db_column='datasources_hub_key', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sessions_datasources_link'


class SessionsHub(models.Model):
    sessions_hub_key = models.AutoField(primary_key=True)
    sessions_businesskey = models.CharField(max_length=5, blank=True, null=True)
    loaddatetime = models.DateTimeField(blank=True, null=True)
    recordsource = models.CharField(max_length=10, blank=True, null=True)
    index = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sessions_hub'
