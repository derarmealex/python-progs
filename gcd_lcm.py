def gcd_lcm(x, y):
    gcd = 1
    if y % x == 0:
        return (f'{x}, | {y * x / gcd}')
    for z in range(y, 0, -1):
        if y % z == 0 and x % z == 0:
            gcd = z
            break
    return (f'{gcd}, {y * x / gcd}')
print('gcd | lcm of 3, 15 is', gcd_lcm(3, 15))
print('gcd | lcm of 19, 21 is', gcd_lcm(19, 21))
print('gcd | lcm of 36, 12 is', gcd_lcm(36, 12))
print('gcd | lcm of 15, 17 is', gcd_lcm(15, 17))
print('gcd | lcm of 6, 4 is', gcd_lcm(6, 4))
print('gcd | lcm of 360, 336 is', gcd_lcm(360, 336))