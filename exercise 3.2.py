print("*********Placement Eligibility System***********")

score = float(input(" Enter graduation score (%) :"))
backlog = int(input(" Enter Number of Academic backlogs : "))
interview = input(" Did the candidate clear the interview: ").lower()

if score >= 70 and backlog == 0 and interview == "yes":
    print("  Candidate is Eligible for placement.")

else:
    print("  Candidate is not Eligible for placement.")
    