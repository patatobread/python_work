print("You walk into the chamber in the desert... the doors slam shut, darkness falls, flames ignite, and the massive statue awakens to speak!")
print(r'''                                   _
                                 ,d8b,
                         _,,aadd8888888bbaa,,_
                    _,ad88P"""8,  I8I  ,8"""Y88ba,_
                  ,ad88P" `Ya  `8, `8' ,8'  aP' "Y88ba,
               ,d8"' "Yb   "b, `b  8  d' ,d"   dP" `"8b,
              dP"Yb,  `Yb,  `8, 8  8  8 ,8'  ,dP'  ,dP"Yb
           ,ad8b, `Yb,  "Ya  `b Y, 8 ,P d'  aP"  ,dP' ,d8ba,
          dP" `Y8b, `Yb, `Yb, Y,`8 8 8',P ,dP' ,dP' ,d8P' "Yb
         ,88888888Yb, `Yb,`Yb,`8 8 8 8 8',dP',dP' ,dY88888888,
         dP     `Yb`Yb, Yb,`8b 8 8 8 8 8 d8',dP ,dP'dP'     Yb
        ,8888888888b "8, Yba888888888888888adP ,8" d8888888888,
        dP        `Yb,`Y8P""'             `""Y8P',dP'        Yb
       ,88888888888P"Y8P'_.---.._     _..---._`Y8P"Y88888888888,
       dP         d'  8 '  ____  `. .'  ____  ` 8  `b         Yb
      ,888888888888   8   <(@@)>  | |  <(@@)>   8   888888888888,
      dP          8   8    `"""         """'    8   8          Yb
     ,8888888888888,  8          ,   ,          8  ,8888888888888,
     dP           `b  8,        (.-_-.)        ,8  d'           Yb
    ,88888888888888Yaa8b      ,'       `,      d8aaP88888888888888,
    dP               ""8b     _,gd888bg,_     d8""               Yb
   ,888888888888888888888b,    ""Y888P""    ,d888888888888888888888,
   dP                   "8"b,             ,d"8"                   Yb
  ,888888888888888888888888,"Ya,_,ggg,_,aP",888888888888888888888888,
  dP                      "8,  "8"\x/"8"  ,8"                      Yb
 ,88888888888888888888888888b   8\\x//8   d88888888888888888888888888,
 8888bgg,_                  8   8\\x//8   8                  _,ggd8888
  `"Yb, ""8888888888888888888   Y\\x//P   8888888888888888888"" ,dP"'
    _d8bg,_"8,              8   `b\x/d'   8              ,8"_,gd8b_
  ,iP"   "Yb,8888888888888888    8\x/8    8888888888888888,dP"  `"Yi,
 ,P"    __,888              8    8\x/8    8              888,__    "Y,
,8baaad8P"":Y8888888888888888 aaa8\x/8aaa 8888888888888888P:""Y8baaad8,
dP"':::::::::8              8 8::8\x/8::8 8              8:::::::::`"Yb
8::::::::::::8888888888888888 8::88888::8 8888888888888888::::::::::::8
8::::::::::::8,             8 8:::::::::8 8             ,8::::::::::::8
8::::::::::::8888888888888888 8:::::::::8 8888888888888888::::::::::::8
8::::::::::::Ya             8 8:::::::::8 8             aP::::::::::::8
8:::::::::::::888888888888888 8:::::::::8 888888888888888:::::::::::::8
8:::::::::::::Ya            8 8:::::::::8 8            aP:::::::::::::8
Ya:::::::::::::88888888888888 8:::::::::8 88888888888888:::::::::::::aP
`8;:::::::::::::Ya,         8 8:::::::::8 8         ,aP:::::::::::::;8'
 Ya:::::::::::::::"Y888888888 8:::::::::8 888888888P":::::::::::::::aP
 `8;::::::::::::::::::::""""Y8888888888888P""""::::::::::::::::::::;8'
  Ya:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::aP
   "b;:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;d"
    `Ya;::::::::::::::::::::::::::::::::::::::::::::::::::::::::;aP'
      `Ya;:::::::::::::::::::::::::::::::::::::::::::::::::::;aP'
         "Ya;:::::::::::::::::::::::::::::::::::::::::::::;aP"
            "Yba;;;:::::::::::::::::::::::::::::::::;;;adP"
                `"""""""Y888888888888888888888P"""""""'

''')
print("How dare you, mortal, disrupt me! You have no way out now... the quiz has begun!")
name = input("Mortal, speak your name: ")
print(f"Answer wisely,{name}... for each mistake brings torment!")
rivername = input(f"{name}..What river gave life to my kingdom? Answer with letters:\nA)Amazon\nB)Nile\nC)Tigris\nD)Danube\n ")
if rivername.lower() == "b": #Nile river is the answer of quetsion 1
    print("Your answer is accepted.")
else:
    print(" Wrong word! The chamber rejects you...")
    print('''
        ,.   (   .      )        .      "
   ("     )  )'     ,'        )  . (`     '`
 .; )  ' (( (" )    ;(,     ((  (  ;)  "  )"
 _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '..\nFlames erupt,scorching your path... You are dead now.
    ''')
    exit()
greattombs = input("Now mortal next question of the quiz...\nWhich great tomb pierce the skies of Giza?Answer with letters:\nA)The Hanging Gardens\nB)The Colosseum\nC)The Pyramids\nD)The Great Wall\n ")
if greattombs.lower() == "c": print("Your answer is accepted.")
else:
    print('''
    
                     _.---._     .---.
            __...---' .---. `---'-.   `.
  ~ -~ -.-''__.--' _.'( | )`.  `.  `._ :
 -.~~ .'__-'_ .--'' ._`---'_.-.  `.   `-`.
  ~ ~_~-~-~_ ~ -._ -._``---. -.    `-._   `.
    ~- ~ ~ -_ -~ ~ -.._ _ _ _ ..-_ `.  `-._``--.._
     ~~-~ ~-_ _~ ~-~ ~ -~ _~~_-~ -._  `-.  -. `-._``--.._.--''. ~ -~_
         ~~ -~_-~ _~- _~~ _~-_~ ~-_~~ ~-.___    -._  `-.__   `. `. ~ -_~
              ~~ _~- ~~- -_~  ~- ~ - _~~- _~~ ~---...__ _    ._ .` `. ~-_~
                ~ ~- _~~- _-_~ ~-_ ~-~ ~_-~ _~- ~_~-_~  ~--.....--~ -~_ ~
                     ~ ~ - ~  ~ ~~ - ~~-  ~~- ~-  ~ -~ ~ ~ -~~-  ~- ~-~
    ''')
    print("Crocodiles snap their jaws beneath you....You are dead now..")
goddworshiped = input(f"Well {name}, so far you are safe.. Next question:\nI was worshipped as the sun god. Who am I?\nA)Osiris\nB)Ra\nC)Anubis\nHorus\n  ")
if goddworshiped.lower() == "b":
    print("Your answer is accepted.")
else:
    print(r"""
    T  <|>  (|||)   . .    _   _     .   .
        |     |    ( | )  / \|/ \  .` \_/ `.    __
              |     `|`   \_/|\_/  .   #   .  .`  `//``.
                     |       |      `./#\.`   .   //   .
                     |       |         #       ``//\_.`
                             |         #        //
                                       #       //
                                       #      // 
    ------------------------------------------------
    """)
    print("Blades swing from the walls..You are dead now..")
    exit()
scriptquest = input(f" Once again you found the answer {name}, let's see if you will find the answer of this:\nWhat script of sacred signs did my scribes carve upon stone?\nA)Cuneiform\nB)Hieroglyphics\nC)Latin\nD)Arabic\n  ")
if scriptquest.lower() == "b":
    print("Your answer is accepted.")
else:
    print('''
                        _,..,,,_
                   '``````^~"-,_`"-,_
     .-~c~-.                    `~:. ^-.
 `~~~-.c    ;                      `:.  `-,     _.-~~^^~:.
       `.   ;      _,--~~~~-._       `:.   ~. .~          `.
        .` ;'   .:`           `:       `:.   `    _.:-,.    `.
      .' .:   :'    _.-~^~-.    `.       `..'   .:      `.    '
     :  .' _:'   .-'        `.    :.     .:   .'`.        :    ;
     :  `-'   .:'             `.    `^~~^`   .:.  `.      ;    ;
      `-.__,-~                  ~-.        ,' ':    '.__.`    :'
                                   ~--..--'     ':.         .:'
                                                   ':..___.:'
---------------------------------------------------------------------------
    ''')
    print("Venomous snakes slither from the shadows, striking at your feet...You are dead now..")
    exit()
journal = input("The final question mortal, the sand of eternity will be yours if you find the answer:\nMy soul journeys through the underworld in search of rebirth. What is this passage called?\nA)Valhalla\nB)Duat\nC)Hades\nC)Nirvana\n  ")
if journal.lower() == "b":
    print("Your answer is accepted.")
    print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."-` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/___eli__
*******************************************************************************\n
You have proven wisdom. The sands of eternity are yours.
    ''')
else:
    print("""
                                 ____
                     __,-~~/~    `---.
                   _/_,---(      ,    )
               __ /        <    /   )  )___
- ------===;;;'====------------------===;;;===----- -  -
                 ( ~~  ~"~"~"~"~"~)~"~)~"/
                  (_ (  (     >    |/)
                   (_( _ <         >_>'
                      ~ `-i' ::>|--"
                          I;|.|.|
                         <|i::|i|`.
                        (` ^'"`-' ")
------------------------------------------------------------------\n The chamber collapses, sealing you in eternal darkness...Game is over.....
    """)
    exit()
