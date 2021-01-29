x = {"Red":4/7, "Black":3/7}
y = {"Red":5/9, "Black":4/9}
z = {"Red":4/8, "Black":4/8}

# Get possibilities
first_possibility = x["Red"] * y["Red"] * z["Black"]
second_possibility = x["Red"] * y["Black"] * z["Red"]
third_possibility = x["Black"] * y["Red"] * z["Red"]

# Get probability
print(first_possibility + second_possibility + third_possibility)

=======================================================================
Urn X has a 4/7 probability of giving a red ball
Urn Y has a 5/9 probability of giving a red ball
Urn Z has a 1/2 probability of giving a red ball

Urn X has a 3/7 probability of giving a black ball
Urn Y has a 4/9 probability of giving a black ball
Urn Z has a 1/2 probability of giving a black ball

P(2 red, 1 black)
= P(Red Red Black) + P(Red Black Red) + P(Black Red Red)
= (4/7)(5/9)(1/2) + (4/7)(4/9)(1/2) + (3/7)(5/9)(1/2)
= 20/126 + 16/126 + 15/126
= 51/126
= 17/42

==========================================================================
P(Red Red Black) represents drawing a Red on Draw 1, a Red on Draw 2, and a Black on Draw 3.

P(Red Black Red) represents drawing a Red on Draw 1, a Black on Draw 2, and a Red on Draw 3.

P(Black Red Red) represents drawing a Black on Draw 1, a Red on Draw 2, and a Red on Draw 3.

These are 3 different scenarios. Since these events are mutually exclusive, we have P(A or B or C) = P(A) + P(B) + P(C), so adding the 3 probabilities gives us the total probability of drawing the 2 Red balls and 1 Black ball in any order.
==================