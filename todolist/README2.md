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

<h1> hingga <h6> -> membuat heading
<div> -> membuat sebuah divisi tersendiri
<meta> -> membuat database mengenai dokumen HTML
<form> -> membuat form HTML
<input> -> membuat sebuah kontrol input
<button> -> membuat sebuah tombol yang dapat diklik
<img> -> membuat gambar
<p> -> membuat paragraf
<br> -> memasukkan suatu baris putus
<b> -> membuat huruf bercetak tebal
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
