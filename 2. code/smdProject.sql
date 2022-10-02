
-- 1: Creating the Database DataVault2
CREATE DATABASE SMD_SP_G14;

-- 2: Connecting to the Database DataVault2
\connect SMD_SP_G14

-- 3) Creating the Hubs - please copy and paste all hubs in pgAdmin and run
CREATE TABLE Patient_Hub (
    Patient_Hub_Key serial, 
    Patient_BusinessKey varchar(5),   
    LoadDateTime TIMESTAMP,  
    RecordSource varchar(10),
    index bigint, 
    PRIMARY KEY(Patient_Hub_Key)
);

CREATE TABLE Experiment_Hub (
    Experiment_Hub_Key serial,
    Experiment_BusinessKey varchar(5),
    LoadDateTime TIMESTAMP, 
    RecordSource varchar(10),
    Experiment_Type varchar(15),
    index bigint,
    PRIMARY KEY (Experiment_Hub_Key)
);

CREATE TABLE Sessions_Hub (
    Sessions_Hub_Key serial,
    Sessions_BusinessKey varchar(5),
    LoadDateTime TIMESTAMP, 
    RecordSource varchar(10),
    index bigint,
    PRIMARY KEY (Sessions_Hub_Key)
);

CREATE TABLE DataSources_Hub (
    DataSources_Hub_Key serial,
    DataSources_BusinessKey varchar(5),
    LoadDateTime TIMESTAMP, 
    RecordSource varchar(10),
    DataSource_Name varchar(10),
    index bigint,
    PRIMARY KEY (DataSources_Hub_Key)
);

CREATE TABLE fNIRS_Hub (
    fNIRS_Hub_Key serial,
    fNIRS_BusinessKey varchar(5),
    LoadDateTime TIMESTAMP, 
    RecordSource varchar(10),
    Name varchar(30),
    index bigint,
    PRIMARY KEY (fNIRS_Hub_Key)
);

CREATE TABLE ProbeData_Hub (
    ProbeData_Hub_Key serial,
    ProbeData_BusinessKey varchar(5),
    LoadDateTime TIMESTAMP, 
    RecordSource varchar(10),
    index bigint,
    PRIMARY KEY (ProbeData_Hub_Key)
);

--Please now run the staging python files for all the Hubs,found in the Hubs folder to populate the Hub tables.

-- 3.1) Creating the link Tables - please copy and paste all code below and run on PgAdmin

CREATE TABLE Patient_Experiment_Link (
    PatientExperiment_Link_Key SERIAL, 
    LoadDateTime TIMESTAMP NOT NULL,
    RecordSource varchar(10) NOT NULL, 
    index bigint,
    Patient_Hub_Key int REFERENCES Patient_Hub(Patient_Hub_Key), 
    Experiment_Hub_Key int REFERENCES Experiment_Hub(Experiment_Hub_Key), 
    PRIMARY KEY(PatientExperiment_Link_Key)
);

CREATE TABLE ProbeData_Experiment_Link(
    ProbeDataExperiment_Link_Key SERIAL, 
    LoadDateTime TIMESTAMP NOT NULL,
    RecordSource varchar(10) NOT NULL, 
    index bigint,
    Experiment_Hub_Key int REFERENCES Experiment_Hub(Experiment_Hub_Key), 
    ProbeData_Hub_Key int REFERENCES ProbeData_Hub(ProbeData_Hub_Key),
    PRIMARY KEY(ProbeDataExperiment_Link_Key)
);

CREATE TABLE ProbeData_Sessions_Link(
    ProbeDataSession_Link_Key SERIAL,
    LoadDateTime TIMESTAMP NOT NULL,
    RecordSource varchar(10) NOT NULL,
    index bigint,
    Sessions_Hub_Key int REFERENCES Sessions_Hub(Sessions_Hub_Key),
    ProbeData_Hub_Key INT REFERENCES ProbeData_Hub(ProbeData_Hub_Key),
    PRIMARY KEY(ProbeDataSession_Link_Key)
);

CREATE TABLE Sessions_DataSources_Link(
    SessionDataSources_Link_Key SERIAL, 
    LoadDateTime TIMESTAMP NOT NULL,
    RecordSource varchar(10) NOT NULL, 
    index bigint,
    Sessions_Hub_Key int REFERENCES Sessions_Hub(Sessions_Hub_Key), 
    DataSources_Hub_Key int REFERENCES DataSources_Hub(DataSources_Hub_Key), 
    PRIMARY KEY(SessionDataSources_Link_Key)
);

CREATE TABLE DataSources_fNIRS_Link(
    DataSourcesfNIRS_Link_Key SERIAL, 
    LoadDateTime TIMESTAMP NOT NULL,
    RecordSource varchar(10) NOT NULL, 
    index bigint,
    DataSources_Hub_Key int REFERENCES DataSources_Hub(DataSources_Hub_Key), 
    fNIRS_Hub_Key int REFERENCES fNIRS_Hub(fNIRS_Hub_Key), 
    PRIMARY KEY(DataSourcesfNIRS_Link_Key)
);


CREATE TABLE PatientData_Sources_Link(
    PatientDataSources_Link_Key SERIAL,
    LoadDateTime TIMESTAMP NOT NULL,
    RecordSource varchar(10) NOT NULL, 
    index bigint,
    Patient_Hub_Key int REFERENCES Patient_Hub(Patient_Hub_Key), 
    DataSources_Hub_Key int REFERENCES DataSources_Hub(DataSources_Hub_Key), 
    PRIMARY KEY(PatientDataSources_Link_Key)
);

----Please now run the staging python files for all the Links,found in the Links folder to populate the Hub tables.


-- 3.2) Creating the Satellites
--Satellites below are created and populated by running their respective staging python files, the tables will then appear on pgAdmin
--Patient_Satellite, 
--Exp1_Metadata_Satellite,
--Exp2_Metadata_Satellite,
--ProbeData_Satellite,
--fNIRS_Deoxy_Satellite,
--fNIRS_Oxy_Satellite,
--fNIRS_Exp2Sess1WL_Satellite,
--fNIRS_Exp2Sess2WL_Satellite,
--fNIRS_Exp2Sess1Dat_Satellite,
--fNIRS_Exp2Sess2Dat_Satellite

--Create this Satellite by pasting this code into pgAdmin and then running the staging python file to populate it
CREATE TYPE Stimuli_Type AS ENUM ('Moto', 'Rest', 'ViMo', 'Viso', 'NormalConvo', 'StressedConvo');
CREATE TABLE Experimental_Session_Satellite (
    Time_stamp TIMESTAMP,
    Sessions_Hub_Key INT,
    Name Stimuli_Type,
    index bigint,
    FOREIGN KEY (Sessions_Hub_Key) REFERENCES Sessions_Hub(Sessions_Hub_Key),
    PRIMARY KEY(Sessions_Hub_Key, Time_stamp)
);

--Please now run the staging python file for Experimental Session Sat,found in the Satellite folder to populate the table.

--3.3) Constraints for the Satellites 
--Example:
--Patient_Satellite 
ALTER TABLE public."Patient_Satellite"
	ADD PRIMARY KEY ("Patient_Hub_Key", "TimeStamp");

--Exp1_Metadata_Satellite
ALTER TABLE public."Exp1_Metadata_Satellite"
	ADD PRIMARY KEY ("Experiment_Hub_Key", "time_stamp");

--Exp2_Metadata_Satellite
ALTER TABLE public."Exp2_Metadata_Satellite"
	ADD PRIMARY KEY ("Experiment_Hub_Key", "time_stamp");

--ProbeData_Satellite
ALTER TABLE public."ProbeData_Satellite"
	ADD PRIMARY KEY ("ProbeData_Hub_Key", "time_stamp");

--fNIRS_Deoxy_Satellite
ALTER TABLE public."fNIRS_Deoxy_Satellite"
	ADD PRIMARY KEY ("fNIRS_Hub_Key", "time_stamp");

--fNIRS_Oxy_Satellite
ALTER TABLE public."fNIRS_Oxy_Satellite"
	ADD PRIMARY KEY ("fNIRS_Hub_Key", "time_stamp");

--fNIRS_Exp2Sess1Dat_Satellite
ALTER TABLE public."fNIRS_Exp2Sess1Dat_Satellite"
	ADD PRIMARY KEY ("fNIRS_Hub_Key", "Time stamp");

--fNIRS_Exp2Sess2Dat_Satellite
ALTER TABLE public."fNIRS_Exp2Sess2Dat_Satellite"
	ADD PRIMARY KEY ("fNIRS_Hub_Key", "Time stamp");

--fNIRS_Exp2Sess1WL_Satellite
ALTER TABLE public."fNIRS_Exp2Sess1WL_Satellite"
	ADD PRIMARY KEY ("fNIRS_Hub_Key", "time_stamp");

--fNIRS_Exp2Sess2WL_Satellite
ALTER TABLE public."fNIRS_Exp2Sess2WL_Satellite"
	ADD PRIMARY KEY ("fNIRS_Hub_Key", "time_stamp");

--3.4) Queries 
--Query 1 - Patient 1's moto channels
SELECT * FROM public."ProbeData_Satellite"
WHERE patient_id = '1'
AND "Stimuli_Type" = 'moto'
ORDER BY "ProbeData_Hub_Key" ASC, time_stamp ASC 

--Query 2 - Patient 2's rest data from deoxy & oxy readings
SELECT * 
FROM public."fNIRS_Deoxy_Satellite"
JOIN public."fNIRS_Oxy_Satellite"
ON (public."fNIRS_Deoxy_Satellite"."Patient_ID" = public."fNIRS_Oxy_Satellite"."Patient_ID")
WHERE "fNIRS_Deoxy_Satellite"."fNIRS_type" = 'rest'
AND "fNIRS_Oxy_Satellite"."fNIRS_type" = 'rest'
AND "fNIRS_Deoxy_Satellite"."Patient_ID" = '2'
AND "fNIRS_Oxy_Satellite"."Patient_ID" = '2'

--3.5) Visualisations & user authentication
CREATE TABLE IF NOT EXISTS public.image
(
    data bytea,
    datatype varchar(30),
    sessionid bigint,
    patientid bigint NOT NULL,
    PRIMARY KEY (patientid,datatype,sessionid)
);

CREATE TABLE IF NOT EXISTS public.login_user
(
    id bigint NOT NULL,
    name character varying(128) COLLATE pg_catalog."default" NOT NULL,
    password character varying(256) COLLATE pg_catalog."default" NOT NULL,
    email character varying(254) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT login_user_pkey PRIMARY KEY (id),
    CONSTRAINT login_user_email_key UNIQUE (email),
    CONSTRAINT login_user_name_key UNIQUE (name)
);
INSERT INTO login_user VALUES (1, 'admin', 123456789, 'hxw188@student.bham.ac.uk');

