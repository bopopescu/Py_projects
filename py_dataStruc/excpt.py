def try_syntax(numerator, denominator):
    try:
        print(f'In the try block: {numerator}/{denominator}')
        result = numerator / denominator
    except ZeroDivisionError as zde:
        print(zde)
    else:
        print('The result is:', result)
        return result
    finally:
        print('Exiting')

# print(try_syntax(12, 4))
# print(try_syntax(11, 0))

import json
# json_data = '{}'
json_data = "{2}"
try:
    data = json.loads(json_data)
except (ValueError, TypeError) as e:
    print(type(e), e)

