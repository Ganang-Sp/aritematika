from art import intro_ba, intro_da, outro
wadah = []

def rumus_deret(suku_pertama,beda,n):
	#rumus deret aritematika n / 2 ( 2 . a + ( n - 1 ) . b)
	if n % 2 == 0:	
		q = n / 2
		w = 2 * suku_pertama
		e = n - 1
		r = e * beda
		t = w + r
		hasil = q * t
		print(f" Suku pertama / a : {suku_pertama}")
		print(f" Beda / b : {beda}")
		print(f"Sn = n / 2 ( 2 . a + ( n - 1 ) . b)")
		print(f"S{n} = {n} / 2 ( 2 . {suku_pertama} + ( {n} - 1 ) . {beda} ) ")	
		print(f"S{n} = {q} ( {w} + ( {e} ) . {beda} ) ")
		print(f"S{n} = {q} ( {w} + {r} )")
		print(f"S{n} = {q} . {t}")
		print(f"S{n} = {hasil}")
		round(hasil)
		salah_ketik = True
		while salah_ketik:
			tanya_ulang = input("Kembali ke Menu? [Y/n]\nJawaban : ")
			if tanya_ulang == "n" or tanya_ulang == "N":
				salah_ketik = False
				print(outro)
				print("Sampai Jumpa, Jangan Lupa Balik Lagi :)")
			elif tanya_ulang == "Y" or tanya_ulang == "y":
				salah_ketik = False
				home()
			else:
				salah_ketik = True
				print("Salah Ketik")
	else:
		w = 2 * suku_pertama
		e = n - 1
		r = e * beda
		t = w + r
		hasil = n * t / 2
		print(f" Suku pertama / a : {suku_pertama}")
		print(f" Beda / b : {beda}")
		print(f"Sn = n / 2 ( 2 . a + ( n - 1 ) . b)")
		print(f"S{n} = {n} / 2 ( 2 . {suku_pertama} + ( {n} - 1 ) . {beda} ) ")	
		print(f"S{n} = {n} / 2 ( {w} + ( {e} ) . {beda} ) ")
		print(f"S{n} = {n} / 2 ( {w} + {r} )")
		print(f"S{n} = {n} / 2 . {t}")
		print(f"S{n} = {hasil}")
		round(hasil)
		salah_ketik = True
		while salah_ketik:
			tanya_ulang = input("Kembali ke Menu? [Y/n]\nJawaban : ")
			if tanya_ulang == "n" or tanya_ulang == "N":
				salah_ketik = False
				print(outro)
				print("Sampai Jumpa, Jangan Lupa Balik Lagi :)")
			elif tanya_ulang == "Y" or tanya_ulang == "y":
				salah_ketik = False
				home()
			else:
				salah_ketik = True
				print("Salah Ketik")


def rumus_baris(suku_pertama,beda,n):
	print(intro_ba)	
	print(f"suku pertama / a = {suku_pertama}")
	print(f"beda / b = {beda}")
	rumus = suku_pertama + (n - 1) * beda
	print(f"U{n} = {rumus}")
	def ke_n(suku_pertama,beda):
		print("Mencari Rumus Suku Ke-n")
		x = suku_pertama - beda
		bn = f"{beda}n"
		print("Un = a + (n - 1) * b")
		print(f"Un = {suku_pertama} + (n - 1) * {beda}")
		print(f"Un = {suku_pertama} + {bn} - {beda}")
		print(f"Un = {bn} + {x}")
	ke_n(suku_pertama=suku_pertama,beda=beda)
	tanya_ulang = input("Kembali ke Menu? [Y/n]\nJawaban : ")
	if tanya_ulang == "n" or tanya_ulang == "N":
		print(outro)
		print("Sampai Jumpa, Jangan Lupa Balik Lagi :)")
	elif tanya_ulang == "Y" or tanya_ulang == "y":
		home()
	else:
		print("Salah Ketik")

#menu
def home():
	print("__________________________")
	print("|                        |")
	print("|      MENU PILIHAN      |")
	print("|________________________|\n")
	print("1. Barisan Aritematika")
	print("2. Deret Aritematika")
	print("0. Keluar Program")
	tanya_menu = input("Pilihan : ")
	if tanya_menu == "0":
		ulangi = True
		print(outro)
		print("Sampai Jumpa, Jangan Lupa Balik Lagi :)")
	elif tanya_menu == "1":
		tanya_jumlah = int(input("Masukkan Jumlah Angka Yang Berada Di Soal!(Minimal 2) misal jika soalnya 2,3,4,5 masukkan angka 4, kalau 2,4,6,8,10 masukkan angka 5 dan seterusnya : ")) 
		for tj in range(1, tanya_jumlah + 1):
			tanya_soal = int(input(f"Masukkan nilai yang ke {tj}: "))
			wadah.append(tanya_soal)
		tanya_suku = int(input("Ingin Mencari nilai dari suku ke berapa? : "))
		a = wadah[0]
		b = wadah[1] - wadah[0]
		rumus_baris(suku_pertama=a,beda=b,n=tanya_suku)
	elif tanya_menu == "2":
		tanya_jumlah = int(input("Masukkan Jumlah Angka Yang Berada Di Soal!(Minimal 2) misal jika soalnya 2,3,4,5 masukkan angka 4, kalau 2,4,6,8,10 masukkan angka 5 dan seterusnya : ")) 
		for tj in range(1, tanya_jumlah + 1):
			tanya_soal = int(input(f"Masukkan nilai yang ke {tj}: "))
			wadah.append(tanya_soal)
		tanya_suku = int(input("Ingin Mencari nilai dari suku ke berapa? : "))
		a = wadah[0]
		b = wadah[1] - wadah[0]
		rumus_deret(suku_pertama=a,beda=b,n=tanya_suku)
	else:
		print("Salah Ketik Kah?, Menu Tidak Ada")
home()