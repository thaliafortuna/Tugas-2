Nama: Thalia Fortuna
Kelas: A
NPM: 2106751890

https://aplikasidjango.herokuapp.com/todolist/login/


1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Setiap elemen HTML memiliki atribut style, maka di atribut tersebutlah inline CSS ditulis.

Kelebihan:

- Sangat membantu ketika Anda hanya ingin menguji dan melihat perubahan pada satu elemen.

- Berguna untuk memperbaiki kode dengan cepat.

- Proses permintaan HTTP yang lebih kecil dan proses load website akan lebih cepat.

Kekurangan:
- Tidak efisien karena Inline style CSS hanya bisa diterapkan pada satu elemen HTML.

Eksternal CSS adalah kode CSS yang ditulis secara terpisah yaitu HTML eksternal CSS ditulis di file khusus yang berekstensi .css. File eksternal CSS biasanya diletakkan setelah bagian <head> pada halaman.

Kelebihan:
- Ukuran file HTML cenderung lebih kecil dan struktur dari kode HTML menjadi lebih rapi.

- Loading website akan menjadi lebih cepat.

- File CSS dapat digunakan di beberapa halaman website sekaligus. 

Kekurangan:
- Halaman akan menjadi lebih berantakan jika file CSS gagal dipanggil oleh file HTML. Hal ini terjadi karena koneksi internet yang lambat.

Internal CSS adalah kode CSS yang ditulis di dalam tag <style> dan kode HTML dituliskan di bagian atas (header) file HTML.

Kelebihan:
- Lebih rapi karena perubahan pada Internal CSS hanya berlaku pada satu halaman saja.

- Anda tidak perlu melakukan upload beberapa file karena HTML dan CSS berada dalam satu file.

- Class dan ID bisa digunakan oleh internal stylesheet.

Kekurangan:
- Tidak efisien apabila Anda ingin menggunakan CSS yang sama dalam beberapa file.

- Membuat performa website lebih lemot. Sebab, CSS yang berbeda-beda akan mengakibatkan loading ulang setiap kali Anda ganti halaman website. 


2. Jelaskan tag HTML5 yang kamu ketahui.

(abaikan titik)

<.h1> hingga <.h6> -> membuat heading

<.div> -> membuat sebuah divisi tersendiri

<.meta> -> membuat database mengenai dokumen HTML

<.form> -> membuat form HTML

<.input> -> membuat sebuah kontrol input

<.button> -> membuat sebuah tombol yang dapat diklik

<.img> -> membuat gambar

<.p> -> membuat paragraf

<.br> -> memasukkan suatu baris putus

<.b> -> membuat huruf bercetak tebal

dsb.


3. Jelaskan tipe-tipe CSS selector yang kamu ketahui.

* -> select seluruh elemen
.class -> select seluruh elemen dalam class tersebut

.class1.class2 -> select seluruh elemen dengan atribut class1 dan class2

.element -> select seluruh element yang ditetapkan, contoh seluruh elemen <p>
.element.class -> select seluruh elemen yang ditetapkan, dengan class yang di ditetapkan, contoh p.intro maka seluruh elemen <p> dengan class intro

#id -> select elemen dengan id yang dipilih

:valid -> select seluruh elemen input dengan value valid

:root -> select root elemen dari dokumen

:read-only -> select elemen input dengan atribut "readonly"

:read-write -> select elemen input yang tidak diberi atribut "readonly"

::visited -> select seluruh link yang dikunjungi


4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

Menambahkan potongan kode berikut untuk utilisasi bootstrap.


    <meta charset="utf-8">

    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>


Anda bisa menambahkan style CSS secara inline, internal, maupun external. Saya menggunakan inline dan internal CSS. Saya membuat divisi (div) yang diperlukan dan memasukkan class. Hal ini dilakukan untuk mempermudah. Untuk halaman logim, register, dan create-task, saya menambahkan container dan centerized penampilan agar semakin rapi, juga memasukkan background color, menetapkan margin dan padding, dll. Hal ini dilakukan di block style. Selain itu untuk kustomisasi pada inline CSS, dilakukan hal yang sama namun terletak pada atribut yang lebih spesifik.

Setelah memodifikasi ketiga halaman tersebut, saya memodifikasi halaman utama todo lists dengan cards. Saya mengubah table menjadi form, lalu menggunakan class card, card-group, dan card-deck. Card group berada di dalam iterasi sehingga setiap task todolist akan dimasukkan dalam sebuah card. Dilanjutkan dengan kustomisasi warna, header, button, dll.

Untuk membuat halaman login, register, create-task, dan todolist menjadi positif, saya menggunakan Media Query. Saya menambahkan media query di internal CSS tepatnya block style. Potongan kode yang saya tambahkan:
 
@media (max-width: 600px) {
            .container {
              font-size: 20px;
              padding: 5px;
            }
        }

Kode ini memastikan bahwa di layar dengan 600px atau kurang, akan dilakukan modifikasi font size serta padding agar menyesuaikan dengan layar.
      
