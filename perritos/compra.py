
class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito=carrito 
    
    def agregar(self, perrito):
        if perrito.id not in self.carrito.keys():
            self.carrito[perrito.id]={
                "perrito_id":perrito.id, 
                "marca": perrito.marca,
                "raza": perrito.raza,
                "producto": perrito.producto,
                "precio": str (perrito.precio),
                "cantidad": 1,
                "total": perrito.precio,
            }
        else:
            for key, value in self.carrito.items():
                if key==perrito.id:
                    value["cantidad"] = value["cantidad"]+1
                    value["precio"] = perrito.precio
                    value["total"]= value["total"] + perrito.precio
                    break
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified=True


    def eliminar(self, perrito):
        id = perrito.id
        if id in self.carrito: 
            del self.carrito[id]
            self.guardar_carrito()
    
    def restar (self,perrito):
        for key, value in self.carrito.items():
            if key == perrito.id:
                value["cantidad"] = value["cantidad"]-1
                value["total"] = int(value["total"])- perrito.precio
                if value["cantidad"] < 1:   
                    self.eliminar(perrito)
                break
        self.guardar_carrito()
     
    def limpiar(self):
        self.session["carrito"]={}
        self.session.modified=True 
