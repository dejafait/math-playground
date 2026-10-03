# L012 — The proposed relative boundary domain is not closed off shell under BRST

## Hypotheses

Let D = (-4,4)^4. On each flat face F, let n be its constant outward unit normal, A_n = n^mu A_mu, and A_t denote each tangential component. Take a smooth SU(2) connection A, odd ghost and antighost c and bar c, and an independent even auxiliary field b. All coefficient functions extend smoothly to a neighborhood of the closed cube and take values in the anti-Hermitian Lie algebra, tensored with a Grassmann algebra.

Absorb the coupling into A and use the standard BRST transformations

\[
sA_\mu=\partial_\mu c+[A_\mu,c],\qquad
sc=-\tfrac12[c,c],\qquad
s\bar c=b,\qquad sb=0.
\tag{1}
\]

Impose, separately on all eight faces and their intersections,

\[
A_t=0,\qquad \partial_n A_n=0,\qquad
c=\bar c=b=0.
\tag{2}
\]

No field equation, ghost equation, or restriction to Laplacian eigenfunctions is imposed. Closure off shell means that s applied to every boundary constraint vanishes for every smooth configuration satisfying (2).

The algebra (1) is a supporting standard input: Barnich–Brandt–Henneaux, *Local BRST cohomology in gauge theories*, [hep-th/0002245v3](https://arxiv.org/pdf/hep-th/0002245v3), (2.8)–(2.9) and the nonminimal pair (2.47). The [prior assessment](../drafts/literature/2026-10-03-boundary-brst-counterterms.md) preapproves this exact smooth-domain specialization. No full boundary-counterterm theorem is imported.

## Conclusion

The domain (2) is **not** closed off shell under (1). On any face its unconstrained normal variation is

\[
s(\partial_n A_n)|_F
=\bigl(\partial_n^2c+[A_n,\partial_nc]\bigr)|_F.
\tag{3}
\]

There is an explicit counterexample with A = bar c = b = 0 and a single-colour smooth polynomial ghost. It satisfies (2) on every face and even partial_n c = 0 on every face. Only the upper-face normal Neumann constraint fails after the variation, already at the face-interior point (0,0,0,4).

This stops the proposed strong off-shell boundary-domain shortcut. It does not refute spectral relative boundary conditions, the Gaussian representation in L003, a formulation retaining b with a different connection domain, or the Yang–Mills target. It establishes no counterterm coefficient, cutoff divergence, O(1) remainder or interacting reflected-error bound.

## Proof

Since the normal and tangential frame is constant on a flat face, s commutes with these spatial derivatives. The restriction of c to F is identically zero, so every tangential derivative of that trace vanishes. Hence

\[
(sA_t)|_F=(\partial_t c+[A_t,c])|_F=0.
\]

The other algebraic traces are preserved: sc vanishes where c = 0; s bar c = b = 0 on F; and sb = 0. For the normal derivative, the product rule gives

\[
s(\partial_n A_n)
=\partial_n^2c+[\partial_n A_n,c]+[A_n,\partial_nc].
\]

The middle bracket vanishes on F because c = 0 there, giving (3). A zero ghost trace places no general restriction on its second normal derivative.

For a fully explicit simultaneous test of all faces, put

\[
H(u)=(1-u^2/16)^3,\qquad
R(v)=\frac{(4-v)^2(v+4)^3}{1024},\qquad
\phi(x)=R(x_4)\prod_{j=1}^3 H(x_j).
\tag{4}
\]

Choose a nonzero odd generator xi and T = (i/2) diag(1,-1) in su(2), and set

\[
A=0,\qquad \bar c=0,\qquad b=0,\qquad
c(x)=\mathord{\mathrm{xi}}\,T\phi(x).
\tag{5}
\]

All coefficient functions are polynomials, so there is no regularity or extension issue. H has a triple zero at both endpoints, while R has a triple zero at -4 and a double zero at 4. Direct differentiation therefore gives

\[
H(\pm4)=H'(\pm4)=H''(\pm4)=0,\quad H(0)=1,
\]
\[
R(-4)=R'(-4)=R''(-4)=0,\qquad
R(4)=R'(4)=0,\quad R''(4)=1.
\tag{6}
\]

On every lateral face a factor H vanishes, and on either time face R vanishes. Thus c = 0 on the entire boundary. The same endpoint identities give partial_n c = 0 on every face. The zero connection, antighost and independent auxiliary field satisfy all remaining conditions in (2).

At this configuration D_A c = dc. On the upper face F_+ = {x_4 = 4}, n = e_4, so (3) and (6) yield

\[
s(\partial_n A_n)|_{F_+}
=\mathord{\mathrm{xi}}\,T\prod_{j=1}^3H(x_j).
\tag{7}
\]

At (0,0,0,4) this equals xi T, which is nonzero. The normal derivative constraint is consequently not preserved. On the other seven faces the second normal derivative vanishes by the triple-root identities. At intersections of F_+ with lateral faces the product in (7) vanishes as well; the counterexample has no conflicting corner traces. The tangential, ghost, antighost and auxiliary constraints are preserved as checked above. The ghost's self-bracket also vanishes everywhere for this single odd generator.

For the source qualification, at A = 0 a smooth Dirichlet ghost obeying -Delta c = lambda c up to a flat face also obeys partial_n^2 c = 0 there: its tangential second derivatives vanish with its boundary trace, and the eigenfunction equation supplies the remaining normal derivative. Our ghost has partial_n^2 c = xi T at the indicated point and obeys no such equation. Thus the counterexample is outside that eigenfunction restriction. It says nothing about closing the full nonlinear domain under a modified restriction.

The closest inspected boundary statements retain precisely such qualifications: Moss–Silva, *BRST Invariant Boundary Conditions for Gauge Theories*, [gr-qc/9610023v1](https://arxiv.org/pdf/gr-qc/9610023v1), (31), (33), (37)–(39), distinguishes the independent auxiliary field from its eliminated on-shell form; Christiansen Murguizur–Manzo–Pisani, *Worldline Images for Yang-Mills Theory within Boundaries*, [2604.05082v1](https://arxiv.org/html/2604.05082v1), section 2, (2.5)–(2.11), invokes a Laplacian eigenfunction parameter. The calculation reproduces this domain distinction in the exact cube test; it claims no result beyond the checked literature.

## Mathlib

Coverage of the full off-shell boundary-domain statement, BRST algebra and smooth cube specialization: **not checked**. The named sources above support the algebra and domain qualifications; they are not asserted Mathlib matches or full source-dependent counterterm classifications. The proof uses only the stated algebra, boundary traces and polynomial differentiation.
