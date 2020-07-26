"""
PercolationStats performs a serious of computational experiments and provides statistics gathered from the experiments.
"""
from Percolation import Percolation
import math
from statistics import stdev


class PercolationStats:

    def __init__(self, n, trials):
        self.results = []
        self.trials = trials
        for trial in range(self.trials):
            p = Percolation(n)
            p.run_simulation()
            self.results.append(p.percolation_threshold())

    def mean(self):
        return sum(self.results) / self.trials

    def stddev(self):
        mean = self.mean()
        s_squared = math.sqrt(sum([(x - mean) ** 2 for x in self.results]) / (self.trials - 1))
        return s_squared

    def confidence_low(self):
        mean = self.mean()
        return mean - (1.96 * self.stddev())/(math.sqrt(self.trials))

    def confidence_high(self):
        mean = self.mean()
        return mean + ((1.96 * self.stddev()) / math.sqrt(self.trials))


if __name__ == '__main__':
    n = 200
    trials = 100
    perc_stats = PercolationStats(n, trials)
    print(f"{'mean':<25}= {perc_stats.mean()}")
    print(f"{'stddev':<25}= {perc_stats.stddev()}")
    print(f"{'95% Confidence Interval':<25}= [{perc_stats.confidence_low()}, {perc_stats.confidence_high()}]")
