 # Plotting acuracy of test cases used in MIT paper
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, List, Dict
from dataclasses import dataclass

@dataclass
class TestResult:
    """Class for storing test results"""
    matrix_size: int
    actual_norm: float
    theoretical_bound: float
    ratio: float
    satisfies_bound: bool

class MatrixTheoryTest:
    def __init__(self):
        """Initialize the testing framework"""
        self.results: List[TestResult] = []

    @staticmethod
    def frobenius_norm(A: np.ndarray) -> float:
        """Calculate the Frobenius norm of a matrix."""
        return np.sqrt(np.sum(A * A))

    def verify_lower_bound(self, A: np.ndarray) -> TestResult:
        """
        Verify the lower bound for the Frobenius norm of the inverse of a non-negative matrix.
        The bound states that ||A^(-1)||_F >= (2n/(n+1))||A||_max^(-1).
        """
        if not np.all(A >= 0):
            raise ValueError("Input matrix must be non-negative")
            
        n = A.shape[0]
        max_norm = np.max(np.abs(A))
        
        try:
            A_inv = np.linalg.inv(A)
            inv_frob_norm = self.frobenius_norm(A_inv)
        except np.linalg.LinAlgError:
            return TestResult(n, 0, 0, 0, False)
            
        theoretical_bound = (2 * n / (n + 1)) / max_norm
        satisfies_bound = inv_frob_norm >= theoretical_bound
        ratio = inv_frob_norm / theoretical_bound
        
        return TestResult(n, inv_frob_norm, theoretical_bound, ratio, satisfies_bound)

    def generate_random_nonnegative_matrix(self, n: int) -> np.ndarray:
        """Generate a random non-negative matrix for testing."""
        # Generate random matrix with entries between 0 and 1
        A = np.random.rand(n, n)
        
        # Ensure matrix is well-conditioned
        A = A + n * np.eye(n)
        return A

    def run_tests(self, num_tests: int = 50) -> List[TestResult]:
        """Run multiple tests with varying matrix sizes."""
        # Generate matrix sizes from 4 to 1200
        matrix_sizes = np.linspace(4, 1200, num_tests, dtype=int)
        
        results = []
        for n in matrix_sizes:
            # Generate and test random matrix
            A = self.generate_random_nonnegative_matrix(n)
            result = self.verify_lower_bound(A)
            results.append(result)
            
        self.results = results
        return results

    def plot_results(self):
        """Create visualizations of the test results."""
        if not self.results:
            raise ValueError("No test results available. Run tests first.")

        # Set up the plot with a clean style
        plt.style.use('default')
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12))

        # Extract data
        sizes = [r.matrix_size for r in self.results]
        ratios = [r.ratio for r in self.results]
        satisfies = [r.satisfies_bound for r in self.results]

        # Plot 1: Scatter plot of ratios
        colors = ['green' if s else 'red' for s in satisfies]
        ax1.scatter(sizes, ratios, c=colors, alpha=0.6)
        ax1.axhline(y=1.0, color='blue', linestyle='--', label='Theoretical Minimum')
        ax1.set_xlabel('Matrix Size (n)')
        ax1.set_ylabel('Ratio (Actual/Theoretical)')
        ax1.set_title('Frobenius Norm Ratio vs Matrix Size')
        ax1.grid(True, alpha=0.3)
        ax1.legend()

        # Plot 2: Distribution of ratios
        bins = np.linspace(min(ratios), max(ratios), 20)
        ax2.hist(ratios, bins=bins, alpha=0.6, color='blue')
        ax2.axvline(x=1.0, color='red', linestyle='--', label='Theoretical Minimum')
        ax2.set_xlabel('Ratio (Actual/Theoretical)')
        ax2.set_ylabel('Count')
        ax2.set_title('Distribution of Frobenius Norm Ratios')
        ax2.grid(True, alpha=0.3)
        ax2.legend()

        # Add summary statistics text
        satisfied_count = sum(satisfies)
        avg_ratio = np.mean(ratios)
        min_ratio = np.min(ratios)
        
        summary = (f'Summary Statistics:\n'
                  f'Tests satisfying bound: {satisfied_count}/{len(self.results)}'
                  f' ({satisfied_count/len(self.results)*100:.1f}%)\n'
                  f'Average ratio: {avg_ratio:.4f}\n'
                  f'Minimum ratio: {min_ratio:.4f}')
                  
        fig.text(0.15, 0.02, summary, fontsize=10, family='monospace')

        plt.tight_layout()
        plt.show()

def main():
    """Run the test suite and display results."""
    # Initialize and run tests
    tester = MatrixTheoryTest()
    tester.run_tests(50)
    
    # Display results
    tester.plot_results()

if __name__ == "__main__":
    main()