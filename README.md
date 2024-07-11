
GET+     api/todos/' LİSTELEME
POST+    api/todos/create/' CREATE
GET+     api/todos/<int:pk>/' İD Sİ GİRİLEN TODO GÖSTERME
put+     api/todos/update/<int:pk>/' İD Sİ  GİRİLEN TODO GÜNCELLE
DELETE+  api/todos/delete/<int:pk>/'İD Sİ GİRİLEN TODO SİL
		
	GET /todos/?search=example  EXAMPLE YERİNE İNPUT GİRİLECEK ARAMA MOTORU OLARAK ÇALIŞIR
	GET /todos/?completed=False   COMPLETEDE GÖRE FİLTRELER TRUE FALSE KISMI İNPUT ALINACAK
