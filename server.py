import grpc
from concurrent import futures  # Importa ThreadPoolExecutor desde concurrent.futures
import shop_pb2
import shop_pb2_grpc

class ShopServicer(shop_pb2_grpc.ShopServiceServicer):
    def PurchaseItem(self, request, context):
        # Lógica para procesar la compra de un artículo
        # Esta es solo una implementación de ejemplo
        total_price = 10 * request.quantity  # Precio unitario de ejemplo
        return shop_pb2.PurchaseResponse(message="Artículo comprado exitosamente", total_price=total_price)

    def MakePayment(self, request, context):
        # Lógica para procesar el pago
        # Esta es solo una implementación de ejemplo
        success = True  # Simulando un pago exitoso
        return shop_pb2.PaymentResponse(message="Pago exitoso", success=success)

    def PlaceOrder(self, request, context):
        # Lógica para realizar un pedido
        # Esta es solo una implementación de ejemplo
        order_id = "123456"  # ID del pedido generado
        purchases = []
        total_price = 0
        for item in request.items:
            total_price += 10 * item.quantity  # Precio unitario de ejemplo
            purchases.append(shop_pb2.PurchaseResponse(message="Artículo comprado exitosamente", total_price=total_price))
        return shop_pb2.OrderResponse(order_id=order_id, purchases=purchases)
    
    def GetProductInfo(self, request, context):
        products = {"234": ["Cpu Pc Gamer Armado i3 10100F Intel Ssd 480Gb Disco Duro 1Tb 16Gb Ram Nvidia Gtx 1650 80+", "$10,000", 4], "112": ["Cpu Computadora Armada Ryzen 7, 16Gb Ram 960Gb Ssd, Gabinete Rgb", "$10.567", 0], "666" : ["Cpu Computadora Armada Ryzen 7, 16Gb Ram 960Gb Ssd, Gabinete Rgb", "9800", 0]}
        if request.product in products:
            name, price, stock = products[request.product]
            description = "Nombre del producto: " + name + " Precio: " + price
            return shop_pb2.ProductDescription(description= description, quentity = stock)
        else:
            return shop_pb2.ProductDescription(description="Articulo no encontrado", quentity = 0)




def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))  # Utiliza ThreadPoolExecutor de concurrent.futures
    shop_pb2_grpc.add_ShopServiceServicer_to_server(ShopServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor iniciado. Escuchando en el puerto 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()