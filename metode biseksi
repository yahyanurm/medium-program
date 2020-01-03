"""
Program mencari akar dengan metode biseksi
"""
# of Bisection Method for 
# Mencari akar dari suatu persamaan 


# kita pilih fungsi x^4+4x^3+x^2-50 
def f(x): 
    #fungsi yang ingin dicari akarnya
	return x**4+4*x**3 + x**2 -50

# menampilkan akar dari f(x) 
# dengan error EPSILON 
def biseksi(a,b): 

	if (f(a) * f(b) >= 0): 
		print("Nilai a dan b yang dipilih salah\n") 
		return

	c = a 
	while ((b-a) >= 0.00001): 

		# mencari titik tengah
		c = (a+b)/2

		# melakukan pengecekan apakah nilai tengah adalah akar 
		if (f(c) == 0.0): 
			break

		# melakukan iterasi 
		if (f(c)*f(a) < 0): 
			b = c 
		else: 
			a = c 
			
	print("Nilai akarnya adalah : ","%.7f"%c) 

# memilih interval a dan b 
a =0
b =25
biseksi(a, b) 
