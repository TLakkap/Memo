import time

def tiedostonAvaaminen(tiedosto):
	try:
		avattu = open(tiedosto)
		avattu.close()
	except IOError:
		luotu = open(tiedosto, "w")
		if tiedosto == "muistio.txt":
			print("Oletusmuistioa ei löydy, luodaan tiedosto.")
		else:
			print("Tiedostoa ei löydy, luodaan tiedosto.")
		luotu.close()

def muistikirja():
	tiedosto = "muistio.txt"
	tiedostonAvaaminen(tiedosto)
	while True:
		print("Käytetään muistiota: ", tiedosto)
		print("(1) Lue muistikirjaa")
		print("(2) Lisää merkintä")
		print("(3) Tyhjennä muistikirja")
		print("(4) Vaihda muistiota")
		print("(5) Lopeta\n")
		valinta = input("Mitä haluat tehdä?: ")
		
		if valinta == "1":
			muistio = open(tiedosto)
			sisalto = muistio.read()
			muistio.close()
			print(sisalto)
		elif valinta == "2":
			muistio = open(tiedosto, "a")
			merkinta = input("Kirjoita uusi merkintä: ")
			aika = time.strftime("%X %x")
			muistio.write(merkinta + ":::" + aika)
			muistio.close()
		elif valinta == "3":
			muistio = open(tiedosto, "w")
			muistio.close()
			print("Muistio tyhjennetty.")
		elif valinta == "4":
			tiedosto = input("Anna tiedoston nimi: ")
			tiedostonAvaaminen(tiedosto)
		elif valinta == "5":
			print("Lopetetaan.")
			break

def main():
	muistikirja()

if __name__ == "__main__":
	main()