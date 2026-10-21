# L104 — Centered translated-pole collision reduction

## Hypotheses

Use L102's Q=65537, E=F_Q, H=<19139> of order n=1024,
F=F_(Q^28), degree bound k=64 and every m>=1, with the closed
simultaneous-column list model in
[foundations/02](../foundations/02-pinned-list-model.md).
Put s=67, Z=X-3, R=E[Z]/(Z^3), G=R^*,
D=(Q-1)Q^2, C=binomial(n,s), T=Q^28/2^128 and mu=C/D.
For any subset A of H, let g_A(X)=product_(x in A)(X-x) and
rho(A)=g_A(Z+3) mod Z^3. The empty product is one.
Let N(z), z in G, be L102's full class distribution, retaining empty
labels, and let W_chi=sum_(|S|=s) chi(rho(S)). Define

\[
 V=\sum_{z\in G}(N(z)-\mu)^2.
\]

For 0<=r<=s, let K_r be the number of **ordered** pairs (A,B)
of disjoint r-subsets of H with rho(A)=rho(B). Set

\[
 w_r=\binom{n-2r}{s-r},\qquad
 P_r=\binom nr\binom{n-r}r,\qquad B_*=(T-\mu)^2.
\]

All binomial arguments here are nonnegative and in range.

## Conclusion

The mean gap is positive, with exact rational comparisons

\[
 \frac{24558746}{10^{12}}<\frac\mu T<\frac{24558747}{10^{12}}<1.
                                                               \tag{1}
\]

The fully normalized centered identities are

\[
 V=\frac1D\sum_{\chi\ne1}|W_\chi|^2
   =\sum_{r=0}^{67}w_rK_r-\frac{C^2}{D}
   =\sum_{r=0}^{67}w_r\left(K_r-\frac{P_r}{D}\right). \tag{2}
\]

In particular K_0=1 and K_1=K_2=K_3=0. Put

\[
 L=\frac1D\sum_{r=0}^3w_rP_r,\quad \delta=C-L,\quad
 \mathcal E=\sum_{r=4}^{67}w_r\left(K_r-\frac{P_r}{D}\right).
\]

Then

\[
 V=\delta+\mathcal E,\qquad
 0<\delta<2^{-280}B_*,\qquad
 V\le B_*\ \Longleftrightarrow\quad
 \mathcal E\le B_*-\delta.                            \tag{3}
\]

Writing M=sum_z N(z)^2, the same sufficient energy test is

\[
 M\le\frac{C^2}{D}+B_*,                               \tag{4}
\]

or, equivalently, sum_(r=4)^67 w_r K_r <= C^2/D+B_*-C.
The raw collision allowance above its uniform baseline satisfies

\[
 \frac{5889972}{10^{12}}<\frac{B_*}{C^2/D}
                      <\frac{5889973}{10^{12}}.        \tag{5}
\]

The bulk-only relative allowance (B_*-delta)/(C^2/D-L) lies in
this same interval. Thus about 5.89 parts per million of positive
weighted collision excess is allowed. This is an exact required
scale, **not an estimate of the actual excess**.

If (3) is proved, every L102 fiber is at most T for every m.
No bound on mathcal E is proved here. No family exclusion, actual
large fiber, arbitrary-center safety or 955–957 boundary improvement
follows from this reduction. This is a REPRODUCTION/specialization
of standard finite-group energy and elementary overlap counting,
not a claim of progress beyond the sources checked. The completed
step is EXPLORATION; a separate critical audit remains pending.

## Proof

**Imported identity and applicability.** The prior
[EXPLORE assessment](../drafts/literature/2026-10-20-translated-pole-centered-second-moment.md)
covers precisely this reduction and threshold diagnostic. Import
Tao, [245C Notes 2: The Fourier transform](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/),
2009-04-06, Section 2 Lemma 17, Theorem 21 (finite abelian group
cases) and Corollary 22 (Parseval). The probability-Haar Fourier
coefficient of N at chi is D^(-1)sum_z N(z)overline(chi(z)).
Its magnitude is |W_chi|/D since N is real and
sum_z N(z)chi(z)=sum_S chi(rho(S)). Parseval therefore gives
D^(-1)sum_z N(z)^2=D^(-2)sum_chi |W_chi|^2.
Multiplication by D gives the first normalization used in (2).
There is no reproof of the imported general Fourier theorem.

L102 proves that every factor Z+3-x is a unit: C012a has 3 outside
H. It also proves that G has exactly D elements and supplies the
entire-list dictionary for every m, including extension-field
completeness. No smaller group or constant-in-H hypothesis is used.
Each s-subset has exactly one label, so sum_z N(z)=C and W_1=C.
Expanding the square defining V gives V=sum_z N(z)^2-C^2/D;
removing the principal Fourier term gives the first equality in (2).
All nonprincipal characters, including constant-only ones, remain
in the sum. Empty labels contribute mu^2 and are retained.

**Ordered overlap decomposition.** The integer M=sum_z N(z)^2
counts ordered s-subset pairs (S,U) with equal residues. Write
A=S\U, B=U\S and J=S intersect U. Then |A|=|B|=r,
A and B are disjoint, and J is an (s-r)-subset of H\(A union B).
Since rho(J) is a unit, rho(S)=rho(U) if and only if
rho(A)=rho(B). Conversely, any ordered pair (A,B) counted by K_r
and any such J reconstruct exactly one ordered colliding pair
(S,U)=(A union J,B union J). There are exactly w_r choices for J,
independent of the particular A,B. No symmetry quotient or additional
factor two is appropriate. This proves M=sum_r w_r K_r.

Without the residue equality there are P_r ordered disjoint pairs.
The identical bijection counts all C^2 ordered s-subset pairs, giving
sum_r w_r P_r=C^2. Equivalently, for each r,

\[
 w_rP_r=C\binom sr\binom{n-s}r.                       \tag{6}
\]

Subtracting C^2/D now gives the remaining equalities in (2).
This centering is algebraic: P_r/D is a reference baseline, not an
assertion that equality of residues occurs with probability 1/D.

For clarity, the exact residual collision condition also has a
three-coordinate description. L102's logarithmic unit coordinates
give, for every A,

\[
 c_A=\prod_{x\in A}(3-x),\quad
 u_A=\sum_{x\in A}(3-x)^{-1},\quad
 v_A=-\tfrac12\sum_{x\in A}(3-x)^{-2}.
\]

Thus rho(A)=rho(B) is exactly c_A=c_B, u_A=u_B and v_A=v_B
in E; 2 is invertible. All three conditions must be kept. There is
no transfer from a shifted-subgroup product-quadruple estimate.

**All small difference classes.** The empty pair is the unique
r=0 pair, giving K_0=1 and w_0=C. For 1<=r<=3, equality of
residues implies that g_A-g_B is divisible by (X-3)^3. The monic
leading terms cancel, so its degree is at most r-1<=2 unless it
is zero. Hence it is zero. Equality of the monic root products
implies A=B; disjointness then contradicts r>0. This includes all
r=1,2,3 cases without division by a root difference. For r>=4,
the exact equivalent condition is g_A-g_B=(X-3)^3 h for some
nonzero h of degree at most r-4. No count of such h is supplied.
Substituting the four forced K-values into (2) proves V=delta+mathcal E.

**Threshold and diagnostic.** For each z, the nonnegative square
(N(z)-mu)^2 is at most V. Once mu<T is checked, V<=B_* gives
N(z)<=mu+sqrt(V)<=T. By L102 this excludes precisely this family
as a strict threshold witness for every m; it does not address all
centers. A failure of V<=B_* would only stop this sufficient test,
not prove a fiber larger than T. No such failure is established here.

The exact arithmetic in (1), (3) and (5) uses the stated C,D,T,
not an asymptotic field-size replacement. In particular

\[
 \frac{975213642}{10^9}<\frac\delta C<\frac{975213643}{10^9},
 \qquad
 \frac{169780092}{1000}<\frac{C^2/D}{B_*}
                           <\frac{169780093}{1000}.
\]

These comparisons also show B_*-delta>0 and C^2/D-L>0.
The tiny delta/B_* shows that the forced low-overlap correction
alone does not consume the positive excess budget. It is not a lower
bound on V: mathcal E may have negative contributions. Bulk control,
including cancellations against its uniform baseline, remains essential.
Since M and M-C are integers, the endpoints in (4) can be floored
once; the certificate retains these integer endpoints as well.

**Verification and limits.** Run
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/coefficient-fibers/translated_pole_centered_moment.py`.
The complete certificate is
`scripts/coefficient-fibers/translated-pole-centered-moment-results.json`.
All 13030 checks pass. It reconstructs C by factorials, checks (6)
for all 68 r, sums every overlap weight to C^2, retains the four
forced classes, and checks every displayed threshold inequality by
exact rational/integer arithmetic. The required bulk excess is stored
in full, not replaced by its decimal scale. No K_r for r>=4 is
computed on the actual 1024-point domain.

For a supporting finite check, use H=<9> of order eight in F_17
and the same pole 3 outside H. For every subset size 0 through 8,
the script directly enumerates every ordered subset pair, tests unit
cancellation, reconstructs every overlap histogram from independently
enumerated ordered disjoint pairs, and checks centering over all
D_small=16*17^2 labels including empty ones. The disjoint counts are
(1,0,0,0,0) for r=0,...,4. This test has no nontrivial colliding
small-domain pair, so it cannot validate a bulk estimate. Nor does
it numerically verify the complex Parseval theorem; that theorem is
imported and its normalization is justified above. The general overlap
bijection, rather than this small example, proves (2).

## Mathlib

Full centered translated-pole collision reduction: **not checked**.
Supporting finite-group Parseval, polynomial divisibility, finite-field
and subset-counting coverage: **not checked** in Mathlib; no absence
is inferred. Tao's precisely cited standard results provide the
Fourier input. Pinned ArkLib definitions in foundations/02 are present
and specify the list model, not the specialized energy estimate.
