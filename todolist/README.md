Nama: Thalia Fortuna

Kelas: A

NPM: 2106751890

https://aplikasidjango.herokuapp.com/todolist/


1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
  
  {% csrf_token %} tag di Django template dimasukkan di dalam form. CSRF token sendiri adalah value unik dan rahasia oleh server-side dari aplikasi yang dibuat untuk melindungi CSRF (Cross Site Request Forgery) resource. CSRF token mencegah serangan CSRF dengan membuat penyerang tidak bisa membuat HTTP request yang valid, karena penyerang tidak dpaat menebak value dari CSRF token user, maka mereka tidak bisa membuat request dengan parameter-parameter yang diperlukan agar aplikasi menerima request tersebut. Jika tidak terdapat potongan kode {% csrf_token %} pada elemen <form>, maka Anda meng-expose aplikasi Anda terhadap CSRF attacks. Terutama ketika aplikasi memiliki aksi-aksi relevan seperti manipulasi user-specific data dan memiliki cookie-based session handlin, attacker pun bisa meng-trigger HTTP request dan mendapat cookie dalam request, sehingga dapat memanipulasi data user. Secara kode, ketika dicoba tanpa menggunakan tag {% csrf_token %} dan di-run di localhost, site akan mengembalikan "CSRF verification fialed. Request aborted." dan menjadi Forbidden.

 
2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

Bisa. Membuat form secara manual dilakukan dengan memunculkan {{ form }} dan melakukan manipulasi kolom dan baris secara manual. Hal ini dilakukan dengan membagi <div></div>, <label></label>, dan memanggil form secara spesifik seperti {{ form.title }}. Namun dengan adanya kemudahan form.as_table, render akan dilakukan dalam bentuk table cells dengan tag <tr>.
  
  
3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

  Ketika pengguna melakukan submisi melalui HTML form, <form> pada HTML akan mendefinisikan bagaimana data akan dikirim. Atribut form yaitu Action akan menentukan kemana data dikirim, jika action kosong maka akan dikirim ke halaman dimana form berada. Selain action, ada juga atribut form yaitu method akan mendefinisikan bagaimana data dikirim. Di kasus ini, saya menggunakan POST method untuk menambahkan data ke body dari HTTP request. Dikarenakan saya menggunakan method POST, saya mengosongkan Action karena data tidak akan ditambahkan ke URL. Lalu form akan dicek apakah valid di views.py, lalu diolah, di kasus ini saya menggunakan cleane_data untuk mengambil data sesuai models lalu menambahkan models aplikasi dengan penambahan dari form. Tidak lupa melakukan save() yang menyimpan  model instance ke database. Barulah data siap digunakan di template manapun.

 
4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

  Pertama, saya membuat dan menyalakan virtual environment, barulah saya membuat aplikasi todolist di proyek tugas Django dengan python manage.py startapp todolist. Saya memasukkan aplikasi todolist pada INSTALLED_APPS di settings.py dan mulai membuat models di folder todolist.
  
  Setelah membuat models di file models.py, saya mempersiapkan migrasi dan menerapkan skema model ke database Django lokal dengan python manage.py makemigrations dan python manage.py migrate.
  
  Lalu pada views.py, saya membuat fungsi register, login_user, logout_user, show_todolist, dan create_todolist.
  
  Setelah membuat fungsi pada views, saya melakukan routing todolist/ di urls.py yang berada di folder project_django. Tidak lupa melakukan routing juga pada urls.py yang berada di folder todolist, saya memastikan setiap path dihubungkan dengan fungsi views yang tepat.
  
  Pada folder todolist, daya membuat folder templates dan beberapa files di dalamnya: create-task.html, login.html, register.html, dan todolist.html.
  
  Login.html akan me
  
  
