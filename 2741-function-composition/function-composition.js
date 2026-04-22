/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    if (functions.length === 0) {
        return function(x) { return x; };
    }

    return function(x) {
        return functions.reduceRight((acc, fn) => {
            return fn(acc);
        }, x);
    };
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9 (2 * 4 = 8, then 8 + 1 = 9)
 */