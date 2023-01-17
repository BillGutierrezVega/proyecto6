import mercadopago
import os
import json

def lambda_handler(event, context):
    # Crea una instancia de la clase MercadoPago
    sdk = mercadopago.SDK(os.environ["ACCESS_TOKEN"])
    event = json.loads(event["body"])
    
    # Crea un objeto de pago
    payment_data = {
        "transaction_amount": event['transaction_amount'],
        "description": event['description'],
        "installments": event['installments'],
        "payment_method_id": event['payment_method_id'],
        "payer": {
            "email": event['email']
        }
    }

    # Realiza el pago
    payment_response = sdk.payment().create(payment_data)
    payment = payment_response["response"]

    # Devuelve el resultado
    return {
        "statusCode": 200,
        "body": json.dumps(payment)
    }