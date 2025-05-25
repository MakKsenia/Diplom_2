import data

def modify_create_user_body(key,value):
    body = data.DataForUser.CREATE_USER_BODY.copy()
    body[key]=value
    return body

def modify_create_order_body(key,value):
    body = data.DataForOrderCreate.CREATE_ORDER_BODY.copy()
    body[key]=value
    return body