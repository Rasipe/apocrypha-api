import bottle

service = {}

@bottle.route('/')
def test():
    global service
    print(service.get_all())
    return str(service.get_all()[0])
