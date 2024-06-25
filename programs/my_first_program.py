from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    
    # Inputs from party1
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))
    
    # Computation: summing two integers
    sum_result = my_int1 + my_int2
    
    # Return the result of the sum to party1
    return [Output(sum_result, "sum_output", party1)]
