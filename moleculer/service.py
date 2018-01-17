import json


def service_builder(name, cache=False, params=None):
    """

    :param name:
    :param cache:
    :param params: dict. Example: {'name': {'optional': bool, 'type': 'typeof'}}
    :return:
    """

    result = {
        'cache': cache,
        'name': name,
    }
    if params is not None:
        result['params'] = params
    return result


def request_handler(action: str, params: dict) -> bool:
    with open('1.txt', 'w') as f:
        f.write(action)
        f.write('\n')
        f.write(json.dumps(params))
    return True


INFO_PACKET_TEMPLATE = {
    'ver': '2',
    'sender': None,
    'services': [{
        'actions': {'$python.test': service_builder('$python.test')},
        'events': {},
        'metadata': {},
        'name': '$python',
        'nodeID': None,
        'settings': {}
    }],
    'config': {},
    'ipList': ['127.0.0.1', ],
    'port': None,
    'client': {'langVersion': '3.6.3', 'type': 'python', 'version': '0.0.1'},
}