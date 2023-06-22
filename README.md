# test_final
Repositorio que contiene ambos archivos del test para la emresa CHR

##Descripción de ambos proyectos
Modo de uso del Primer proyecto:
    
    Sobre la vista en la aplicación:
    Al iniciar el servidor de Django, se carga una página con una barra de navegación, en donde se incluye un campo de búsqueda, para que coloque la palabra asociada a la Jurisprudencia que está buscando. Al darle click a buscar, será redirigido a la página que contiene todos los datos extraidos de la búsqueda (puede retornar hasta 1000 registros).
    Además puede seleccionar una Jurisprudencia en específico para ver de forma más detallada, los datos de la misma.

    Sobre la vista en el administrador:
    Luego de que cree su SuperUsuario, en la vista de administración de Django, dispondrá de una vista de las Jurisprudencias, la cual muestra 4 campos (Id, Caratula, Nombre del proyecto y el Url de la sentencia), podrá
    filtrar los datos utilizando el ID o la Caratula y, además, podrá buscar empleando el ID y los Descriptores de la Jurisprudencia. Al hacer click en alguna Jurisprudencia, también se visualizarán con ella, los valores asociados que se obtuvieron del raspado.

Modo de uso del Segundo Proyecto:

    Sobre la vista de la aplicación:
    Consta de una barra de navegación con dos botones: "Home" (que redirige a la lista de concesiones) y "Concesiones" (que ejecuta el Script de raspado web con Selenium), al hacer click en el botón Concesiones, se abrirá un navegador Edge y procederá a ejecutarse el raspado de los datos del sitio de concesiones marítimas. (Aquí no se incluye una vista de detalle)

    Sobre la vista en el administrador:
    Luego de que cree su SuperUsuario, en la vista de administración de Django, dispondrá de una vista de las Concesiones, la cual muestra 4 campos (Número de concesiones, Tipo de Concesion, lugar de la concesion y el tipo de vigencia), podrá
    filtrar los datos utilizando el Numero de Concesion o el lugar y, además, podrá buscar empleando el Numero de Concesion y el N RS/RD. Puede dar click en cualquier Concesion y obtendrá datos más detallados. 
