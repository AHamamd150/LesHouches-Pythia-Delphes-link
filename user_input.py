LesHouches= []

##################################################################
## Python script to link between LesHouches events file+pythia+delphes+madanalysis
####################################################################
run_name = 'Run_1' # Name of the folder to store the outputs
###############################
LesHouches.append('ttbar.lhe') #Name of the input LesHuches files, in case of QCD= on, the code will ignore this inputs
LesHouches.append('evenets_parton_1mm.lhe')
#LesHouches.append('unweighted_2_events_sig.lhe')
Number_of_lhe_files = 2 # Number of LesHouches files you want to be used
################################################
pythia = 'on'   #Here the user should define pythia options by on/off
######Options you can control if you have input LesHouches files ######
Hadronizatoin = 'on'
Decay_of_heavy_hadrons = 'on'
Initial_state_radiation = 'on'
Final_state_radiation = 'on'
Multiple_interaction = 'off'
Beam_remnants = 'off'          
Tau_decays = 'off'             ####Enables tau lepton decays
Tau_decay_mode = 1       ###methods to keep the polarization of tau decay products, look at pythia8 online manual

####QCD generation using pythia stand alone (No input LesHuches files) ##########
QCD = 'off'  ##generate QCD processes using pythia and ignore the LesHouche inputs
N_events = 100 ##Number of QCD events
QCD_soft_all='on'  ##generate soft QCD
QCD_hard_all='on'  ##generate hard QCD
QCD_hard_2to3 ='on'  ##generate hard QCD with three particles final state
center_of_mass_energy= 12000 ## unites of GeV
PT_minimum = 2    ##Minimum pt for the generated events in GeV

####Matching###########
merging = '0'  # If '0' no matching used. '1' CKKW matching '2' MLM matching "recommended"
# Other options for the merging&matching algorithm has to be chagned by the user (if needed)  

#########Remove the unnecissary produced files ###########
Remove_lhe = 'false' ## for the space issue one can remove any of these files after it produced by changing to (true)
Remove_hepmc ='false'   ## if true the hepmc files will be deleted 
Remove_root='false'
Remove_lhco='false'
########################################################################
# Fo the moment delphes input card is the default CMS one for RUN-II if it set to default##
########################################################################
Delphes = 'off'  # 'on/off' turn on or off delphes
delphes_card =  'defalut'  #full path to delphes card
################################################
# Write the commands as in madanalysis
# input files for both gen and reco level added automatically
# the cross section for each file will taken automatically from pythia.log files
# You can revise the input cards for madanalysis wihch can found in gen_plot and reco_plt dirs
madanalysis = 'off'
madanalysis_commands='''
define l = l+ l-
define e = e+ e-
define mu = mu+ mu-
set main.stacking_method = superimpose
set main.lumi = 300
set main.normalize = lumi
plot PT( l- l+) 100 0 220 
plot N(j) 100 -5 10 
        '''
