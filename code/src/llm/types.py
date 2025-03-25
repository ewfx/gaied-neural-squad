from json import dumps

request_types = {
    "requestType": [
        {
            "name": "Adjustments",
            "description": "Requests related to loan adjustments, such as interest or principal corrections.",
            "fields": [
                "Loan ID",
                "Borrower Name",
                "Adjustment Amount",
                "Reason for Adjustment",
                "Effective Date",
                "Supporting Documents",
            ],
            "subtypes": [],
        },
        {
            "name": "AU Transfer",
            "description": "Requests involving the transfer of an AU (Authorized User) or loan-related accounts.",
            "fields": [
                "Loan ID",
                "Borrower Name",
                "Transfer Amount",
                "Transfer From",
                "Transfer To",
                "Effective Date",
                "Reason for Transfer",
            ],
            "subtypes": [],
        },
        {
            "name": "Closing Notice",
            "description": "Notifications regarding changes in loan closure, including reallocation or amendment fees.",
            "fields": ["Loan ID", "Borrower Name", "Effective Date"],
            "subtypes": [
                {
                    "name": "Reallocation Fees",
                    "description": "Requests to reallocate fees within loan accounts.",
                    "fields": [
                        "Fee Type",
                        "Amount",
                        "Justification for Reallocation",
                        "Supporting Documents",
                    ],
                },
                {
                    "name": "Amendment Fees",
                    "description": "Requests to apply or modify amendment-related fees on the loan.",
                    "fields": [
                        "Fee Type",
                        "Amount",
                        "Amendment Details",
                        "Supporting Documents",
                    ],
                },
                {
                    "name": "Reallocation Principal",
                    "description": "Requests to reallocate principal amounts between loan accounts.",
                    "fields": [
                        "Principal Reallocated Amount",
                        "Reason for Reallocation",
                    ],
                },
            ],
        },
        {
            "name": "Commitment Change",
            "description": "Requests to modify loan commitments, such as increases or decreases in amounts.",
            "fields": ["Loan ID", "Borrower Name", "Effective Date"],
            "subtypes": [
                {
                    "name": "Cashless Roll",
                    "description": "Extending or rolling a commitment without cash movement.",
                    "fields": [
                        "Amount",
                        "Current Commitment Amount",
                        "New Commitment Amount",
                        "Justification",
                    ],
                },
                {
                    "name": "Decrease",
                    "description": "Requests to decrease the loan commitment.",
                    "fields": [
                        "Amount Decreased",
                        "Reason for Decrease",
                        "Supporting Documents",
                    ],
                },
                {
                    "name": "Increase",
                    "description": "Requests to increase the loan commitment.",
                    "fields": [
                        "Requested Increase Amount",
                        "Justification",
                        "Supporting Documents",
                    ],
                },
            ],
        },
        {
            "name": "Fee Payment",
            "description": "Requests related to payment of fees associated with the loan.",
            "fields": ["Loan ID", "Borrower Name", "Due Date", "Payment Method"],
            "subtypes": [
                {
                    "name": "Ongoing Fee",
                    "description": "Requests related to periodic or recurring fees on the loan.",
                    "fields": ["Fee Type", "Amount"],
                },
                {
                    "name": "Letter of Credit Fee",
                    "description": "Requests related to Letter of Credit fees linked to the loan.",
                    "fields": ["Fee Type", "Amount", "Letter of Credit Details"],
                },
            ],
        },
        {
            "name": "Money Movement - Inbound",
            "description": "Requests related to inbound payments, such as principal and interest payments.",
            "fields": ["Loan ID", "Borrower Name", "Payment Method", "Effective Date"],
            "subtypes": [
                {
                    "name": "Principal",
                    "description": "Requests regarding principal-only payments.",
                    "fields": ["Principal Amount"],
                },
                {
                    "name": "Interest",
                    "description": "Requests regarding interest-only payments.",
                    "fields": ["Interest Amount"],
                },
                {
                    "name": "Principal + Interest",
                    "description": "Requests involving payments covering both principal and interest.",
                    "fields": ["Total Amount"],
                },
                {
                    "name": "Principal + Interest + Fee",
                    "description": "Requests involving payments covering principal, interest, and applicable fees.",
                    "fields": ["Total Amount", "Fee Type"],
                },
            ],
        },
        {
            "name": "Money Movement - Outbound",
            "description": "Requests related to outbound payments, such as transfers or foreign currency transactions.",
            "fields": [
                "Loan ID",
                "Borrower Name",
                "Payment Date",
                "Beneficiary Details",
            ],
            "subtypes": [
                {
                    "name": "Timebound",
                    "description": "Requests related to scheduled or time-sensitive outbound payments.",
                    "fields": ["Amount", "Reason for Transfer"],
                },
                {
                    "name": "Foreign Currency",
                    "description": "Requests involving outbound payments in a foreign currency.",
                    "fields": [
                        "Amount in Foreign Currency",
                        "Currency Type",
                        "Exchange Rate",
                        "Reason for Transfer",
                    ],
                },
            ],
        },
    ]
}

request_types_str = dumps(request_types).replace("{", "(").replace("}", ")")

alternate_request_types = """(
  "Request Types": (
    "Adjustments": (
      "description": "Adjustments refer to any changes or corrections made to a loan agreement or its terms after the loan has been disbursed. These can include modifying payment amounts, applying rebates, or rectifying errors in loan details.",
      "subtypes": []
    ),
    "AU Transfer": (
      "description": "This refers to the transfer of loan between Administrative Units, where the loan servicing is moved between entities or accounts internal to the bank.",
      "subtypes": []
    ),
    "Closing Notice":
      "description": "The closing notice is issued when a loan is nearing the end of its term or when it is being settled early. It notifies involved parties of the final payment and confirms the closure of the loan.",
      "subtypes": (
        "Reallocation Fees": "Fees that are charged to adjust or redistribute loan charges or payments upon the loan's closure.",
        "Amendment Fees": "Fees that apply when changes are made to the loan terms before it is closed.",
        "Reallocation Principal": "Involves adjusting the principal balance upon closure, which might include redistributing the amount owed."
      )
    ),
    "Commitment Change": (
      "description": "A commitment change refers to any alterations to the original agreement terms, such as changes to the commitment level or conditions of the loan.",
      "subtypes": (
        "Cashless Roll": "A type of commitment change where the loan term is extended, and no additional cash is exchanged, usually meaning the principal remains unchanged while the loan is carried over to a new term.",
        "Decrease": "A decrease in the committed loan amount, reducing the funds available or the limit on a revolving credit facility.",
        "Increase": "An increase in the committed loan amount, expanding the available funds or credit limit for the borrower."
      )
    ),
    "Fee Payment": (
      "description": "Fee payments are requests related to the payment of specific loan-associated fees. These could include charges for ongoing service or special agreements in the loan contract.",
      "subtypes": (
        "Ongoing Fee": "Regularly charged fees associated with maintaining or servicing the loan, typically occurring on a periodic basis.",
        "Letter of Credit Fee": "Fees charged for issuing or maintaining a letter of credit, which is often used as a financial guarantee for certain loan arrangements or agreements."
      )
    ),
    "Money Movement - inbound": (
      "description": "Inbound money movement refers to funds coming into the loan account, typically representing payments or deposits made by the borrower or third-party.",
      "subtypes": (
        "Principal": "Repayment of the principal amount of the loan.",
        "Interest": "Payment of the interest accrued on the loan.",
        "Principal + Interest": "A payment covering both the principal and interest amounts owed on the loan.",
        "Principal + Interest + Fee": "A combined payment that covers the principal, interest, and any associated fees, ensuring the full repayment amount."
      )
    ),
    "Money Movement - Outbound": (
      "description": "Outbound money movement refers to funds leaving the loan account, typically related to transfers or repayments made to other parties.",
      "subtypes": (
        "Timebound": "A payment or movement of funds that must occur within a specified timeframe, often tied to the loan's repayment schedule or contractual obligations.",
        "Foreign Currency": "Money movement that involves the exchange or transfer of funds in a foreign currency, typically related to international loans or transactions requiring currency conversion."
      )
    )
  )
)
"""
