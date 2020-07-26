"""
PercolationStats performs a serious of computational experiments and provides statistics gathered from the experiments.
"""
from Percolation import Percolation
import math


class PercolationStats:

    def __init__(self, n, trials):
        self.results = []
        self.trials = trials
        for trial in range(self.trials):
            p = Percolation(n)
            p.run_simulation()
            self.results.append(p.percolation_threshold())
        self.print_results()

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

    def print_results(self):
        print(f"{'mean':<25}= {self.mean()}")
        print(f"{'stddev':<25}= {self.stddev()}")
        print(f"{'95% Confidence Interval':<25}= [{self.confidence_low()}, {self.confidence_high()}]")


if __name__ == '__main__':
    percolation_stats = PercolationStats(200, 100)
