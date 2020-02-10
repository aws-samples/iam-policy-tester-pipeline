from datetime import datetime 
 
def handler(event, context): 
    dateTimeObj = datetime.now() 
    message = 'The time in London is: ' + str(dateTimeObj) 
    return { 
        'headers': {
            'Content-Type': "text/plain"
        },
        'statusCode': 200,
        'body' : message 
    } 
