import psycopg2
import os
import numpy as np
import mne
import warnings
warnings.filterwarnings(action="ignore")
basepath1='D:/Google Drive/University/Masters/Course/Semester 1/Data/Group Project/Data/fNIRS-Data/1raSessionDR'
basepath2='D:/Google Drive/University/Masters/Course/Semester 1/Data/Group Project/Data/fNIRS-Data/2daSessionDR'
con = psycopg2.connect("host=localhost dbname=SMD_SP_G14 user=postgres password=2831997 port=5433 ")
cur = con.cursor()
def readImage(name):
    fin = open(name, "rb")
    img = fin.read()
    return img
def imagedatabase(patient_id,datatype,session_id,name):
    data = readImage(name)
    binary = psycopg2.Binary(data)
    cur.execute("INSERT INTO image(patientid,datatype,data,sessionid) VALUES (%s,%s,%s,%s)", (patient_id,datatype,binary,session_id) )
    con.commit()
def datapath1():
    asd = os.listdir(basepath1)
    asd.remove('desktop.ini')
    finalresult=[]
    for i in range(len(asd)):
        filename=os.path.join(basepath1,asd[i])
        finalresult.append(filename)
    return(finalresult)
def datapath2():
    asd = os.listdir(basepath2)
    asd.remove('NIRS-2019-10-10_005.nirs')
    asd.remove('desktop.ini')
    finalresult=[]
    for i in range(len(asd)):
        filename=os.path.join(basepath2,asd[i])
        finalresult.append(filename)
    return(finalresult)
def createpicture(function,sessionid):
    a=11
    for fname in function():
        raw_intensity = mne.io.read_raw_nirx(fname)
        raw_intensity.load_data()
        raw_intensity.annotations.set_durations(5)
        unwanted = np.nonzero(raw_intensity.annotations.description == '15.0')
        raw_intensity.annotations.delete(unwanted)
        picks = mne.pick_types(raw_intensity.info, meg=False, fnirs=True)
        dists = mne.preprocessing.nirs.source_detector_distances(
            raw_intensity.info, picks=picks)
        raw_intensity.pick(picks[dists > 0.01])
        plot1 = raw_intensity.plot(n_channels=len(raw_intensity.ch_names), duration=500, show_scrollbars=False,
                                   show=False, block=False)
        name = "patient{b}_session1_selectingchannels".format(b=a)
        plot1.savefig(name)
        name = name + '.png'
        imagedatabase(a, "channels", sessionid, name)

        raw_od = mne.preprocessing.nirs.optical_density(raw_intensity)
        plot1 = raw_od.plot(n_channels=len(raw_od.ch_names), duration=500, show_scrollbars=False, block=False,show=False)
        name = "patient{b}_session1_optimaldensity".format(b=a)
        plot1.savefig(name)
        name = name + '.png'
        imagedatabase(a, "optimaldensity", sessionid, name)

        raw_od = mne.preprocessing.nirs.optical_density(raw_intensity)
        sci = mne.preprocessing.nirs.scalp_coupling_index(raw_od)
        raw_haemo = mne.preprocessing.nirs.beer_lambert_law(raw_od, ppf=0.1)
        plot1 = raw_haemo.plot(n_channels=len(raw_haemo.ch_names),
                               duration=500, show_scrollbars=False, block=False, show=False)
        name = "patient{b}_session1_raw_haemo".format(b=a)
        plot1.savefig(name)
        name = name + '.png'
        imagedatabase(a, "raw_haemo", sessionid, name)
        raw_haemo = raw_haemo.filter(0.05, 0.7, h_trans_bandwidth=0.2,
                                     l_trans_bandwidth=0.02)
        fig = raw_haemo.plot_psd(average=True, show=False)
        fig.suptitle('After filtering', weight='bold', size='x-large')
        fig.subplots_adjust(top=0.88)
        plot1 = fig
        name = "patient{b}_session1_filtering".format(b=a)
        plot1.savefig(name)
        name = name + '.png'
        imagedatabase(a, "filtering", sessionid, name)
        try:

            events, event_dict = mne.events_from_annotations(raw_haemo)
            reject_criteria = dict(hbo=80e-6)
            tmin, tmax = -5, 15
            epochs = mne.Epochs(raw_haemo, events, event_id=event_dict,
                                tmin=tmin, tmax=tmax,
                                reject=reject_criteria, reject_by_annotation=True,
                                proj=True, baseline=(None, 0), preload=True,
                                detrend=None, verbose=True)
            evoked_dict = {'Tapping/HbO': epochs['2.0'].average(picks='hbo'),
                           'Tapping/HbR': epochs['2.0'].average(picks='hbr')}
            # Rename channels until the encoding of frequency in ch_name is fixed
            for condition in evoked_dict:
                evoked_dict[condition].rename_channels(lambda x: x[:-4])
            color_dict = dict(HbO='#AA3377', HbR='b')
            c = mne.viz.plot_compare_evokeds(evoked_dict, combine="mean", ci=0.95, colors=color_dict, show=False
                                             )
            name = "patient{b}_session1_responseimage".format(b=a)
            plot1 = c[0]
            plot1.savefig(name)
            name = name + '.png'
            imagedatabase(a, "responseimage", sessionid, name)
        except:
            try:
                events, event_dict = mne.events_from_annotations(raw_haemo)
                reject_criteria = dict(hbo=80e-6)
                tmin, tmax = -5, 15
                epochs = mne.Epochs(raw_haemo, events, event_id=event_dict,
                                    tmin=tmin, tmax=tmax,
                                    reject_by_annotation=True,
                                    proj=True, baseline=(None, 0), preload=True,
                                    detrend=None, verbose=True)
                evoked_dict = {'Tapping/HbO': epochs['2.0'].average(picks='hbo'),
                               'Tapping/HbR': epochs['2.0'].average(picks='hbr')}
                # Rename channels until the encoding of frequency in ch_name is fixed
                for condition in evoked_dict:
                    evoked_dict[condition].rename_channels(lambda x: x[:-4])
                color_dict = dict(HbO='#AA3377', HbR='b')
                mne.viz.plot_compare_evokeds(evoked_dict, combine="mean", ci=0.95,
                                             colors=color_dict, show=False)
                name = "patient{b}_session1_responseimage".format(b=a)
                plot1 = c[0]
                plot1.savefig(name)
                name = name + '.png'
                imagedatabase(a, "responseimage", sessionid, name)
            except:
                a = a + 1
                continue
        a = a + 1
# createpicture(datapath1,1)
# createpicture(datapath2,2)
