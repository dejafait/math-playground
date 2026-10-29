# Cubic internal-curl bulk source limit — work checkpoint

2026-10-26. Work under the unchanged prior EXPLORE assessment
`literature/2026-10-26-complete-cubic-quadratic-asymptotic.md`, on its
exact complete-cubic target. One bounded partial test: evaluate L288's
finite-range bulk row sum and pass it through L282's actual source
fields. Main gap remains interacting continuum existence and finite
positive mass. A complete limit of L287's G_-+ group would supply one
coefficient for comparison with L285(4); the two mixed groups and the
distinct-line group remain independent obligations. Continue only with
a full relative-boundary and source-tail argument; stop an argument
that depends only on bulk entries or an unestimated boundary layer.

Reused the supplied ready literature assessment. Read complete L287,
L288 and relevant L282 sections 2–4, the exact cubic jet L286(4)–(5),
L280(20), L283's bulk normalization and L285(4). ATTEMPTS/047–049
remain preserved. No known result for the exact cubic limit is imported;
this is the approved Wilson-specific specialization of existing inputs.

Tentative calculation, to be checked before promotion: on a mu,nu
plaquette, raw signed slots are A=x_mu(n), B=x_nu(n+mu),
C=-x_mu(n+nu), D=-x_nu(n). For a constant external field U in direction
mu, differentiation of zeta=1/2 sum_[j<k][X_j,X_k] gives
[U,B+(A+C)/2]=[U,(A+B+C+D)/2+(B-D)/2]. The curl dotted with its
own bracket is zero. The retained contribution is therefore the curl
dotted with [U,the mu-average of x_nu]. The analogous nu term has a
minus sign. This keeps all raw slot phases.

In midpoint Fourier coordinates put d_mu=2 sin(q_mu/2),
c_mu=cos(q_mu/2), lambda=|d|^2, P=I-dd*/lambda. The positive
polynomial covariance is gamma_m P, gamma_m=lambda h_m(lambda)^2.
For constant external direction mu and one fixed color, symmetrizing
the spatial quadratic kernel gives -i c_mu A_mu, where
A_mu=d_mu I-(e_mu d*+d e_mu*)/2. Thus P A_mu P=d_mu P.
The color bracket matrix has square trace -2. The Gaussian variance
and E=2 covariance factors appear to give the bulk row sum
24 integral sin(q_mu)sin(q_nu) gamma_m^2, hence a scalar
 e_m=24 integral sin(q_1)^2 lambda^2 h_m(lambda)^4 -> 24 I_1.
Need verify normalization by an independent real-mode calculation,
and prove the row-sum extraction via finite periodic tori, then the
fixed-m boundary physical norm and strong-field passage. Only then
combine L288's uniform error, L282's source fields and L287's external
tail. Tentative M_3/N^2 limit is (3/128)(24 I_1) S_f.
No coefficient or completed result is yet asserted by this work note.

## Completed partial result and checks

[L289](../lemmas/L289-cubic-mixed-covariance-quadratic-asymptotic.md)
completes the proposed G_-+ group limit. The exact constant-field
bracket gives the midpoint Fourier quadratic matrix -i H_u tensor J_A.
Projection yields P H_u P=(sum_mu u_mu sin q_mu)P. The real Gaussian
pairing factor, Tr J_A^2=-2 and Tr P=3 give the bulk row sum
24 integral sin(q_1)^2 lambda^2 h_m(lambda)^4 -> 24 I_1.
A separate cosine/sine real-mode calculation checks the factor 24.
This is an analytic normalization check, not a separate critical audit.

For fixed m, finite range and bounded row sums leave O_m(N^3) boundary
edges with squared physical error O_m(a^4 N^3)->0. L288's whole-operator
error permits m->infinity only after this fixed-m limit. Uniform norms
extend the result to L282's actual strong source fields. L287's complete
external mode tail then permits removal of the external cutoff. All
internal vertices and normal links stay in these estimates. The complete
M_3/N^2 limit is (9 I_1/16) S_f with o(N^2) error.

The comparison also simplifies exactly: integrate
partial_1(sin q_1/lambda) on the Brillouin cube with a small ball removed.
The small-sphere flux is O(epsilon^2), and both derivatives are integrable.
Thus 2 I_1=integral cos q_1/lambda=Z_0-1/8. This cancels the entire S_f
coefficient of M_3 plus L285(4) and reduces that subtotal to Z_0 J_f/64.
This elementary evaluation is included in L289 because the comparison
requires it; no external scalar kernel result is imported or reproved.

Remaining obligations: both mixed insertion/action groups, distinct-line
G_-/G_+ group and their possible J_f compensation; subleading control
and the uniform higher remainder. L286–L289 still lack separate critical
audits. The continuum and physical mass gaps are unchanged. Continue the
same approved full cubic target by testing complete mixed groups with
source weights, boundary rows and uniform summed errors retained; no
subfamily's scale or cancellation may be presumed for the remaining sum.
