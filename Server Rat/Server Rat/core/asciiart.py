import random
import string
def get_ascii(nude='no'):
    
    ASCII_CHRISTMAS = ['''
                        _...
                  o_.-"`    `\
           .--.  _ `'-._.-'""-;     _
         .'    \`_\_  {_.-a"a-}  _ / \
       _/     .-'  '. {c-._o_.){\|`  |
      (@`-._ /       \{    ^  } \\ _/
       `~\  '-._      /'.     }  \}  .-.
         |>:<   '-.__/   '._,} \_/  / ())  
         |     >:<   `'---. ____'-.|(`"`
         \            >:<  \\_\\_\ | ;
          \                 \\-{}-\/  \
           \                 '._\\'   /)
            '.                       /(
              `-._ _____ _ _____ __.'\ \
                / \     / \     / \   \ \ 
             _.'/^\'._.'/^\'._.'/^\'.__) \
         ,=='  `---`   '---'   '---'      )
         `"""""""""""""""""""""""""""""""`''','''
        
                        .------,
          .\/.          |______|
        _\_}{_/_       _|_Ll___|_
         / }{ \       [__________]          .\/.
          '/\'        /          \        _\_\/_/_
                     ()  o  o    ()        / /\ \
                      \ ~~~   .  /          '/\'
                 _\/   \ '...'  /    \/_
                  \\   {`------'}    //
                   \\  /`---/',`\\  //
                    \/'  o  | |\ \`//
                    /'      | | \/ /\
       __,. -- ~~ ~|    o   `\|      |~ ~~ -- . __
                   |                 |
                   \    o            /
                    `._           _.'
                       ^~- . -  ~^ ''']
    
    
    ASCII_NUDE = ['''
                       

                             . ...
                         .''.' .    '.
                    . '' ".'.:I:.'..  '.
                  .'.:.:..,,:II:'.'.'.. '.
                .':.'.:.:I:.:II:'.'.'.'.. '.
              .'.'.'.'::.:.:.:I:'.'.'.'. .  '
             ..'.'.'.:.:I::.:II:.'..'.'..    .
            ..'.'':.:.::.:.::II::.'.'.'.'..   .
           ..'.'.'.:.::. .:::II:..'.'.'.'.'.   .
          .':.''.':'.'.'.:.:I:'.'.'.'.'.. '..  ..
          ':. '.':'. ..:.::.::.:.'..'  ':.'.'.. ..
         .:.:.':'.   '.:':I:.:.. .'.'.  ': .'.. . ..
         '..:.:'.   .:.II:.:..   . .:.'. '.. '. .  ..
        .. :.:.'.  .:.:I:.:. .  . ..:..:. :..':. .  '.
       .:. :.:.   .:.:I:.:. .    . ..:I::. :: ::  .. ..
       .. :'.'.:. .:.:I:'.        ..:.:I:. :: ::.   . '.
       '..:. .:.. .:II:'         ,,;IIIH.  ::. ':.      .
      .:.::'.:::..:.AII;,      .::",,  :I .::. ':.       .
      :..:'.:II:.:I:  ,,;'   ' .;:FBT"X:: ..:.. ':.    . .
     .. :':III:. :.:A"PBF;.  . .P,IP;;":: :I:..'::. .    ..
     . .:.:II: A.'.';,PP:" .  . ..'..' .: :.::. ':...  . ..
     . .: .:IIIH:.   ' '.' .  ... .    .:. :.:.. :...    .'
     . .I.::I:IIA.        ..   ...    ..::.'.'.'.: ..  . .
      .:II.'.':IA:.      ..    ..:.  . .:.: .''.'  ..  . .
     ..::I:,'.'::A:.  . .:'-, .-.:..  .:.::AA.. ..:.' .. .
      ':II:I:.  ':A:. ..:'   ''.. . : ..:::AHI: ..:..'.'.
     .':III.::.   'II:.:.,,;;;:::::". .:::AHV:: .::'' ..
     ..":IIHI::. .  "I:..":;,,,,;;". . .:AII:: :.:'  . .
     . . IIHHI:..'.'.'V::. ":;;;"   ...:AIIV:'.:.'  .. .
      . . :IIHI:. .:.:.V:.   ' ' . ...:HI:' .:: :. .  ..
      . .  ':IHII:: ::.IA..      .. .A .,,:::' .:.    .
      :.  ...'I:I:.: .,AHHA, . .'..AHIV::' . .  :     ..
      :. '.::::II:.I:.HIHHIHHHHHIHHIHV:'..:. .I.':. ..  '.
   . . .. '':::I:'.::IHHHHHHHHMHMHIHI. '.'.:IHI..  '  '  '.
    ':... .  ''" .::'.HMHI:HHHHMHHIHI. :IIHHII:. . . .    .
     :.:.. . ..::.' .IV".:I:IIIHIHHIH. .:IHI::'.': '..  .  .
   . .:.:: .. ::'.'.'..':.::I:I:IHHHIA.'.II.:...:' .' ... . '..
  '..::::' ...::'.IIHII:: .:.:..:..:III:.'::' .'    .    ..  . .
  '::.:' .''     .. :IIHI:.:.. ..: . .:I:"' ...:.:.  ..    .. ..
     .:..::I:.  . . . .IHII:.:'   .. ..".::.:II:.:. .  ...   . ..
  .. . .::.:.,,...-::II:.:'    . ...... . .. .:II:.::  ...  .. ..
   ..:.::.I .    . . .. .:. .... ...:.. . . ..:.::.   :..   . ..
    .'.::I:.      . .. ..:.... . ..... .. . ..::. .. .I:. ..' .
  .'':.: I.       . .. ..:.. .  . .. ..... .:. .:.. .:I.'.''..
  . .:::I:.       . . .. .:. .    .. ..  . ... .:.'.'I'  .  ...
  . ::.:I:..     . . . ....:. . .   .... ..   .:...:.:.:. ''.''
  '.'::'I:.       . .. ....:. .     .. . ..  ..'  .'.:..:..    '
        :. .     . .. .. .:.... .  .  .... ...   .  .:.:.:..    '.
        :.      .  . . .. .:.... . . ........       .:.:.::. .    .
        :. .     . . . . .. .::..:  . ..:.. .        ::.:.:.. .    .
        :.. .    . . .  . .. ..:.:  .. .. .:. ..     ':::.::.:. .   .
        ':.. .  . . . .. .. ...::' .. ..  . .:. .     V:I:::::.. .   :.
         ::. .  . .. .. ... .:.::  .. .  . .. .. .     VI:I:::::..   ''B
          :.. .   . .. ..:.. ..I:... . .  . .. ... .    VII:I:I:::. .'::
          ':.. . . . .. ..:..:.:I:.:. .  . .. . .:. .    VHIII:I::.:..':
           ::..   . . .. ..:..:.HI:. .      . . .... .   :HHIHIII:I::..:
           ':. .  . .. .. ..:.:.:HI:.    . . .. ..... .   HHHHIHII:I::.'
            :.. .  . . .. .:.:.:.HI:.      . . .. ... .   IHHHHIHHIHI:'
             :..  .  . . .. ..:..IH:.     . . .. .. ,,, . 'HHHHHHHHI:'
             ':..   . . .. ..:.:.:HI..   .  . .. . :::::.  MIH:"""'
              :. . .  . .. ..::.:.VI:.     . . .. .:::'::. HIH
               :..  .  . .. .:.:.:.V:.    . . . ...::I"A:. HHV
                :. .  .  . .. ..:.:.V:.     . . ....::I::'.HV:
                 :. .  . . . .. .:..II:.  . . . ....':::' AV.'
                  :.. . . .. ... .:..VI:. . . .. .:. ..:.AV'.
                  ':.. . .  .. ..:.:.:HAI:.:...:.:.:.:.AII:.
                   I:. .  .. ... .:.:.VHHII:..:.:..:A:'.:..
                   IA..  . . .. ..:.:.:VHHHHIHIHHIHI:'.::.
                   'HA:.  . . .. ..:.:.:HHHIHIHHHIHI:..:.
                    HIA: .  . . .. ...:.VHHHIHIIHI::.:...
                    HIHI:. .  .. ... .::.HHHIIHIIHI:::..
                    HII:.:.  .  .. ... .::VHHIHI:I::.:..
                    AI:..:..  .  . .. ..:.VHIII:I::.:. .
                   AI:. ..:..  .  . .. ..' VHIII:I;... .
                  AI:. .  .:.. .  .  . ...  VHIII::... .
                .A:. .      :.. .  . .. .:.. VHII::..  .
               A:. . .       ::. .. .. . .:.. "VHI::.. .
             .:.. .  .        :.. .:..... .::.. VHI:..
            ... . .  .     . . :.:. ..:. . .::.. VI:..  .
           .. .. .  .    . . ...:... . .. . .:::. V:..  .
          '.. ..  .   .  .. ..:::.... .:. . ..::.. V..  .
        . . .. . .   . . .. ..:::A. ..:. . . .::.. :..
       . .. .. .. . .  . ... ..::IA.. .. . .  ..::. :..  .
      .. .. ... . .  .. .... .:.::IA. . .. . ..:.::. :.  .
     . . . .. .   . . .. ..:..:.::IIA. . .  .. .:.::. :. .
    .. . .  .   . . .. ... ..:.::I:IHA. .  . . ..:.::. . .
   .: ..  .  .   . . ... .:.. .:I:IIHHA. .  . .. .::I:. .
  .::.  .     . . .. ..:. .::.:IIHIIHHHA.  .  .. ..:I:. . .
  A::..      .  .  ...:..:.::I:IHIHIHHHHA.  .  . ..::I:. .
 :HI:.. .       . .. .:.:.::I:IHIHIIHIHHHA. .   .. .::I:. ..
 AI:.. .. .    . .. .:.:.::II:IHIIIHIHIHHHA.  .  . ..::I:. ..
:HI:.. . .   .  . .. .::.:I:IHIHIIIHIHIIHHHA..  . .. .::I:. ..
AI:.:.. .  .  .  ... .::.::I:IHIIHIHIHIHIHIHHA. .  . ..::I:. .
HI:. .. . .  .  . .. .:..::IIHIHIHIIIIWHIIHHMWA.  . . .:::I:. . .
HI:.. . .  .   . .. ..:.::I:IIHHIIHIHIHIHHMMW"  '.. . ..:::II: . .
HI::.. .  .   .  .. .:..:::IIHIHIIWIWIIWMWW" .    .. . ..::III: .  .
HI::... . . .  . ... ..:.:::IIHIWIWIWMWMWW. .  .   . .. .:.:III. .   .
II::.:.. . .  .  .. ......:..IHWHIWWMWMW".. . . . . '... .:.:IHI:..    .
II:I::.. .  .   .  . .....::.:IHWMWWWMW:.. .  .  . .  .:..:::IIHII..
:II:.:.:.. .  .   . ......:.:.:IWWMWWW:.:.. .  .  .  . :...:.:IHHI:..
 HI::.:. . . .  .  . ...:.::.::.VWMWW::.:.:.. .  . .. . :.. ..:IHHI::.'-
 HII::.:.. .  .  . .. .:..:.'.  'WWWI::.::.:.. . .  . .. ':...:II:IIII::
 III::.:... .  .  . ...:.:... .   WII:I::.:.. .  .  .. . . :.:::...::.::
  VII::.:.. . . . .. ...:....      VHI:I::.:.. .  . ... .. .::.:..:.:..:
   VII::.:.. . .  . ..:.::.. .     :HHII:I::.:.. . . .. ..  .'::':......
   III:I::.. .. . . .. .:.:.. .    :VHIHI:I::.:... . . .. .. .':. .. .AH
  AA:II:I::.. . . .  .. ..:.. . .  ::HHIHII:I::.:... .. .. ... .:.::AHHH
 AHH:I:I::.:.. .  . .. ..:.:.. .   ::VHHHVHI:I::.:.:.. ..:. .::.A:.AHHHM
 HHHAII:I::.:.. . . . .. ..:.. . . :::HIHIHIHII:I::.:.. .. .:. ..AHHMMM:
AHHHH:II:I::.:.. . . .. ..:.:.. . .:I:MMIHHHIHII:I:::.:. ..:.:.AHHHMMM:M
HHHHHA:II:I::.. .. . . .. .:... . .:IIVMMMHIHHHIHII:I::. . .. AHHMMMM:MH
HHHHHHA:I:I:::.. . . . ... ..:.. ..:IHIVMMHHHHIHHHIHI:I::. . AHMMMMM:HHH
HHHHHMM:I::.:.. . . . .. ...:.:...:IIHHIMMHHHII:.:IHII::.  AHMMMMMM:HHHH
HHHHHMMA:I:.:.:.. . . . .. ..:.:..:IIHHIMMMHHII:...:::.:.AHMMMMMMM:HHHHH
HHHHHMMMA:I::... . . . . .. ..:.::.:IHHHIMMMHI:.:.. .::AHMMMMMMM:HHHHHHH
VHHHHMMMMA:I::.. . .  . . .. .:.::I:IHHHIMMMMHI:.. . AHMMMMMMMM:HHHHHHHH
 HHHMMMMMM:I:.:.. . .  . . ...:.:IIHIHHHIMMMMMHI:.AHMMMMMMMMM:HHHHHHHHHH
 HHHHMMMMMA:I:.:.. .  .  . .. .:IIHIHHHHIMMMMMH:AMMMMMMMMMMM:HHHHHHHHHHH
 VHHHMMMMMMA:I:::.:. . . . .. .:IHIHHHHHIMMMV"AMMMMMMMMMMMM:HHHHHHHHHHHH
  HHHHHMMMMMA:I::.. .. .  . ...:.:IHHHHHHIM"AMMMMMMMMMMMM:HHHHHHHHHHHHHH
  VHHHHHMMMMMA:I:.:.. . . .  .. .:IHIHHHHI:AMMMMMMMMMMMIHHHHHHHHHHHHHHHH
   VHHHHHMMMMMA:I::.:. . .  .. .:.:IHHHV:MMMMMIMMMMMMMMMMMMMHHHHHHHHV::.
    VHHHHMMMMMMA:::.:..:.. . .. .:::AMMMMMMMM:IIIIIHHHHHHHHHHHHHHHV:::..
     HHHHHMMMIIIA:I::.:.:..:... AMMMMMMMMMM:IIIIIIHHHHHHHHHHHHHHHV::::::
     VHHHHMMIIIIMA:I::::.::..AMMMMMMMMMMM:IIIIIIIHHHHHHHHHHHHHHV::::::::
      HHHHMIIIIMMMA:II:I::AIIIMMMMMMMMMM:IIIIIIIHHHHHHHHHHHHHHV:::::::::
      VHHHHIIIMMMMMMA:I:AIIIIIIMMMMMM:IIIIIIIIHHHHHHHHHHHHHHV::::::::"'
       HHHHHIIMMMMMMIMAAIIIIIIIIMMM:IIIIIIIIHHHHHHHHHHHHHHHV:::::""'
       VHHHIIIIMMMMIIIIIIIIIIIIII:IIIIIIIIHHHHHHHHHHHHHHHV::""'
        VHHIIIMMMMMIIIIIIIIIIIIIIIIIIIIIHHHHHHHHHHHHHHHV
         VHHIMMMMMMMIIIIIIIIIIIIIIIIIHHHHHHHHHHHHHV
          VHHHMMMMMMMMIIIIIIIIIIIHHHHHHHHHHHV
           VHHHMMMMMMMMMMMMMHHHHHHHHHHHHHV''','''
                                    8888  8888888
                  888888888888888888888888
               8888:::8888888888888888888888888
             8888::::::8888888888888888888888888888
            88::::::::888:::8888888888888888888888888
          88888888::::8:::::::::::88888888888888888888
        888 8::888888::::::::::::::::::88888888888   888
           88::::88888888::::m::::::::::88888888888    8
         888888888888888888:M:::::::::::8888888888888
        88888888888888888888::::::::::::M88888888888888
        8888888888888888888888:::::::::M8888888888888888
         8888888888888888888888:::::::M888888888888888888
        8888888888888888::88888::::::M88888888888888888888
      88888888888888888:::88888:::::M888888888888888   8888
     88888888888888888:::88888::::M::;o*M*o;888888888    88
    88888888888888888:::8888:::::M:::::::::::88888888    8
   88888888888888888::::88::::::M:;:::::::::::888888888     
  8888888888888888888:::8::::::M::aAa::::::::M8888888888       8
  88   8888888888::88::::8::::M:::::::::::::888888888888888 8888
 88  88888888888:::8:::::::::M::::::::::;::88:88888888888888888
 8  8888888888888:::::::::::M::"@@@@@@@"::::8w8888888888888888
  88888888888:888::::::::::M:::::"@a@":::::M8i888888888888888
 8888888888::::88:::::::::M88:::::::::::::M88z88888888888888888 
8888888888:::::8:::::::::M88888:::::::::MM888!888888888888888888
888888888:::::8:::::::::M8888888MAmmmAMVMM888*88888888   88888888
888888 M:::::::::::::::M888888888:::::::MM88888888888888   8888888
8888   M::::::::::::::M88888888888::::::MM888888888888888    88888
 888   M:::::::::::::M8888888888888M:::::mM888888888888888    8888
  888  M::::::::::::M8888:888888888888::::m::Mm88888 888888   8888
   88  M::::::::::::8888:88888888888888888::::::Mm8   88888   888
   88  M::::::::::8888M::88888::888888888888:::::::Mm88888    88
   8   MM::::::::8888M:::8888:::::888888888888::::::::Mm8     4
       8M:::::::8888M:::::888:::::::88:::8888888::::::::Mm    2
      88MM:::::8888M:::::::88::::::::8:::::888888:::M:::::M
     8888M:::::888MM::::::::8:::::::::::M::::8888::::M::::M
    88888M:::::88:M::::::::::8:::::::::::M:::8888::::::M::M
   88 888MM:::888:M:::::::::::::::::::::::M:8888:::::::::M:
   8 88888M:::88::M:::::::::::::::::::::::MM:88::::::::::::M
     88888M:::88::M::::::::::*88*::::::::::M:88::::::::::::::M             
    888888M:::88::M:::::::::88@@88:::::::::M::88::::::::::::::M
    888888MM::88::MM::::::::88@@88:::::::::M:::8::::::::::::::*8
    88888  M:::8::MM:::::::::*88*::::::::::M:::::::::::::::::88@@
    8888   MM::::::MM:::::::::::::::::::::MM:::::::::::::::::88@@
     888    M:::::::MM:::::::::::::::::::MM::M::::::::::::::::*8
     888    MM:::::::MMM::::::::::::::::MM:::MM:::::::::::::::M
      88     M::::::::MMMM:::::::::::MMMM:::::MM::::::::::::MM
       88    MM:::::::::MMMMMMMMMMMMMMM::::::::MMM::::::::MMM
        88    MM::::::::::::MMMMMMM::::::::::::::MMMMMMMMMM
         88   8MM::::::::::::::::::::::::::::::::::MMMMMM
          8   88MM::::::::::::::::::::::M:::M::::::::MM
              888MM::::::::::::::::::MM::::::MM::::::MM
             88888MM:::::::::::::::MMM:::::::mM:::::MM
             888888MM:::::::::::::MMM:::::::::MMM:::M
            88888888MM:::::::::::MMM:::::::::::MM:::M
           88 8888888M:::::::::MMM::::::::::::::M:::M
           8  888888 M:::::::MM:::::::::::::::::M:::M:
              888888 M::::::M:::::::::::::::::::M:::MM
             888888  M:::::M::::::::::::::::::::::::M:M
             888888  M:::::M:::::::::@::::::::::::::M::M
             88888   M::::::::::::::@@:::::::::::::::M::M
            88888   M::::::::::::::@@@::::::::::::::::M::M
           88888   M:::::::::::::::@@::::::::::::::::::M::M
          88888   M:::::m::::::::::@::::::::::Mm:::::::M:::M
          8888   M:::::M:::::::::::::::::::::::MM:::::::M:::M
         8888   M:::::M:::::::::::::::::::::::MMM::::::::M:::M
        888    M:::::Mm::::::::::::::::::::::MMM:::::::::M::::M
      8888    MM::::Mm:::::::::::::::::::::MMMM:::::::::m::m:::M
     888      M:::::M::::::::::::::::::::MMM::::::::::::M::mm:::M
  8888       MM:::::::::::::::::::::::::MM:::::::::::::mM::MM:::M:
             M:::::::::::::::::::::::::M:::::::::::::::mM::MM:::Mm
            MM::::::m:::::::::::::::::::::::::::::::::::M::MM:::MM
            M::::::::M:::::::::::::::::::::::::::::::::::M::M:::MM         
           MM:::::::::M:::::::::::::M:::::::::::::::::::::M:M:::MM
           M:::::::::::M88:::::::::M:::::::::::::::::::::::MM::MMM
           M::::::::::::8888888888M::::::::::::::::::::::::MM::MM
           M:::::::::::::88888888M:::::::::::::::::::::::::M::MM
           M::::::::::::::888888M:::::::::::::::::::::::::M::MM
           M:::::::::::::::88888M:::::::::::::::::::::::::M:MM
           M:::::::::::::::::88M::::::::::::::::::::::::::MMM
           M:::::::::::::::::::M::::::::::::::::::::::::::MMM
           MM:::::::::::::::::M::::::::::::::::::::::::::MMM
            M:::::::::::::::::M::::::::::::::::::::::::::MMM
            MM:::::::::::::::M::::::::::::::::::::::::::MMM
             M:::::::::::::::M:::::::::::::::::::::::::MMM
             MM:::::::::::::M:::::::::::::::::::::::::MMM
              M:::::::::::::M::::::::::::::::::::::::MMM
              MM:::::::::::M::::::::::::::::::::::::MMM
               M:::::::::::M:::::::::::::::::::::::MMM  
               MM:::::::::M:::::::::::::::::::::::MMM
                M:::::::::M::::::::::::::::::::::MMM
                MM:::::::M::::::::::::::::::::::MMM
                 MM::::::M:::::::::::::::::::::MMM
                 MM:::::M:::::::::::::::::::::MMM
                  MM::::M::::::::::::::::::::MMM
                  MM:::M::::::::::::::::::::MMM
                   MM::M:::::::::::::::::::MMM
                   MM:M:::::::::::::::::::MMM
                    MMM::::::::::::::::::MMM
                    MM::::::::::::::::::MMM
                     M:::::::::::::::::MMM
                    MM::::::::::::::::MMM
                    MM:::::::::::::::MMM
                    MM::::M:::::::::MMM:
                    mMM::::MM:::::::MMMM
                     MMM:::::::::::MMM:M
                     mMM:::M:::::::M:M:M
                      MM::MMMM:::::::M:M
                      MM::MMM::::::::M:M
                      mMM::MM::::::::M:M
                       MM::MM:::::::::M:M
                       MM::MM::::::::::M:m
                       MM:::M:::::::::::MM
                       MMM:::::::::::::::M:
                       MMM:::::::::::::::M:
                       MMM::::::::::::::::M
                       MMM::::::::::::::::M
                       MMM::::::::::::::::Mm
                        MM::::::::::::::::MM
                        MMM:::::::::::::::MM
                        MMM:::::::::::::::MM
                        MMM:::::::::::::::MM
                        MMM:::::::::::::::MM
                         MM::::::::::::::MMM
                         MMM:::::::::::::MM
                         MMM:::::::::::::MM
                         MMM::::::::::::MM
                          MM::::::::::::MM
                          MM::::::::::::MM
                          MM:::::::::::MM
                          MMM::::::::::MM
                          MMM::::::::::MM
                           MM:::::::::MM
                           MMM::::::::MM
                           MMM::::::::MM
                            MM::::::::MM
                            MMM::::::MM
                            MMM::::::MM
                             MM::::::MM
                             MM::::::MM
                              MM:::::MM
                              MM:::::MM:
                              MM:::::M:M
                              MM:::::M:M
                              :M::::::M:
                             M:M:::::::M
                            M:::M::::::M
                           M::::M::::::M
                          M:::::M:::::::M
                         M::::::MM:::::::M
                         M:::::::M::::::::M
                         M;:;::::M:::::::::M
                         M:m:;:::M::::::::::M
                         MM:m:m::M::::::::;:M
                          MM:m::MM:::::::;:;M
                           MM::MMM::::::;:m:M
                            MMMM MM::::m:m:MM
                                  MM::::m:MM
                                   MM::::MM
                                    MM::MM''','''
                                    

           .:IIIIHIHHIHHHII::I:.
         .IIIIHIHHHHHHIHIIIIMHHI:,
       :IIIIHIHHHHHHMMHHIHHIIHHIII:.
     .:IHIHHHHHHHHHHHHHIHIHHIHHHIH:I:,
    ,.:HIHHHHHHHHHHHHHHHHHHHHHIHIHHII:.
   ,.:IHHHHHHHHHHMMMMHHHHHHHIIHHHIHIII,
  .:IIHHHHHHHHMMMMMHHHHMMMHHMHHHIIIHIIII:
  .IIHHHMMMMMMMHHMMMHHHMMMHHMHII:HHHII:I.
  :HIHHHMHMMMMMMMMMMMMHMHHHHII:HHMMHII:II
 :HHHHMHMMMMMMMMMMMMMMMHIIHIHHMMHHHHII::I:
:IIHHHHHMHMMMMMMMMMMHMMHIHMMMMHHHI:"::IIHII:
:IHHHHHMHMMMMMMMMMMMMHHI:II::I:"' .   '"IHH.
::HHHHMHMMMMMMMMMMHMHHI:II::.'  .       'VMA.
IHHHHHMHNMMMMMMMMHMHHI:II:. . .          "MMH.
HHHHHMHMMMMMMMMMMHMHI:I::.' .  . .      .,MMM:.
HHHHMHMMMMMMMMMMMHMHI:II:. ..  .    ..LI:"IMMI.
HMHMMMMMMMMMMMMMMHMHI:II.'.        :HT;.,, VHI:
HHHHHMHMMMMMMMMMHMHHHI:HMHII:,.   ':,MHP"HPIHII.
IHHHHMHMMMMMMMMMHMHHHII::IT:.I:.  'HMMH ,:" VII:
:HHHHHHHMHMMMMMHMHHHHIIMMMPVHI::. .P"TIT"'  IH:I
HHIHHHHHHMHMMMMHMHHHHH:VMMM:.HI:H:. :. . . .II:I.
:HHHHHMHMMMMMHMHHHHIIHMMHHI:.:HI:. . .. .   :III;
IHHHHMHMMMMMMMHHHHHI:IT:TI:..:HI:.. ..:. .  :IHII
 IHHMHMMMMMMMMMMMHHI:I::.:. ..:II::.. :I..  :HIIH.
 'HHHMHMMMMMHMHHHH:II:.. ...:II:II./'::.  ' IHHIH;
  HHMHMMMMMMMHMHHHH:I:I::....::VIHI;, ' . . IHHIHA
  MHHMMMMMMMMMHMHHH:II:::...::II:::.;,,,:   AHHIHH;
  ;HHMHMMMMMMMMHMHH-:II::..:::I::"",,:"''  .HHHIHHI.
  'HHHMHMMMMMMMMHMHHA:II:.:H.::-"'""' ,'. .AMHHIHHH;
   :HHMHMMMMMMMMMMHMHA:II::.::::-;,,:: .. :AMHI:IHHI
   'HHMHMMMMMMMMMMHMHHA:III:::II:II::. . .AMMHI:IHHH.
    :HHHMHMMMMMMMMMHMHHA:IIIHII:.:::. . .AMMMHI:IHHH:.
    'HHMHMMMMMMMMMMMMHMHHHI:":VIII::...:AMMMMHHI:IHHHI
     ;IHMHMMMMMMMMMMMMMHMHHII:. '"" 'AMMMMMMMHI:IIHHH:I.
     :IMHMMMMMMMMMMMMMMHMHHHII:.  .:IHMMMMMMHHHIHIHHHI::.
     ;HHHMHMMMMMMMMMMMMMMHMHHHI:..IHHMHMMHHHHHIHHHMHH;I:".'
     ;HHHHHMHMMMMMNMMMMMMMHMHHHI::.HHHHMMHHHHHIHIHHHHHI:'
     :HHHHHHHHMHMMMMMMMMMHHHMHHHI:IHHMHMMHHHHHMHIHHHHIHI;
     ;HHHHHHHHMMHMMMMMHMHHMMHIHMI:IIHHHMHHHHMHMHIHIHHHHI:.
     IHHHHHHHHHHMHMMMMMHMHHMMHHMMII:IHHMMHMHHHHMMHMHMHHHH;
     ;HH:":IHHHHMHMMMMMHMHIHMHIIMMHI:IMHMMMI:HHHHHMMHHHHI:I.
    ;HV" . .:IIHHHMMMMMMMHHHMMHIIHMHHI:HHHMHI:IHHIHHIHHMHI:II;.
   ;IV"   . .''":VMMMMMMHMHHHMMHI:HHHHI:HHHIHI:IHHHHHIHHHIHII;,
   .II"   .. .  ':VHHHMHMMMMMHMHHI:HMMHI:IHHHI::IHHHI:HIHHHI:I:.
  .II . . .  . .  ':HHHHMHMMMHMMMHIHIMMMHI:HHHMI:IHHHIHI:HHHHII:I.
 .;V' . .. .  .    'IHMMMHHMHHHMMMHIHIHHHHI:IHHHI:IHHHHHIHHHHHIIHII:.
.:I" .. . .    .   :IHMMMHHHMHHIHHHI:HHIHHHIHIHHHAIHHHHHHI:HHHIHII:.
'..:  .  .       .  :IMMMHMHHIMHIIHHI:IHHI:IHHIHHHHIHIHHHHIHIHHHHIHI:.
.: .. . . .      ..:IHMMMHMHMHMHHHHMHIHHI:.IVIIHHHIHHHHHHHHI:HIHHIHII:.
.: .   . .        . :IHMMMHMIHIH:IIHHHIHH:.I:IIHHHIHHHHHHHHIHI:IHHHI:;.
:: .:. .  .   .   ..:IHHMMMHMIHIH:IIHHHMHH::..:HHHHI:HHHHHHI:I:IIIHII;
:. ... . .  .     ..::HHHMMHMHHII:HIIHHMMHH:..:HHHMHHIHHHI:: . :IHII:I
':....   . .      . ..:IHHHMMMMHMHI:HIHMMMHA...VHMMHHHMI:'  .' :IH::"
 :. ..  ....    .    ..IHHHHMMMMHHII:I:IHMMHA. .VHMHHHI:' ''    '':,
 ::...  . .... .   . ..::IHHHMMMMIHII::I:IHMMHHMHIHIHI''   .  .     ,
 ::.... . .....  ..  ...::IIIHHHMMIHI::IHHHIIIHHHIIHI".  ..   .      ,
 ::.:.......... .. . ....:::HHIIHHHHHHHIIHMMMHI:' 'VI::..  . .        ,
 ::.:............. .. . ...AHIHIIIIIHHHI::""'      'VII:.. ..    .
 ::.:.:.......... .. .  ...HHHIIIIIIHHHI::. .       'VII::. . .       ,
 ':::.:.:..... .. . . . ..:MHHIHIIIII:I::. .         'VII:::. ..      .
  :::::.:..:.... . . . ...AHHHHIHIIII:::. .           'VII:::. . .   :.
  :::::::.:..... .. . ....MHHHHHIHIII::.:.. .          'VII::.  .   ::
  :::::::::.:.... .. ....:MHHHHIHII:I::::...  .         'VI::. .   ::I)
  '::::::::::.:... .. ...:MHHHHIHIIII::::..  .           'VI:.    ...:V
   .:::::::::::.:.... . .AMMHHIHIII:I::::...  .  .        I::.   ...:-"
   :.::I::::::::.:. .  ..MMMHHIHIIII:I:::... .  .        .::.  ,..-"
   :..:II:I:::::.:.. . ..MMMHHIHIIIIIII:I::.... .  .    ..::""'
  .::.:III:I::::::.:.. ..MMMMIVHIHIIIII:I::::.... .   .....:,
.:.::..:III:I:::::.:... .MMHMAIVHHIHIIIII:I::::.. .  ..::..:,
. .:::.::III:I::::.:... .VMMHMAIVHHHIHIIII:I::::..  ..:...:::
. :::I.:::III:I:::.::.. .:MMHHMAIVHHIHIIIII:I::::....:::.::::
 .::IIH.:::III:I::::.:.. .MMHMHMAIVHHHIHIIIIII:I:::.:::::::I)
.::IIHH.II:::II:I::::.:...MMMHMHMAIVHHHHHIHII:I:::..::::::HV
::IIIHIH.III::I:I::::.:. .MHHMHHHIAIIVHHHHIHIII:...::::.:-"
:IIHIHHA.VIHII:I:::::::...HHHHHHIHI::":VHHHII:I:::...:-'
IIHIHHHHI.HHIHII:I:::::...HHHIHII:' .  .'"VIIIII::-'
IHIHHHHH-:HHIHIIII:I::.:..HIHI::. ..  ...:"
HIHHHHIHHH:HHHIHIIII:I::.:HII:'. .   ..:"
HHHHHHMHHHIHHHHHHIHIII::.IHI:.  .    ..:-.,
HHHHHHHMHHIHHHHHHHIHII:..II:'  .    .:"    ''"-.
HHHHHHHMHHIHHHHHHIHII::..I;'. .   ..:"          '"-.
HHHHHHHMHIHHHHHHHHIHI::,.I;' . .   .;"          "- . ",
MMHMHHHHHH-IHHHHHHIHII::.::;.   :.:;.... .             '"-.
MMMHMHHHHHHIHHHHHHIHII::..:.,  .N.:I::.... .               '"-.
MMMMHMHHHHHIHHHHHHIHIII:..:.;. :.:AI:::..... .  .             .'-.
MMMMMHMHHHIHHHHHHHHHIHII:..:.;:.:AIII::::....... .               .':,
MMMMHMHHHHIHHHHHHHHHHIH:I:.:.,::AHIHIII:I::::::::...... .    .  ...::,
MMMHMHHHHHIHVHHHHHHHHHIII::.:.:AHHIHIHIIIII:I:::::::.:....... .. ...::.
MHMHHHIHIIII:HHHHHHHIHII:I:. :AHHHHHHHHHHHIHIIHIIIIIII:I::.:..... ..::.
HHHHIHIIII:I:HHHHHHHHIHII:: .IHHHHHHHHHHHHHHHHHHHHIIHIII:I::::::::::::.
HHIHIIIII:I::VHHHHHHHIHII::. :MHHHHHHHHHHHHHHHHHHHHHHIHIIHIIIIIIIIIIIV
HHIHIIII:I::::MHHHHHHHIII::.. MMMMMMMMMMMMMMMMMMMMHMHHHHHHIIHIIIHIIIV'
HHHIHII:I::I::MHHHHHHIHIII:: .HHIHHHHHIHHHHHHHHIHHIHHHIHHHHIHHIHIHHV'
HHHHIHII:I::::HHHHHHHIHII:I:. MHHHIHHHHHHHIHHHHHHIHHHHHHHIHHHHHHHHV'
MMHHHIHIII:I::HHHHHHHHIHIII: .:MMMMMMMMMMMMMHMHHHHHHHHHHHHHHHHHV:'
II:IHMHHI::::AIHHHHHHHHHIII::. MMMMMMMMMMMMMMMMMMMMMHMHHHHHHHV:'
III:IHMHIAMMMIHHHHHHHHHIHII....MMMMMMMMMMMMMMMMM--"""''
IIIII:I:IIHMMMMMHHHHHHHHHHHII:::"""""""""""""''
IIIII:I:II:.T,  'VHHHHHHHHIHI:::
IIIHIII:I:::.:,  :HHHHHHHHHHIHII
IIIIII:I::::::.,  VHHHHHHHHHHIHI
IIHII:I::::.:..., 'MMMHMHHHHHIHI.
IIII:I:::::.:....:.VMMMHMHHHHHIH.
IIIIII:I::::::.:..:.MMMMMHMHHHHH:
IHIIIIII:II::::.:.:.VMMMMMHMHHHHA.
IIIHIIIHIII:I::::.:..VMMMMMHMHHHHA
IIIIIHIIIIIII:I:::.:..VMMMMHMMHHHH.
IIHIIIIIIHIIIII:I:::..IMMMMMMMHMHHI
HIIIIIHIIIIIIIII:I:.:..VMMMMMHMHHI:.
HIHIIIIHIIIIIHIHI:I::..IMMMMHMHIHI:.
HHIHIIIIIIHIIIIHIHIII:.:MMMMMHMHHI::
HHHIHHHHHHIIIIIIHHHHIHI:MMMMMHMHHII:
HHHHIHIIIHIIIIHIHHHHHHHI..HHHIHIIHI:.
HHHHHHIHIIIIIIIIIHIHH..IHHHHIHI:III:,
HMHHHHHIHIIIIIIIIIHIHMHHIIHIIHI:II:::,
MMHHHHHHHHIHIIIIIIIHMIHIIHHIIIHI:I::..,
MHMHMHHHHHHHHHIHIIH.;I:IIIHHIIHHI:::::.,
MMMMMHMHHHHHHHHIHIH;I:IHIHII:HI:HII::.::.
MMMMMMMMHMHHHHHHHIH;I:IHMHI.:HIIHI:II:IHA
HMMMMMMMMMHMHHHHHHVI::IMHIHHHMH:IH::I:IHH.
HHHMMMMMMMMMMHMHH;I:HHIMHHHHMHHIHHI.:AMHI:
HHHHMMMHHHHMMMMM;I:IIHHIIHAIIIHI:HI:HA:IHI
HIHHHHMMMHHHMMM:II:IMHHIIMIHIIIHIHHIHMMH.I''','''

                          ,.--..
                       ,:'.   .,'V:.::..  .
                     ,::.,..  . . 'VI:I'.,:-.,.
                    :I:I:.. .   .    MHMHIHI:MHHI:I:,.:.
                   :I:I:.. .   .    MHMHIHI:MHHI:I:,.:.
                   A:I::. ...  .   .MMHHIIHIHI:IHHII:.:,
                  .M:I::... ..   . AMMMMMHI::IHII::II.::.
                  IMA'::.:.. .    .MMMMMHHII:IMHIHIA:::',
                  ,MV.:.:.. .     AMMMMHMHI:I:HIHHIIIA;.
                   P.:.:.. .  .  .MMMMMMMHHIIMHHHIIHIIH.
                   :..:.. . .    AMMMMMMMHHI:AMIVHI:HIII:
                  ,:. :.. .  .    MMMMMMMMMH:IHHI:HHI:HIIH.
                  :..:...  .    .MMMHP:'',,,:HHIH:HHH:HIII
                 ;.:..:.. .     AMH:'. , , ,,':HII:HHH:HII:
                 ::..:.. . .   .H:,.. .     ,'.:VA:I:H::HI:
                ;.:.:... ..    A:.,...     .   ,:HA:IHI::I:
               ,::..:. . .    .M::. .    .      ,:HA:HH:II:.
               ;.::... ..     AML;,,,       .    .:VHI:HI:I:;
              ,:.:.:. . .    .H. 'PA,           .:IHH:HHII::.
             ,:.::... ..     A:I:::';, .   .  ,ILIIIH:HI:I:I;
            ,;:.:.:.. . .   .H:TP'VB,)..   .,;T;,,::I:HI:I:::
           ,::.:.:.. . .    AI:.':IAAT:.  .(,:BB,);V::IH:I:I;
         ,::.:.:.. . .    .H:. , . . ..  .':;AITP;I:IIH:I::;,
        ,::.::.:. . . .   A::.   . ..:.  .  . ..:AI:IHII:I::;.
         ;:.::.:.. .  .   AM:I:.   ..:.   .: . .::HIIIHIIHII::.
        ,:::.:.:..  .    .MM:I:..  .:,    .:.  .::HHIIIHIHII::;
       ,::.:..:.. .   .  AMM:I:.  . .,'-'',,. ..::HIHI:HI:III:
       ;:.::..:.. . .   AMMM::. . ,,,, ,..   ,.::IMHIHIHIIHI::;
      ,:::.:..:. .   .  MMMM:I:.  ,:::;;;::;, .::AMHIHIHHIHHI:'
      ;::.:.:.. . .   .:VMMV:A:. .  ,:;,,.'  .::AMMMIHIHHIHHII
     ;::.:.:.. ..  .  .::VM:IHA:. .,,   , . ..:AMMMMHIHHHIHHII:
     ;:::.:.. .  .. . .::P::IHHAA.. .   .. .:AMMMMMMMIIHHIHHI::
     ;::.:.. .  . .  ..:.:VIHHHIHHA::,,,,,:AMMMMMMMMMHIIHHHHII;
     ;.::.. .    . .  ..:.;VHHIHI:IHIHHIHI:MMMMMMMMMMHIHHIHHII:
     ::.:.. .     ..  ...:.::VHI:IIVIHIHII:MMMMMMMMMMMIHHIHHII:,
     ;:..:. .    ..  . ..:.::::VAII:IIIIII:MMMMMMMMMMMIHHIIHIIHI
     ,;:.. .        . .. ..:...:.VII::III:.VMMMMMMMMMHIHHHIHI::I,
      ;:. . .    , . .. ... . .::.::V::II:..VMMMMMMMMHIHHHIHI::I;
      ;:.. . .     . .. ..:..  .::...:VIITPL:VMMMMMMMVIHHHIH:. :;
      ;:. .  .    . .. ... .   ..:.:.. .:IIIA:.MMMMMVI:HIHIH:. .:
      I:. . .   . .. . .. . . . . ..:.. ..::IIA.VMMMVIHIIHIV:. .,
      I:..    . . .. .... .  .   . .. ... .:.:IA:.VMVIMHIHIH:..:
      I.. .  .  . ..... .       .  . .. . .. .:IIAV:HIMHHIHII:.;
      :. ..   . . .:.. .          .  .. ... ..::.:CVI:MHHIHHI...
      :..  . . .. ..:.               . . ... .:.:::VHA.VIHHMI:..
      :. .. .  . ..:..        . .     . .  ..  .. ...:VIIHIHI: .
      ,:.. .  . .::. .       .::,.      .    .  . .  ...V:IHII..
       ;:.. .. .:I:.        ..:T'::.     .  . .  .  . .  .VIIH:.
       ;:.:.. .:I:..        .::V:::.         . . . .  .    VIII..
       ;:.. ..::::. .        ..::. .      .  . .. . .  .    VIII.
       I:.:.. .:I:.           ..:.,        . . .. :. .  .    'VI:.
       I::......::.  .                    . .. .:.:.:. .       'I:
       II::.. ..::. .       .    .     . .. .. .::::.. .      .:.
       II::.:. ..::. .  . .   .    .     .:. . .:I:::. .       .::HD
       ,I:::.. .: . .. ..  .. . .    .  .::. . .:I:. .         .:V:
        I:. .. .  . . ... ..  .. . .    .. ..  ..::.             .:.
        I:.. .. .  ..:.. .. .. ..  . .      .   .                . :
        ;:.... . ..:::I:.. ..:.. ... .::. . ... . ..              .I.
        ::.:....::.::I:III:I::::I:II:I::.. .:.. . .:. .     .  . .AI:
        ,::.:...:..::::::III::II::::::.. ...::. .  .::. . .. .  .AMMI.
          :::.:.:. ..::::III:II:I:::.:. .. ..::.. ..  ..::,.  ..::HMMI:
         ,:::.:.. ...::I:::I:I:::.:.. :. . ..::.. . . . .,PTIHI:IIHHI:.
          ::I::.:...:::II:I::.:....:.:. . ...::. .  . .  .AI:IHI,,:,  ,.
          ,:::.:... ..I::I::.:....:. .: .. ...::. .  .   III:II:.  ,
           ,I:::..:...:.::I::.:..:. .: .. . ..:... .  .  III.I,
            VI:::.::.::...:II::...:...:. . . .:::. . .   :,,
            ,HI:I::.::.::..:II::.:..:.... . .:.:I:.. .   :
             VI:I:I::.::.:...:I:::I:::.... ..:.:I::...   :
             ,II:I::II:I:::.:.:I:III:I:... ....::::... .  :
              VII::I::I::.::..:.::II::.:.. . .:.::::. .   .
               VI:.:..::II:::..:..::.... .   ..::I::...  . .
               ,I::.. ..::II::..:.::.... . ...::I:::.   .  .
                V::.:.. .:I:II::.:..::.. .. ...:::I::..  . . .
                I:::.:....::III:::.:..:.:.. .:.:II:::. .  . . .
                I::.:::...:::II::.:.:.:... ...:II::.. . . . .  .
                I::..:...:.:::.:.:.:.:..:.. .:II:. .. .    . .   .
               .::.:.:....:.:::.:.:.:.:.: . .:I:... . . . . .  .  .
               :.:.:...:.:.:::.::.:.::.... .:::.. .. .  . .  . .
              .:. ..:.:.:::.:..::.::.:.. . .::.. .. . . .  . . .   :
             .:. .:....::..:.:.:.:.:... .. .NI:.. . .. . . .  . .  :.
            .:. . . ..:.:.::.::.::.::.::.. . :.:.. .. .. . . . . . .)O
           .:.. ... .. ..:.::.::.:::.:..:.. . ..:.. .. .. . .. . . ,()
           ::.:. ...:.. ..:..::..::.:.:.:.:. .:.:... .. .. .:.. ..0OO.
          /:::.:...:.:..:..:..::.::.::.:..:..:.:..:.... ..:.:..:.()',
        (0):::.::...:..:..:...::::I:.:I:.:.:.::.::..:.:...:..::O0O... .
         : ::.:..:.:..:.:..:.:I:.::I:::I::.:I::.I:.::..:.:.::.:/0O/.. .
        .:: ::I:.:..::.::.::.::I:::I::.:I::.::I::.:::.::.I::( ):.:..  .
        '.:: ::I:.:..::.::.::.::I:::I::.:I::.::I::.:::.::.:I::( ):.:.. .
        ::I:::,(,,)OO::.:.::.::III:::III::III::I:::::.:I:'V0O:., .   .
       .:::I::I::-:000::..:::.::::III:I::I::II::I:::IIII( ),) .    . . .
       .:.::I::II:I(,)(  )00):.::.::II:I:II:I:I:::III0OO'.M:M.   . . .
       .. .:.::.:I:I:IIHHI000 ,)OO:II:O:II:III::OO(')00//XXVM . .. . . .
       . .. ..:.::.::II:II:III,(0O0'')!0:III:(0OO)..AMV AXXXXI .. .. . .
       . :.. . .::I:IIIHHII:IHIHH(0),,0OOO( )M00AMMHMM,,XXXXXX.. . .  .
      .:.:.:.. . ..:IHHHII::::.,.MMIIIMMXIMMMMMMMMMMV AXXXV:MI. .. .  .
      ::.:.:.:.:.. . ,,., .. ..:.MMIII:MMIMMMMMMMMMMMM, .X::M.MI.. . . .
     .::.::..::.:.:.:. .  .. .::AMMXXXIAMHMMIHMMMMMMV ...::M.MM ... . ..
     ::.::.::.::.::.:.:.. . .:::MMXXXXI:.:VMMHMPMHVMI ..:I:H-,',,.:. . .
    ::.::..:.:.:..:.:.::.:. . .:MMXXX:IXX:MMMMMLMMAM, ..I:M.  :  ,:.. .
   .::.:..:...:...::.:.::I::...IMM:XXX:XX:LMMMMMI:MV  ..I:V   .   :... .
   :.:.:..:.:.:..:..:::II:II:'..M'.VMXX:XXMMMMMMMI.I ...IVI   .  .::. ..
  :.:.:.:.:.:.::...:.::IHI, - . .'VIMHX:XIIMMV/IMLMI ...HV     .  ::.. .
 .::.:.:.:.:..:.. ..::IHI:-.  . .  ',IX:XXIVMI XMMV I...HI    .   :::...
.::.:.:.:.:.:.. ...:.:IHHHI:., .    .XXX:XX.MMAXMHA I..AMI    .    ::...
::.::.::.:.:.... .:.:IHHIHI'. ..    :XXX:XX:MHHIMMMAI,AHHI     .  :::...
:::.:.:.:.:.:.. .:.::IHHHHI:  ..   ,:XXX:XX:MV''.I,V:,:HHI.    .   :::..
::.::.:.:..:.. ...::IIHHHHI:   .   :.XXX:XXXI:.,.    '-VH:    .    ::.:.
:::.::..:..:.. ..:.:IHHHHHI,   .    ::XX:XXXI:.A. .  'VHH      .   :::..
::.::.::.:... ...:::IIHHHIH   ..    :IAX:XXXIHHH:  .  .:MI    .   .:::..
:::.::.:..... ..:.::IIHHIHH   .     ::XX:IXXIHHV .     'V. . . .  :I:::.
:.::.:.:... ...:.::IIIHHHIH    .    I:XX:XXVHMMI .      I.. .:. . .I::.:
::.:::.:.... ..:.::IIIHIHHH.  .     :'XX:XXXVIVI  . .   ::..:. . .I::::.
''']
    if(nude == "y"):
        rannudenum = random.randint(0,len(ASCII_NUDE) - 1)
        return ASCII_NUDE[rannudenum]
    else:
        rannum = random.randint(0,len(ASCII_CHRISTMAS) - 1)
        return ASCII_CHRISTMAS[rannum]

def get_banner():
    banner = [''' 
___________.__                  ____.                    .__          
\__    ___/|  |__   ____       |    |__ __  ____    ____ |  |   ____  
  |    |   |  |  \_/ __ \      |    |  |  \/    \  / ___\|  | _/ __ \ 
  |    |   |   Y  \  ___/  /\__|    |  |  /   |  \/ /_/  >  |_\  ___/ 
  |____|   |___|  /\___  > \________|____/|___|  /\___  /|____/\___  >
                \/     \/                      \//_____/           \/ 
    ''']
    return banner[0]
    