from flask import Flask, request, jsonify, Blueprint
from app.domain.models import Order
from app.domain.services import OrderService
from app.adapters.db_repository import OrderRepository
from app.adapters.sqs_queue import SQSQueue
from app.adapters.payment_gateway import PaymentGateway

app = Flask(__name__)

# Initialize repositories and services
order_repository = OrderRepository()
payment_gateway = PaymentGateway()
sqs_queue = SQSQueue(queue_name='order-queue')
order_service = OrderService(order_repository, payment_gateway, sqs_queue, sqs_queue)
api = Blueprint('api', __name__)


@api.route('/')
def index():
    return "API Home"


@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    order = Order(id=data['id'], customer_id=data['customer_id'], status='CREATED', total_amount=data['total_amount'])
    order_service.create_order(order)
    return jsonify({'message': 'Order created successfully'}), 201
