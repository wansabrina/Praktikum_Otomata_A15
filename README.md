# Program Deteksi Palindrom

| Nama                         | NRP        | Kelas      |
|------------------------------|------------|------------|
| Wan Sabrina Mayzura          | 5025211023 | Otomata F  |
| Rr. Diajeng Alfisyahrinnisa A.| 5025211147 | Otomata F |
| Syarifah Talitha Erfany      | 5025211175 | Otomata F  |

## Deskripsi Masalah

Tugas praktikum ini bertujuan untuk mengembangkan sebuah program yang dapat mengenali apakah suatu string merupakan **palindrom**, yaitu string yang tetap sama ketika dibaca dari depan maupun belakang. Program harus mampu memproses string yang terdiri dari huruf, angka, atau kombinasi keduanya, tanpa membedakan huruf besar dan kecil serta mengabaikan karakter non-alfanumerik seperti spasi atau simbol.

Contoh input valid:  
- `ABBA`  
- `12321`  
- `A1B2B1A`  

Program akan menentukan apakah input tersebut tergolong sebagai palindrom atau bukan.

---

## Penjelasan Logika Kode Program

### 1. Import Library

```python
import re
import customtkinter as ctk
from tkinter import messagebox
````

* `re`: Untuk memproses string dengan ekspresi reguler, khususnya menghapus karakter non-alfanumerik.
* `customtkinter`: Library modern berbasis tkinter untuk membangun antarmuka (install dengan `pip install customtkinter`).
* `messagebox`: Untuk menampilkan pesan peringatan saat input kosong.


### 2. Fungsi `is_palindrome(s: str) -> bool`

```python
def is_palindrome(s: str) -> bool:
    normalized = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return normalized == normalized[::-1]
```

* Fungsi ini menentukan apakah string adalah palindrom.
* `re.sub(r'[^a-zA-Z0-9]', '', s)` menghapus semua karakter selain huruf dan angka.
* `.lower()` memastikan pemeriksaan tidak case-sensitive.
* `[::-1]` membalik string.
* Jika hasilnya sama dengan string asli → `True`.

---

### 3. Fungsi `check_palindrome()`

```python
def check_palindrome():
    user_input = entry.get()
    if not user_input.strip():
        messagebox.showwarning("Input Kosong", "Silakan masukkan string terlebih dahulu.")
        return
    if is_palindrome(user_input):
        result_label.configure(text=f'"{user_input}" adalah palindrom.', text_color="green")
    else:
        result_label.configure(text=f'"{user_input}" bukan palindrom.', text_color="red")
```

* Menangani logika saat tombol "Cek" ditekan.
* Memastikan input tidak kosong. Jika kosong, tampilkan peringatan.
* Jika ada input, panggil fungsi `is_palindrome()`.
* Tampilkan hasil dalam teks hijau (palindrom) atau merah (bukan palindrom).

---

### 4. Antarmuka Program (GUI)

Antarmuka dibangun menggunakan `customtkinter`, dengan:

* `CTk()` sebagai jendela utama, judul ditentukan dengan `app.title()`, ukuran jendela dengan `app.geometry("500x370")`.
* `CTkFrame`: untuk wadah layout antarmuka.
* `CTkLabel`: menampilkan judul dan deskripsi.
* `CTkEntry`: field input teks.
* `CTkButton`: tombol "Cek" yang memanggil `check_palindrome()`.
* `CTkLabel` (lainnya): untuk menampilkan hasil pengecekan.

Aplikasi berjalan terus-menerus dengan:

```python
app.mainloop()
```

---

## Contoh Input dan Output

### ✅ Contoh 1

![images](/images/palindrome.png)

* Input: `25MAMAM52`
* Output: `"25MAMAM52 adalah palindrom."`


### ❌ Contoh 2

![images](/images/nonpalindrome.png)

* Input: `123`
* Output: `"123 bukan palindrom."`

### ⚠️ Contoh 3

![images](/images/noinput.png)

* Input: *(kosong)*
* Output: Pop-up: *"Silakan masukkan string terlebih dahulu."*