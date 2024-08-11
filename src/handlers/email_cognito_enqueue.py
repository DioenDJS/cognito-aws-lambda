import json
import structlog

def lambda_handler(event, context):
    # TODO implement
    logger = structlog.get_logger()
    logger.info(event)

    logger.info(context)
    return {
        'statusCode': 200,
        'headers': {
            "Content-Type": "application/json",  # Corrected typo
        },
        'body': json.dumps({
            "name": "Dioane",
            "email": "diovane2gmail.com"
        })
    }