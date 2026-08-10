import json, ast

p = r'e:\github\learn-algorithm\Untitled-1.ipynb'
with open(p, encoding='utf-8') as f:
    nb = json.load(f)

src = ''.join(nb['cells'][1]['source'])
ast.parse(src)
print('syntax OK')

exec(compile(src, '<test>', 'exec'))
s = Solution()
print('isAnagram("anagram","nagaram") =', s.isAnagram("anagram", "nagaram"))
print('isAnagram("rat","car") =', s.isAnagram("rat", "car"))
