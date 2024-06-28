from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Performing addition operation on the two input integers
    result = my_int1 + my_int2

    # Output the result of the addition operation
    return [Output(result, "result_output", party1)]
