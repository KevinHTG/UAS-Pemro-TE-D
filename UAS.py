#pylint:disable=E1101
#section1 Variable
print("Biodata Mahasiswa:")
Nama = "Albert Sihite"
Umur = "19"
Alamat = "Jalan Melanthon Siregar no. 17"
Hobby = "Bermain Sepakbola"
print(Nama, Umur, Alamat, Hobby)
def biodata():
	print("Mahasiswa berprestasi adalah", 			Nama)

biodata()

#File konstanta.py
UAS = 97
UTS = 100

#section2 Konstanta
import konstanta
print("Nilai Rata-Rata:")
Rata_Rata = (konstanta.UAS + konstanta.UTS)/2
print(Rata_Rata)

#section3 Strings
Biodata = Nama, Umur, Alamat, Hobby
print(Biodata[0:1])
print(Biodata[1:2])
print(Biodata[:4])

#section4 List
Mata_Pelajaran = "Fisika Dasar", "Elektronika Daya", "Sistem Digital 1"
Nilai = "A", "B+", "B", "C+", "C", "D", "E", "F"
print("Nilai", Nama, "=")
print(Mata_Pelajaran[0], ":", Nilai[2])
print(Mata_Pelajaran[1], ":", Nilai [4])
print(Mata_Pelajaran[2], ":", Nilai[0])

#section5 Dict
Keterangan = {
	Mata_Pelajaran[0] : "Lulus",
	Mata_Pelajaran[1] : "Tak Lulus",
	Mata_Pelajaran[2] : "Lulus"
}
print(Keterangan)

#section6 Def
def Kesimpulan():
	if Keterangan == "Lulus":
		print("Lanjut")
	else:
		print("Mengulang")
print(Kesimpulan())

#section7
Kesimpulan = "Albert Sihite Mengulang"
List = Kesimpulan.split(" ")
print(List)
print(Kesimpulan.upper())
print(Kesimpulan.lower())
print(Kesimpulan.capitalize())

#section8
Pernyataan1 = lambda x,y : x + y
print(Pernyataan1("Hobby Albert adalah ",Hobby))

Pernyataan2 = lambda a,b,c : a + b + c
print(Pernyataan2(Kesimpulan, " karena ", Mata_Pelajaran[1] ))

z = len(Kesimpulan)
print(z)