class OrderService:
    def __init__(self, order_repository, payment_service, notification_service, shipment_service):
        self.order_repository = order_repository
        self.payment_service = payment_service
        self.notification_service = notification_service
        self.shipment_service = shipment_service

    def create_order(self, order):
        # Business logic to create an order
        self.order_repository.save(order)
        self.notification_service.notify_order_created(order)
        self.shipment_service.prepare_shipment(order)