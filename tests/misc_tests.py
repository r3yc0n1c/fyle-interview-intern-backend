from core.libs.exceptions import FyleError


def test_root(client):
    """
    check for root endpoint
    """
    response = client.get('/')

    assert response.status_code == 200
    assert response.json['status'] == 'ready'


def test_method_not_allowed(client):
    """
    test wrong http method 
    """
    response = client.post('/')

    assert response.status_code == 405
    assert response.json['error'] == 'MethodNotAllowed'


def test_validation_error(client, h_teacher_1):
    """
    check validation error handling
    """
    response = client.post(
        '/teacher/assignments/grade',
        headers=h_teacher_1,
        json={})
    
    assert response.status_code == 400
    assert response.json['error'] == 'ValidationError'


def test_unknown_endpoint(client):
    """
    test invalid endpoint
    """
    response = client.get('/unknown-endpoint')
    assert response.status_code == 404
    assert response.json['error'] == 'NotFound'