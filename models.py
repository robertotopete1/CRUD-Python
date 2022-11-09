import json
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER + '/DB/' 'database.json')

with open (my_file, "r") as f: 
    datos = json.load(f) 

datos_personas = datos['Personas']
f.close()

class Persona(object):
    contador_id = datos["Configuraciones"][0]["contador_id_db"]
    def __init__(self, nombre, apellido, apodo, telefono, direccion):
        print("El contador está en: ", Persona.contador_id)
        self.id = Persona.contador_id #Atriuto id es igual a la variable
        self.nombre = nombre
        self.apellido = apellido
        self.apodo = apodo
        self.telefono = telefono
        self.direccion = direccion
        
    def crear_contacto(self):    
        with open (my_file, "w") as modid:
            datos["Configuraciones"][0]["contador_id_db"]+=1#
            json.dump(datos, modid, indent=4)
            modid.close() 
            print("El contador está ahora en: ", datos["Configuraciones"][0]["contador_id_db"])
            Persona.contador_id +=1
            nueva_persona = Persona(
                self.nombre,
                self.apellido,
                self.apodo,
                self.telefono, 
                self.direccion).__dict__ 
            with open (my_file, "w") as fr: 
                datos['Personas'].append(nueva_persona) 
                json.dump(datos, fr, indent =4) 
                fr.close()
    def actualizar_contacto(id, atr, nuevo_valor):
        for persona in datos["Personas"]:
            if persona["id"] == id: 
                print (persona)
            indice = datos["Personas"].index(persona) 
            datos["Personas"][indice][atr] = nuevo_valor 
            print (datos["Personas"][indice][atr]) 
            with open (my_file, "w") as modificar: 
                json.dump(datos, modificar, indent =4) 
                modificar.close()
    def leer_contacto(atr, valor):
        encontradas = {}
        for persona in datos["Personas"]: 
            if persona[atr] == valor or valor == 'all':
                indice = datos["Personas"].index(persona)
                encontradas[indice] = persona
        return (encontradas)
    def eliminar_contacto(id):
        for persona in datos["Personas"]:
            if persona["id"] == id:
                print ("Se va a borrar: ", persona)
                indice = datos["Personas"].index(persona)
                datos["Personas"].pop(indice)
                with open (my_file, "w") as eliminar:
                    json.dump(datos, eliminar, indent =4)
                    eliminar.close()



persona_test = Persona(0, "Mariano", "Laca", "Pyromaniac", "34343434", "pythones.net").__dict__
print(persona_test)
persona_test4 = Persona("Mariano", "Laca", "Pyromaniac", "34343434", "pythones.net")
persona_test4.crear_contacto()
persona_test5 = Persona("Martin", "Paredes", "el loco", 343455555, "los buitres 123")
persona_test5.crear_contacto()
persona_test6= Persona("Marcos", "Talo", "El pepo", 343455555, "sin nombre 123")
persona_test6.crear_contacto()