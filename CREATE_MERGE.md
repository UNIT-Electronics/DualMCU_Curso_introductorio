## Comando `git`

El comando `git` es una herramienta de control de versiones ampliamente utilizada en el desarrollo de software. Permite a los desarrolladores rastrear los cambios en sus proyectos, colaborar con otros y revertir a versiones anteriores si es necesario.

1. [Control_de_versiones](#control-de-versiones-por-ramas)
1. [Actualiza_tus_cambios_de_manera_local](#actualiza-tus-cambios-de-manera-local)
1. [Actualiza_la_colaboracion_principal](#actualiza-la-colaboracion-principal)

## Creación de ramas (branch)

Este apartado está diseñado para la creación de nuevas ramas con el propósito de gestionar las versiones de forma tanto local como remota:

Crea una nueva rama (branch):


```bash
 git checkout -b your_name
```

El proceso para cambiar tu ubicación de origen a your_name. Se recomienda utilizar tu nombre de usuario de Git o tu nombre personal.

Además, puedes alternar entre ramas utilizando el siguiente comando. Por ejemplo, para cambiar a la rama principal (main):

```bash 
git checkout main
```
o ir a la rama *your_name*: 
```bash
git checkout your_name
```


### Actualiza tus cambios de manera local 

El procedimiento para actualizar los cambios de manera general utilizando el comando git add .:

```bash
git add .
```
Es fundamental proporcionar información detallada sobre los cambios realizados cada vez que actualices tu código. Utiliza el siguiente comando con un comentario pertinente:

```bash 
git commit -m "your comments"
```
Posteriormente, envía tus cambios a tu rama de forma remota. Es crucial tener en cuenta que este proceso se realiza por ramas:

```bash 
git push origin your_name
```
>**Nota:** Recuerda ajustar ***your_name*** con el nombre de tu rama específica.



## Actualiza la colaboracion principal

Con el objetivo de integrar los cambios realizados por otros colaboradores y actualizar la versión final del proyecto, es necesario seguir los siguientes pasos:

Cambia a la rama principal:
```bash
git checkout main
```
Actualiza los cambios generados por los demás colaboradores. Ten en cuenta que puedes actualizar tu versión en tu rama sin afectar la versión principal:

> **Advertencia:** Puedes actualizar tu version en tu rama y tener una version anterior en la principal, recuerda actualizar tantas ramas tengas.

```bash 
git pull origin main
```
Tambien puedes actualizar tu rama, si trabajas en otra computadora sobre tu misma rama.

```bash 
git pull origin your_name
```

Genera el merge, asegurándote de estar sobre la rama principal para permitir el merge en tu rama:

```bash
git merge origin/your_name
```
Finalmente, los cambios que se visualizarán en la rama principal deben ser enviados a la versión principal mediante la instrucción:

```bash
git push origin main 

```
Recuerda ajustar 'your_name' con el nombre de tu rama específica en los pasos correspondientes.

## Propuesta de desarrollo para actualizar en colaboración


![](../Documents/Diagrama%20sin%20título.drawio.png)