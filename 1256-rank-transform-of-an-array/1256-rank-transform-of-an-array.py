class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_ = sorted(arr)
        rank_map = {}
        r = 1
        for i, e in enumerate(arr_):
            if not rank_map.get(e):
                rank_map[e] = r 
                r += 1

        out = []
        for e in arr:
            out.append(rank_map[e])
        return out
        