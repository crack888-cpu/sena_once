Algoritmo inicio
	Definir estado_m Como Cadena
	Definir edad, lb_prest Como Entero
	Definir multas Como Real
	Definir es_ad, es_ref, lb_disp Como L�gico
	Leer estado_m, edad, multas, es_ad, es_ref, lb_prest, lb_disp
	Si edad > 18 Entonces
		Escribir 'Categor�a adulto apta'
	SiNo
		Escribir 'Categor�a adulto no apta'
	FinSi
	Si lb_disp Y edad > 18 Y estado_m = 'activa' Y multas < 10 Y  NO es_ref Y es_ad Entonces
		Si libros_prestados < 2 Entonces
			Escribir 'Pr�stamo aprobado'
		SiNo
			Escribir 'M�x. de pr�stamos'
		FinSi
	SiNo
		Escribir 'No puedes realizar el pr�stamo. Debido a que no has cumplido con los requisitos; te recomendamos cumplir con todo lo necesario'
	FinSi
FinAlgoritmo
