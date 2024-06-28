"""
PROGRAM 2

nr of stores: m = 3
nr of products: n = 2
"""
from nada_dsl import *
#store program
def nada_main():

    # 1. Parties initialization
    store0 = Party(name="Store0")
    store1 = Party(name="Store1")
    store2 = Party(name="Store2")
    outparty = Party(name="OutParty") 

    # 2. Inputs initialization
    ## Sales from store 0
    s0_p0 = SecretUnsignedInteger(Input(name="s0_p0", party=store0))
    s0_p1 = SecretUnsignedInteger(Input(name="s0_p1", party=store0))
    ## Sales from store 1
    s1_p0 = SecretUnsignedInteger(Input(name="s1_p0", party=store1))
    s1_p1 = SecretUnsignedInteger(Input(name="s1_p1", party=store1))
    ## Sales from store 2
    s2_p0 = SecretUnsignedInteger(Input(name="s2_p0", party=store2))
    s2_p1 = SecretUnsignedInteger(Input(name="s2_p1", party=store2))

    # 3. Computation
    ## Add sales for product 0
    result_p0 = s0_p0 + s1_p0 + s2_p0
    ## Add sales for product 1
    result_p1 = s0_p1 + s1_p1 + s2_p1
    
    # 4. Output
    result_p0 = Output(result_p0, "final_sales_count_p0", outparty)
    result_p1 = Output(result_p1, "final_sales_count_p1", outparty)

    return [result_p0, result_p1]
