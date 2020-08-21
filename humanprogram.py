import pyttsx3
import os



pyttsx3.speak("How can i help you")

while True:
	print("How can i help you : " , end = '')
	p = input()
	

	if (("run" in p.lower())  or  ("open" in p.lower())  or  ("launch" in p.lower()))  and (("chrome" in p.lower()) or ("google" in p.lower())):
	  if (("don't" in p.lower()) or ("dont" in p.lower()) or ("do not" in p.lower())):
	    pyttsx3.speak("ok, i will not")
	    print("ok i will not")
	  else:
	    pyttsx3.speak("launching google chrome ")
	    os.system("chrome")

	elif (("run" in p.lower())  or  ("open" in p.lower())  or  ("launch" in p.lower()))  and (("camera" in p.lower()) or ("cam" in p.lower())):
	  if (("don't" in p.lower()) or ("dont" in p.lower()) or ("do not" in p.lower())):
	    pyttsx3.speak("ok, i will not")
	    print("ok i will not")
	  else:
	    pyttsx3.speak("launching windows camera ")
	    os.system("start microsoft.windows.camera:")

	elif (("run" in p.lower())  or  ("open" in p.lower())  or  ("launch" in p.lower()))  and (("calculator" in p.lower())):
	  if (("don't" in p.lower()) or ("dont" in p.lower()) or ("do not" in p.lower())):
	    pyttsx3.speak("ok, i will not")
	    print("ok i will not")
	  else:
	    pyttsx3.speak("launching calculator ")
	    os.system("start calculator:")

	elif (("run" in p.lower()) or  ("open" in p.lower())  or  ("launch" in p.lower())) and  (("notepad" in p.lower()) or ("editor" in p.lower())):
	  if (("don't" in p.lower()) or ("dont" in p.lower()) or ("do not" in p.lower())):
	    pyttsx3.speak("ok, i will not")
	    print("ok i will not")
	  elif (("notepad" in p.lower()) and ("++" in p.lower())):
	    pyttsx3.speak("launching notepad++")
	    os.system("notepad++")
	  else:
	    pyttsx3.speak("launching notepad ")
	    os.system("notepad")

	elif (("run" in p.lower()) or ("open" in p.lower()) or ("launch" in p.lower()))  and ((("player" in p.lower()) and ("media" in p.lower())) or ("vlc" in p.lower())):
	  if (("don't" in p.lower()) or ("dont" in p.lower()) or ("do not" in p.lower())):
	    pyttsx3.speak("ok, i will not")
	    print("ok i will not")
	  else:
	    if (("run" in p.lower()) or ("open" in p.lower()) or ("launch" in p.lower())) and ("vlc" in p.lower()):
	      pyttsx3.speak("launching vlc media player")
	      os.system("vlc")
	    else:
	      pyttsx3.speak("launching windows media player")
	      os.system("wmplayer")

	elif (("run" in p.lower()) or ("open" in p.lower()) or ("launch" in p.lower())) and ("scilab" in p.lower()):
	  if (("don't" in p.lower()) or ("dont" in p.lower()) or ("do not" in p.lower())):
	    pyttsx3.speak("ok, i will not")
	    print("ok i will not")
	  else:
	    pyttsx3.speak("launching skylab ")
	    os.system("scilab")

	elif (("run" in p.lower()) or ("open" in p.lower()) or ("launch" in p.lower())) and ("spotify" in p.lower()):
	  if (("don't" in p.lower()) or ("dont" in p.lower()) or ("do not" in p.lower())):
	    pyttsx3.speak("ok, i will not")
	    print("ok i will not")
	  else:
	    pyttsx3.speak("launching spotify")
	    os.system("spotify")

	elif (("run" in p.lower()) or ("open" in p.lower()) or ("launch" in p.lower())) and ("word" in p.lower()):
	  if (("don't" in p.lower()) or ("dont" in p.lower()) or ("do not" in p.lower())):
	    pyttsx3.speak("ok, i will not")
	    print("ok i will not")
	  else:
	    pyttsx3.speak("launching microsoft word")
	    os.system("start winword")

	elif (("run" in p.lower()) or ("open" in p.lower()) or ("launch" in p.lower())) and ("excel" in p.lower()):
	  if (("don't" in p.lower()) or ("dont" in p.lower()) or ("do not" in p.lower())):
	    pyttsx3.speak("ok, i will not")
	    print("ok i will not")
	  else:
	    pyttsx3.speak("launching microsoft excel")
	    os.system("start EXCEL")

	elif (("run" in p.lower()) or ("open" in p.lower()) or ("launch" in p.lower())) and (("store" in p.lower()) and ("windows" in p.lower())):
	  if (("don't" in p.lower()) or ("dont" in p.lower()) or ("do not" in p.lower())):
	    pyttsx3.speak("ok, i will not")
	    print("ok i will not")
	  else:
	    pyttsx3.speak("launching windows store")
	    os.system("start ms-windows-store:")

	elif (("run" in p.lower()) or ("open" in p.lower()) or ("launch" in p.lower())) and (("cmd" in p.lower()) or ("command prompt" in p.lower())):
	  if (("don't" in p.lower()) or ("dont" in p.lower()) or ("do not" in p.lower())):
	    pyttsx3.speak("ok, i will not")
	    print("ok i will not")
	  else:
	    pyttsx3.speak("launching command prompt")
	    os.system("cmd")

	elif (("run" in p.lower()) or ("open" in p.lower()) or ("launch" in p.lower())) and ((("file" in p.lower()) and ("explorer" in p.lower())) or ("my computer" in p.lower())):
	  if (("don't" in p.lower()) or ("dont" in p.lower()) or ("do not" in p.lower())):
	    pyttsx3.speak("ok, i will not")
	    print("ok i will not")
	  else:
	    pyttsx3.speak("launching file explorer")
	    os.system("explorer")

	elif (("run" in p.lower()) or ("open" in p.lower()) or ("launch" in p.lower())) and (("control" in p.lower()) and ("panel" in p.lower())):
	  if (("don't" in p.lower()) or ("dont" in p.lower()) or ("do not" in p.lower())):
	    pyttsx3.speak("ok, i will not")
	    print("ok i will not")
	  else:
	    pyttsx3.speak("launching control panel")
	    os.system("control")

	elif (("run" in p.lower()) or ("open" in p.lower()) or ("launch" in p.lower())) and (("mail" in p.lower()) and ("microsoft" in p.lower())):
	  if (("don't" in p.lower()) or ("dont" in p.lower()) or ("do not" in p.lower())):
	    pyttsx3.speak("ok, i will not")
	    print("ok i will not")
	  else:
	    pyttsx3.speak("launching microsoft mail")
	    os.system("explorer.exe shell:appsFolder\microsoft.windowscommunicationsapps_8wekyb3d8bbwe!microsoft.windowslive.mai")


	elif (("run" in p.lower()) or ("open" in p.lower()) or ("launch" in p.lower())) and ("gmail" in p.lower() or (("google" in p.lower()) and ("mail" in p.lower()))):
	  if (("don't" in p.lower()) or ("dont" in p.lower()) or ("do not" in p.lower())):
	    pyttsx3.speak("ok, i will not")
	    print("ok i will not")
	  else:
	    pyttsx3.speak("launching google mail")
	    os.system("start www.gmail.com")

	elif (("run" in p.lower()) or ("open" in p.lower()) or ("launch" in p.lower())) and ("flipkart" in p.lower()):
	  if (("don't" in p.lower()) or ("dont" in p.lower()) or ("do not" in p.lower())):
	    pyttsx3.speak("ok, i will not")
	    print("ok i will not")
	  else:
	    pyttsx3.speak("launching flipkart sohpping website")
	    os.system("start www.flipkart.com")

	elif (("run" in p.lower()) or ("open" in p.lower()) or ("launch" in p.lower())) and ("amazon" in p.lower()):
	  if (("don't" in p.lower()) or ("dont" in p.lower()) or ("do not" in p.lower())):
	    pyttsx3.speak("ok, i will not")
	    print("ok i will not")
	  else:
	    pyttsx3.speak("launching amazon shopping website")
	    os.system("start www.amazon.in")

#	elif (("run" in p) or ("open" in p) or ("launch" in p)) and (("google meet" in p) or ("meet" in p) or ("hangout" in p) or ("hangouts" in p)): 
#	  if (("don't" in p) or ("dont" in p) or ("do not" in p)):
#	    print("ok i will not")
#	  else:
#	    os.system("start meet.google.com")

	elif (("run" in p.lower()) or ("open" in p.lower()) or ("launch" in p.lower())) and (("facebook" in p.lower()) or ("fb" in p.lower())):
	  if (("don't" in p.lower()) or ("dont" in p.lower()) or ("do not" in p.lower())):
	    pyttsx3.speak("ok, i will not")
	    print("ok i will not")
	  else:
	    if (("iiec-rise" in p.lower()) or ("iiec" in p.lower())):
	      pyttsx3.speak("launching i  i  e  c rise facebook page ")
	      os.system("start www.facebook.com/IIECRise:")
	    else:
	      pyttsx3.speak("launching facebook page")
	      os.system("start www.facebook.com:")

	elif (("run" in p.lower()) or ("open" in p.lower()) or ("launch" in p.lower())) and (("instagram" in p.lower()) or ("insta" in p.lower())):
	  if (("don't" in p.lower()) or ("dont" in p.lower()) or ("do not" in p.lower())):
	    pyttsx3.speak("ok, i will not")
	    print("ok i will not")
	  else:
	    if(("iiec" in p.lower()) or ("iiec-rise" in p.lower())):
	      pyttsx3.speak("launching i  i  e  c rise enstagram page")
	      os.system("start www.instagram.com/iiec_connect/?hl=en:")
	    elif (("kriyanshi" in p.lower()) or ("kriyanshi's" in p.lower()) or ("kiya" in p.lower()) or ("kiya's" in p.lower())):
	      pyttsx3.speak("launching kriyanshi's enstagram page")
	      os.system("start www.instagram.com/kriyanshishahh/")
	    else:
	      pyttsx3.speak("launching enstagram")
	      os.system("start www.instagram.com:")

	elif (("run" in p.lower()) or ("open" in p.lower()) or ("launch" in p.lower())) and (("linked in" in p.lower()) or ("linked-in" in p.lower()) or ("linkedin" in p.lower())):
	  if (("don't" in p.lower()) or ("dont" in p.lower()) or ("do not" in p.lower())):
	    pyttsx3.speak("ok, i will not")
	    print("ok i will not")
	  else:
	    if (("iiec" in p.lower()) or ("iiec-rise" in p.lower())):
	      pyttsx3.speak("launching i  i  e  c rise linked in account ")
	      os.system("start www.linkedin.com/company/iiec-rise")
	    else:
	      pyttsx3.speak("launching linked in accouunt")
	      os.system("start www.linkedin.com:")

		#	if (("run" in p) or ("open" in p) or ("launch" in p)) and (("iiec rise facebook" in p) or (("iiec" in p) and ("facebook" in p))):
#	  if (("don't" in p) or ("dont" in p) or ("do not" in p)):
#	    print("ok i will not")
#	  else:
#	    os.system("start www.facebook.com/IIECRise")


	elif (("run" in p.lower()) or ("open" in p.lower()) or ("launch" in p.lower())) and (("8086" in p.lower()) and ("emulator" in p.lower())):
	  if (("don't" in p.lower()) or ("dont" in p.lower()) or ("do not" in p.lower())):
	    pyttsx3.speak("ok, i will not")
	    print("ok i will not")
	  else:
	    pyttsx3.speak("launching 8 0 8 6 emulator")
	    os.system("emu8086")

	elif (("run" in p.lower()) or ("open" in p.lower()) or ("launch" in p.lower())) and ("zoom" in p.lower()):
	  if (("don't" in p.lower()) or ("dont" in p.lower()) or ("do not" in p.lower())):
	    pyttsx3.speak("ok, i will not")
	    print("ok i will not")
	  else:
	    pyttsx3.speak("launching zoom meeting app ")
	    os.system("zoom")

	elif (("run" in p.lower()) or ("open" in p.lower()) or ("launch" in p.lower())) and ("telegram" in p.lower()):
	  if (("don't" in p.lower()) or ("dont" in p.lower()) or ("do not" in p.lower())):
	    pyttsx3.speak("ok, i will not")
	    print("ok i will not")
	  else:
	    pyttsx3.speak("launching telegram")
	    os.system("telegram")

	elif (("empty" in p.lower()) or ("delete" in p.lower())) and (("recycle" in p.lower()) or ("bin" in p.lower()) or ("data" in p.lower())):
	  if (("don't" in p.lower()) or ("dont" in p.lower()) or ("do not" in p.lower())):
	    pyttsx3.speak("ok, i will not")
	    print("ok i will not")
	  else:
	    pyttsx3.speak("THIS WILL EMPTY YOUR RECYCLE BIN\n")
	    print("DO YOU WISH TO PROCEED  | y/n or yes/no | :" , end='')
	    boo = input()
	    if (("y" in boo.lower()) or ("yes" in boo.lower())):
	        os.system("rd /s e:\$Recycle.Bin /q")
	        os.system("rd /s c:\$Recycle.Bin /q")
	        os.system("rd /s d:\$Recycle.Bin /q")
	        pyttsx3.speak("Check your RECYCLE-bin. It is already empty. It's good that you have me")
	    else:
	        pyttsx3.speak("GOOD CHOICE :) CHECK BEFORE EMPTYING BIN, WILL you!!")
	        print("\n GOOD CHOICE :) CHECK BEFORE EMPTYING BIN, WILL You !!")

	elif (("run" in p.lower()) or ("open" in p.lower()) or ("launch" in p.lower())) and (("settings" in p.lower()) or ("setting" in p.lower())):
	  if (("don't" in p.lower()) or ("dont" in p.lower()) or ("do not" in p.lower())):
	    pyttsx3.speak("ok, i will not")
	    print("ok i will not")
	  else:
	    pyttsx3.speak("launching requested setting")
	    if (("wifi" in p.lower()) or ("network" in p.lower())):
	      os.system("start ms-settings:network-wifi")
	    elif("bluetooth" in p.lower()):
	      os.system("start ms-settings:bluetooth")
	    elif(("brightness" in p.lower()) or ("light" in p.lower()) or ("display" in p.lower())):
	      os.system("start ms-settings:display")
	    elif("airplain" in p.lower()):
	      os.system("start 	ms-settings:network-airplanemode:")
	    elif("battery" in p.lower()):
	      os.system("start ms-settings:batterysaver")
	    elif ("storage" in p.lower()):
	      os.system("start ms-settings:storagesense")
	    elif (("about" in p.lower()) or ("my pc" in p.lower()) or ("my laptop" in p.lower()) or ("laptop" in p.lower()) or ("pc" in p.lower())):
	      os.system("start ms-settings:about")
	    elif ("mouse" in p.lower()):
	      os.system("start ms-settings:mousetouchpad")
	    elif ("touchpad" in p.lower()):
	      os.system("start ms-settings:devices-touchpad")
	    elif ("background" in p.lower()):
	      os.system("start ms-settings:personalization-background")
	    elif (("colors" in p.lower()) or ("colors" in p.lower())):
	      os.system("start ms-settings:colors")
	    elif ("lock screen" in p.lower()):
	      os.system("start 	ms-settings:lockscreen")
	    elif (("themes" in p.lower()) or ("theme" in p.lower())):
	      os.system("start ms-settings:themes")
	    elif ("satrt" in p.lower()):
	      os.system("start ms-settings:personalization-start")
	    elif ("taskbar" in p.lower()):
	      os.system("start ms-settings:taskbar")
	    elif (("date" in p.lower()) or ("time" in p.lower())):
	      os.system("start ms-settings:dateandtime")
	    elif ("keyboard" in p.lower()):
	      os.system("start ms-settings:easeofaccess-keyboard:")
	    else:
	      pyttsx3.speak("launching settings")
	      os.system("start ms-settings:")


	elif (("run" in p.lower()) or ("open" in p.lower()) or ("launch" in p.lower())) and (("youtube" in p.lower()) or ("yt" in p.lower())):
	  if (("don't" in p.lower()) or ("dont" in p.lower()) or ("do not" in p.lower())):
	    pyttsx3.speak("ok, i will not")
	    print("ok i will not")
	  else:
	    if (("iiec" in p.lower()) or ("iiec-rise" in p.lower())):
	      pyttsx3.speak("launching i i e c rise youtube channel")
	      os.system("start https://www.youtube.com/channel/UCtY-JhEZ3iPLtozWGgd2efQ")
	    else:
	      pyttsx3.speak("launching youtube ")
	      os.system("start www.youtube.com")

	elif (("exit" in p.lower())  or ("quit" in p.lower()) or ("leave" in p.lower()) or ("bye" in p.lower())):
	  if (("don't" in p.lower()) or ("dont" in p.lower()) or ("do not" in p.lower())):
	    pyttsx3.speak("ok, i will not")
	    print("ok i will not")
	  else:
	    pyttsx3.speak("Hope you enjoyed our time together. Talk to you soon")
	    break

	elif (("run" in p.lower()) or ("open" in p.lower()) or ("launch" in p.lower())) and ("shopping" in p.lower()):
	  if (("don't" in p.lower()) or ("dont" in p.lower()) or ("do not" in p.lower())):
	    pyttsx3.speak("ok, i will not")
	    print("ok i will not")
	  else:
	    pyttsx3.speak("unable FIND SHOPPING APP OF YOUR CHOICE. TRY TYPING amazon or flipkart")
	    print("unable FIND SHOPPING APP OF YOUR CHOICE. TRY TYPING amazon or flipkart")

	elif (("run" in p.lower()) or ("open" in p.lower()) or ("launch" in p.lower())) and (("app" in p.lower()) or ("application" in p.lower())):
	  if (("don't" in p.lower()) or ("dont" in p.lower()) or ("do not" in p.lower())):
	    pyttsx3.speak("ok, i will not")
	    print("ok i will not")
	  else:
	    pyttsx3.speak("unable to FIND APP OF YOUR CHOICE. TRY TO BE MORE SPECIFIC")
	    print("unable to FIND APP OF YOUR CHOICE. TRY TO BE MORE SPECIFIC")

	elif (("run" in p.lower()) or ("open" in p.lower()) or ("launch" in p.lower())) and (("task" in p.lower()) and ("manager" in p.lower())) :
	  if (("don't" in p.lower()) or ("dont" in p.lower()) or ("do not" in p.lower())):
	    pyttsx3.speak("ok, i will not")
	    print("ok i will not")
	  else:
	    pyttsx3.speak("launching task manager")
	    os.system("taskmgr")

	elif (("thanks" in p.lower()) or ("thank you" in p.lower()) or ("awesome" in p.lower()) or ("good" in p.lower()) or ("helpfull" in p.lower()) or ("help" in p.lower()) or ("thankyou" in p.lower())):
	  pyttsx3.speak("you are welcome. Happy to help you")

	else:
	  pyttsx3.speak("i don't understand what you are asking me ")


