class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1 
            lenght = int(s[i:j])
            i = j + 1
            result.append(s[i: i + lenght])
            i += lenght
        return result


