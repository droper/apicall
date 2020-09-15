"""
Select the proper response.
"""


def select_response(response_list):
    """
    Function that selects between all the responses from the api functions.
    What we do is to compare the three values (deductible, stop_loss and oop_max)
    with the following criteria:

    deductible: The less the better for the patient.
    stop_loss: The bigger the best for the patient.
    oop_max: The less the better for the patient.

    The selection algorithm is:

    1. Add all the values from the same parameters.
    2. Obtain the weight for each parameter as the percentage
       of the total amount.
    3. For each response multiply every parameter for the weight and divide
       stop_loss between the sum of deductible and oop_max.
    4. The greater the value, the best for the patient it is.

    WARNING!!!
    This can be more generic (big amount!!) but time constraint make us wrote
    the code in this hardcoded way.

    :param response: The responses of the functions
    :return: the selected response.
    """

    add = {"deductible": [0, 0], "stop_loss": [0, 0], "oop_max": [0, 0]}

    # Sum all the parameters from the responses
    for response in response_list:
        add["deductible"][0] += response["deductible"]
        add["stop_loss"][0] += response["stop_loss"]
        add["oop_max"][0] += response["oop_max"]

    # Obtain the weight for each parameter
    for key in add.keys():
        add[key][1] = add[key][0]/sum(map(lambda item: item[0], add.values()))

    # Calculate the value of each response
    value = 0
    final_response = None
    for response in response_list:
        temp = response["stop_loss"]*add["stop_loss"][1]/(response["deductible"]*add["deductible"][1] + response["oop_max"]*add["oop_max"][1])
        if temp > value:
            value = temp
            final_response = response

    return final_response


def api_call(api):
    """
    Calling the different api functions.

    Can be more generic by using a predefined list of functions to call for example.

    :param api: Api object
    :return: list of responses
    """

    response_list = []

    response_list.append(api.func_api1(1))
    response_list.append(api.func_api2(1))
    response_list.append(api.func_api3(1))

    return response_list

if __name__ == '__main__':

    from api import Api

    response_list = api_call(Api())

    final_response = select_response(response_list)
    print(final_response)


