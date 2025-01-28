# 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import NMF


# V is the original non-negative data 
 ## t columns of f-dimensional data 
 ### Each column is a sample, each row is a feature
# W constitutes the basis vectors - a dictionary matrix
## A kinear combination of these approximates any sample in V
### Each column is called a basis vextor
# H is the activation matrix
## Each column encodes a linear combination of all basis vectors, 
##... corresponding to a sample in V
### Each column is called a set of activations (or weights or gains)

# Data
np.random.seed(42)
n_samples = 150
n_features = 10
n_components = 8

# true components and coefficients
true_W = np.abs(np.random.normal(1, 0.3, (n_samples, n_components)))
true_H = np.abs(np.random.normal(1, 0.3, (n_components, n_features)))
V = true_W @ true_H + np.abs(np.random.normal(0, 0.1, (n_samples, n_features)))

# nndsvd in NFM theorem refers to Non-Negative Double Singular Value Decomposition
# DSVD is the act of computing the SVD of the input, then using this computation to initialise factors
# I'm using the init='nndsvd' to initialise the factor matrices W (basis vectors) and H (coefficents)

# Thus we build out the NMF model
model = NMF(n_components=n_components, init='nndsvd', max_iter=1000, random_state=42)
W = model.fit_transform(V)
H = model.components_

V_reconstructed = W @ H

# contingency in case of error 
reconstruction_error = np.linalg.norm(V - V_reconstructed, 'fro')

# visualise lol
plt.figure(figsize=(18, 10))

# Now to build out four plots 


# i) OG vs reconstructed data
plt.subplot(2, 2, 1)
# creates a 2x2 grid 
plt.plot(V[0], 'b-', label='Original (sample 1)')
plt.plot(V_reconstructed[0], 'r--', label='Reconstructed (Sample 1)')
plt.plot(V[1], 'g-', label='Original (Sample 2)')
plt.plot(V_reconstructed[1], 'm--', label='Reconstructed (Sample 2)')
plt.title('OG vs Reconstructed Features\n(Frobenius Norm Error: {:.4f})'.format(reconstruction_error))
plt.xlabel('Feature Index')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
# 53-61 to show OG vs reconstructed 

# ii) H matrix
plt.subplot(2, 2, 2)
plt.imshow(H, cmap='viridis')
plt.title('NMF Components (H Matrix)')
plt.xlabel('OG Features')
plt.ylabel('Latent Components')
plt.colorbar(label='Component Weight')

# Weight == activations 

# iii) Component Weight/Activation (W Matrix)
plt.subplot(2, 2, 3)
plt.scatter(range(n_samples), W[:, 0], label= 'Component 1', alpha=0.6)
plt.scatter(range(n_samples), W[:, 1], label='Component 2', alpha=0.6)
plt.title('Component Activations Across Samples')
plt.xlabel('Sample Index')
plt.ylabel('Activation Strength')
plt.legend()
plt.grid(True)


# iv) Convergence 
plt.subplot(2, 2, 4)
plt.plot(model.reconstruction_err_, 'k-')
plt.title('NMF Convergence (Reconstruction Error)')
plt.xlabel('Iteration')
plt.ylabel('Error')
plt.grid(True)
plt.tight_layout()
plt.grid(True)

# All plots built...
# Now to print all charts together in the same figure
plt.show()

# Component info using f strings
print(f"NMF Components Shape: {H.shape}")
print(f"Sample Activations Shape: {W.shape}")
print(f"Final Reconstruction Error: {reconstruction_error: .4f}")
