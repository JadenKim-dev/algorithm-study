def solution(enroll, referral, sellers, amounts):
    parent = {e:r for e, r in zip(enroll, referral)}
    benefit = {name:0 for name in enroll}
    
    def sell(seller, amount):
        to_upper = amount//10
        if to_upper == 0:
            benefit[seller] += amount
            return
        
        benefit[seller] += (amount - to_upper)
        
        if parent[seller] == '-':
            return
        sell(parent[seller], to_upper)
    
    for i in range(len(sellers)):
        seller, amount = sellers[i], amounts[i]*100
        sell(seller, amount)
        
    return [benefit[name] for name in enroll]