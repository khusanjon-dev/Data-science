""" 5. Tuple ichida qatnashgan elementlar sonini hisoblaydigan funksiya yozing.

 Misol uchun:
 ```
  ('a', 'b', 'a', 'c', 'b', 'a', 'd', 'c')
```
javob: ```  {'a': 3, 'b': 2, 'c': 2, 'd': 1} ```"""


signs = ('a', 'b', 'a', 'c', 'b', 'a', 'd', 'c')
def count_letters(signs):
    result = {}
    for sign in signs:
        if result.get(sign):
            result[sign] += 1
        else:
            result[sign] = 1
    print(result)
