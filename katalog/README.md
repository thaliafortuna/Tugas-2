Tugas-2 PBP
Thalia Fortuna, NPM: 2106751890

https://aplikasidjango.herokuapp.com/katalog/

Pertanyaan pemicu:
•	Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html; 
•	Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment? 
•	Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
 

Kaitan antara urls.py, views.py, models.py, dan berkas HTML:
Mengacu pada bagan di atas, Django adalah framework yang mengikuti struktur MVT (Model-View-Template), yang merupakan turunan dari struktur MVC (Model-View-Controller). Ketika terdapat request client di sebuah web aplikasi berbasis Django, permintaan yang masuk ke dalam sever Django akan diproses melalui urls.py terlebih dahulu yang bertujuan untuk memilih dan meneruskan proses ke views yang telah didesain oleh developer untuk memproses permintaan. Jika diperlukan akses database, views akan memanggil query ke models dan database akan mengembalikan hasil query ke views. Setelah selesai diproses, hasil proses akan dipetakan ke dalam HTML. HTML pun dikembalikan lagi ke user sebagai respons.
Penggunaan virtual environment atau lingkungan virtual bertujuan untuk memisahkan pengaturan dan package yang diinstall pada setiap proyek Django. Dalam kata lain, virtual environment mencegah perubahan yang dilakukan pada suatu proyek dalaml memengaruhi proyek lainnya. Maka dari itu, setiap proyek Django seringkali memiliki virtual environmentnya masing-masing.

Pada tugas-2 ini, kami menggunakan template untuk memudahkan proyek. Maka dari itu, hal yang pertama dilakukan adalah menggunakan fitur “use this template” pada repository template github. Dengan template tersebut, saya membuat repositori baru yang di-clone ke dalam computer saya dengan perintah git clone <>. Selanjutnya, saya mengubah directory cmd menjadi repository yang telah di-clone sebelumnya dan membuat sebuah virtual environment dengan perintah python -m venv env. Virtual enviromeent dinyalakan dengan perintah env\Scripts\activate.bat sesuai dengan jenis operation system yang saya pakai, yakni Windows. Selanjutnya, dilakukan install dependencies yang diperlukan untuk menjalankan proyek Django dengan perintah pip install -r requirements.txt. Dengan langkah permulaan di atas, saya telah berhasil mengonfigurasi repositori dan proyek Django.
Selanjutnya, saya melakukan pengecekan terhadap template yang telah saya clone. Ternyata, sudah terdapat sebuah Django-app Bernama katalog yang telah ditambahkan juga pada variabel ‘INSTALLED_APPS’ pada file settings.py di folder project_django. Maka dari itu, saya tidak membuat aplikasi Django baru dan melanjutkan proses ke konfigurasi model. Saya melakukan pengecekan terhadap file models.py dan menemukan bahwa models telah diimport sehingga dapat dilanjutkan ke langkah migrasi. Saya menjalankan perintah python manage.py makemigrations untuk mempersiapkan migrasi skema model ke dalam database Django lokal. Dilanjutkan dengan python manage.py migrate untuk menerapkan skema model tersebut ke dalam database Django lokal. Setelah melakukan migrasi ke dalam database Django lokal, saya melakukan pengecekan terhadap ketersediaan data dan menemukan file initial_catalog_data.json yang berada di folder fixtures di dalam folder aplikasi katalog. Untuk memasukkan data yang berada di file json tersebut ke dalam database Django lokal, saya menjalankan perintah python manage.py loaddata initial_wishlist_data.json.

 
Setelah mengonfigurasi model, proses dilanjutkan dengan mengimplementasi views. Di dalam folder aplikasi katalog, tepatnya file views.py, saya menambahkan sebuah fungsi Bernama show_katalog yang menerima parameter request. Fungsi tersebut akan mengambil data berupa CatalogItem dari models.py sehingga menambahkan “from katalog.models import CatalogItem” untuk melakukan pengambilian data dari database. Dilanjutkan dengan membuat data_barang_katalog dan context yang akan mempermudah konteks variabel yang dituliskan di HTML. Pemanggilan tersebut berfungsi untuk memanggil query ke model database dan menyimpan hasil query tersebut ke dalam sebuah variabel. Fungsi ini pun nantinya mengembalikan render (request, ‘katalog.html, context). 

 
Untuk melakukan routing terhadap views yang telah dibuat agar dapat menampilkan file HTML melalui browser, urls.py di folder aplikasi katalog diisi sedemikian rupa yaitu mengisi app_name dan menambahkan path pada variabel urlpatterns.
 
Dilanjutkan dengan mendaftarkan aplikasi katalog ke dalam urls.py yang berada di folder project_django pada variabel urlpatterns.

 
 
Selanjutnya, di dalam folder templates yang berada di dalam folder aplikasi katalog, terdapat sebuah file HTML bernama katalog.html yang akan saya modifikasi. Sesuai context yang telah saya tetapkan di file views.py, saya mengisi nama dan id menggunakan sintaks {{nama}} dan {{id}}. Dilanjutkan dengan menambahkan table dengan judul-judul kecil: Item name, item price, item stock, rating, description, dan item URL. Selanjutnya, saya melakukan iterasi terhadap list_barang yang merupakan sebuah container berisikan objek yang telah dirender ke dalam HTML.
Setelah membuat fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML. Lalu membuat routing untuk memetakan fungsi tersebut dan memetakan data dalam HTML menjadi sintaks Django untuk pemetaan data template, saya melakukan deployment ke Heroku terhadap aplikasi katalog yang telah dibuat. Tidak lupa melakukan git add, commit, dan push ke github, serta menambahkan secrets (settings->secrets->action) berupa HEROKU_API_KEY yang diambil dari API key Heroku serta HEROKU_APP_NAME yang diambil dari nama aplikasi yang digunakan, disini saya menggunakan app ‘aplikasidjango’ saya. Setelah mendambahkan secrets, saya menjalankan workflow sekali lagi untuk melihat keberhasilan deployment. Apabila telah sukses, aplikasi Django dapat dilihat dengan mengakses https://aplikasidjango.herokuapp.com/katalog/


