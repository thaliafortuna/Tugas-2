1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

Asynchronous programming adalah  membuat proses jalannya program bisa dilakukan secara bersamaan tanpa harus menunggu proses antrian. Asynchronous programming merupakan sebuah pendekatan pemrograman yang tidak terikat pada input output. Asynchronous programming melakukan pekerjaannya tanpa harus terikat dengan proses lain atau secara independent. 

Synchronous adalah proses jalannya program secara sequential. Sequential dalam artian berdasarkan antrian ekseskusi program. Synchronous programming artinya berada dalam urutan, yaitu setiap pernyataan kode dieksekusi satu per satu. Pada dasarnya sebuah pernyataan harus menunggu pernyataan sebelumnya untuk dieksekusi, dimana task dieksekusi sesuai dengan urutan dan prioritas task. 

2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Event-Driven Programming adalah salah satu teknik pemograman, yang konsep kerjanya tergantung dari kejadian atau event tertentu. Event-Driven programming juga bisa dibilang suatu paradigma pemrograman yang alur programnya ditentukan oleh suatu event / peristiwa yang merupakan keluaran atau tindakan pengguna atau bisa berupa pesan dari program lainnya.

Penerapan Event-Driven Programming di tugas kali ini dapat dilihat dari melakukan update table secara asinkronus menggunakan button refresh. Ketika menekan button refresh, akan terjadi pemanggilan metode updateTable() yang melakukan AJAX GET untuk menampilkan task terbaru di dalam tabel. 

3. Jelaskan penerapan asynchronous programming pada AJAX.

Penerapan asynchronous programming pada AJAX terletak pada AJAX get yang menerima data dan AJAX POST yang mengirimkan data. Penggunaan AJAX membuat proses jalannya program bisa dilakukan secara bersamaan karena proses GET dan POST telah dibedakan. Maka, GET tidak perlu menunggu POST karena keduanya terpisahkan, oleh karena itu refresh pun dapat dilakukan secara asinkronus tanpa reload satu page. Di konteks saya, hanya perlu menekan button, tidak usah reload page.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

Untuk melakukan AJAX GET, saya membuat sebuah fungsi view baru untuk mengembalikan seluruh data task dalam bentuk JSON. lalu menambahkan path /todolist/json dpada urls.py di folder todolist yang mnegarah pada fungsi baru tersebut. Selanjutnya, saya membuat sebuah html baru yang saya namakan todolist_ajax.html untuk tugas kali ini. Untuk melakukan pengambilan tugas menggunakan AJAX GET, saya membuat fungsi updateTable() yang menambahkan (append) date, title, dan description ke dalam table. Saya menggunakan counter agar memastikan task tidak double. Lalu ketika $(document).ready(function()), page akan ter-refresh secara asinkronus ketika menekan button refresh. Hal ini dikarenakan button refresh memanggil kembali fungsi updateTable().

AJAX POST digunakan ketika user menekan button submit alias $(document).on('submit', '#form_task', function(e)). AJAX POST dilakukan dengan mengambil konten dari title dan description yang telah diisi user dan menyimpannya dalam data. Saya menambahkan fungsi add_todolist_ajax pada views untuk menambahkan task baru ke dalam database, tidak lupa untuk menambahkan path /todolist/add yang mengarah ke fungsi tersebut. Pada fungsi add_todolist_ajax, akan dilakukan request.POST.get untuk title dan description tadi dan membuat objects.create dari model class sesuai dengan fields di dalamnya(date harini, user, title, dan description). Setelah membuatnya, tidak lupa untuk di-save dan return HttpResponse dan render. Melanjutkan AJAX POST di todolist_ajax.html, saya panggil kembali fungsi updateTable() dan reload page ketika function success.

Selain AJAX GET dan AJAX POST, tugas kali ini juga mengimplementasikan modal. Saya mempelajari modal melalui Modal Bootstrap v5.2 dan menerapkannya di todolist_ajax.html. Ketika button submit di modal ditekan, maka modal akan tertutup dan POST akan dijalankan.
