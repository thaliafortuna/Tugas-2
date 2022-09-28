Nama: Thalia Fortuna

Kelas: A

NPM: 2106751890

https://aplikasidjango.herokuapp.com/todolist/


1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
  
  {% csrf_token %} tag di Django template dimasukkan di dalam form. CSRF token sendiri adalah value unik dan rahasia oleh server-side dari aplikasi yang dibuat untuk melindungi CSRF (Cross Site Request Forgery) resource. CSRF token mencegah serangan CSRF dengan membuat penyerang tidak bisa membuat HTTP request yang valid, karena penyerang tidak dpaat menebak value dari CSRF token user, maka mereka tidak bisa membuat request dengan parameter-parameter yang diperlukan agar aplikasi menerima request tersebut. Jika tidak terdapat potongan kode {% csrf_token %} pada elemen <form>, maka Anda meng-expose aplikasi Anda terhadap CSRF attacks. Terutama ketika aplikasi memiliki aksi-aksi relevan seperti manipulasi user-specific data dan memiliki cookie-based session handling. 

  
  
Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
