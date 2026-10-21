# Lemma 410: five scalar moments admit a law avoiding the target joint sign

## Hypotheses

Let a,b,beta,kappa be fixed strictly positive finite real constants.
The parameter ell tends to infinity through positive real values.
Only the following five scalar constraints on probability laws of real
pairs (D,B) are imposed:

    E D       = -a ell + o(ell),
    E D^2     =  b ell^4 + o(ell^4),
    E(DB)     =  beta ell^2 + o(ell^2),
    E(DB^2)   =  kappa ell^4 + o(ell^4),
    E |B|^3   = O(ell^(9/4)).                              (1)

The implicit constant in the last constraint must be independent of ell;
all displayed expectations must be absolutely integrable at each ell.
Atom positions and weights may depend on ell.

For the notebook application D is an abstract analogue of normalized
Delta, not of the unnormalized physical discriminant called D in L388.
B analogizes the exact Bcal, and ell=log H. The exact constants supplied
by L388, L393, L405 and L409 are

    c=1/(4pi), S=zeta(5)zeta(3)^2/zeta(6),
    a=S/(240pi^2),
    b=c^4 * 263 Psi/(1425600 zeta(2)),
    kappa=233 c^4 Psi/(4989600 zeta(2)),
    beta=(17 c^3/20160)
          sum_(m,n,k>=1) (mn)^(-2) k^(-3) A_(mn/gcd(mn,k)),
    A_u=u^(-2) sum_(j=1)^u gcd(j,u),
    Psi=sum_(m,n>=1) tau(m)tau(n)(mn)^(-5/2)
        product_(p^e || (m/g)(n/g)) [1+e(p-1)/(p+1)]
        /sqrt((m/g)(n/g)), g=gcd(m,n).                     (2)

Here tau counts positive divisors. These canonical inputs establish
absolute convergence and strict positivity of the constants; b is the
renamed square coefficient from L393, whereas beta is the cubic
coefficient from L409. L406 (1), together with its full-response bound
(7), gives the fifth constraint: |Bcal|^3<=C U^(3/2) and its sharp
average is O(ell^(9/4)). No additional physical relationship, envelope,
first moment of B or sign assumption on B is imposed on the abstract law.

## Conclusion

For every sufficiently large real ell there is a probability law on
exactly two real atoms satisfying all five constraints (1), with the
exact constants (2) in the notebook application, and supported in

    K={(D,B): D<=0 or B>=0}.

Indeed the entire law has B>=0, and

    P(D>0 and B<0)=0,
    E |B|^3=(beta kappa/b) ell^2.                         (3)

Thus the five selected scalar constraints alone cannot imply occurrence
of that joint sign, or strict positivity of a negative-B clipped square
mean E[D B^2 1_(B<0)]. That clipped mean is identically zero for this law.
The statement is about a family of abstract probability laws; it does
not assert realization by actual functions or by the physical jets.
In particular it does not settle the actual clipped mean, any regulator
scale, total L367 margin, common-zero upper count, global mixed
positivity, zero-exclusion range or RH. The separate step-123 critical
audit below validates this selected-information obstruction.

## Proof

This is the bounded mathematical specialization authorized by the prior
SPECIALIZE assessment
`drafts/literature/2026-10-14-cubic-benchmark-moment-obstruction.md`.
The exact construction below was not supplied by an inspected source;
POTENTIALLY_NEW records that limited comparison, not certified originality.

The known conditional atomic reduction is Bayer and Teichmann,
*The proof of Tchakaloff's Theorem*, Proc. Amer. Math. Soc. 134 (2006),
3035–3040, DOI 10.1090/S0002-9939-06-08249-9,
[arXiv:math/0502473v2, Corollary 2, pp. 3–4](https://arxiv.org/pdf/math/0502473v2).
Applied to the six integrable coordinates
(1,D,D^2,DB,DB^2,|B|^3) on the Borel set K, it preserves those
integrals with at most six atoms whenever a feasible law exists. This
result is imported by citation, not reproved or used to assert feasibility.
The present explicit two-atom construction makes that reduction unnecessary
for the existence proof. No duality or compact moment theorem is assumed.

Put

    q=beta^2/kappa,
    ell_0=max(1,(2q^2/b)^(1/4)),
    p=p_ell=q^2/(b ell^4).                               (4)

For every ell>=ell_0, 0<p<=1/2. Assign probability p to

    (D_+,B_+)=(b ell^4/q, (kappa/beta) ell^2),

and probability 1-p to

    (D_-,B_-)=(-(a ell+q)/(1-p), 0).                      (5)

The weights are strictly positive and sum exactly to one. Both atoms
are finite at every such ell and distinct, since D_+>0>D_-.
All coordinates in (1) are therefore absolutely integrable. Their
support lies in B>=0, a subset of K, so the joint event in (3) is empty.

First, pD_+=q and (1-p)D_-=-(a ell+q), giving exactly

    E D=-a ell.                                         (6)

For the second moment, the two contributions are

    pD_+^2=b ell^4,
    (1-p)D_-^2=(a ell+q)^2/(1-p).

Since ell>=1 and 1-p>=1/2,

    0<=E D^2-b ell^4
      =(a ell+q)^2/(1-p)
      <=2(a+q)^2 ell^2.                                 (7)

The remainder divided by ell^4 is at most
2(a+q)^2/ell^2, which tends to zero. This proves the second
constraint with its specified b, without approximating that constant.

The negative atom has B_-=0, so it contributes nothing to either mixed
moment or the third absolute B moment. At the positive atom,

    E(DB)=pD_+ B_+
          =q (kappa/beta) ell^2=beta ell^2,

    E(DB^2)=pD_+ B_+^2
            =q (kappa/beta)^2 ell^4=kappa ell^4.          (8)

Finally B_+ is positive and

    E |B|^3=p B_+^3
      =[q^2/(b ell^4)] (kappa/beta)^3 ell^6
      =(beta kappa/b) ell^2
      <=(beta kappa/b) ell^(9/4).                        (9)

The last inequality uses ell>=1, and its constant is finite and
independent of ell. Equations (6)–(9) verify every requirement in (1)
for all ell>=ell_0, not merely for a sequence of parameters. Three
mixed/first-moment remainders vanish exactly; (7) supplies the complete
nonzero remainder. Because B never is negative, the clipped mean in
the conclusion is exactly zero.

To specialize, use the positive finite constants (2). L388 and L393
are for the same normalized Delta; L405 uses the square of the same
Bcal, L409 its signed product with Delta, and L406 supplies the third
absolute envelope above. No rescaling of Delta or change from ordinary
jets is being hidden. The construction only copies the five resulting
scalar constraints, and does not copy the additional identities or
pointwise estimates involving U. Rare atoms have D_+ of order ell^4,
B_+ of order ell^2 and probability of order ell^(-4); these are allowed
by exactly the stated scope. Whether further actual-family constraints
exclude such behavior is a separate question. This proves the claimed
moment-only obstruction and no actual-zeta sign assertion.

### Separate critical audit — 2026-10-14, step 123

This RESEARCH / REPRODUCTION proof audit uses the pre-existing SPECIALIZE
assessment `drafts/literature/2026-10-14-two-atom-moment-obstruction-audit.md`.
The construction passes unchanged. This verifies the local obstruction;
it does not establish originality or another zeta-moment theorem.

**Canonical constants and normalization.** L388 (1) gives exactly a in
(2), with Delta=D_physical/(A^4 T^4 L^4). L393 (1) supplies b, including
the factor c^4, 263/1425600 and its full positive Psi. L405 (1) supplies
kappa with c^4, not c^2; since c^4=1/(256 pi^4), its alternative
denominator is 4989600*256=1277337600. L409 (1)--(2) supplies beta
with c^3 and the same gcd argument in A_u. Its stated positive lower
bound and finite upper bound verify beta is strictly positive and finite.
The positive absolutely convergent Psi and real zeta values verify the
same facts for a,b,kappa. No coefficient is being compared under two
different normalizations. All four averages use H^(-1) integral_[H,2H],
which has total mass one, and ell=log H. L406 (1), (7) gives
H^(-1) integral |Bcal|^3 <= C^3 H^(-1) integral U^(3/2)
=O(ell^(9/4)), with an H-independent constant. This checks the precise
fifth envelope, not just a power-three bound for a surrogate B0.

**All-real-parameter construction.** Since q=beta^2/kappa is fixed,
positive and finite, (4) gives a finite ell_0 and 0<p<=1/2 for every
real ell>=ell_0. Thus all denominators q, beta and 1-p in (5) are positive, both
weights are positive, and the two finite atoms are distinct. Every
absolute moment in (1), including the absolute integrals of the signed
coordinates, is a finite two-term sum. No uniform bound on individual
atom coordinates is required or asserted.

**Independent moment check.** The key mass-times-value identity is
pD_+=q. It makes the negative atom cancel the constant q exactly in
E D, while q*kappa/beta=beta and q*(kappa/beta)^2=kappa verify both
mixed coefficients. For the absolute third moment the independent
coefficient cancellation is q^2*kappa^3/(b*beta^3)=beta*kappa/b.
The positive atom contributes exactly b ell^4 to E D^2; the negative
atom contributes the nonnegative remainder (a ell+q)^2/(1-p).
Its ratio to ell^4 is bounded by 2(a+q)^2/ell^2 for every ell>=ell_0.
Thus the first, third and fourth asymptotic errors are zero, the second
is uniformly little-o at its required scale, and the fifth has the single
uniform constant beta*kappa/b because ell^2<=ell^(9/4) for ell>=1.
These are exact checks for every sufficiently large real parameter,
not numerical evidence or separate subsequence limits.

**Support and logical scope.** B_+>0 and B_-=0; the boundary B=0 is
allowed by K and contributes zero to the clipped square. Therefore both
the forbidden event and that square's expectation are exactly zero.
This refutes an implication from only (1), including its exact leading
constants. It does not refute an implication using a first moment of B,
additional joint moments, pointwise jet identities, a stronger envelope
scale, or consistency of dyadic laws for one fixed function.
None of those is assumed here. In particular the law is not asserted to
copy all information in L406: its auxiliary U relations remain outside
the selected scope. Bayer--Teichmann remains a precisely cited conditional
replacement theorem, unnecessary to the construction; its citation is
not being used to claim feasibility or uniform atom locations.

No repair, new direct mathematical input, script or numerical certificate
is needed. The five listed DAG inputs supply exactly the copied scalar
data. Preserve the scalar-only stop, independently of the L394/L399/L400
weight failures and the step-99 missing clipped-sign coverage. A later
target must supply genuinely additional information; the present audit
neither approves nor attempts such an extension.

## Mathlib

Full matching coverage for this finite-atomic support-constrained family
and the measurable-coordinate atomic replacement theorem is **not
checked**; no absence claim is made. The construction uses only finite
sums and real algebra and imports no Mathlib theorem. Supporting
integration or convexity lemmas are not asserted to match the full result.
