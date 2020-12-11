#!/usr/bin/env python3

import os
#[+------------------+] FUNCIONES [+------------------+]
def instalar_requisitos(programa):
	if (programa == "BATTERY-SCRIPT"):
		os.system("sudo apt-get install acpi -y")
	elif (programa == "0"):
		pass






def instalar_scripts(plataforma):
	os.system("sudo chmod +x scripts/genericos/*")
	os.system("sudo chmod +x scripts/especificos/*")
	if (plataforma == "PC"):
		os.system("sudo cp scripts/genericos/* /usr/bin/")
		# Añadir aqui Scripts especificos
	elif (plataforma == "PC-NOGUI"):
		os.system("sudo cp scripts/genericos/* /usr/bin/")
		# Añadir aqui Scripts especificos
	elif (plataforma == "LAPTOP"):
		os.system("sudo cp scripts/genericos/* /usr/bin/")
		# Añadir aqui Scripts especificos
	elif (plataforma == "LAPTOP-NOGUI"):
		os.system("sudo cp scripts/genericos/* /usr/bin/")
		# Añadir aqui Scripts especificos
	elif (plataforma == "WSL2"):
		os.system("sudo cp scripts/genericos/* /usr/bin/")
		# Añadir aqui Scripts especificos
	elif (plataforma == "NETHUNTER"):
		os.system("sudo cp scripts/genericos/* /usr/bin/")
		# Añadir aqui Scripts especificos



def instalar_kali_pc():
	instalar_scripts("PC")

def instalar_kali_pc_nogui():
	instalar_scripts("PC-NOGUI")
	eliminar_Desktop_Enviroment()

def instalar_kali_laptop():
	instalar_requisitos("BATTERY-SCRIPT")
	instalar_scripts("LAPTOP")

def instalar_kali_laptop_nogui():
	instalar_scripts("LAPTOP-NOGUI")

def instalar_kali_wsl2():
	instalar_scripts("WSL2")

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

opt=input(">")

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