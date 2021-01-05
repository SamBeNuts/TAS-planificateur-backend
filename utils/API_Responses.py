import json

def _CustomResponse(data = None, statusCode = 500):
    return {
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Methods': '*',
            'Access-Control-Allow-Origin': '*',
        },
        'statusCode': statusCode,
        'body': json.dumps(data, indent=2),
    }

# Ok
def _200(data = None):
    return _CustomResponse(data, 200)

# Created
def _201(data = None):
    return _CustomResponse(data, 201)

# Accepted
def _202(data = None):
    return _CustomResponse(data, 202)

# No content
def _204():
    return _CustomResponse(statusCode=204)

# Bad request
def _400(data = None):
    return _CustomResponse(data, 400)

# Forbidden
def _403(data = None):
    return _CustomResponse(data, 403)

# Internal server error
def _500(data = None):
    return _CustomResponse(data, 500)
