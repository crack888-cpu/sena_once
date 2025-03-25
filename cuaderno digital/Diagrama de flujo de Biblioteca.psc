Algoritmo inicio
	Definir estado_m Como Cadena
	Definir edad, lb_prest Como Entero
	Definir multas Como Real
	Definir es_ad, es_ref, lb_disp Como Lógico
	Leer estado_m, edad, multas, es_ad, es_ref, lb_prest, lb_disp
	Si edad > 18 Entonces
		Escribir 'Categoría adulto apta'
	SiNo
		Escribir 'Categoría adulto no apta'
	FinSi
	Si lb_disp Y edad > 18 Y estado_m = 'activa' Y multas < 10 Y  NO es_ref Y es_ad Entonces
		Si libros_prestados < 2 Entonces
			Escribir 'Préstamo aprobado'
		SiNo
			Escribir 'Máx. de préstamos'
		FinSi
	SiNo
		Escribir 'No puedes realizar el préstamo. Debido a que no has cumplido con los requisitos; te recomendamos cumplir con todo lo necesario'
	FinSi
FinAlgoritmo
