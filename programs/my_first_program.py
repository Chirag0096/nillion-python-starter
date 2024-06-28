import nada_numpy as na
from nada_ai import nn
from nada_dsl import *

class CreditScoreNN(nn.Module):
    """Privacy-preserving credit score neural network"""

    def __init__(self) -> None:
        """Model with three layers and activations"""
        self.linear_0 = nn.Linear(10, 8)
        self.linear_1 = nn.Linear(8, 4)
        self.linear_2 = nn.Linear(4, 1)
        self.relu = nn.ReLU()

    def forward(self, x: na.NadaArray) -> na.NadaArray:
        """Forward pass for credit score prediction"""
        x = self.linear_0(x)
        x = self.relu(x)
        x = self.linear_1(x)
        x = self.relu(x)
        x = self.linear_2(x)
        return x

def nada_main():
    # Step 1: Create "Bank" (Provider) and "Customer" (User)
    customer = Party(name="Customer")
    bank = Party(name="Bank")

    # Step 2: Instantiate credit score model
    credit_model = CreditScoreNN()

    # Step 3: Load model weights from Nillion network
    credit_model.load_state_from_network("credit_score_model", bank, na.SecretRational)

    # Step 4: Load customer's financial data (provided by Customer)
    # Assume 10 features: income, debt, credit history, etc.
    customer_data = na.array((10,), customer, "customer_financial_data", na.SecretRational)

    # Step 5: Compute credit score
    credit_score = credit_model(customer_data)

    # Step 6: Output the credit score for the Customer
    return credit_score.output(customer, "credit_score_result")