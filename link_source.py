#!/usr/bin/python
import fileinput
import os
import re
import sys
import shutil
import array
import time
from scan_input import  * 
from os import remove
from shutil import move
import tarfile
import glob
path = os.getcwd()
#################################
def yes_no(question, default="yes"):
        valid = {"yes":True,   "y":True,  "ye":True}
        notvalid ={"no":False,     "n":False}
        if default == None:
                prompt = " [y/n] "
        elif default == "yes":
                prompt = " [Y/n] "
        elif default == "no":
                prompt = " [y/N] "
        else:
                raise ValueError("invalid answer: ")
        while True:
                sys.stdout.write(question + prompt)
                choice = raw_input().lower()
                if choice in valid:
                    shutil.rmtree(str(path)+'/'+str(run_name))
                    return valid[choice]
                elif choice in notvalid:
                        os.rename(str(path)+'/'+str(run_name),str(path)+'/'+str(run_name)+'_old')
                        print 'Changing the old dir to %s'%(str(path)+'/'+str(run_name)+'_old')
                        time.sleep(8)
                        return notvalid[choice]
                else:
                        sys.stdout.write("Please respond with 'yes' or 'no' "\
                                        "(or 'y' or 'n').\n")

def yes1_no1(question, default="yes"):
        valid = {"yes":True,   "y":True,  "ye":True}
        notvalid ={"no":False,     "n":False}
        if default == None:
                prompt = " [y/n] "
        elif default == "yes":
                prompt = " [Y/n] "
        elif default == "no":
                prompt = " [y/N] "
        else:
                raise ValueError("invalid answer: ")
        while True:
                sys.stdout.write(question + prompt)
                choice = raw_input().lower()
                if choice in valid:
            
                    return valid[choice]
                elif choice in notvalid:
                        exit()
                        return notvalid[choice]
                else:
                        sys.stdout.write("Please respond with 'yes' or 'no' "\
                                        "(or 'y' or 'n').\n")                                        
############ colors ##############
def Red(prt): print("\033[91m {}\033[00m" .format(prt))
def Green(prt): print("\033[92m {}\033[00m" .format(prt))
def Yellow(prt): print("\033[93m {}\033[00m" .format(prt))
##############################################
Yellow('''***********************************************
 *  Script to Link LesHouches events at parton *
 *  level to Pythia8 including jet matching    *
 *  (MLM/CKKW) + Delphes + MadAnalysis         *
 *           A. Hammad                         *
 *********************************************** ''')
time.sleep(5)
##############################################
if os.path.exists(str(path)+'/'+str(run_name)):
    Red('The directory %s exists'%str(run_name))
    yes_no('Do you want to overwrite it?')
    
os.mkdir(str(path)+'/'+str(run_name))
if (Delphes =='on' and pythia !='on'):
    Red(''' Delphes is activated, while pythia is off
    please trun pythia on''')
    exit()
######################################
if not os.path.exists(str(path)+str('/Pythia.822/pythia/hepmc/lib'))and pythia =='on':
    Red( '---> pythia8 not installed in %s, '%str(path))
    if os.path.exists(str(path)+str('/Pythia.822/')):
        shutil.rmtree(str(path)+str('/Pythia.822/'))
    Green('---> Downloading Pythia8')    
    os.system('git clone https://github.com/AHamamd150/Pythia.822.git')
    os.chdir(str(path)+str('/Pythia.822'))
    Green( '---> Install Pythia8')
    os.system('tar zxvf pythia.tar.gz')
    os.remove(str(path)+str('/Pythia.822/pythia.tar.gz'))
   # os.remove(str(path)+str('/Pythia.822/README.md'))
    os.chdir(str(path)+str('/Pythia.822/pythia/hepmc'))
    time.sleep(5)
    Green('---> hepmc will confugured with units GEV and CM')
    time.sleep(5)
    os.system('./configure --prefix=%s/Pythia.822/pythia/hepmc/ --with-momentum=GEV --with-length=CM'%str(path))
    os.system('make')
    os.system('make install')
    os.chdir(str(path)+str('/Pythia.822/pythia/'))
    os.system('./configure --with-hepmc2=%s/Pythia.822/pythia/hepmc/  --with-hepmc2-include=%s/Pythia.822/pythia/hepmc/include --cxx-common=\'-ldl -fPIC -lstdc++\''%(str(path),str(path)))
    time.sleep(5)
    os.system('make')
    os.system('make install')
    os.chdir(str(path)+str('/Pythia.822/pythia/examples/'))
    Green('---> Creating HepMC link')
    time.sleep(5)
    #os.system('cat main42.cc > mainx1.cc')
    #os.system('cat main42.cc > mainx2.cc')
    #os.system('cat main42.cc > mainx3.cc')
    #os.system('cat main42.cc > mainx4.cc')
    #os.system('cat main42.cc > mainx5.cc')
    #os.system('cat main42.cc > mainx6.cc')
    #os.system('cat main42.cc > mainx7.cc')
    #os.system('cat main42.cc > mainx8.cc')
    #os.system('cat main42.cc > mainx9.cc')
    #os.system('cat main42.cc > mainx10.cc')
    os.system('make main42')
    os.system('make main41')
    #os.system('make mainx1')
    #os.system('make mainx2')
    #os.system('make mainx3')
    #os.system('make mainx4')
    #os.system('make mainx5')
    #os.system('make mainx6')
    #os.system('make mainx7')
    #os.system('make mainx8')
    #os.system('make mainx9')
    #os.system('make mainx10')
    os.system('make main89')
 #   os.chdir(str(path)+str('/Pythia_82/pythia/rootexamples/'))
 #   print '---> Creating Pythia_ROOT link'
 #   os.system('make hist')
    Green('---> pythia8 installed in %s'%str(path))
    time.sleep(5)
    os.chdir(str(path))
#else:
    #Green('---> pythia8 installed')
if not os.path.exists(str(path)+str('/delphes/delphes/DelphesHepMC'))and Delphes=='on':
    Red('---> delphes not installed in %s,'%str(path))
    Yellow(''' ************************************************
 *  Please be sure that root-config is activated *
 ************************************************ ''')
    if os.path.exists(str(path)+str('/delphes/')):
        shutil.rmtree(str(path)+str('/delphes/'))
    Green('--->Downloading delphes')
    os.system('git clone https://github.com/AhmedHammad1/delphes.git')
    Green('---> Installing delphes')
    os.chdir((str(path)+str('/delphes/')))
    os.system('tar zxvf delphes.tar.gz')
    os.remove('delphes.tar.gz')
    os.remove('README.md')
    os.chdir((str(path)+str('/delphes/delphes')))
    os.system('make')
    time.sleep(4)
    if not os.path.exists(str(path)+str('/delphes/delphes/DelphesHepMC')):
        Red(''' ********************************
    *       Delphes not installed 
    *          EXIT !!!!!!!!!!!                                          
    *********************************************** ''')
        exit()   
    os.chdir(str(path))
    Green('---> delphes installed in %s'%str(path))
    time.sleep(5)
#else:
    #Green('---> delphes installed')
if not os.path.exists(str(path)+str('/madanalysis5/')) and madanalysis =='on':
    Red('---> madanalysis5 not installed in %s,'%str(path))
    Green('---> Downloading MadAnalysis')
    os.system('wget \'https://launchpad.net/madanalysis5/trunk/v1.4/+download/MadAnalysis5_v1.4.tar.gz\'')
    os.system('tar zxvf MadAnalysis5_v1.4.tar.gz')
    Green('---> MadAnalaysis installed in %s'%str(path))
    time.sleep(5)
#else:    
    #Green('---> MadAnalysis5 installed')
#########QCD  ##############################################
if (pythia == 'on'and QCD=='on'):
    os.chdir(str(path)+str('/Pythia.822/pythia/examples/'))
    root=open ('main41.cc')
    f = open ('fout','w+')
    for y in root:
            
        if str ('NEVENTS =') in y:
            x = y.rsplit()
            y = y.replace(' '+str(x[-2]),' '+str(N_events))    
        if str ('pythia.readString("Beams:eCM =  ') in y:
            x = y.rsplit()
            y = y.replace(' '+str(x[-2]),' '+str(center_of_mass_energy))    
        if str ('pythia.readString("SoftQCD:all =  ') in y:
            x = y.rsplit()
            y = y.replace(' '+str(x[-2]),' '+str(QCD_soft_all))        
        if str ('pythia.readString("HardQCD:all =  ') in y:
            x = y.rsplit()
            y = y.replace(' '+str(x[-2]),' '+str(QCD_hard_all))  
        if str ('pythia.readString("HardQCD:3parton =   ') in y:
            x = y.rsplit()
            y = y.replace(' '+str(x[-2]),' '+str(QCD_hard_2to3))     
        if str ('pythia.readString("PhaseSpace:pTHatMin =  ') in y:
            x = y.rsplit()
            y = y.replace(' '+str(x[-2]),' '+str(PT_minimum))                    
            
        f.write(y)
    os.rename('fout','main41.cc')
    f.close()
    Yellow('---> Creating hepMC file, please be patient it takes awhile')
        
    #Yellow('---> please take a look at %s/%s to catch the modified cross section'%(str(path+'/'+str(run_name)),str(name[0])+'_pythia.log'))
    os.system('make main41  >/dev/null')
    os.system('./main41')
    if os.path.exists(str(path+'/'+str(run_name))+'/pythia.log'):
        os.remove(str(path+'/'+str(run_name)+'/pythia.log'))
   # shutil.move(str(path)+str('/Pythia.822/pythia/examples/pythia.log'),(str(path)+'/'+str(run_name)))
    #os.rename(str(path)+'/'+str(run_name)+'/pythia.log',str(path)+'/'+str(run_name)+'/'+str(name[0])+'_pythia.log')
    if not os.path.exists(str(path)+str('/Pythia.822/pythia/examples/H.hep')):
        Red(''' ******************************************************************
    * Pythia couldnt produce hepmc file please take a look at %s/%s
    *          EXIT !!!!!!!!!!!                                          
    ****************************************************************** '''%(str((path)+'/'+str(run_name))),str(name[0])+'_pythia.log')
        exit()            
    if os.path.exists(str(path)+str('/Pythia.822/pythia/examples/H.hep')):    
        os.rename('H.hep','QCD_pythia.hepmc')
        os.chdir(str(path+'/'+str(run_name)))
        if os.path.exists(str(path+'/'+str(run_name)+'/'+'QCD_pythia.hepmc')):
            os.remove(str(path+'/'+str(run_name)+'/'+'QCD_pythia.hepmc'))
        shutil.move(str(path)+str('/Pythia.822/pythia/examples/')+'QCD_pythia.hepmc',(str(path)+'/'+str(run_name)))
os.chdir(str(path))
#########QCD delphes#####
if (Delphes == 'on' and pythia == 'on'):
    os.chdir(str(path)+'/delphes/delphes')
    Green('---> Runing delphes')
    if os.path.exists(str(path)+str('/delphes/delphes/delphes.root')):    
        os.remove(str(path)+str('/delphes/delphes/delphes.root'))
    if str(delphes_card) != 'defalut':
        if not os.path.exists(str(delphes_card)):
            Red('''delphes card not exist, please enter a vailed location
                                EXIT''')
            exit()
        else:
            os.system('./DelphesHepMC %s  delphes.root %s >/dev/null'\
                  %(str(delphes_card),(str(path+'/'+str(run_name)+'/')+'QCD_pythia.hepmc')))
           
    else:
        os.system('./DelphesHepMC %s  delphes.root %s >/dev/null'\
                  %(str(path)+'/delphes/delphes/cards/delphes_card_CMS.tcl',(str(path+'/'+str(run_name)+'/')+'QCD_pythia.hepmc')))
    #print (str(path)+'/'+str(name[0])+'.hep')
    if os.path.exists(str(path)+str('/delphes/delphes/delphes.root')):    
        os.rename('delphes.root','QCD_delphes.root')
        os.system(' ./root2lhco %s  e.lhco'%('QCD_delphes.root'))
        if os.path.exists(str(path)+str('/delphes/delphes/e.lhco')):    
            os.rename('e.lhco','QCD_delphes.lhco')
        os.chdir(str(path+'/'+str(run_name)))
        if os.path.exists(str(path+'/'+str(run_name)+'/'+'QCD_delphes.root')):
            os.remove(str(path+'/'+str(run_name)+'/'+'QCD_delphes.root'))
        shutil.move(str(path)+str('/delphes/delphes/')+'QCD_delphes.root',(str(path)+'/'+str(run_name)))
    if os.path.exists(str(path+'/'+str(run_name)+'/'+'QCD_delphes.lhco')):
        os.remove(str(path+'/'+str(run_name)+'/'+'QCD_delphes.lhco'))
    shutil.move(str(path)+str('/delphes/delphes/')+'QCD_delphes.lhco',(str(path)+'/'+str(run_name)))
    
    if (Remove_hepmc == 'true'):
      if os.path.exists((str(path)+'/'+str(run_name))+'/QCD_pythia.hepmc') :
         os.remove((str(path)+'/'+str(run_name))+'/QCD_pythia.hepmc')        
    if (Remove_root == 'true'):
       if os.path.exists((str(path)+'/'+str(run_name))+'/QCD_delphes.root') :
         os.remove((str(path)+'/'+str(run_name))+'/QCD_delphes.root')           
    if (Remove_lhco == 'true'):
       if os.path.exists((str(path)+'/'+str(run_name))+'/QCD_delphes.lhco') :
         os.remove((str(path)+'/'+str(run_name))+'/QCD_delphes.lhco') 
os.chdir(str(path))
     
 
 
       
########### preparing LesHouches file #######
for zz in range(0,Number_of_lhe_files):
    lhe = str(LesHouches[zz])
    if not os.path.exists(str(path)+'/'+str(lhe)):
        Red('%s Not exist,  EXIT'%(str(lhe)))
        exit()
    name = lhe.rsplit(".")
    root=open(lhe)
    f = open ('fout','w+')
    for y in root:
        if '<LesHouchesEvents version="2.0">' in y:
            y =y.replace('<LesHouchesEvents version="2.0">','<LesHouchesEvents version="1.0">')
        if '<LesHouchesEvents version="3.0">' in y:
            y =y.replace('<LesHouchesEvents version="3.0">','<LesHouchesEvents version="1.0">')
        f.write(y)
    os.rename('fout',lhe)
    f.close()
    shutil.copy(str(path)+'/'+str(lhe),(str(path)+'/'+str(run_name)))

    ###############################################
    if (merging == '0' and pythia == 'on' and QCD!='on'):
        os.chdir(str(path)+str('/Pythia.822/pythia/examples/'))
        root=open ('main42.cmnd')
        f = open ('fout','w+')
        for y in root:
            if str ('Beams:LHEF') in y:
                x = y.rsplit()
                y = y.replace(str(x[-1]),str(path)+'/'+str(run_name)+'/'+str(lhe))
            if str ('HadronLevel:Hadronize =') in y:
                x = y.rsplit()
                y = y.replace(' '+str(x[-1]),' '+str(Hadronizatoin))    
            if str ('PartonLevel:MPI') in y:
                x = y.rsplit()
                y = y.replace(' '+str(x[-1]),' '+str(Multiple_interaction))
            if str ('PartonLevel:ISR =') in y:
                x = y.rsplit()
                y = y.replace(' '+str(x[-1]),' '+str(Initial_state_radiation))
            if str ('PartonLevel:FSR =') in y:
                x = y.rsplit()
                y = y.replace(' '+str(x[-1]),' '+str(Final_state_radiation))
            if str ('HadronLevel:Decay') in y:
                x = y.rsplit()
                y = y.replace(' '+str(x[-1]),' '+str(Decay_of_heavy_hadrons))
            if str ('15:mayDecay= ') in y:
                x = y.rsplit()
                y = y.replace(' '+str(x[-1]),' '+str(Tau_decays))
            if str ('TauDecays:externalMode= ') in y:
                x = y.rsplit()
                y = y.replace(' '+str(x[-1]),' '+str(Tau_decay_mode))        
            if str ('PartonLevel:Remnants =') in y:
                x = y.rsplit()
                y = y.replace(' '+str(x[-1]),' '+str(Beam_remnants))
            f.write(y)
        os.rename('fout','main42.cmnd')
        f.close()
        Yellow('---> Creating hepMC file, please  be patient it takes awhile')
        Yellow('---> please take a look at %s/%s to catch the modified cross section'%(str(path+'/'+str(run_name)),str(name[0])+'_pythia.log'))
        os.system('./main42 main42.cmnd H.hep')
        if os.path.exists(str(path+'/'+str(run_name))+'/pythia.log'):
            os.remove(str(path+'/'+str(run_name))+'/pythia.log')
      #  shutil.move(str(path)+str('/Pythia.822/pythia/examples/pythia.log'),(str(path)+'/'+str(run_name)))
       # os.rename(str(path)+'/'+str(run_name)+'/pythia.log',str(path)+'/'+str(run_name)+'/'+str(name[0])+'_pythia.log')
        if not os.path.exists(str(path)+str('/Pythia.822/pythia/examples/H.hep')):
            Red(''' ******************************************************************
        * Pythia couldnt produce hepmc file please take a look at %s/%s 
        *          EXIT !!!!!!!!!!!                                          
        ****************************************************************** '''%(str((path)+'/'+str(run_name))),str(name[0])+'_pythia.log')
            exit()            
        if os.path.exists(str(path)+str('/Pythia.822/pythia/examples/H.hep')):    
            os.rename('H.hep',str(name[0])+'_pythia.hepmc')
            os.chdir(str(path+'/'+str(run_name)))
            if os.path.exists(str(path+'/'+str(run_name)+'/'+str(name[0])+'_pythia.hepmc')):
                os.remove(str(path+'/'+str(run_name)+'/'+str(name[0])+'_pythia.hepmc'))
            shutil.move(str(path)+str('/Pythia.822/pythia/examples/')+str(name[0])+'_pythia.hepmc',(str(path)+'/'+str(run_name)))

    ##############################################
    if (merging == '1' and pythia == 'on'and QCD!='on'):
        os.chdir(str(path)+str('/Pythia.822/pythia/examples/'))
        root=open ('main89mlm.cmnd')
        f = open ('fout','w+')
        for y in root:
            if str ('Beams:LHEF') in y:
                x = y.rsplit()
                y = y.replace(str(x[-1]),str(path)+'/'+str(run_name)+'/'+str(lhe))
            if str ('HadronLevel:Hadronize =') in y:
                x = y.rsplit()
                y = y.replace(' '+str(x[-1]),' '+str(Hadronizatoin))    
            if str ('PartonLevel:MPI') in y:
                x = y.rsplit()
                y = y.replace(' '+str(x[-1]),' '+str(Multiple_interaction))
            if str ('PartonLevel:ISR =') in y:
                x = y.rsplit()
                y = y.replace(' '+str(x[-1]),' '+str(Initial_state_radiation))
            if str ('PartonLevel:FSR =') in y:
                x = y.rsplit()
                y = y.replace(' '+str(x[-1]),' '+str(Final_state_radiation))
            if str ('HadronLevel:Decay') in y:
                x = y.rsplit()
                y = y.replace(' '+str(x[-1]),' '+str(Decay_of_heavy_hadrons))
            if str ('PartonLevel:Remnants =') in y:
                x = y.rsplit()
                y = y.replace(' '+str(x[-1]),' '+str(Beam_remnants))
            f.write(y)
        os.rename('fout','main89mlm.cmnd')
        f.close()
        Yellow('---> Creating hepMC file, please be patient it takes awhile')
        
        Yellow('---> please take a look at %s/%s to catch the modified cross section'%(str(path+'/'+str(run_name)),str(name[0])+'_pythia.log'))
        os.system('./main89 main89mlm.cmnd H.hep')
        if os.path.exists(str(path+'/'+str(run_name))+'/pythia.log'):
            os.remove(str(path+'/'+str(run_name)+'/pythia.log'))
       # shutil.move(str(path)+str('/Pythia.822/pythia/examples/pythia.log'),(str(path)+'/'+str(run_name)))
        #os.rename(str(path)+'/'+str(run_name)+'/pythia.log',str(path)+'/'+str(run_name)+'/'+str(name[0])+'_pythia.log')
        if not os.path.exists(str(path)+str('/Pythia.822/pythia/examples/H.hep')):
            Red(''' ******************************************************************
        * Pythia couldnt produce hepmc file please take a look at %s/%s
        *          EXIT !!!!!!!!!!!                                          
        ****************************************************************** '''%(str((path)+'/'+str(run_name))),str(name[0])+'_pythia.log')
            exit()            
        if os.path.exists(str(path)+str('/Pythia.822/pythia/examples/H.hep')):    
            os.rename('H.hep',str(name[0])+'_pythia.hepmc')
            os.chdir(str(path+'/'+str(run_name)))
            if os.path.exists(str(path+'/'+str(run_name)+'/'+str(name[0])+'_pythia.hepmc')):
                os.remove(str(path+'/'+str(run_name)+'/'+str(name[0])+'_pythia.hepmc'))
            shutil.move(str(path)+str('/Pythia.822/pythia/examples/')+str(name[0])+'_pythia.hepmc',(str(path)+'/'+str(run_name)))
    os.chdir(str(path))
    ##############################################
    if (Delphes == 'on' and pythia == 'on'):
        os.chdir(str(path)+'/delphes/delphes')
        Green('---> Runing delphes')
        if os.path.exists(str(path)+str('/delphes/delphes/delphes.root')):    
            os.remove(str(path)+str('/delphes/delphes/delphes.root'))
        if str(delphes_card) != 'defalut':
            if not os.path.exists(str(delphes_card)):
                Red('''delphes card not exist, please enter a vailed location
                                    EXIT''')
                exit()
            else:
                os.system('./DelphesHepMC %s  delphes.root %s >/dev/null'\
                      %(str(delphes_card),(str(path+'/'+str(run_name)+'/'+str(name[0]))+'_pythia.hepmc')))
           
        else:
            os.system('./DelphesHepMC %s  delphes.root %s >/dev/null'\
                      %(str(path)+'/delphes/delphes/cards/delphes_card_CMS.tcl',(str(path+'/'+str(run_name)+'/'+str(name[0]))+'_pythia.hepmc')))
        #print (str(path)+'/'+str(name[0])+'.hep')
        if os.path.exists(str(path)+str('/delphes/delphes/delphes.root')):    
            os.rename('delphes.root',str(name[0])+'_delphes.root')
            os.system(' ./root2lhco %s  e.lhco'%(str(name[0])+'_delphes.root'))
            if os.path.exists(str(path)+str('/delphes/delphes/e.lhco')):    
                os.rename('e.lhco',str(name[0])+'_delphes.lhco')
            os.chdir(str(path+'/'+str(run_name)))
            if os.path.exists(str(path+'/'+str(run_name)+'/'+str(name[0])+'_delphes.root')):
                os.remove(str(path+'/'+str(run_name)+'/'+str(name[0])+'_delphes.root'))
            shutil.move(str(path)+str('/delphes/delphes/')+str(name[0])+'_delphes.root',(str(path)+'/'+str(run_name)))
        if os.path.exists(str(path+'/'+str(run_name)+'/'+str(name[0])+'_delphes.lhco')):
            os.remove(str(path+'/'+str(run_name)+'/'+str(name[0])+'_delphes.lhco'))
        shutil.move(str(path)+str('/delphes/delphes/')+str(name[0])+'_delphes.lhco',(str(path)+'/'+str(run_name)))
        if (Remove_lhe == 'true'):
           if os.path.exists((str(path)+'/'+str(run_name))+str(lhe)) :
              os.remove((str(path)+'/'+str(run_name))+str(lhe))    
        if (Remove_hepmc == 'true'):
          if os.path.exists((str(path)+'/'+str(run_name))+str(name[0])+'_pythia.hepmc') :
             os.remove((str(path)+'/'+str(run_name))+str(name[0])+'_pythia.hepmc')        
        if (Remove_root == 'true'):
           if os.path.exists((str(path)+'/'+str(run_name))+str(name[0])+'_delphes.root') :
             os.remove((str(path)+'/'+str(run_name))+str(name[0])+'_delphes.root')           
        if (Remove_lhco == 'true'):
           if os.path.exists((str(path)+'/'+str(run_name))+str(name[0])+'_delphes.lhco') :
             os.remove((str(path)+'/'+str(run_name))+str(name[0])+'_delphes.lhco') 
    os.chdir(str(path))
    
  #  if (Delphes == 'on' and pythia != 'on'):
  #      Red('Delphes is on, put pythia is disapled !!!!')
  #      Red('Exit,')
  #      exit()
##########################################################################################
if (madanalysis == 'on' and pythia =='on' and Delphes == 'on'):
    Green('---> Runing madanalysis5, Parton level')
    time.sleep(5)
    os.mkdir(str(path)+'/'+str(run_name)+'/parton_plots')
    os.mkdir(str(path)+'/'+str(run_name)+'/Hadron_plots')
    os.mkdir(str(path)+'/'+str(run_name)+'/reco_plots')
    os.chdir(str(path)+'/madanalysis5')
    root=open (str(path)+'/madanalysis5/madanalysis/input/installation_options.dat')
    f = open ('fout','w+')
    for y in root:
        if str ('# fastjet_veto     = 0') in y:
            y = y.replace('# fastjet_veto     = 0',' fastjet_veto     = 1')
        f.write(y)
    os.rename('fout',str(path)+'/madanalysis5/madanalysis/input/installation_options.dat')
    f.close()    
    mad = open ('setup.sh','w+')
    mad.write('''#!/bin/bash
./bin/ma5 -s -f gen.txt &>/dev/null''')
    os.system('chmod 777 setup.sh')
    gen = open ('gen.txt','w+')
    gen.write('''define l = l+ l-
define j = u u~ d d~ c c~ s s~ g
define mu = mu+ mu-
define ta = ta+ ta-
define e = e- e+
''')
    for zz in range(0,Number_of_lhe_files):
        lhe = str(LesHouches[zz])
        name = lhe.rsplit(".")
        gen.write('import %s as %s \n'%(str(path+'/'+str(run_name)+'/'+str(lhe)),str(name[0])))
        m = raw_input (" Please enter the cross section for '%s' in Pb \n"%str(lhe)) 
        gen.write('set %s.xsection = %s \n'%(str(name[0]),str(m)))
    gen.write(str(madanalysis_commands)+'\n')
    gen.write('submit gen')
    mad.close()
    gen.close()
    os.system('./setup.sh >/dev/null')
    os.system('cp -rf %s/madanalysis5/gen/PDF/selection_* %s'%(str(path),(str(path)+'/'+str(run_name)+'/parton_plots/')))
    os.system('cp -rf %s/madanalysis5/gen/Histo/selection_* %s'%(str(path),(str(path)+'/'+str(run_name)+'/parton_plots/')))
    os.system('cp -rf %s/madanalysis5/gen/PDF/main.pdf %s'%(str(path),(str(path)+'/'+str(run_name)+'/parton_plots/')))
    os.system('cp -rf %s/madanalysis5/gen.txt %s'%(str(path),(str(path)+'/'+str(run_name)+'/parton_plots/')))
    os.remove('setup.sh')
    shutil.rmtree(str(path)+'/madanalysis5/gen/')
    os.chdir(str(path)+'/madanalysis5')
    root=open (str(path)+'/madanalysis5/madanalysis/input/installation_options.dat')
    f = open ('fout','w+')
    for y in root:
        if str ('# fastjet_veto     = 0') in y:
            y = y.replace('# fastjet_veto     = 0',' fastjet_veto     = 1')
        f.write(y)
    os.rename('fout',str(path)+'/madanalysis5/madanalysis/input/installation_options.dat')
    f.close()    
    Green('---> Runing madanalysis5, for Hadron level')
    time.sleep(5)
    mad = open ('setup.sh','w+')
    mad.write('''#!/bin/bash
./bin/ma5 -s -f -H gen.txt &>/dev/null''')
    os.system('chmod 777 setup.sh')
    gen = open ('gen.txt','w+')
    gen.write('''define l = l+ l-
define j = p
define ta = ta+ ta-
define e = e- e+
''')
    for zz in range(0,Number_of_lhe_files):
        lhe = str(LesHouches[zz])
        name = lhe.rsplit(".")
        gen.write('import %s as %s \n'%(str(path+'/'+str(run_name)+'/'+str(name[0])+'_pythia.hepmc'),str(name[0])))
        f = open(str(path)+'/'+str(run_name)+'/'+str(name[0])+'_pythia.log','r')
        for line in f :
            if str('| sum                                                |') in line :
                o = line.rsplit()
                m = float(o[7])*1e+09
                gen.write('set %s.xsection = %s \n'%(str(name[0]),str(m)))
    gen.write(str(madanalysis_commands)+'\n')
    gen.write('submit gen')
    mad.close()
    gen.close()
    os.system('./setup.sh &>/dev/null')
    os.system('cp -rf %s/madanalysis5/gen/PDF/selection_* %s'%(str(path),(str(path)+'/'+str(run_name)+'/Hadron_plots/')))
    os.system('cp -rf %s/madanalysis5/gen/Histo/selection_* %s'%(str(path),(str(path)+'/'+str(run_name)+'/Hadron_plots/')))
    os.system('cp -rf %s/madanalysis5/gen/PDF/main.pdf %s'%(str(path),(str(path)+'/'+str(run_name)+'/Hadron_plots/')))
    os.system('cp -rf %s/madanalysis5/gen.txt %s'%(str(path),(str(path)+'/'+str(run_name)+'/Hadron_plots/')))
    os.remove('setup.sh')
    shutil.rmtree(str(path)+'/madanalysis5/gen/')
    ########## RECO LEVEL ##########
    mad = open ('setup.sh','w+')
    mad.write('''#!/bin/bash
./bin/ma5 -s -f -R reco.txt &>/dev/null''')
    os.system('chmod 777 setup.sh')
    gen = open ('reco.txt','w+')
    gen.write('''define l = l+ l-
#define j = u u~ d d~ c c~ s s~ g
define mu = mu+ mu-
define ta = ta+ ta-
define e = e- e+
''')
    for zz in range(0,Number_of_lhe_files):
        lhe = str(LesHouches[zz])
        name = lhe.rsplit(".")
        gen.write('import %s as %s \n'%(str(path+'/'+str(run_name)+'/'+str(name[0])+'_delphes.lhco'),str(name[0])))
        f = open(str(path)+'/'+str(run_name)+'/'+str(name[0])+'_pythia.log','r')
        for line in f :
            if str('| sum                                                |') in line :
                o = line.rsplit()
                m = float(o[7])*1e+09
                gen.write('set %s.xsection = %s \n'%(str(name[0]),str(m)))
    gen.write(str(madanalysis_commands)+'\n')
    gen.write('submit gen')
    mad.close()
    gen.close()
   
    Green('---> Running MadAnalysis for Reco level')
    os.system('./setup.sh >/dev/null')
    os.system('cp -rf %s/madanalysis5/gen/PDF/selection_* %s'%(str(path),(str(path)+'/'+str(run_name)+'/reco_plots/')))
    os.system('cp -rf %s/madanalysis5/gen/Histo/selection* %s'%(str(path),(str(path)+'/'+str(run_name)+'/reco_plots/')))
    os.system('cp -rf %s/madanalysis5/gen/PDF/main.pdf %s'%(str(path),(str(path)+'/'+str(run_name)+'/reco_plots/')))
    os.system('cp -rf %s/madanalysis5/reco.txt %s'%(str(path),(str(path)+'/'+str(run_name)+'/reco_plots/')))
    os.remove('setup.sh')
    shutil.rmtree(str(path)+'/madanalysis5/gen/')
os.chdir(str(path))

########################################
if (madanalysis == 'on' and pythia =='on' and Delphes != 'on'):
    Red('WARNING: Running MadAnalysis for hep file only')
    time.sleep(5)
    Green('---> Runing madanalysis5, for Parton level')
    os.mkdir(str(path)+'/'+str(run_name)+'/parton_plots')
    os.chdir(str(path)+'/madanalysis5')
    root=open (str(path)+'/madanalysis5/madanalysis/input/installation_options.dat')
    f = open ('fout','w+')
    for y in root:
        if str ('# fastjet_veto     = 0') in y:
            y = y.replace('# fastjet_veto     = 0',' fastjet_veto     = 1')
        f.write(y)
    os.rename('fout',str(path)+'/madanalysis5/madanalysis/input/installation_options.dat')
    f.close()    
    
    mad = open ('setup.sh','w+')
    mad.write('''#!/bin/bash
./bin/ma5 -s -f gen.txt &>/dev/null''')
    os.system('chmod 777 setup.sh')
    gen = open ('gen.txt','w+')
    gen.write('''define l = l+ l-
define j = u u~ d d~ c c~ s s~ g
define mu = mu+ mu-
define ta = ta+ ta-
define e = e- e+
''')
    for zz in range(0,Number_of_lhe_files):
        lhe = str(LesHouches[zz])
        name = lhe.rsplit(".")
        gen.write('import %s as %s \n'%(str(path+'/'+str(run_name)+'/'+str(lhe)),str(name[0])))
        m = raw_input (" Please enter the cross section for '%s' in Pb \n"%str(lhe)) 
        gen.write('set %s.xsection = %s \n'%(str(name[0]),str(m)))
    gen.write(str(madanalysis_commands)+'\n')
    gen.write('submit gen')
    mad.close()
    gen.close()
    Green('---> Running MadAnalysis for Gen level')
    os.system('./setup.sh >/dev/null')
    os.system('cp -rf %s/madanalysis5/gen/PDF/selection_* %s'%(str(path),(str(path)+'/'+str(run_name)+'/parton_plots/')))
    os.system('cp -rf %s/madanalysis5/gen/Histo/selection_* %s'%(str(path),(str(path)+'/'+str(run_name)+'/parton_plots/')))
    os.system('cp -rf %s/madanalysis5/gen/PDF/main.pdf %s'%(str(path),(str(path)+'/'+str(run_name)+'/parton_plots/')))
    os.system('cp -rf %s/madanalysis5/gen.txt %s'%(str(path),(str(path)+'/'+str(run_name)+'/parton_plots/')))
    os.remove('setup.sh')
    shutil.rmtree(str(path)+'/madanalysis5/gen/')


    os.mkdir(str(path)+'/'+str(run_name)+'/Hadron_plots')
    os.chdir(str(path)+'/madanalysis5')
    root=open (str(path)+'/madanalysis5/madanalysis/input/installation_options.dat')
    f = open ('fout','w+')
    for y in root:
        if str ('# fastjet_veto     = 0') in y:
            y = y.replace('# fastjet_veto     = 0',' fastjet_veto     = 1')
        f.write(y)
    os.rename('fout',str(path)+'/madanalysis5/madanalysis/input/installation_options.dat')
    f.close()    
    Green('---> Runing madanalysis5, for Hadron level')
    
    mad = open ('setup.sh','w+')
    mad.write('''#!/bin/bash
./bin/ma5 -s -f -H gen.txt &>/dev/null''')
    os.system('chmod 777 setup.sh')
    gen = open ('gen.txt','w+')
    gen.write('''define l = l+ l-
define j = p
define mu = mu+ mu-
define ta = ta+ ta-
define e = e- e+
''')
    for zz in range(0,Number_of_lhe_files):
        lhe = str(LesHouches[zz])
        name = lhe.rsplit(".")
        gen.write('import %s as %s \n'%(str(path+'/'+str(run_name)+'/'+str(name[0])+'_pythia.hepmc'),str(name[0])))
        f = open(str(path)+'/'+str(run_name)+'/'+str(name[0])+'_pythia.log','r')
        for line in f :
            if str('| sum                                                |') in line :
                o = line.rsplit()
                m = float(o[7])*1e+09
                gen.write('set %s.xsection = %s \n'%(str(name[0]),str(m)))
    gen.write(str(madanalysis_commands)+'\n')
    gen.write('submit gen')
    mad.close()
    gen.close()
    os.system('./setup.sh >/dev/null')
    os.system('cp -rf %s/madanalysis5/gen/PDF/selection_* %s'%(str(path),(str(path)+'/'+str(run_name)+'/Hadron_plots/')))
    os.system('cp -rf %s/madanalysis5/gen/Histo/selection_* %s'%(str(path),(str(path)+'/'+str(run_name)+'/Hadron_plots/')))
    os.system('cp -rf %s/madanalysis5/gen/PDF/main.pdf %s'%(str(path),(str(path)+'/'+str(run_name)+'/Hadron_plots/')))
    os.system('cp -rf %s/madanalysis5/gen.txt %s'%(str(path),(str(path)+'/'+str(run_name)+'/Hadron_plots/')))
    os.remove('setup.sh')
    shutil.rmtree(str(path)+'/madanalysis5/gen/')




########################################
if (madanalysis == 'on' and pythia !='on'):
    Red('WARNING:')
    yes1_no1('Pythia is off, and madAnalysis will proceed in parton level, do you want to continue?')
    os.mkdir(str(path)+'/'+str(run_name)+'/parton_plots')
    os.chdir(str(path)+'/madanalysis5')
    root=open (str(path)+'/madanalysis5/madanalysis/input/installation_options.dat')
    f = open ('fout','w+')
    for y in root:
        if str ('# fastjet_veto     = 0') in y:
            y = y.replace('# fastjet_veto     = 0',' fastjet_veto     = 1')
        f.write(y)
    os.rename('fout',str(path)+'/madanalysis5/madanalysis/input/installation_options.dat')
    f.close()    
    Green('---> Runing madanalysis5, for Parton level only')
    
    mad = open ('setup.sh','w+')
    mad.write('''#!/bin/bash
./bin/ma5 -s -f gen.txt &>/dev/null''')
    os.system('chmod 777 setup.sh')
    gen = open ('gen.txt','w+')
    gen.write('''define l = l+ l-
define j = u u~ d d~ c c~ s s~ g
define mu = mu+ mu-
define ta = ta+ ta-
define e = e- e+
''')
    for zz in range(0,Number_of_lhe_files):
        lhe = str(LesHouches[zz])
        name = lhe.rsplit(".")
        gen.write('import %s as %s \n'%(str(path+'/'+str(run_name)+'/'+str(lhe)),str(name[0])))
        m = raw_input (" Please enter the cross section for '%s' in Pb \n"%str(lhe)) 
        gen.write('set %s.xsection = %s \n'%(str(name[0]),str(m)))
    gen.write(str(madanalysis_commands)+'\n')
    gen.write('submit gen')
    mad.close()
    gen.close()
    os.system('./setup.sh >/dev/null')
    os.system('cp -rf %s/madanalysis5/gen/PDF/selection_* %s'%(str(path),(str(path)+'/'+str(run_name)+'/parton_plots/')))
    os.system('cp -rf %s/madanalysis5/gen/Histo/selection_* %s'%(str(path),(str(path)+'/'+str(run_name)+'/parton_plots/')))
    os.system('cp -rf %s/madanalysis5/gen/PDF/main.pdf %s'%(str(path),(str(path)+'/'+str(run_name)+'/parton_plots/')))
    os.system('cp -rf %s/madanalysis5/gen.txt %s'%(str(path),(str(path)+'/'+str(run_name)+'/parton_plots/')))
    os.remove('setup.sh')
    shutil.rmtree(str(path)+'/madanalysis5/gen/')
       
    
Yellow('''  All files and plots are in %s ,
          Good Bye              
    '''%(str(path)+'/'+str(run_name)))    
