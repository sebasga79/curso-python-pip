'''import main # Esta no es una buena práctica. Al correr el print podemos ver que no solo nos da la información sino que se ejecuta main.py dentro de example. Acá debemos modular el archivo original que estamos importando para que esto no ocurra

print("Esta información proviene de example.py ----> ", main.data)'''

import main 

print(main.data)

main.run() # Esta es una buena práctica porque no se ejecuta por sí misma, necesitamos usar .run para que se ejecute por nuestra solicitud