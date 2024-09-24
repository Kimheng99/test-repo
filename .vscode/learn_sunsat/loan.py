work_cos = 50000
score_cos = 750
pay_cos = 30000


min_work = 30000
min_score = 700
max_pay = 20000

loan_approve = False
if min_work <= work_cos:
    if min_score <= score_cos:
        if max_pay >= pay_cos:
            loan_approve = True
if loan_approve:
    print("loan is Approv for you")
else:
    print("loan not approve")


