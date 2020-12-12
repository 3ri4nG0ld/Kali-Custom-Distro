#!/usr/bin/env python3

import os
#[+------------------+] FUNCIONES [+------------------+]
def instalar_requisitos(programa):
	os.system("sudo apt-get update")
	os.system("clear")
	if (programa == "BATTERY-SCRIPT"):
		os.system("sudo apt-get install acpi -y")
	elif (programa == "BSPWM"):
		os.system("sudo apt-get install libxcb-xinerama0-dev libxcb-icccm4-dev libxcb-randr0-dev libxcb-util0-dev libxcb-ewmh-dev libxcb-keysyms1-dev libxcb-shape0-dev -y")
		os.system("sudo apt-get install compton feh rofi compton git -y")
def use_vmware():
	os.system("clear")
	opt=input("Usas VMware?? (yes/No): ")
	if ((opt == "YES") or (opt == "yes") or (opt == "y") or (opt == "Y")):
		os.system("sudo echo -e '\nvmware-user-suid-wrapper &' >> /etc/bspwm/bspwmrc")
	elif ((opt == "") or (opt == "N") or (opt == "NO") or (opt == "no") or (opt == "n")):
		return
	else:
		return
def instalar_scripts(plataforma):
	os.system("sudo chmod +x scripts/genericos/*")
	os.system("sudo chmod +x scripts/especificos/*")

	os.system("sudo cp scripts/genericos/* /usr/bin/") # Copia los scripts Genericos a /usr/bin/

	if (plataforma == "PC"):
		pass # Añadir aqui Scripts especificos

	elif (plataforma == "PC-NOGUI"):
		pass # Añadir aqui Scripts especificos

	elif (plataforma == "LAPTOP"):
		instalar_requisitos("BATTERY-SCRIPT")
		os.system("sudo cp scripts/especificos/battery-laptop /usr/bin/battery")
		# Añadir aqui Scripts especificos

	elif (plataforma == "LAPTOP-NOGUI"):
		instalar_requisitos("BATTERY-SCRIPT")
		os.system("sudo cp scripts/especificos/battery-laptop /usr/bin/battery")
		# Añadir aqui Scripts especificos

	elif (plataforma == "WSL2"):
		pass
		# Añadir aqui Scripts especificos

	elif (plataforma == "NETHUNTER"):
		pass
		# Añadir aqui Scripts especificos
def eliminar_Desktop_Enviroment():
	os.system("clear")
	print("Esto eliminara el entorono de escitorio actual")
	opt=input("Estas seguro de querer continuar?(yes/No): ")
	if((opt == "YES") or (opt == "yes") or (opt == "y") or (opt == "Y")):
		print("SI se elimina")
		os.system("sudo apt-get remove xfce4* xserver-xorg lightdm* -y")
		os.system("sudo apt-get purge xfce4* xserver-xorg lightdm* -y")
		os.system("sudo apt-get autoremove -y")
		os.system("clear")
		opt=input("Desea eliminar tambien la animacion de inicio?(yes/No): ")
		if((opt == "YES") or (opt == "yes") or (opt == "y") or (opt == "Y")):
			os.system("sudo apt-get remove plymouth -y")
			os.system("sudo apt-get purge plymouth -y")
			os.system("sudo apt-get autoremove -y")
		elif ((opt == "") or (opt == "N") or (opt == "NO") or (opt == "no") or (opt == "n")):
			print("NO se Eliminara")
		else:
			print("NO se Eliminara")
	elif ((opt == "") or (opt == "N") or (opt == "NO") or (opt == "no") or (opt == "n")):
		print("NO se Eliminara")
	else:
		print("NO se Eliminara")
# Terminar de Configurar
# |
# v
def instalar_y_configurar_i3wm_kali():
	os.system("sudo apt-get update")
	os.system("clear")
	opt=input("Quieres instalar i3wm??(yes/No): ")

	if((opt == "YES") or (opt == "yes") or (opt == "y") or (opt == "Y")):
		os.system("sudo apt-get install i3wm -y")
	elif ((opt == "") or (opt == "N") or (opt == "NO") or (opt == "no") or (opt == "n")):
		print("NO se Instalara")
	else:
		print("NO se Instalara")
def configuracion_qterminal():
	os.system("sudo cp configs/qterminal.ini /etc/xdg/qterminal.org/qterminal.ini")
	print("Configuracion de Qterminal copiada")
def instalar_fuentes():

	os.system("cd /usr/local/share/fonts && sudo wget https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/Hack.zip && sudo unzip /usr/local/share/fonts/Hack.zip && sudo rm -rf /usr/local/share/fonts/Hack.zip")
def instalar_y_configurar_polybar(tipo):
	os.system("sudo apt-get install polybar -y")
	instalar_fuentes()
	os.system("sudo cp configs/launch-polybar.sh /etc/bspwm/scripts/launch-polybar.sh")
	os.system("sudo chmod 555 /etc/bspwm/scripts/launch-polybar.sh")
	os.system("sudo mkdir /etc/polybar/")


	if (tipo == "PC"):
		print("Configurar Polybar PC")
		os.system("sudo cp configs/POLYBAR-PC /etc/polybar/config")
	elif (tipo == "LAPTOP"):
		print("Configurar Polybar LAPTOP")
		os.system("sudo cp configs/POLYBAR-LAPTOP /etc/polybar/config")
def instalar_y_configurar_bspwm_kali():
	os.system("sudo apt-get update")
	os.system("clear")
	opt=input("Quieres instalar bspwm??(Yes/no): ")
	if((opt == "") or (opt == "YES") or (opt == "yes") or (opt == "y") or (opt == "Y")):
			instalar_requisitos("BSPWM")
			os.system("sudo apt-get install bspwm -y")
			os.system("git clone https://github.com/baskerville/bspwm.git")
			os.system("git clone https://github.com/baskerville/sxhkd.git")
			os.system("cd bspwm && make && sudo make install")
			os.system("cd sxhkd && make && sudo make install")

			os.system("sudo mkdir /etc/bspwm")
			os.system("sudo mkdir /etc/sxhkd")
			os.system("sudo mkdir /etc/bspwm/scripts/")
			os.system("sudo mkdir /etc/compton/")

			os.system("sudo cp configs/bspwmrc /etc/bspwm/bspwmrc")
			os.system("sudo cp configs/sxhkdrc /etc/sxhkd/sxhkdrc")
			os.system("sudo cp configs/bspwm_resize /etc/bspwm/scripts/resize")
			os.system("sudo chmod +x /etc/bspwm/scripts/resize")
			os.system("sudo cp configs/bspwm.desktop /usr/share/xsessions/bspwm.desktop")
			os.system("sudo cp configs/compton.conf /etc/compton/compton.conf")
			os.system("sudo chmod 555 /etc/compton/compton.conf")
			os.system("sudo chmod 555 /etc/bspwm/bspwmrc")

			os.system("sudo mkdir /etc/wallpaper")
			os.system("sudo cp wallpaper/wallpaper.jpg /etc/wallpaper/wallpaper.jpg")

			instalar_y_configurar_polybar("PC")
			use_vmware()
			print("[ BSPWM instalado ]")
			reiniciar()
	elif ((opt == "N") or (opt == "NO") or (opt == "no") or (opt == "n")):
		print("NO se Instalara")
	else:
		print("NO se Instalara")
def configurar_tmux():
	return
def reiniciar():
	os.system("clear")
	opt = input("Desea reiniciar para aplicar los cambios??(Yes/no): ")
	if((opt == "") or (opt == "YES") or (opt == "yes") or (opt == "y") or (opt == "Y")):
		print("Reiniciando...")
		os.system("sudo reboot")
	elif ((opt == "N") or (opt == "NO") or (opt == "no") or (opt == "n")):
		print("Saliendo...")
def instalar_otras_herramientas():
	os.system("sudo apt-get install bat")




#  Funciones Principales
#------------------------------------------------------
def instalar_kali_pc():
	instalar_scripts("PC")
	instalar_y_configurar_i3wm_kali()
	instalar_y_configurar_bspwm_kali()

def instalar_kali_pc_nogui():
	instalar_scripts("PC-NOGUI")
	eliminar_Desktop_Enviroment()

def instalar_kali_laptop():
	instalar_scripts("LAPTOP")
	instalar_y_configurar_i3wm_kali()
	instalar_y_configurar_bspwm_kali()

def instalar_kali_laptop_nogui():
	instalar_scripts("LAPTOP-NOGUI")
	eliminar_Desktop_Enviroment()

def instalar_kali_wsl2():
	instalar_scripts("WSL2")
	configurar_tmux()

def instalar_kali_nethunter():
	instalar_scripts("NETHUNTER")

#[+------------------+] MAIN [+------------------+]
os.system("clear")
print("""Elige una instalacion:
1.- Kali Linux (PC Escritorio)
2.- Kali Linux (PC Escritorio) sin GUI
3.- Kali Linux (Laptop)
4.- Kali Linux (Laptop) sin GUI
5.- Kali Linux (WSL2)
6.- Kali Nethunter (android)""")

opt=input("> ")

if (opt=="1"):
	instalar_kali_pc()
elif (opt=="2"):
	instalar_kali_pc_nogui()
elif (opt=="3"):
	instalar_kali_laptop()
elif (opt=="4"):
	instalar_kali_laptop_nogui()
elif (opt=="5"):
	instalar_kali_wsl2()
elif (opt=="6"):
	instalar_kali_nethunter()
else:
	print("* Opcion no valida")