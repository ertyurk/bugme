def ResponseModel(data, message, code=200):
    return {"code": code, "message": message, "data": data}


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
