class Solution {
    func hIndex(_ citations: [Int]) -> Int {
        let n: Int = citations.count
        var count: [Int] = Array(repeating: 0, count: n + 1)

        for c in citations {
            if c >= n {
                count[n] += 1
            } else {
                count[c] += 1
            }
        }

        var total: Int = 0
        for i in stride(from: n, through: 0, by: -1) {
            total += count[i]
            if total >= i {
                return i
            }
        }
        return 0
    }
}