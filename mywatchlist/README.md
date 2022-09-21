Nama: Thalia Fortuna
Kelas: PBP A
NPM: 2106751890

LINK HEROKU:
https://aplikasidjango.herokuapp.com/mywatchlist/html/
https://aplikasidjango.herokuapp.com/mywatchlist/xml/
https://aplikasidjango.herokuapp.com/mywatchlist/json/

JSON atau JavaScript Object Notation digunakan pada banyak aplikasi web maupun mobile untuk menyimpan dan mengirimkan data. 
JSON menyimpan semua datanya dalam format map (key / value). Sintaks JSON merupakan turunan dari Object JavaScript dan format JSON berbentuk text, sehingga kode JSON banyak terdapat dibanyak bahasa pemrograman. JSON didesain menjadi self-describing, dimana representasi diberikan secara eksplisit, sehingga sangat mudah dimengerti

XML atau Extensible Markup Language digunakan pada banyak aplikasi web maupun mobile untuk menyimpan dan mengirimkan data. 
XML adalah informasi yang dibungkus di dalam tag. Lalu, harus dilanjutkan dengan penulisan program untuk mengirim, menerima, menyimpan, atau menampilkan informasi tersebut. 
XML didesain menjadi self-descriptive, maka dengan membaca XML tersebut kita bisa mengerti informasi apa yang ingin disampaikan dari data yang tertulis. 
XML membuat pertukaran data semakin mudah dengan memberikan struktur data yang.

HTML atau Hyper Text Markup Language adalah bahasa yang digunakan untuk membuat halaman web. 
HTML disusun berdasar kode tertentu yang dimasukkan dalam sebuah file sehingga dapat ditampilkan pada layar komputer. 
File ini dapat dibuka dengan menggunakan web browser kesukaan Anda. Namun agar dapat diakses oleh banyak orang, Anda perlu menyewa layanan hosting website dan mengupload file website Anda di sana. 
Lalu, browser akan membaca dan me-render file HTML menjadi tampilan halaman website. HTML juga didesain menjadi self-describing, dimana representasi diberikan secara eksplisit, sehingga sangat mudah dimengerti.

Pentingnya data delivery dalam pengimplementasian sebuah platform dirasakan ketika kita hendak mengirimkan data dari satu stack ke stack lainnya. 
Seperti Namanya ‘data delivery’, maka Anda dapat melakukan transfer dan menerima informasi demi keperluan penampilan data-data yang dimaksud. 
Format-format data tersebut dapat berupa HTML, XML, dan JSON.

Penjelasan implementasi checklist:

Langkah pertama adalah membuat dan menyalakan virtual environment dengan python -m venv env dan env\Scripts\activate,bat. 
Lalu, dilanjutkan dengan membuat sebuah aplikasi baru bernama mywatchlist dengan menjalankan python manage.py startapp mywatchlist di direktori proyek Django Tugas 2 (sudah meng-install dependencies). 
Setelah membuat aplikasi, kita tambahkan path mywatchlist di urls.py dalam folder project_django

![image](https://user-images.githubusercontent.com/88278165/191562007-5137ffc5-fb54-4e56-9f83-0cae75646675.png)

Di dalam models.py folder mywatchlist, saya menambahkan watched, title, rating, release_date, dan review. Tidak lupa melakukan perintah python manage.py makemigrations untuk mempersiapkan migrasi model ke dalam database Django lokal dan python manage.py migrate untuk menerapkannya ke database tersebut. Berikut isi models.py yang saya susun:

![image](https://user-images.githubusercontent.com/88278165/191562087-431b3df6-8d46-4048-ba9c-2e0d561b2d47.png)

Sesuai dengan models yang telah dibuat, saya menambahkan 10 data untuk objek MyWatchList tersebut di file initial_watchlist_data.json yang saya buat di folder fixtures. Tidak lupa melakukan perintah python manage.py loaddata initial_watchlist_data.json untuk memasukkan data ke dalam database Django lokal. Berikut adalah contoh salah satu datanya:

![image](https://user-images.githubusercontent.com/88278165/191562126-f82ef387-9953-4f77-8eb6-974f359b445b.png)

Selanjutnya adalah penyajian data yang telah dibuat dalam tiga format, yaitu HTML, XML, dan JSON melalui file views.py. Berikut adalah pengambilan data dari database:

![image](https://user-images.githubusercontent.com/88278165/191562155-bd289839-d58d-4aca-8472-b57fd931c045.png)

Setelah itu, akan dilakukan mapping data yang telah di-render pada views.py. Pertama-tama, saya membuat file HTML Bernama mywatchlist.html di folder templates di dalam folder mywatchlist. Lalu saya membuat kode sedemikian rupa untuk memunculkan sebuah tabel berisi my watch list:

![image](https://user-images.githubusercontent.com/88278165/191562192-8cf587f3-4a24-4c46-a647-5563e410976f.png)

Tidak lupa membuat routing pada file urls.py di folder mywatchlist agar dapat mengakses data melalui:

http://localhost:8000/mywatchlist/html untuk mengakses mywatchlist dalam format HTML

http://localhost:8000/mywatchlist/xml untuk mengakses mywatchlist dalam format XML

http://localhost:8000/mywatchlist/json untuk mengakses mywatchlist dalam format JSON

![image](https://user-images.githubusercontent.com/88278165/191562252-15961c1a-4f80-4b77-934b-55ab6c4bd3c7.png)

Lalu, dilanjutkan dengan git add, git commit-m “comment”, dan git push origin main untuk melakukan push ke akun github. Saya menggunakan aplikasi aplikasidjango saya pada Heroku dan di-deploy ke Heroku agar dapat diakses melalui internet. Setelah melakukan deployment (dengan secrets API KEY dan API NAME yang telah ditambahkan), Anda dapat mengakses link-link berikut:

https://aplikasidjango.herokuapp.com/mywatchlist/html/

https://aplikasidjango.herokuapp.com/mywatchlist/xml/

https://aplikasidjango.herokuapp.com/mywatchlist/json/

Selanjutnya, saya akan mengakses ketiga URL (localhost) di atas menggunakan Postman dan dapat dilihat bahwa status menyatakan 200 OK. Berikut adalah hasilnya:
 
![image](https://user-images.githubusercontent.com/88278165/191562304-53e41946-93f5-43ab-b69b-d3177df9898d.png)

![image](https://user-images.githubusercontent.com/88278165/191562333-6f853be8-a65f-44fe-9a69-18dcdce07c4e.png)

![image](https://user-images.githubusercontent.com/88278165/191562361-5d2ee9c8-762e-48b1-9570-dae0af3bb392.png)
 
Selain itu, saya juga menambahkan unit test pada tests.py pada folder mywatchlist untuk menguji ketiga URL di atas, berikut adalah potongan kodenya:

![image](https://user-images.githubusercontent.com/88278165/191562401-f744dccd-4e99-41c8-a76f-637226a66f82.png)
 
Saya lanjutkan dengan membuat folder css di dalam folder static, lalu membuat sebuah file bernama style.css di folder css tersebut. Lalu saya jalankan perintah python manage.py collectstatic dan python manage.py test untuk melakukan testing. Dapat dilihat bahwa testing berjalan dengan lancar:

![image](https://user-images.githubusercontent.com/88278165/191562502-95e2f9dd-0608-457a-884e-2af213409546.png)



