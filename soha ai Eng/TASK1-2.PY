#Customer Message Classifier
Message=input("Choose the keyword in the customer's message:(Payment,Delivery,Erorr,Other)")
Hours=float(input("How many hours has the ticket been open? "))
Keyword_Lower=Message.lower()
if "payment" in Keyword_Lower:
    print("Billing Team")
elif "delivery" in Keyword_Lower:
    print("logistics Team")
elif "erorr" in Keyword_Lower:
    print("tech team") 
else:
    print("General Team") 

if Hours > 24:
    print("LOWER")
elif Hours ==24:
    print("NORMAL")
elif Hours < 24:
    print("HIGHER")