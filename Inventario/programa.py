import sys
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from tablahash import Tablahash
from articulo import Articulo
from validaciones import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("La Primera Estacion")
        self.setFont(QFont('Ubuntu'))
        self.setGeometry(200,100,1024,600)
        self.setStyleSheet(
            "background:rgba(20,50,50,1);"
        )
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.componentes = {}
        self.articulos = cargar_registros()
        self.tablahash = generar_tabla_hash(self.articulos)
        self.mensaje = QMessageBox()
        self.mensaje.setStyleSheet("background:white;"+"color:black;")
        

        self.show()

    #Limpiar el frame actual
    def limpiar_frame(self):
        for comp in self.componentes:
            self.componentes[comp].hide()
        self.componentes = {}
    
    #frame donde se cargan todos los componentes
    def frame_principal(self):
        self.frame_principal_layout = QGridLayout() 
        self.frame = QFrame(self)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet(
            "#frame { border:2px solid rgba(25,150,25,1); border-radius:4px; }"
        )
        self.frame.setLayout(self.frame_principal_layout)
        self.frame.setFrameShape(QFrame.StyledPanel)
        
        self.layout.addWidget(self.frame)

    #frame secundaria para el menu
    def frame_botones(self):
        frame_botones_layout = QVBoxLayout()
        self.frame_botones = QFrame(self)
        self.frame_botones.setObjectName("frame")
        self.frame_botones.setStyleSheet(
            "#frame { border:2px solid rgba(25,150,25,1); border-radius:4px; }"
        )
        self.frame_botones.setFrameShape(QFrame.StyledPanel)
        self.frame_botones.setFixedWidth(200)
        self.frame_botones.setLayout(frame_botones_layout)

        boton_consultar_articulo = QPushButton("Consultar Articulo")
        boton_consultar_articulo.clicked.connect(self.mostrar_frame_consulta)
        boton_consultar_articulo.setStyleSheet(
            "background:rgba(60,150,0,1);"+
            "padding:8px;"+
            "color:white;"
        )

        boton_agregar_articulo = QPushButton("Agregar Articulo")
        boton_agregar_articulo.clicked.connect(self.mostrar_frame_agregar)
        boton_agregar_articulo.setStyleSheet(
            "background:rgba(60,150,0,1);"+
            "padding:8px;"+
            "color:white;"
        )

        boton_modificar_articulo = QPushButton("Modificar Articulo")
        boton_modificar_articulo.clicked.connect(self.mostrar_frame_modificar)
        boton_modificar_articulo.setStyleSheet(
            "background:rgba(60,150,0,1);"+
            "padding:8px;"+
            "color:white;"
        )

        boton_eliminar_articulo = QPushButton("Eliminar Articulo")
        boton_eliminar_articulo.clicked.connect(self.mostrar_frame_eliminar)
        boton_eliminar_articulo.setStyleSheet(
            "background:rgba(60,150,0,1);"+
            "padding:8px;"+
            "color:white;"
        )

        boton_compra_venta = QPushButton("Compra o Venta")
        boton_compra_venta.clicked.connect(self.mostrar_frame_compra__venta)
        boton_compra_venta.setStyleSheet(
            "background:rgba(60,150,0,1);"+
            "padding:8px;"+
            "color:white;"
        )


        boton_listar_articulo = QPushButton("Listar Articulos")
        boton_listar_articulo.clicked.connect(lambda:self.mostrar_tabla(self.articulos))
        boton_listar_articulo.setStyleSheet(
            "background:rgba(60,150,0,1);"+
            "padding:8px;"+
            "color:white;"
        )

        boton_ventas_2020 = QPushButton("Ventas 2020")
        boton_ventas_2020.clicked.connect(self.mostrar_ventas_2020)
        boton_ventas_2020.setStyleSheet(
            "background:rgba(60,150,0,1);"+
            "padding:8px;"+
            "color:white;"
        )
        boton_listar_disponibles = QPushButton("Articulos Disponibles")
        boton_listar_disponibles.clicked.connect(self.mostrar_disponibles)
        boton_listar_disponibles.setStyleSheet(
            "background:rgba(60,150,0,1);"+
            "padding:8px;"+
            "color:white;"
        )

        boton_mostrar_inicio = QPushButton("Inicio")
        boton_mostrar_inicio.clicked.connect(self.mostrar_frame_inicio)
        boton_mostrar_inicio.setStyleSheet(
            "background:rgba(60,150,0,1);"+
            "padding:8px;"+
            "color:white;"
        )
    


        frame_botones_layout.addWidget(boton_mostrar_inicio)
        frame_botones_layout.addWidget(boton_consultar_articulo)
        frame_botones_layout.addWidget(boton_agregar_articulo)
        frame_botones_layout.addWidget(boton_modificar_articulo)
        frame_botones_layout.addWidget(boton_eliminar_articulo)
        frame_botones_layout.addWidget(boton_compra_venta)
        frame_botones_layout.addWidget(boton_listar_articulo)
        frame_botones_layout.addWidget(boton_ventas_2020)
        frame_botones_layout.addWidget(boton_listar_disponibles)

        self.layout.addWidget(self.frame_botones)

    def frame_inicio(self):
        header = QLabel()
        header.setText("Inventario Papeleria")
        header.setStyleSheet(
            "color:white;"+
            "font-size:48px;"+
            "font-weight:bold;"
        )
        self.componentes["header"] = header

        sub_header = QLabel()
        sub_header.setText("Desarrolladores")
        sub_header.setAlignment(Qt.AlignCenter)
        sub_header.setStyleSheet(
            "color:white;"+
            "font-size:32px;"+
            "font-weight:bold;"+
            "margin:40px 0;"
        )
        self.componentes["sub_header"] = sub_header


        imagen_1 = QPixmap('gamer.png')
        label_imagen1 = QLabel()
        label_imagen1.setPixmap(imagen_1)
        label_imagen1.setAlignment(Qt.AlignCenter)
        self.componentes["label_imagen1"] = label_imagen1

        nombre_desarrollador1 = QLabel()
        nombre_desarrollador1.setText("Cesar Zabala")
        nombre_desarrollador1.setStyleSheet(
            "color:white;"+
            "font-size:24px;"+
            "font-weight:bold;"
        )
        self.componentes["nombre_desarrollador1"] = nombre_desarrollador1

        imagen_2 = QPixmap('programmer.png')
        label_imagen2 = QLabel()
        label_imagen2.setPixmap(imagen_2)
        label_imagen2.setAlignment(Qt.AlignCenter)
        self.componentes["label_imagen2"] = label_imagen2

        nombre_desarrollador2 = QLabel()
        nombre_desarrollador2.setText("Jesus Figuera")
        nombre_desarrollador2.setStyleSheet(
            "color:white;"+
            "font-size:24px;"+
            "font-weight:bold;"
        )
        self.componentes["nombre_desarrollador2"] = nombre_desarrollador2

        imagen_3 = QPixmap('senior.png')
        label_imagen3 = QLabel()
        label_imagen3.setPixmap(imagen_3)
        label_imagen3.setAlignment(Qt.AlignCenter)
        self.componentes["label_imagen3"] = label_imagen3

        nombre_desarrollador3 = QLabel()
        nombre_desarrollador3.setText("Ulises Hernandez")
        nombre_desarrollador3.setStyleSheet(
            "color:white;"+
            "font-size:24px;"+
            "font-weight:bold;"
        )
        self.componentes["nombre_desarrollador3"] = nombre_desarrollador3

        
        footer = QLabel()
        footer.setText("UDO - Nueva Esparta")
        footer.setStyleSheet(
            "font-size:24px;"+
            "color:white;"+
            "margin-top:150px;"+
            "font-weight:bold;"
        )
        footer.setAlignment(Qt.AlignCenter)
        self.componentes["footer"] = footer
        
        self.frame_principal_layout.addWidget(self.componentes["header"],0,0,1,3)
        self.frame_principal_layout.addWidget(self.componentes["sub_header"],1,0,1,3)
        self.frame_principal_layout.addWidget(self.componentes["label_imagen1"],2,0)
        self.frame_principal_layout.addWidget(self.componentes["label_imagen2"],2,1)
        self.frame_principal_layout.addWidget(self.componentes["label_imagen3"],2,2)
        self.frame_principal_layout.addWidget(self.componentes["nombre_desarrollador1"],3,0)
        self.frame_principal_layout.addWidget(self.componentes["nombre_desarrollador2"],3,1)
        self.frame_principal_layout.addWidget(self.componentes["nombre_desarrollador3"],3,2)
        self.frame_principal_layout.addWidget(self.componentes["footer"],4,0,1,3)
        self.frame_principal_layout.setRowStretch(10,2)
    
    #frame para consultar un articulo
    
    def frame_consulta(self):
        header = QLabel()
        header.setText("Consultar Articulo")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size:24px;"+"font-weight:bold;"+"margin-bottom:10px;"+"color:white;")

        self.componentes["header"] = header


        referencia_label = QLabel()
        referencia_label.setText("Referencia")
        referencia_label.setStyleSheet("color:white;"+"margin:0 200px;"+"font-size:16px;")

        self.componentes["referencia_label"] = referencia_label



        leer_referencia = QLineEdit()
        leer_referencia.setStyleSheet(
            "font-size:16px;"+
            "background:white;"+
            "margin-bottom:10px;"+
            "margin-left:200px;"+
            "margin-right:200px;"
        )
        self.componentes["leer_referencia"] = leer_referencia

        boton_consulta = QPushButton("Consultar")
        boton_consulta.setStyleSheet(
            "margin:0 250px;"+
            "font-size:16px;"+
            "padding:6px;"+
            "color:white;"+
            "background:rgba(0,0,140,1);"
            )
        boton_consulta.clicked.connect(lambda:self.buscar_articulo(leer_referencia.text()))
        self.componentes["boton_consulta"] = boton_consulta

        self.frame_principal_layout.addWidget(self.componentes["header"],0,0)
        self.frame_principal_layout.addWidget(self.componentes["referencia_label"],1,0)
        self.frame_principal_layout.addWidget(self.componentes["leer_referencia"],2,0)
        self.frame_principal_layout.addWidget(self.componentes["boton_consulta"],3,0)
        self.frame_principal_layout.setRowStretch(4,1)

    #frame para agregar un articulo
    def frame_agregar(self):
        header = QLabel()
        header.setText("Agregar Articulo")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size:24px;"+"font-weight:bold;"+"margin-bottom:10px;"+"color:white;")

        self.componentes["header"]  = header

        referencia_label = QLabel()
        referencia_label.setText("Referencia")
        referencia_label.setStyleSheet(
            "font-size:16px;"+
            "color:white;"
        )

        self.componentes["referencia_label"] = referencia_label

        leer_referencia = QLineEdit()
        leer_referencia.setStyleSheet(
            "background:white;"+
            "font-size:16px;"+
            "margin-right:350px;"
        )

        self.componentes["leer_referencia"] = leer_referencia

        distribuidora_label = QLabel()
        distribuidora_label.setText("Distribuidora")
        distribuidora_label.setStyleSheet(
            "font-size:16px;"+
            "color:white;"
        )

        self.componentes["distribuidora_label"] = distribuidora_label

        leer_distribuidora = QLineEdit()
        leer_distribuidora.setStyleSheet(
            "background:white;"+
            "font-size:16px;"+
            "margin-right:350px;"
        )

        self.componentes["leer_distribuidora"] = leer_distribuidora

        nombre_label = QLabel()
        nombre_label.setText("Nombre")
        nombre_label.setStyleSheet(
            "font-size:16px;"+
            "color:white;"
        )

        self.componentes["nombre_label"] = nombre_label

        leer_nombre = QLineEdit()
        leer_nombre.setStyleSheet(
            "background:white;"+
            "font-size:16px;"+
            "margin-right:350px;"
        )

        self.componentes["leer_nombre"] = leer_nombre

        cantidad_label = QLabel()
        cantidad_label.setText("Cantidad en inventario")
        cantidad_label.setStyleSheet(
            "font-size:16px;"+
            "color:white;"
        )

        self.componentes["cantidad_label"] = cantidad_label

        leer_cantidad = QLineEdit()
        leer_cantidad.setStyleSheet(
            "background:white;"+
            "font-size:16px;"+
            "margin-right:350px;"
        )

        self.componentes["leer_cantidad"] = leer_cantidad


        precio_label = QLabel()
        precio_label.setText("Precio")
        precio_label.setStyleSheet(
            "font-size:16px;"+
            "color:white;"
        )

        self.componentes["precio_label"] = precio_label

        leer_precio = QLineEdit()
        leer_precio.setStyleSheet(
            "background:white;"+
            "font-size:16px;"+
            "margin-right:350px;"
        )

        self.componentes["leer_precio"] = leer_precio

        fecha_label = QLabel()
        fecha_label.setText("Fecha de salida (MM/DD/AA)")
        fecha_label.setStyleSheet(
            "font-size:16px;"+
            "color:white;"
        )

        self.componentes["fecha_label"] = fecha_label

        leer_fecha = QLineEdit()
        leer_fecha.setStyleSheet(
            "background:white;"+
            "font-size:16px;"+
            "margin-right:350px;"+
            "margin-bottom:20px;"
        )

        self.componentes["leer_fecha"] = leer_fecha

        boton_agregar = QPushButton("Agregar Articulo")
        boton_agregar.setStyleSheet(
            "margin:0 250px;"+
            "font-size:16px;"+
            "padding:6px;"+
            "color:white;"+
            "background:rgba(0,0,140,1);"
            )

        
        boton_agregar.clicked.connect(lambda:self.registrar_articulo(
            leer_referencia.text(),
            leer_distribuidora.text(),
            leer_nombre.text(),
            leer_cantidad.text(),
            leer_precio.text(),
            leer_fecha.text(),

        ))
        self.componentes["boton_agregar"] = boton_agregar
        



        self.frame_principal_layout.addWidget(self.componentes["header"],0,0)
        self.frame_principal_layout.addWidget(self.componentes["referencia_label"],1,0)
        self.frame_principal_layout.addWidget(self.componentes["leer_referencia"],2,0)
        self.frame_principal_layout.addWidget(self.componentes["distribuidora_label"],3,0)
        self.frame_principal_layout.addWidget(self.componentes["leer_distribuidora"],4,0)
        self.frame_principal_layout.addWidget(self.componentes["nombre_label"],5,0)
        self.frame_principal_layout.addWidget(self.componentes["leer_nombre"],6,0)
        self.frame_principal_layout.addWidget(self.componentes["cantidad_label"],7,0)
        self.frame_principal_layout.addWidget(self.componentes["leer_cantidad"],8,0)
        self.frame_principal_layout.addWidget(self.componentes["precio_label"],9,0)
        self.frame_principal_layout.addWidget(self.componentes["leer_precio"],10,0)
        self.frame_principal_layout.addWidget(self.componentes["fecha_label"],11,0)
        self.frame_principal_layout.addWidget(self.componentes["leer_fecha"],12,0)
        self.frame_principal_layout.addWidget(self.componentes["boton_agregar"],13,0)
        self.frame_principal_layout.setRowStretch(15,1)
    
    #frame para dibujar una tabla, tomando como parametro la lista con los datos
    def frame_tabla(self,articulos):

        boton_volver = QPushButton("Volver")
        boton_volver.setStyleSheet(
            "margin:0 200px;"+
            "padding:6px;"+
            "font-size:16px;"
        )
        boton_volver.clicked.connect(self.mostrar_frame_inicio)
        boton_volver.setStyleSheet(
            "margin-right:650px;"+
            "margin-top:20px;"+
            "font-size:16px;"+
            "padding:6px;"+
            "color:white;"+
            "background:rgba(0,0,140,1);"
            )
        self.componentes["boton_volver"] = boton_volver

        table_headers = ["Referencia","Distribuidora","Nombre","Cantidad","Precio","Fecha de salida"]
        tabla = QTableWidget()
        tabla.setFixedHeight(300)
        tabla.setColumnCount(6)
        tabla.setRowCount(len(articulos))
        tabla.setStyleSheet(
            "background:white;"
        )
        
        for index,articulo in enumerate(articulos):
            item1 = QTableWidgetItem(articulo.referencia)
            item2 = QTableWidgetItem(articulo.distribuidora)               
            item3 = QTableWidgetItem(articulo.nombre_art)                
            item4 = QTableWidgetItem(articulo.cantidad_art)
            item5 = QTableWidgetItem(articulo.precio)                
            item6 = QTableWidgetItem(articulo.fecha_salida["Dia"]+'/'+articulo.fecha_salida["Mes"]+"/"+articulo.fecha_salida["Año"])   
            tabla.setItem(index,0,item1)             
            tabla.setItem(index,1,item2)             
            tabla.setItem(index,2,item3)             
            tabla.setItem(index,3,item4)             
            tabla.setItem(index,4,item5)             
            tabla.setItem(index,5,item6)             
        tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        tabla.setHorizontalHeaderLabels(table_headers)
        tabla.verticalHeader().setVisible(False)

        self.componentes["tabla"] = tabla

        total_registros = QLabel()
        total_registros.setText("Total registros: "+str(len(articulos)))
        total_registros.setStyleSheet(
            "font-size:16px;"+
            "color:white;"
        )
        self.componentes["total_registros"] = total_registros

        self.frame_principal_layout.addWidget(self.componentes["boton_volver"],0,0)
        self.frame_principal_layout.addWidget(self.componentes["tabla"],1,0)
        self.frame_principal_layout.addWidget(self.componentes["total_registros"],2,0)

    def frame_eliminar(self):
        header = QLabel()
        header.setText("Eliminar Articulo")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size:24px;"+"font-weight:bold;"+"margin-bottom:10px;"+"color:white;")

        self.componentes["header"] = header


        referencia_label = QLabel()
        referencia_label.setText("Referencia")
        referencia_label.setStyleSheet("color:white;"+"margin:0 200px;"+"font-size:16px;")

        self.componentes["referencia_label"] = referencia_label



        leer_referencia = QLineEdit()
        leer_referencia.setStyleSheet(
            "font-size:16px;"+
            "background:white;"+
            "margin-left:200px;"+
            "margin-right:200px;"+
            "margin-bottom:10px;"
        )

        self.componentes["leer_referencia"] = leer_referencia

        boton_eliminar = QPushButton("Eliminar")
        boton_eliminar.setStyleSheet(
            "margin:0 250px;"+
            "font-size:16px;"+
            "padding:6px;"+
            "color:white;"+
            "background:rgba(150,0,0,1);"
            )
        boton_eliminar.clicked.connect(lambda:self.eliminar_articulo(leer_referencia.text()))
        self.componentes["boton_eliminar"] = boton_eliminar

        self.frame_principal_layout.addWidget(self.componentes["header"],0,0)
        self.frame_principal_layout.addWidget(self.componentes["referencia_label"],1,0)
        self.frame_principal_layout.addWidget(self.componentes["leer_referencia"],2,0)
        self.frame_principal_layout.addWidget(self.componentes["boton_eliminar"],3,0)
        self.frame_principal_layout.setRowStretch(4,1)

    def frame_modificar(self):

        header = QLabel()
        header.setText("Modificar Articulo")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size:24px;"+"font-weight:bold;"+"margin-bottom:10px;"+"color:white;")

        self.componentes["header"] = header


        referencia_label = QLabel()
        referencia_label.setText("Referencia")
        referencia_label.setStyleSheet(
            "font-size:16px;"+
            "color:white;"
        )

        self.componentes["referencia_label"] = referencia_label



        leer_referencia = QLineEdit()
        leer_referencia.setStyleSheet(
            "background:white;"+
            "font-size:16px;"+
            "margin-right:350px;"
        )

        self.componentes["leer_referencia"] = leer_referencia

        boton_buscar = QPushButton("Buscar")
        boton_buscar.setStyleSheet(
            "margin:0 250px;"+
            "font-size:16px;"+
            "padding:6px;"+
            "color:white;"+
            "background:rgba(0,0,140,1);"+
            "margin-top:10px;"
            )

        


        referencia_modificar_label = QLabel()
        referencia_modificar_label.setText("Modificar Referencia")
        referencia_modificar_label.setStyleSheet(
            "font-size:16px;"+
            "color:white;"
        )

        self.componentes["referencia_modificar_label"] = referencia_modificar_label

        leer_nueva_referencia = QLineEdit()
        leer_nueva_referencia.setEnabled(False)
        leer_nueva_referencia.setStyleSheet(
            "background:white;"+
            "font-size:16px;"+
            "margin-right:350px;"
        )
        self.componentes["leer_nueva_referencia"] = leer_nueva_referencia

        distribuidora_modificar_label = QLabel()
        distribuidora_modificar_label.setText("Modificar Distribuidora")
        distribuidora_modificar_label.setStyleSheet(
            "font-size:16px;"+
            "color:white;"
        )

        self.componentes["distribuidora_modificar_label"] = distribuidora_modificar_label

        leer_nueva_distribuidora = QLineEdit()
        leer_nueva_distribuidora.setEnabled(False)
        leer_nueva_distribuidora.setStyleSheet(
            "background:white;"+
            "font-size:16px;"+
            "margin-right:350px;"
        )
        self.componentes["leer_nueva_distribuidora"] = leer_nueva_distribuidora


        nombre_modificar_label = QLabel()
        nombre_modificar_label.setText("Modificar Nombre")
        nombre_modificar_label.setStyleSheet(
            "font-size:16px;"+
            "color:white;"
        )

        self.componentes["nombre_modificar_label"] = nombre_modificar_label

        leer_nuevo_nombre = QLineEdit()
        leer_nuevo_nombre.setEnabled(False)
        leer_nuevo_nombre.setStyleSheet(
            "background:white;"+
            "font-size:16px;"+
            "margin-right:350px;"
        )
        self.componentes["leer_nuevo_nombre"] = leer_nuevo_nombre

        cantidad_modificar_label = QLabel()
        cantidad_modificar_label.setText("Modificar Cantidad en Inventario")
        cantidad_modificar_label.setStyleSheet(
            "font-size:16px;"+
            "color:white;"
        )

        self.componentes["cantidad_modificar_label"] = cantidad_modificar_label

        leer_nueva_cantidad = QLineEdit()
        leer_nueva_cantidad.setEnabled(False)
        leer_nueva_cantidad.setStyleSheet(
            "background:white;"+
            "font-size:16px;"+
            "margin-right:350px;"
        )
        self.componentes["leer_nueva_cantidad"] = leer_nueva_cantidad

        precio_modificar_label = QLabel()
        precio_modificar_label.setText("Modificar Precio")
        precio_modificar_label.setStyleSheet(
            "font-size:16px;"+
            "color:white;"
        )

        self.componentes["precio_modificar_label"] = precio_modificar_label

        leer_nuevo_precio = QLineEdit()
        leer_nuevo_precio.setEnabled(False)
        leer_nuevo_precio.setStyleSheet(
            "background:white;"+
            "font-size:16px;"+
            "margin-right:350px;"
        )
        self.componentes["leer_nuevo_precio"] = leer_nuevo_precio

        fecha_modificar_label = QLabel()
        fecha_modificar_label.setText("Modificar Fecha")
        fecha_modificar_label.setStyleSheet(
            "font-size:16px;"+
            "color:white;"
        )

        self.componentes["fecha_modificar_label"] = fecha_modificar_label

        leer_nueva_fecha = QLineEdit()
        leer_nueva_fecha.setEnabled(False)
        leer_nueva_fecha.setStyleSheet(
            "background:white;"+
            "font-size:16px;"+
            "margin-right:350px;"
        )
        self.componentes["leer_nueva_fecha"] = leer_nueva_fecha

        boton_modificar = QPushButton("Modificar")
        boton_modificar.setEnabled(False)
        boton_modificar.setStyleSheet(
            "margin:0 250px;"+
            "margin-top:20px;"+
            "font-size:16px;"+
            "padding:6px;"+
            "color:white;"+
            "background:rgba(0,0,140,1);"
            )



        boton_buscar.clicked.connect(lambda:self.modificar_articulo(
            leer_referencia,
            leer_nueva_referencia,
            leer_nueva_distribuidora,
            leer_nuevo_nombre,
            leer_nueva_cantidad,
            leer_nuevo_precio,
            leer_nueva_fecha,
            boton_modificar
        ))


        self.componentes["boton_buscar"] = boton_buscar

        self.componentes["boton_modificar"] = boton_modificar


        self.frame_principal_layout.addWidget(self.componentes["header"],0,0)
        self.frame_principal_layout.addWidget(self.componentes["referencia_label"],1,0)
        self.frame_principal_layout.addWidget(self.componentes["leer_referencia"],2,0)
        self.frame_principal_layout.addWidget(self.componentes["boton_buscar"],3,0)
        self.frame_principal_layout.addWidget(self.componentes["referencia_modificar_label"],4,0)
        self.frame_principal_layout.addWidget(self.componentes["leer_nueva_referencia"],5,0)
        self.frame_principal_layout.addWidget(self.componentes["distribuidora_modificar_label"],6,0)
        self.frame_principal_layout.addWidget(self.componentes["leer_nueva_distribuidora"],7,0)
        self.frame_principal_layout.addWidget(self.componentes["nombre_modificar_label"],8,0)
        self.frame_principal_layout.addWidget(self.componentes["leer_nuevo_nombre"],9,0)
        self.frame_principal_layout.addWidget(self.componentes["cantidad_modificar_label"],10,0)
        self.frame_principal_layout.addWidget(self.componentes["leer_nueva_cantidad"],11,0)
        self.frame_principal_layout.addWidget(self.componentes["precio_modificar_label"],12,0)
        self.frame_principal_layout.addWidget(self.componentes["leer_nuevo_precio"],13,0)
        self.frame_principal_layout.addWidget(self.componentes["fecha_modificar_label"],14,0)
        self.frame_principal_layout.addWidget(self.componentes["leer_nueva_fecha"],15,0)
        self.frame_principal_layout.addWidget(self.componentes["boton_modificar"],16,0)
        self.frame_principal_layout.setRowStretch(18,1)
    
    def frame_compra_venta(self):
        compra_header = QLabel()
        compra_header.setText("Compra")
        compra_header.setAlignment(Qt.AlignCenter)
        compra_header.setStyleSheet(
            "font-size:16px;"+
            "color:white;"
        )
        self.componentes["compra_header"] = compra_header

        referencia_label_compra = QLabel()
        referencia_label_compra.setText("Referencia")
        referencia_label_compra.setStyleSheet(
            "color:white;"+
            "font-size:14px;"
        )
        self.componentes["referencia_label_compra"] = referencia_label_compra

        leer_compra_referencia = QLineEdit()
        leer_compra_referencia.setStyleSheet(
            "font-size:16px;"+
            "background:white;"
        )
        self.componentes["leer_compra_referencia"] = leer_compra_referencia

        cantidad_label_compra = QLabel()
        cantidad_label_compra.setText("Cantidad")
        cantidad_label_compra.setStyleSheet(
            "color:white;"+
            "font-size:14px;"
        )
        self.componentes["cantidad_label_compra"] = cantidad_label_compra

        leer_cantidad_compra = QLineEdit()
        leer_cantidad_compra.setStyleSheet(
            "font-size:16px;"+
            "background:white;"
        )
        
        self.componentes["leer_cantidad_compra"] = leer_cantidad_compra

        boton_compra = QPushButton("Registrar Compra")
        boton_compra.setStyleSheet(
            "margin:0 100px;"+
            "padding:8px;"+
            "font-size:16px;"+
            "color:white;"+
            "background:rgba(0,0,140,1);"
        )
        boton_compra.clicked.connect(lambda:self.registrar_compra(leer_compra_referencia.text(),leer_cantidad_compra.text()))
        self.componentes["boton_compra"]  = boton_compra

        venta_header = QLabel()
        venta_header.setText("Venta")
        venta_header.setStyleSheet(
            "font-size:16px;"+
            "color:white;"
        )
        venta_header.setAlignment(Qt.AlignCenter)
        self.componentes["venta_header"] = venta_header

        referencia_venta_label = QLabel()
        referencia_venta_label.setText("Referencia")
        referencia_venta_label.setStyleSheet(
            "color:white;"+
            "font-size:14px;"
        )
        self.componentes["referencia_venta_label"] = referencia_venta_label

        leer_referencia_venta = QLineEdit()
        leer_referencia_venta.setStyleSheet(
            "font-size:16px;"+
            "background:white;"
        )
        self.componentes["leer_referencia_venta"] = leer_referencia_venta


        cantidad_label_venta = QLabel()
        cantidad_label_venta.setText("Cantidad")
        cantidad_label_venta.setStyleSheet(
            "color:white;"+
            "font-size:14px;"
        )
        self.componentes["cantidad_label_venta"] = cantidad_label_venta

        leer_cantidad_venta = QLineEdit()
        leer_cantidad_venta.setStyleSheet(
            "font-size:16px;"+
            "background:white;"
        )
        self.componentes["leer_cantidad_venta"] = leer_cantidad_venta

        fecha_venta = QLabel()
        fecha_venta.setText("Fecha")
        fecha_venta.setStyleSheet(
            "color:white;"+
            "font-size:14px;"
        )
        self.componentes["fecha_venta"] = fecha_venta

        leer_fecha = QLineEdit()
        leer_fecha.setStyleSheet(
            "font-size:16px;"+
            "background:white;"
        )
        self.componentes["leer_fecha"] = leer_fecha

        boton_venta = QPushButton("Registrar Venta")
        boton_venta.setStyleSheet(
            "margin:0 100px;"+
            "padding:8px;"+
            "font-size:16px;"+
            "color:white;"+
            "background:rgba(0,0,140,1);"
        )
        boton_venta.clicked.connect(lambda:self.registrar_venta(leer_referencia_venta.text(),leer_cantidad_venta.text(),leer_fecha.text()))
        self.componentes["boton_venta"] = boton_venta

        self.frame_principal_layout.addWidget(self.componentes["compra_header"],0,0)
        self.frame_principal_layout.addWidget(self.componentes["referencia_label_compra"],1,0)
        self.frame_principal_layout.addWidget(self.componentes["leer_compra_referencia"],2,0)
        self.frame_principal_layout.addWidget(self.componentes["cantidad_label_compra"],3,0)
        self.frame_principal_layout.addWidget(self.componentes["leer_cantidad_compra"],4,0)
        self.frame_principal_layout.addWidget(self.componentes["boton_compra"],5,0)

        self.frame_principal_layout.addWidget(self.componentes["venta_header"],0,1)
        self.frame_principal_layout.addWidget(self.componentes["referencia_venta_label"],1,1)
        self.frame_principal_layout.addWidget(self.componentes["leer_referencia_venta"],2,1)
        self.frame_principal_layout.addWidget(self.componentes["cantidad_label_venta"],3,1)
        self.frame_principal_layout.addWidget(self.componentes["leer_cantidad_venta"],4,1)
        self.frame_principal_layout.addWidget(self.componentes["fecha_venta"],5,1)
        self.frame_principal_layout.addWidget(self.componentes["leer_fecha"],6,1)
        self.frame_principal_layout.addWidget(self.componentes["boton_venta"],7,1)

        self.frame_principal_layout.setRowStretch(10,1)
    
    def mostrar_frame_consulta(self):
        self.limpiar_frame()
        self.frame_consulta()

    def mostrar_frame_agregar(self):
        self.limpiar_frame()
        self.frame_agregar()
    def mostrar_tabla(self,articulos):
        self.limpiar_frame()
        self.frame_tabla(articulos)
    def mostrar_frame_eliminar(self):
        self.limpiar_frame()
        self.frame_eliminar()
       
    def mostrar_frame_modificar(self):
        self.limpiar_frame()
        self.frame_modificar()
    def mostrar_frame_compra__venta(self):
        self.limpiar_frame()
        self.frame_compra_venta()
    def mostrar_frame_inicio(self):
        self.limpiar_frame()
        self.frame_inicio()
    def buscar_articulo(self,referencia):
        if self.tablahash.buscar_elemento(referencia) != False:
            articulos = [self.tablahash.buscar_elemento(referencia)[0]]
            self.mostrar_tabla(articulos)
        else:
            self.mensaje.setText("Referencia Invalida")
            self.mensaje.setWindowTitle("Error")
            self.mensaje.exec()
            #QMessageBox.about(self,'Error','Referencia Invalida')
            

    def registrar_articulo(self,referencia,distribuidora,nombre_art,cantidad_art,precio,fecha):
        validar = validar_registro(referencia,distribuidora,nombre_art,cantidad_art,precio,fecha)
        if validar["status"]:
            if self.tablahash.buscar_elemento(referencia) != False:
                self.mensaje.setText("El articulo ya se encuentra registrado")
                self.mensaje.setWindowTitle("Error")
                self.mensaje.exec()
                #QMessageBox.about(self,'Error',"El articulo ya se encuentra registrado, intente con otra referencia")
            else:
                articulo = Articulo()
                articulo.registrar_articulov2(referencia,distribuidora,nombre_art,cantidad_art,precio,fecha)
                self.tablahash.agregar_elemento(articulo.referencia,articulo)
                actualizar_archivo(self.tablahash)
                self.articulos = cargar_registros()
                self.tablahash = generar_tabla_hash(self.articulos)
                self.mensaje.setText("Registro Exitoso")
                self.mensaje.setWindowTitle("Papeleria")
                self.mensaje.exec()
                #QMessageBox.about(self,"Clear","Registro Exitoso")
                self.mostrar_frame_agregar()
            
        else:
            self.mensaje.setText(validar["error_message"])
            self.mensaje.setWindowTitle("Error")
            self.mensaje.exec()
            #QMessageBox.about(self,"Error",validar["error_message"])

    
    def modificar_articulo_callback(self,referencia,distribuidora,nombre,cantidad,precio,fecha,indice):
        validar = validar_registro(referencia,distribuidora,nombre,cantidad,precio,fecha)
        if validar["status"]:
            articulo = Articulo()
            articulo.registrar_articulov2(referencia,distribuidora,nombre,cantidad,precio,fecha)
            self.tablahash.lista[indice[0]][indice[1]] = [articulo.referencia,articulo]
            actualizar_archivo(self.tablahash)
            self.articulos = cargar_registros()
            self.tablahash = generar_tabla_hash(self.articulos)
            self.mensaje.setText("Modificacion Exitosa!")
            self.mensaje.setWindowTitle("Papeleria")
            self.mensaje.exec()
            #QMessageBox.about(self,"Clear","Modificacion Exitosa!")
            self.mostrar_frame_modificar()
        else:
            self.mensaje.setText(validar["error_message"])
            self.mensaje.setWindowTitle("Error")
            self.mensaje.exec()
            #QMessageBox.about(self,"Error",validar["error_message"])
    def modificar_articulo(self,referencia,nueva_referencia,nueva_distribuidora,nuevo_nombre,nueva_cantidad,nuevo_precio,nueva_fecha,boton_modificar):
        validar = validar_cadena_alfanumerica(referencia.text(),10)
        if validar["status"]:
            if self.tablahash.buscar_elemento(referencia.text()) != False:
                articulo,indice = self.tablahash.buscar_elemento(referencia.text())[0],self.tablahash.buscar_elemento(referencia.text())[1]
                nueva_referencia.setEnabled(True),nueva_referencia.setText(articulo.referencia)
                nueva_distribuidora.setEnabled(True),nueva_distribuidora.setText(articulo.distribuidora)
                nuevo_nombre.setEnabled(True),nuevo_nombre.setText(articulo.nombre_art)
                nueva_cantidad.setEnabled(True),nueva_cantidad.setText(articulo.cantidad_art)
                nuevo_precio.setEnabled(True),nuevo_precio.setText(articulo.precio)
                nueva_fecha.setEnabled(True),nueva_fecha.setText(
                    articulo.fecha_salida["Dia"]+'/'+
                    articulo.fecha_salida["Mes"]+'/'+
                    articulo.fecha_salida["Año"]
                )
                boton_modificar.setEnabled(True)
                boton_modificar.clicked.connect(lambda:self.modificar_articulo_callback(
                    nueva_referencia.text(),
                    nueva_distribuidora.text(),
                    nuevo_nombre.text(),
                    nueva_cantidad.text(),
                    nuevo_precio.text(),
                    nueva_fecha.text(),
                    indice
                ))
            else:
                self.mensaje.setText("Referencia Invalida")
                self.mensaje.setWindowTitle("Error")
                self.mensaje.exec()
        else:
            self.mensaje.setText(validar["error_message"])
            self.mensaje.setWindowTitle("Error")
            self.mensaje.exec()
            #QMessageBox.about(self,'Clear',validar["error_message"])

    def eliminar_articulo(self,referencia):
        validar = validar_cadena_alfanumerica(referencia,10)
        if validar["status"]:
            if self.tablahash.buscar_elemento(referencia) != False:
                self.mensaje.setText("Esta seguro que desea eliminar el articulo?")
                self.mensaje.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                respuesta = self.mensaje.exec()
                if respuesta == QMessageBox.Ok:
                    self.mensaje.setStandardButtons(QMessageBox.Ok)
                    indice = self.tablahash.buscar_elemento(referencia)[1]
                    self.tablahash.lista[indice[0]][indice[1]][1].referencia+='*'
                    actualizar_archivo(self.tablahash)
                    self.articulos = cargar_registros()
                    self.tablahash = generar_tabla_hash(self.articulos)
                    self.mensaje.setText("Articulo Eliminado")
                    self.mensaje.setWindowTitle("Papeleria")
                    self.mensaje.exec()
                    #QMessageBox.about(self,"Clear","Articulo Eliminado")
                    self.mostrar_frame_eliminar()
            else:
                self.mensaje.setText("Referencia Invalida")
                self.mensaje.setWindowTitle("Error")
                self.mensaje.exec()
                #QMessageBox.about(self,"Error","Referencia Invalida")
        else:
            self.mensaje.setText(validar["error_message"])
            self.mensaje.setWindowTitle("Error")
            self.mensaje.exec()
            #QMessageBox.about(self,"Error",validar["error_message"])

    def registrar_compra(self,referencia,cantidad_compra):
        validar_referencia = validar_cadena_alfanumerica(referencia,10)
        validar_cantidad = validar_entero_positivo(cantidad_compra)
        if validar_referencia["status"]:
            if validar_cantidad["status"]:
                if self.tablahash.buscar_elemento(referencia) != False:
                    indice = self.tablahash.buscar_elemento(referencia)[1]
                    self.tablahash.lista[indice[0]][indice[1]][1].cantidad_art = int(self.tablahash.lista[indice[0]][indice[1]][1].cantidad_art)
                    self.tablahash.lista[indice[0]][indice[1]][1].cantidad_art+= int(cantidad_compra)
                    self.tablahash.lista[indice[0]][indice[1]][1].cantidad_art = str(self.tablahash.lista[indice[0]][indice[1]][1].cantidad_art)
                    actualizar_archivo(self.tablahash)
                    self.articulos = cargar_registros()
                    self.tablahash = generar_tabla_hash(self.articulos)
                    self.mensaje.setText("Compra Exitosa!")
                    self.mensaje.setWindowTitle("Papeleria")
                    self.mensaje.exec()
                    #QMessageBox.about(self,"Clear","Compra exitosa!")
                    self.mostrar_frame_compra__venta()
                else:
                    self.mensaje.setText("El articulo no esta registrado")
                    self.mensaje.setWindowTitle("Error")
                    self.mensaje.exec()
            else:
                indice = self.tablahash.buscar_elemento(referencia)[1]
                #QMessageBox.about(self,"Error",validar_cantidad["error_message"]) 
        else:
            self.mensaje.setText(validar_referencia["error_message"])
            self.mensaje.setWindowTitle("Error")
            self.mensaje.exec()
            #QMessageBox.about(self,"Error",validar_referencia["error_message"]) 
    def registrar_venta(self,referencia,cantidad_venta,fecha):
        validar_referencia = validar_cadena_alfanumerica(referencia,10)
        validar_cantidad = validar_entero_positivo(cantidad_venta)
        if validar_referencia["status"]:
            if validar_cantidad["status"]:
                if validar_fecha(fecha)["status"]:
                    if self.tablahash.buscar_elemento(referencia) != False:
                        indice = self.tablahash.buscar_elemento(referencia)[1]
                        cantidad_actual = self.tablahash.lista[indice[0]][indice[1]][1].cantidad_art
                        cantidad_actual = int(cantidad_actual)
                        cantidad_venta = int(cantidad_venta)
                        if cantidad_actual < cantidad_venta:
                            self.mensaje.setText("No puedes vender mas de lo que tienes!")
                            self.mensaje.setWindowTitle("Error")
                            self.mensaje.exec()
                            #QMessageBox.about(self,"Error","No puedes vender mas de lo que tienes!")
                        else:
                            nueva_cantidad = cantidad_actual-cantidad_venta
                            self.tablahash.lista[indice[0]][indice[1]][1].cantidad_art = str(nueva_cantidad)
                            dia,mes,ano = fecha.split('/')
                            self.tablahash.lista[indice[0]][indice[1]][1].fecha_salida["Dia"] = dia
                            self.tablahash.lista[indice[0]][indice[1]][1].fecha_salida["Mes"] = mes
                            self.tablahash.lista[indice[0]][indice[1]][1].fecha_salida["Año"] = ano
                            actualizar_archivo(self.tablahash)
                            self.articulos = cargar_registros()
                            self.tablahash = generar_tabla_hash(self.articulos)
                            self.mensaje.setText("Venta Exitosa!")
                            self.mensaje.setWindowTitle("Papeleria")
                            self.mensaje.exec()
                            #QMessageBox.about(self,"Error","Venta exitosa!")
                            self.mostrar_frame_compra__venta()
                    else:
                        self.mensaje.setText("Referencia Invalida")
                        self.mensaje.setWindowTitle("Error")
                        self.mensaje.exec()
                        #QMessageBox.about(self,"Error",validar_fecha(fecha)["error_message"])
                else:
                    self.mensaje.setText(validar_fecha(fecha)["error_message"])
                    self.mensaje.setWindowTitle("Error")
                    self.mensaje.exec()
                    #QMessageBox.about(self,"Error",validar_fecha(fecha)["error_message"])
            else:
                self.mensaje.setText(validar_cantidad["error_message"])
                self.mensaje.setWindowTitle("Error")
                self.mensaje.exec()
                #QMessageBox.about(self,"Error",validar_cantidad["error_message"])
        else:
            self.mensaje.setText(validar_referencia["error_message"])
            self.mensaje.setWindowTitle("Error")
            self.mensaje.exec()
            #QMessageBox.about(self,"Error",validar_referencia["error_message"])

    def mostrar_ventas_2020(self):
        ventas_2020 = []
        for articulo in self.articulos:
            if articulo.fecha_salida["Año"] == '2020':
                ventas_2020.append(articulo)
        self.mostrar_tabla(ventas_2020)

    def mostrar_disponibles(self):
        lista_disponibles = []
        for articulo in self.articulos:
            if int(articulo.cantidad_art) > 0:
                lista_disponibles.append(articulo)
        self.mostrar_tabla(lista_disponibles)
def generar_tabla_hash(articulos):
    tablahash = Tablahash()
    for articulo in articulos:
        tablahash.agregar_elemento(articulo.referencia,articulo)
    return tablahash

def cargar_registros():
    registros =  []
    for line in open("ARTICULOS.txt",'r'):
        if '*' in line.split(',')[0]:
            continue
        referencia,distribuidora,nombre_art,cantidad_art,precio,fecha_salida = line.split(',')
        fecha_salida = fecha_salida.split('/')
        fecha_salida = { "Dia":fecha_salida[0] , "Mes":fecha_salida[1], "Año":fecha_salida[2].split('\n')[0]}
        articulo = Articulo(referencia,distribuidora,nombre_art,cantidad_art,precio,fecha_salida)
        registros.append(articulo)
    return registros

def actualizar_archivo(registros):
    file = open("ARTICULOS.txt",'w')
    for registro in registros.lista:
        if len(registro) >0:
            for articulo in registro:
                file.write(
                    articulo[1].referencia+','+
                    articulo[1].distribuidora+','+
                    articulo[1].nombre_art+','+
                    articulo[1].cantidad_art+','+
                    articulo[1].precio+','+
                    articulo[1].fecha_salida["Dia"]+'/'+articulo[1].fecha_salida["Mes"]+'/'+articulo[1].fecha_salida["Año"]+'\n'
                )
    file.close()

def comprobar_archivo_existencia():
    try:
        file = open("ARTICULOS.txt",'r')
        file.close()
    except:
        file = open("ARTICULOS.txt","w")
        file.close()


def run_app():
    comprobar_archivo_existencia()
    app = QApplication(sys.argv)
    window = Window()
    window.frame_principal()
    window.frame_botones()
    window.mostrar_frame_inicio()
    sys.exit(app.exec())
