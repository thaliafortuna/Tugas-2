Nama: Thalia Fortuna

Kelas: A

NPM: 2106751890

https://aplikasidjango.herokuapp.com/todolist/


1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
  
  {% csrf_token %} tag di Django template dimasukkan di dalam form. CSRF token sendiri adalah value unik dan rahasia oleh server-side dari aplikasi yang dibuat untuk melindungi CSRF (Cross Site Request Forgery) resource. CSRF token mencegah serangan CSRF dengan membuat penyerang tidak bisa membuat HTTP request yang valid, karena penyerang tidak dpaat menebak value dari CSRF token user, maka mereka tidak bisa membuat request dengan parameter-parameter yang diperlukan agar aplikasi menerima request tersebut. Jika tidak terdapat potongan kode {% csrf_token %} pada elemen <form>, maka Anda meng-expose aplikasi Anda terhadap CSRF attacks. Terutama ketika aplikasi memiliki aksi-aksi relevan seperti manipulasi user-specific data dan memiliki cookie-based session handlin, attacker pun bisa meng-trigger HTTP request dan mendapat cookie dalam request, sehingga dapat memanipulasi data user. Secara kode, ketika dicoba tanpa menggunakan tag {% csrf_token %} dan di-run di localhost, site akan mengembalikan "CSRF verification fialed. Request aborted." dan menjadi Forbidden.

 
2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat < form > secara manual.

Bisa. Membuat form secara manual dilakukan dengan memunculkan {{ form }} dan melakukan manipulasi kolom dan baris secara manual. Hal ini dilakukan dengan membagi < div >, < label >, dan memanggil form secara spesifik seperti {{ form.title }}. Namun dengan adanya kemudahan form.as_table, render akan dilakukan dalam bentuk table cells dengan tag <tr>.
  
  
3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

  Ketika pengguna melakukan submisi melalui HTML form, <form> pada HTML akan mendefinisikan bagaimana data akan dikirim. Atribut form yaitu Action akan menentukan kemana data dikirim, jika action kosong maka akan dikirim ke halaman dimana form berada. Selain action, ada juga atribut form yaitu method akan mendefinisikan bagaimana data dikirim. Di kasus ini, saya menggunakan POST method untuk menambahkan data ke body dari HTTP request. Dikarenakan saya menggunakan method POST, saya mengosongkan Action karena data tidak akan ditambahkan ke URL. Lalu form akan dicek apakah valid di views.py, lalu diolah, di kasus ini saya menggunakan cleaned_data untuk mengambil data sesuai models lalu menambahkan models aplikasi dengan penambahan dari form. Tidak lupa melakukan save() yang menyimpan  model instance ke database. Barulah data siap digunakan di template manapun.

 
4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

  Pertama, saya membuat dan menyalakan virtual environment, barulah saya membuat aplikasi todolist di proyek tugas Django dengan python manage.py startapp todolist. Saya memasukkan aplikasi todolist pada INSTALLED_APPS di settings.py dan mulai membuat models di folder todolist. Tidak lupa melakukan routing todolist/ di urls.py yang berada di folder project_django agar pengguna dapat mengakses [loc](http://localhost:8000/todolist)
  
  ![image](https://user-images.githubusercontent.com/88278165/192799867-968339a0-214c-4efc-9ba6-854026ea5e4f.png)

  Di models.py, saya menambahkan class ListToDo yang isinya adalah user (ForeignKey), date(DateField), title(CharField), dan description(TextField). Setelah membuat models, saya mempersiapkan migrasi dan menerapkan skema model ke database Django lokal dengan python manage.py makemigrations dan python manage.py migrate. Lalu pada folder todolist, saya membuat folder templates dan beberapa files di dalamnya, yaitu create-task.html, login.html, register.html, dan todolist.html. 
  
  todolist.html akan menjadi halaman utama dimana saya menampilkan user, tabel todolist (title, description, date) serta tombol Tambah Task Baru dan logout. Untuk menampilkan tabel, saya melakukan forloop for task in user.todolist.all {{ task.date }}, {{ task.title }}, {{ task.description }}(todolist adalah related_name dari foreign key user).
  
  login.html akan menjadi halaman login dimana terdapat form berupa username dan password. Jika tidak memiliki akun, maka dapat memencet "Buat Akun" yang akan membawa pengguna ke tampilan register.html. register.html adalah halaman register dimana terdapat form registrasi dan tombol submit.
  
  create-task.html akan menjadi halaman pembuatan task jika memencet tombol Buat Task Baru. Di halaman ini juga terdapat form yang menerima title dan description dari aktivitas todo sesuai user yang sedang login. Ada juga tombol submit untuk mengirimkan data.
  
  ![image](https://user-images.githubusercontent.com/88278165/192800576-e0bffda0-2a82-40d0-9e12-31888dd08384.png)

  Lalu pada views.py, saya membuat fungsi register, login_user, logout_user, show_todolist, dan create_todolist serta mengimport segala yang dibutuhkan dalam pembuatan fungsi. Pada fungsi register, saya membuat form dan menyimpan data form untuk login nanti. Pada fungsi login, dilakukan pengecekan terhadap data yang dimasukkan dan data yang sudah tersimpan, sehingga hanya yang telah register yang bisa masuk. Pada fungsi logout_user, dilakukan logout sehingga kembali ke halaman login. Jika pengguna telah berhasil login, maka ia akan dibawa ke halaman todolist dimana fungsi show_todolist akan menampilkan semua data models yang telah disimpan. Selain tomboll logout, di halaman ini juga terdapat tombol Buat task baru yang membawa kita ke halaman create-task.html. Disini, fungsi create_todolist bertugas untuk membuat form dan membiarkan pengguna untuk memasukkan data baru. Data form tersebut saya kembalikan di variabel form. Lalu sata memastikan form telah valid dengan form.is_valid. Jika sudah, maka data akan diolah. Saya menggunakan form.cleaned_data["jenismodel"] untuk mengambil data sesuai dengan model tersebut lalu menambahkan data dari form ke models aplikasi (saya kembalikan di variabel updated), kecuali date yang menggunakan datetime.datetime.now() untuk memasukkan tanggal hari ini dalam model date. Lalu, tidak lupa melakukan save() terhadap variabel updated, hal inilah yang menyimpan  model instance ke database. Barulah dengan request.user.todolist.add(updated), bisa menambahkan todolist tersebut sesuai dengan user yang sedang login. Dengan itu, data siap ditampillkan menggunakan fungsi show_todolist dan todolist.html, todolist user ini nantinya akan ditampilkan di halaman utama todolist. 
  
  Setelah membuat fungsi pada views, tidak lupa melakukan routing juga pada urls.py yang berada di folder todolist, saya memastikan setiap path dihubungkan dengan fungsi views yang tepat. Lalu, saya melakukan git add, commit, dan push untuk melakukan deployment ke Heroku (sudah pernah memasukkan secrets). Setelah deployment, aplikasi dapat diakses di https://aplikasidjango.herokuapp.com/todolist/ , dimana saya telah membuat dua akun pengguna dan tiga dummy data masing-masingnya.
  
  ![image](https://user-images.githubusercontent.com/88278165/192808190-3131bb41-24d8-4478-bad2-18438ef2e4fd.png)

  ![image](https://user-images.githubusercontent.com/88278165/192808247-e63db264-30ac-4624-b2f9-9ef12671d065.png)

  
  
  
  
