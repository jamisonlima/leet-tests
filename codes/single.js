function singleNumber(nums: number[]): number {
    let hash = new Map<number, number>();

    for (let num of nums){
        hash.set(num, hash.has(num) ? 2 : 1)
    }
    for (const [key, value] of hash){
        if (value === 1){
            return key
        }
    }
};
