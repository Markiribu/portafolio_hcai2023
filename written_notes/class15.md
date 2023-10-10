# Clase 15: Documentacion
### La documentacion del software es de gran importancia ya que se convierten no tan solo en la via de comunicacion entre tu y aquellos que lean tu codigo, sino que tambien es la via de comunicacion entre el tu que escribio el codigo y el tu quien lo lee a futuro.
### Es gracias a una buena documentacion que el software escrito puede ser comprensible, utilizable y mantenible.
### Existen dos publicos objetivos de la documentacion, los Usuarios y los Desarrolladores, los primeros utilizan el software final y por ende no requieren conocer los detalles de la implementacion interna, mientras que los segundos, si requieren acceder a los detalles de implementacion para reutilizar, extender o modificar parcial o totalmente el mismo software.
### No es correcto el considerar la escritura de documentacion como una 'perdida de tiempo', es erroneo el pensar en escribir codigo de manera tan cerrada, y es mas completo pensar en desarrollo de software.
## ¿Para quien y como documento?
### Software final: para los Usuarios | obtencion, instalacion, uso | Manuales, sitios web, wikis, tutoriales.
### Codigo fuente: para los desarrolladores | archivos modulos clases funciones metodos | comentarios(# o """ """) | Declarar limitaciones y tecnica utilizada en cada parte del software.
## Buenas practicas
### > Se claro y conciso | 
### > Actualiza tu documentacion | Debe ser parte del proceso de desarrollo
### > Consistente | Estilo y profundidad consistentes para mejorar la legibilidad
### > No es necesario describir | Responde a la pregunta de ¿por que existe o se implementa?
## Documentando tu codigo fuente.
### Dentro de los bloques de codigo puedes colocar breves comentarios que explican el algoritmo
### Clases deben de ser descrito en su proposito, atributos y metodos, ademas de ejemplos de uso(si aplica)
### Las funciones y metodos deben tener descritas su rutina, los parametros de entrada(tipos), sus valores de retorno, sus limitaciones y ejemplos de uso.
## DOXYGEN: genera documentacion a partir de los comentarios en codigo.
### Para utilizarlo: 
### > Instalar Doxygen(Graphviz)
### > Crear archivo de configuración en el directorio: doxygen -g
### > Editar el Doxyfile: revisar-> OPTIMIZE\_OUTPUT\_FOR\_C PYTHON\_DOCTRING INPUT
### > Ejecutar Doxygen.
### Puede a llegar a verse poco placentero visualmente, tanto en la documentacion como dentro del mismo codigo.
## SPHINX: Diseñado para python
### Instalable con pip, anaconda o desde los repositorios
### Reconoce las docstring
### Haciendo uso de Sphinx:
### > sphinx-quickstart docs
### > Este ultimo genera los archivos de configuracion minimo
### > Para generar la documentacion por primera vez: sphinx-build -M html docs/source/ docs/build/
