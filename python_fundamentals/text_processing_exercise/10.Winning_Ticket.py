def sign_check(ticket):
    first = ticket[:10]
    second = ticket[10:]
    for sign in signs:
        if sign * 6 in first and sign * 6 in second:
            result = min(first.count(sign), second.count(sign))
            print(f'ticket "{ticket}" - {result}{sign}')
            return True
    return False


def jackpot(ticket):
    for el in signs:
        if el in ticket:
            if ticket.count(el) == 20:
                print(f'ticket "{ticket}" - {10}{el} Jackpot!')
                return True
    return False


signs = ["@", "#", "$", "^"]

tickets = [x.strip() for x in input().split(",")]

for ticket in tickets:
    if not len(ticket) == 20:
        print(f"invalid ticket")
    elif jackpot(ticket):
        continue
    elif sign_check(ticket):
        continue
    else:
        print(f'ticket "{ticket}" - no match')