##########################################################################################
#####################                                        			##################
#####################    TRABAJO ORDINARIA BIOINFORMÁTICA R             ##################
#####################                                       			##################
##########################################################################################


### 1.- Carga el archivo de entrada "archivo-entrada.txt" correspondiente. 
### Recuerda incluir los nombres de las columnas como el encabezado.
### Examina el archivo con las funciones head(), tail() y dim(). (1 pto)



#Lo primero, hemos creado un proyecto nuevo para adjuntarle este directorio de trabajo.
#Así podremos trabajar más cómodamente y el archivo se leerá con total tranquilidad sin tener que pasar por un "ruta_archivo <- file.choose()"


#Teniendo ya los datos separados por un delim()
##Read.delim funciona igual que read.table, siendo delim un caso específico de table con sep = "\t"
datos <- read.delim(
  "archivo-entrada.txt",
  header = TRUE,
  sep = "\t",
  check.names = FALSE,
  stringsAsFactors = FALSE
)


# Obtenemos las 6 primeras filas. Usamos "head(datos, X)", siendo X un número igual o menor al número de datos que tiene el archivo, para obtener ese número de filas
head(datos)

# Obtenemos las 6 últimas filas, "tail(datos, X)" para obtener un valor personalizado
tail(datos)

# Consultamos las dimensiones del archivo
dim(datos)
#Al eliminar el título de la variable, por "header=TRUE", obtenemos un total de 619 items con 7 variables cada uno
## El documento txt es una tabla de expresión genética con columnas:
  ##Gene name
  ##C2-TPM, C1-TPM, C3-TPM como las tres replicas de expresión para cada gen
  ##1W5-TPM, 1W6-TPM, 1W5-COV es probable que sean filas de expresión en Transcription Per Million (TPM) y cobertura (COV) respectivamente



### 2.- En nuestra tabla tenemos los valores de 619 genes para tres réplicas
### del Control y tres réplicas de una Condición. Calcula la media y la desviación
### estándar del control y del tratamiento para cada gen. Puedes emplear cualquier
### función que consideres como apply(). Añade esos valores como columnas nuevas a tu tabla original. 
### Serán 4 columnas nuevas en total, la media de Control, la DE de Control, la media de Condición y la DE de Condición. (1,5 pto)

#A pesar de lo dicho en el apartado anterior, contamos C2-TPM, C1-TPM, C3-TPM como los controles y 1W5-TPM, 1W6-TPM, 1W5-COV como condiciones, sin distinguir si se tratan de expresión o cobertura


# Creamos las variables CONTROL y CONDICION 
control <- c("C1-TPM", "C2-TPM", "C3-TPM")
condicion <- c("1W5-TPM", "1W6-TPM", "1W5-COV")

# Calculamos la media y la desviación estándar del CONTROL
datos$Media_Control <- apply(datos[, control], 1, mean, na.rm = TRUE)
datos$DE_Control <- apply(datos[, control], 1, sd, na.rm = TRUE)

# Calculamos la media y la desviación estándar de la CONDICION
datos$Media_Condicion <- apply(datos[, condicion], 1, mean, na.rm = TRUE)
datos$DE_Condicion <- apply(datos[, condicion], 1, sd, na.rm = TRUE)

# apply tiene la siguiente estructura:
  ## apply(tabla, margen, función)
    ### Tabla: Datos sobre los que trabajamos
    ### Margen = 1: Indica que queremos aplicar la función por filas, es decir, un gen cada vez
    ### Mean = Media // sd = Desviación típica

# Con esto hemos creado cuatro nuevas culumnas: Media_Control, DE_Control, Media_Condicion y DE_Condicion


# Comprobamos las nuevas columnas
head(datos)

# Comprobamos las dimensiones de la tabla
dim(datos)
# Ahora 11 variables (7 iniciales + 4 nuevas)


### 3.- En una sola imagen, muestra un histograma para la media del Control y otro para la media de la Condicíon.
### Pon colores diferentes en cada uno y mantén esos colores para el resto del trabajo. (1 pto).

# Estos son los colores que utilizaremos a lo largo del trabajo
color_control <- "#3976B9"
color_condicion <- "#E58A32"

# Calculamos unos intervalos comunes para comparar ambos histogramas
rango_medias <- range(
  c(datos$Media_Control, datos$Media_Condicion),
  na.rm = TRUE
)

intervalos <- pretty(rango_medias, n = 15)

# Guardamos la configuración gráfica original
configuracion <- par(no.readonly = TRUE)

# Dividimos la ventana gráfica en dos paneles
par(mfrow = c(1, 2),
    mar = c(4, 4, 3, 1),
    oma = c(0, 0, 2, 0))

# Histograma de las medias del Control
hist(datos$Media_Control,
     breaks = intervalos,
     col = color_control,
     border = "white",
     main = "Media de expresión - Control",
     xlab = "Media TPM",
     ylab = "Frecuencia")

# Histograma de las medias de la Condición
hist(datos$Media_Condicion,
     breaks = intervalos,
     col = color_condicion,
     border = "white",
     main = "Media de expresión - Condición",
     xlab = "Media TPM",
     ylab = "Frecuencia")

mtext("Distribución de las medias de expresión génica",
      outer = TRUE, cex = 1.1)

#En este punto, alguna de las condiciones dan resultados exacerbados que nos disparan los resultados:
  ##C1-TPM: 67608.84375 >> 11394.20215
  ##C2-TPM: 95834.28125 >> 14246.71680
  ##C3-TPM: 72195.24219 >> 15782.44629
  ##1W5-TPM: 1.294060e+05 >> 1.147443e+04	
  ##1W6-TPM: 89719.351560	>> 10065.373050
  ##1W5-COV: 1.239662e+05 >> 1.099208e+04

#Aunque no sea necesario, se va a calcular si son outliyers o simplemente un gen con expresión muy elevada, ya que todos esos valores provienen de "ssrA"
  ##Primero, utilizamos el criterio de Tukey, el utilizado en diagramas de cajas, es decir, calculamos los cuartiles Q1 y Q3, el RIC y los valores atípicos:

# Límites de Tukey para Control
Q1_Control <- quantile(datos$Media_Control, 0.25, na.rm = TRUE)
Q3_Control <- quantile(datos$Media_Control, 0.75, na.rm = TRUE)
RIC_Control <- Q3_Control - Q1_Control

limite_Control <- Q3_Control + 1.5 * RIC_Control

# Límites de Tukey para Condición
Q1_Condicion <- quantile(datos$Media_Condicion, 0.25, na.rm = TRUE)
Q3_Condicion <- quantile(datos$Media_Condicion, 0.75, na.rm = TRUE)
RIC_Condicion <- Q3_Condicion - Q1_Condicion

limite_Condicion <- Q3_Condicion + 1.5 * RIC_Condicion

  ## Identificamos los valores extremos
datos$Outlier_Control <- datos$Media_Control > limite_Control
datos$Outlier_Condicion <- datos$Media_Condicion > limite_Condicion

# Consultar los genes señalados ("Muéstrame el nombre del gen y su media, pero solo de aquellas filas donde el control O la condición sean considerados Outliyers")
datos[datos$Outlier_Control | datos$Outlier_Condicion,
      c("Gene Name", "Media_Control", "Media_Condicion",
        "Outlier_Control", "Outlier_Condicion")]

#Dejamos el resultado analizado por el boxplot para el siguiente apartado
#Realizamos un estudio rápido respecto a la regresión lineal

# Ajustamos el modelo de regresión lineal
modelo_rl <- lm(Media_Condicion ~ Media_Control, data = datos)

summary(modelo_rl)

# Representamos la relación entre ambos grupos
plot(datos$Media_Control,
     datos$Media_Condicion,
     pch = 19,
     col = adjustcolor("grey30", alpha.f = 0.5),
     main = "Regresión lineal: Control frente a Condición",
     xlab = "Media de expresión - Control",
     ylab = "Media de expresión - Condición")

# Añadimos la recta de regresión
abline(modelo, col = color_condicion, lwd = 2)

# Estos son los resultados estadíticos, obtenemos min, max, Q1, Q3 y mediana residual
# Pero también unos valores de significancia del 99'9% y R²	0,9191 y correlación de Pearson	0,9587
  ## Significado Pearson: Al estar cerca de 1 podemos decir que las dos variables están casi solapadas y evolucionan a la vez
  ## Significado R²: El control de la media es capaz de explicar cerca del 92% de la variabilidad de la otra variable


#En este punto podríamos decir que el modelo es muy favorable para explicar las condiciones.
#Sin embargo, como hemos dicho al principio, ssrA influye demasiado, por lo que vamos a realizar un ajuste por distancia de Cook:
  ##Distancia de Cook (Di): Nos va a indicar cómo cambiarían las predicciones del modelo si se eliminase una observación
    ###Si Di > 1: La observación eliminada tiene una influencia grande sobre el modelo y puede distorsionar las conclusiones
    ###Se suele recomendar usar como ubral orientativo "Di>4/nº total", para observar los puntos que merecen más atención, así haremos [Di (4/n) = 0.00646]

cook <- cooks.distance(modelo_rl)

# Añadimos Cook a la tabla como una nueva variable
datos$Distancia_Cook <- cook

# Umbral orientativo: 4/n
umbral_cook <- 4 / nrow(datos)

# Identificamos los genes más influyentes
genes_influyentes <- datos[
  datos$Distancia_Cook > umbral_cook,
  c("Gene Name", "Media_Control",
    "Media_Condicion", "Distancia_Cook")
]

# Ordenamos de mayor a menor influencia
genes_influyentes <- genes_influyentes[
  order(genes_influyentes$Distancia_Cook, decreasing = TRUE),
]

genes_influyentes

#Ahora, si queremos verlo gráficamente:
plot(cook,
     type = "h",
     col = color_control,
     main = "Influencia de los genes en la regresión",
     xlab = "Índice del gen",
     ylab = "Distancia de Cook")

abline(h = umbral_cook,
       col = color_condicion,
       lwd = 2,
       lty = 2)

#Conclusión: ssrA no solo es un punto de influencia extrema, sino que es un outlier crítico al superar el umbral de alerta por approx 2428.82 (Unas 375.000 veces), incluso superando el umbral absoluto miles de veces
  ##Si mantenemos ssrA en el modelo tendremos coeficientes sesgados por ssrA, predicciones falsas e incluso falsos positivos o negativos
  ##No vamos a excluir el valor, pero sí que vamos a calcular la diferencia entre la regresión con y sin ssrA

# Creamos un conjunto temporal sin ssrA (!= "Datos para cada gen que no sean ssrA")
datos_sin_ssrA <- datos[
  tolower(datos$`Gene Name`) != "ssra",
]

# Ajustamos una segunda regresión
modelo_sin_ssrA <- lm(
  Media_Condicion ~ Media_Control,
  data = datos_sin_ssrA
)

# Comparamos los modelos
summary(modelo_rl)
summary(modelo_sin_ssrA)

#Al retirar ssrA R² cae de un 0,9191 a 0,1524 (0.7667 o 83.4185%)
  ##La pendiente ha disminuido drásticamente (1,3413	a 0,2258) y la correlación (0,9587	0,3903) también  

#Puesto que el propio enunciado dice que tomemos las columnas C por un lado y las 1w por otro, no podemos saber si la cobertura está causando un problema en la asociación de las variables
#A partir de ahora vamos a continuir teniendo en cuenta las dos opciones (ssrA vs !ssrA), ya que no sabemos si es posible eliminar ssrA al ser una etiqueta de eliminado en bacterias y no sabemos de dónde proceden los datos


#---------------------------------------------
# 1. Conservamos los genes con datos completos
# --------------------------------------------

datos_reg <- datos[
  complete.cases(datos[, c("Media_Control", "Media_Condicion")]),
]

# --------------------------------------------
# 2. Regresión de todos los genes (Con ssrA)
# --------------------------------------------
modelo_rl <- lm(
  Media_Condicion ~ Media_Control,
  data = datos_reg
)

# Calculamos otra vez su distancia de Cook
datos_reg$Cook <- cooks.distance(modelo_rl)

# --------------------------------------------
# 3. Regresión de todos los genes menos ssrA
# --------------------------------------------

datos_sin_ssrA <- datos_reg[
  tolower(trimws(datos_reg$`Gene Name`)) != "ssra",
]

modelo_sin_ssrA <- lm(
  Media_Condicion ~ Media_Control,
  data = datos_sin_ssrA
)

# Recalculamos la distancia de Cook en el segundo modelo
datos_sin_ssrA$Cook <- cooks.distance(modelo_sin_ssrA)

# Seleccionar los cinco genes más influyentes (De mayor a menor por "decreasing = TRUE" y [1:5] para pillar solo los 5 primeros)
top_genes <- datos_sin_ssrA[
  order(datos_sin_ssrA$Cook, decreasing = TRUE)[1:5],
]

# --------------------------------------------
# 4. Representamos las dos regresiones
# --------------------------------------------

par(mfrow = c(1, 2), mar = c(4, 4, 3, 1))
#par: Dividimos la pantalla en 1 fila y 2 columnas, para que se coloquen ambas regresiones una al lado de la otra en vez de sobre escribirse
#mar (Orden = abajo, izquierda, arriba, derecha): Crea 4 líneas abajo e izquierda, 3 arriba y 1 a la derecha, para que entren los títulos y ejes

# Panel izquierdo: todos los genes
plot(
  datos_reg$Media_Control,
  datos_reg$Media_Condicion,
  pch = 19,
  cex = 0.65,
  col = adjustcolor("grey30", alpha.f = 0.45),
  main = "Regresión con todos los genes",
  xlab = "Media Control",
  ylab = "Media Condición"
)

abline(modelo_rl, col = color_control, lwd = 2)

# Etiquetamos ssrA
gen_ssrA <- datos_reg[
  tolower(trimws(datos_reg$`Gene Name`)) == "ssra",
]
#Con esto podemos buscar ssrA dentro de la tabla
  ## gen_ssrA: Crea una variable para los datos de ssrA
  ## datos_reg[ ... , ]: Esos datos van a provenir de la tabla de datos_reg, la "," sirve para que cumplan la condición de la izquierda de la coma y deje intactas las columnas
  ## tolower(trimws(...)): Primero elimina todos los espacios en blanco del texto ("ssrA" <- " ssrA ") y luego lo convierte a minúsculas ("ssra" <- "ssrA")
  ## Finalmente, le pedimos que busque justamente "ssra" y, si coincide, meta esa fila en la variable

text(
  gen_ssrA$Media_Control,
  gen_ssrA$Media_Condicion,
  labels = "ssrA",
  pos = 2,
  col = color_control,
  font = 2
)
#Ahora, buscamos la variable ssra en los parámetros y le añade la etiqueta del gen para mejor visualización


# Panel derecho: sin ssrA
plot(
  datos_sin_ssrA$Media_Control,
  datos_sin_ssrA$Media_Condicion,
  pch = 19,
  cex = 0.65,
  col = adjustcolor("grey30", alpha.f = 0.45),
  main = "Regresión sin ssrA",
  xlab = "Media Control",
  ylab = "Media Condición"
)

abline(modelo_sin_ssrA, col = color_condicion, lwd = 2)

# Etiquetar los cinco genes más influyentes
text(
  top_genes$Media_Control,
  top_genes$Media_Condicion,
  labels = top_genes$`Gene Name`,
  pos = 2,
  cex = 0.75,
  col = color_condicion,
  font = 2
)
#Siempre: Posición 1 = Abajo, 2 = izq, 3 = arriba, 4 = der)
#El panel azul muestra la relación global, pero está muy condicionado por ssrA
#El panel naranja muestra cómo cambia la relación cuando ssrA deja de influir en el ajuste

# Restauramos la disposición gráfica
par(mfrow = c(1, 1))


### 4.- En una sola imagen, muestra un boxplot para la condición y otro para el control. 
### Añade el título, colores y una una leyenda en la esquina superior izquierda. ( 1,5 pto)

par(mfrow = c(1, 2), mar = c(4, 4, 3, 1))

# Creamos el boxplot con ambos grupos en una sola imagen
boxplot(
  list(
    Control = datos$Media_Control,
    Condicion = datos$Media_Condicion
  ),
  col = c(color_control, color_condicion),
  border = "black",
  main = "Distribución de la expresión génica",
  ylab = "Media de expresión",
  xlab = "Grupo experimental",
  names = c("Control", "Condición"),
  outline = TRUE,
  cex.main = 1.2,
  cex.lab = 1.1
)

# Añadimos la leyenda en la esquina superior izquierda
legend(
  "topleft",
  legend = c("Control", "Condición"),
  fill = c(color_control, color_condicion),
  border = "black",
  bty = "n",
  cex = 0.9
)

#Puesto que, cómo hemos dicho, ssrA comprime demasiado los datos en un extremo, vamos a crear el mismo boxplot pero sin ssrA para apreciarlo mejor


# Boxplot sin ssrA
boxplot(
  list(
    Control = datos_sin_ssrA$Media_Control,
    Condicion = datos_sin_ssrA$Media_Condicion
  ),
  col = c(color_control, color_condicion),
  border = "black",
  main = "Distribución de la expresión génica sin ssrA",
  ylab = "Media de expresión",
  xlab = "Grupo experimental",
  names = c("Control", "Condición"),
  outline = TRUE,
  cex.main = 1.2,
  cex.lab = 1.1
)

# Añadimos la leyenda
legend(
  "topleft",
  legend = c("Control", "Condición"),
  fill = c(color_control, color_condicion),
  border = "black",
  bty = "n",
  cex = 0.9
)
par(mfrow = c(1, 1))

#Incluso quitando ssrA podemos observar que existe una distribución asimétrica de las medias de exprexión génica en ambos grupos, con varios valores atípicos.
#Esta presencia provoca que las cajas aparezcan como comprimidas.
#Tras eliminar ssrA del boxplot se aprecia ligeramente mejor en un zoom a pantalla completa, sin embargo, sabemos ahora que ssrA no es el único gen responsable de la dispersión de los datos



### 5.- Evalúa la normalidad de Control y Condición y acorde con los resultados, haz lo siguiente: (2 pto)
### 		Realiza un test de comparativa de medias para cada gen entre condición y control. 
###			Guarda el p-value de la comparativa y anádelo como una columna extra a tu tabla original.

# Test de normalidad de Shapiro-Wilk
  ## Sirve para comprobar si una variable sigue una distribución normal a través de un p-value
    ### Si p-value > 0'05: Los datos sí siguen la distribución normal
    ### Si p-value < 0'05: Los datos no siguen la distribución normal (Podría estar sesgado)
  ## La diferencia con Cook es que el umbral de Cook mide puntos individuales buscando outliers y el de Saphiro-Wilk mide conjuntos completo a través del p-value y la campana de Gauss
normalidad_control <- shapiro.test(datos$Media_Control)
normalidad_condicion <- shapiro.test(datos$Media_Condicion)

normalidad_control
normalidad_condicion

#Control: SW: 0.0685 // p-value: 2.08 × 10⁻⁴⁷
#Condición: SW: 0.0329 // p-value: 5.54 × 10⁻⁴⁸

#Al no presentar normalidad vamos a usar un test no paramétrico, el test de Wilcoxon:
  ##Para cada gen comparamos: 
    ###Control C1-TPM, C2-TPM y C3-TPM
    ###Condición: 1W5-TPM, 1W6-TPM y 1W5-COV.
  ##Utilizamos los valores originales de cada gen, no solo las medias

# Calculamos el p-value para cada gen
datos$P_value <- apply(
  datos[, c(control, condicion)],
  1,
  function(x) {
    wilcox.test(
      as.numeric(x[1:3]),
      as.numeric(x[4:6]),
      exact = FALSE
    )$p.value
  }
)

# Comprobamos los resultados
head(datos[, c("Gene Name", "Media_Control",
               "Media_Condicion", "P_value")])

# Comprobamos las dimensiones
dim(datos)

#Podemos averiguar cuantos datos son comparativos con la siguiente función, si algún dato es < 0'05 serán significativos
# Contamos genes con diferencias significativas
sum(datos$P_value < 0.05, na.rm = TRUE)

#Como solo comparamos tres observaciones por grupo hay que tomar el test de Wilcoxon con cautela y sería interesante realizar luegoo una corrección de comparaciones múltiples como la de Benjamini-Hochberg

# Corrección de Benjamini-Hochberg
datos$P_ajustado <- p.adjust(
  datos$P_value,
  method = "BH"
)

# Contamos genes significativos tras la corrección
sum(datos$P_ajustado < 0.05, na.rm = TRUE)
head(datos[, c("Gene Name", "P_ajustado")])

#El p-ajustado es de 0.1069436, por lo que ninguno de los 6 primeros genes presenta diferencias estadísiticamente significativas entre control y condición incluso después de corregir por comparaciones múltiples

#Conclusión: Los p-values del test de Wilcoxon corregidos por Benjamini-Hochberg para controlar la tasa de falsos descubrimientos (FDR). Los primeros genes analizados son > 0'05 considerándose no significativos


#ALTERNATIVA: Esta parte del trabajo está hecha al llegar al ejercicio 7 para poder realizar un heatmap, el siguiente punto, explica los motivos:
  ## Hasta ahora, se había evaluado si las distintas medias, del conjunto de 619 genes se ajustaban a la dist. normal, vamos a analizarlo ahora cada gen por separado

# Función para calcular Shapiro-Wilk
calcular_shapiro <- function(x) {
  tryCatch({
    shapiro.test(as.numeric(x))$p.value
  }, error = function(e) {
    NA
  })
}

# Calculamos normalidad para cada gen
datos$Shapiro_Control <- apply(
  datos[, control],
  1,
  calcular_shapiro
)

datos$Shapiro_Condicion <- apply(
  datos[, condicion],
  1,
  calcular_shapiro
)

# Mostramos algunos resultados
head(datos[, c(
  "Gene Name",
  "Shapiro_Control",
  "Shapiro_Condicion"
)])

#Ahora contamos cuantos genes tienen un p-value de Shapiro > 0'05
# Genes que no rechazan la normalidad
sum(datos$Shapiro_Control > 0.05, na.rm = TRUE)
sum(datos$Shapiro_Condicion > 0.05, na.rm = TRUE)
## Ahora por fin tenemos datos para analizar, aunque seguimos teniendo que considerar la baja potencia del SW = 3
head(datos[, c("Gene Name", "Shapiro_Control", "Shapiro_Condicion")])

genes_normalidad_control <- datos[
  datos$Shapiro_Control > 0.05,
  c("Gene Name", "Shapiro_Control")
]

genes_normalidad_condicion <- datos[
  datos$Shapiro_Condicion > 0.05,
  c("Gene Name", "Shapiro_Condicion")
]

View(genes_normalidad_control)
View(genes_normalidad_condicion)

#Conclusión_alternativa: Contándo estos resultados por separado si que llegamos a obtener un nivel de significancia con el que trabajar para los siguientes dos ejercicios


### 6.- De los resultados del apartado 5, saca (mediante código) un listado de los genes diferencialmente expresados (aquellos que tengan un pvalue < 0.05)
### ¿Cuántos genes tienes? Sino te sale ninguno, justifica por qué. En caso de que sí que te salgan, ¿cuántos salen sobreexpresados y cuántos reprimidos? (1 pto)

# Creamos una variable para meter aquellos datos que tengan un p-value < 0'05
genes_DE <- datos[datos$P_value < 0.05, ]

# Mostramos el listado
genes_DE[, c("Gene Name", "Media_Control",
             "Media_Condicion", "P_value")]
#Ninguno, como ya vimos en el apartado anterior

#Claramente, el valor que nos sale es 0
nrow(genes_DE)


# Genes sobreexpresados en Condición (0)
sobreexpresados <- genes_DE[
  genes_DE$Media_Condicion > genes_DE$Media_Control,
]

# Genes reprimidos en Condición 
reprimidos <- genes_DE[
  genes_DE$Media_Condicion < genes_DE$Media_Control,
]

# Mostramos los recuentos
nrow(sobreexpresados)
nrow(reprimidos)

#Conclusión: Cómo ya hemos analizado en el apartado 5, utilizando el p-value original no existen genes diferencialmente expresados, menos reprimidos o sobreexpresados
  ##Explicación: Esto puede deberse a que solo utilizamos 3 réplicas por grupo, lo que limita la capacidad estadística. Esto nos impide concluir que tengan la misma expresión, pero tampoco tenemos evidencias suficientes como para identificar la significancia
  ##Alternativa: Si un gen tuviera un p-value < 0'05 solo tendríamos que evaluar dónde está con mayor expresión:
    ### Media Condición > Media Control: Sobreexpresión
    ### Media Condición < Media Control: Represión
  ##Este sería el código para ese caso

  ## Clasificación de los genes diferencialmente expresados
genes_DE$Regulacion <- ifelse(
  genes_DE$Media_Condicion > genes_DE$Media_Control,
  "Sobreexpresado",
  ifelse(
    genes_DE$Media_Condicion < genes_DE$Media_Control,
    "Reprimido",
    "Sin cambio"
  )
)

  ##En este caso no da nada porque, cómo ya hemos indicado, no hay genes significativos


#ALTERNATIVA: Con los segundos resultados obtenidos en el ejercicio 5

# Genes que no rechazan la normalidad en ambos grupos
genes_normales <- datos[
  datos$Shapiro_Control > 0.05 &
    datos$Shapiro_Condicion > 0.05, ]

# Genes sobreexpresados y reprimidos
sobreexpresados <- genes_normales[
  genes_normales$Media_Condicion > genes_normales$Media_Control, ]

reprimidos <- genes_normales[
  genes_normales$Media_Condicion < genes_normales$Media_Control, ]

# Mostrar resultados
nrow(genes_normales)
nrow(sobreexpresados)
nrow(reprimidos)

sobreexpresados[, c("Gene Name", "Media_Control", "Media_Condicion",
                    "Shapiro_Control", "Shapiro_Condicion")]

reprimidos[, c("Gene Name", "Media_Control", "Media_Condicion",
               "Shapiro_Control", "Shapiro_Condicion")]


### 7.- Por último, realiza un heatmap de los genes diferencialmente expresados
### Emplea la Práctica de R como referencia. (2 pts)

####Llegados a este punto... no sé si yo he cometido algún fallo en algún momento a la hora de tratar los datos, o si estaban pensados para ser menos justificados y yo los he sobre analizado y ahora no me dan...

#El código para el heatmap sería el siguiente:

# Genes con p-value < 0,05
genes_DE <- datos[datos$P_value < 0.05, ]

# Genes que no rechazan la normalidad en ambos grupos
genes_normales <- datos[
  datos$Shapiro_Control > 0.05 &
    datos$Shapiro_Condicion > 0.05, ]

# Clasificamos los genes por dirección del cambio
sobreexpresados <- genes_normales[
  genes_normales$Media_Condicion > genes_normales$Media_Control, ]

reprimidos <- genes_normales[
  genes_normales$Media_Condicion < genes_normales$Media_Control, ]

# Mostramos recuentos
cat("Genes con p-value < 0,05:", nrow(genes_DE), "\n") #Primer grupo, tienen 0 resultados, pero los juntamos para que se vea que es solo por intentar juntar ambos códigos de una manera "simple"
cat("Genes que no rechazan normalidad en ambos grupos:", nrow(genes_normales), "\n") #El único grupo que no los rechaza son los de la alternativa, aunque se traten como "Ambos grupos", es solo el grupo ALTERNATIVA del ejercicio 5
cat("Genes sobreexpresados:", nrow(sobreexpresados), "\n")
cat("Genes reprimidos:", nrow(reprimidos), "\n")

# Mostramos resultados
sobreexpresados[, c("Gene Name", "Media_Control", "Media_Condicion",
                    "Shapiro_Control", "Shapiro_Condicion")]

reprimidos[, c("Gene Name", "Media_Control", "Media_Condicion",
               "Shapiro_Control", "Shapiro_Condicion")]

# Combinamos los genes sobreexpresados y reprimidos
genes_heatmap <- rbind(sobreexpresados, reprimidos)

if (nrow(genes_heatmap) > 0) {
  
  # Seleccionamos las columnas de expresión y aseguramos que sean numéricas
  columnas <- c("C1-TPM", "C2-TPM", "C3-TPM",
                "1W5-TPM", "1W6-TPM", "1W5-COV")
  
  matriz <- as.matrix(
    data.frame(lapply(genes_heatmap[, columnas], function(x) {
      as.numeric(as.character(x))
    }))
  )
  
  # Asignamos los nombres de los genes
  rownames(matriz) <- make.unique(genes_heatmap$`Gene Name`)
  
  # Eliminamos genes con NA, NaN o Inf, si los dejamos dará error (Por experiencia)
  matriz <- matriz[apply(matriz, 1, function(x) all(is.finite(x))), ,
                   drop = FALSE]
  
  # Eliminamos genes con desviación típica cero
  matriz <- matriz[apply(matriz, 1, sd) > 0, , drop = FALSE]
  
  # Dibujamos el heatmap si quedan suficientes genes
  if (nrow(matriz) >= 2) {
    
    heatmap(
      matriz,
      scale = "row",
      col = colorRampPalette(c("blue", "white", "red"))(100),
      main = "Heatmap de genes seleccionados por normalidad"
    )
    
  } else {
    print("No hay suficientes genes válidos para generar el heatmap.")
  }
  
} else {
  
  print("No hay genes que cumplan el criterio de normalidad en ambos grupos.")
  
}

#Finalmente, vamos a guardar el heatmap, NO CORRER SI NO QUIERES GUARDARLO
png(
  filename = "Heatmap_genes_seleccionados.png",
  width = 2400,
  height = 1800,
  res = 300
)

heatmap(
  matriz,
  scale = "row",
  col = colorRampPalette(c("blue", "white", "red"))(100),
  main = "Heatmap de genes seleccionados por normalidad"
)

dev.off()
