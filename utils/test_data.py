# Test data for users
users = [
    {'username': 'standard_user', 'password': 'secret_sauce', 'expected_success': True},
    {'username': 'performance_glitch_user', 'password': 'secret_sauce', 'expected_success': True},
    {'username': 'locked_out_user', 'password': 'secret_sauce', 'expected_success': False},
]

invalid_users = [
    {'username': 'invalid_user', 'password': 'wrong_password'}
]