import re

# vowel = "[AEIOUaeiou]"
# consonant = '[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]'
a = re.findall(
    '(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})[qwrtypsdfghjklzxcvbnm]',
    input(), re.IGNORECASE)

if len(a) == 0:
    print(-1)
else:
    print(*a, sep='\n')
