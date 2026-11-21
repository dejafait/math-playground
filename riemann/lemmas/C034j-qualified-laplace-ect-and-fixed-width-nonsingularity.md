# Corollary C034j: qualified Laplace ECT and fixed-width nonsingularity

## Hypotheses

Retain C033w's qualified actual probability laws and the complete
hypotheses of C034b and C034i. In particular, the labeled multiset Z+
contains all positive-ordinate nontrivial zeros with every multiplicity,
and z_rho=gamma_rho-i*delta_rho, delta_rho=beta_rho-1/2. It is conjugation
invariant, has no ordinate-zero member, gamma_rho>14, |delta_rho|<1/2,
and N(T)=O(T log(T+2)). Displacement is zero through ordinate100, and
the retained real member r in (14,15) is included. No remaining zero
is assumed real. Width sigma is Gaussian half-variance. Use exactly

    G_sigma(v)=exp(-v^2/(4*sigma))/sqrt(4*pi*sigma),
    p_sigma(x)=(1/2)sum_rho[G_sigma(x-z_rho)+G_sigma(x+z_rho)],
    R_sigma(w)=int_0^infinity
                   (p_sigma(x)-p_sigma(i*w))/(x^2+w^2) dx,
    b_sigma(w)=4*int_0^w t*R_sigma(t) dt
                              +2*pi*int_0^w p_sigma(i*t) dt.

The quotient uses its continuous removable values, and both primitives
vanish at zero. Retain C032m/n's regularity and normalized heat identity
partial_sigma b_sigma(w)=-b_sigma''(w)+b_sigma''(0), on (1/2,3).
Here the primes on b denote the complex argument derivatives.

For j=1,2 use C033w's positive-real identification through C033l/C032q,

    k_j(sigma)=k(j,sigma)=exp(-B_sigma(j))
             =exp(-b_sigma(sqrt(j)))
             =int_[0,infinity) exp(-j*u) dnu_sigma(u),

where sqrt(j)>0 and nu_sigma has zero drift and killing. Retain both
fixed-v1 preprint qualifications, heat positivity and the separate
fixed-j=0,1 heat-error inputs, the qualified reciprocal-square tail
sum_(gamma>100) gamma^-2<1, and the finite-zero qualifications above.
Source-wide validity and the finite-zero data remain unverified here.
For the finite matching interpretation, m is exactly C033w's residual
probability transform, with no altered removed Levy interval or law.

Use C034b/audit1841's real C^2 width regularity and first-prefix sign,
and C034i/audit1870's final-prefix sign. Their sign domain is the closed
interval [1,2]; the larger interval is used only for regularity. No
positive spatial profile, global Sobolev membership, RH or signed-width
realization is assumed.

## Conclusion

The ordered real functions

    u_0(sigma)=1, u_1(sigma)=k_1(sigma), u_2(sigma)=k_2(sigma)

form an extended complete Chebyshev system on [1,2]. In particular,
every nonidentically zero linear combination of all three has at most
two zeros there, counting multiplicity. The real evaluation matrix
with rows at widths 1,3/2,2 and columns (u_0,u_1,u_2),

    M = [ 1  k(1,1)    k(2,1)   ]
        [ 1  k(1,3/2)  k(2,3/2) ]
        [ 1  k(1,2)    k(2,2)   ],                       (1)

is nonsingular.

Consequently the linear system

    M^T a = (1,m(1),m(2))^T                              (2)

has a unique real solution. Its finite signed measure
eta=sum_(i=0)^2 a_i delta_(sigma_i), sigma=(1,3/2,2), has mass one
and matches the two observations. This asserts algebraic solvability
only: the coefficients have not been evaluated, and their total
variation sum_i |a_i| is not proved <=2. No determinant sign, magnitude,
quantitative inverse bound, feasibility in C033w's A_2, full-observation
matching or actual-Xi realization follows here.

This is a local application of a classical theorem, not progress beyond
the inspected ECT theory. It passes application audit1874 below under
the unchanged qualifications; it is not a candidate resolution of RH.

## Proof

### Imported all-prefix theorem and exact scope

The unchanged SPECIALIZE assessment1870, separately approved1871,
and source-notes1838 cover this application. Import the classical
all-prefix Wronskian criterion in Douglas D. Novaes and Joan Torregrosa,
*On extended Chebyshev systems with positive accuracy*, UAB
prepublication13, July2015, printed p2 (definitions and criterion),
Section2 pp5-6 (5)-(9), nonvanishing division-derivation/Rolle case,
[primary PDF](https://mat.uab.cat/dpt/Publ/prep/p13_15.pdf); later
J. Math. Anal. Appl.448(2017),171-186,
[DOI](https://doi.org/10.1016/j.jmaa.2016.10.076).

In the needed direction, real C^r functions u_0,...,u_n on a closed
interval, r>=n, form an ECT system if every initial Wronskian
W(u_0,...,u_j), 0<=j<=n, is nowhere zero on that interval. Thus a
nonidentically zero combination of the first j+1 functions has at most
j zeros, counting multiplicity, including endpoint zeros. We use n=2,
with C^2 regularity on an open neighborhood of the closed interval.
All initial Wronskians are required, not merely the final one. Their
signs need not be positive. No zero-Wronskian extension of the source
is used, and its general division-derivation proof is not reproved.

### Local hypothesis matching

C033w's identification is at the positive real square root for each
observation j. These are exactly the functions of C034b and C034i;
they are not the distinct odd kernel studied elsewhere. C034b proves
that k_1,k_2 are real C^2 functions on (1/2,3), and k_j>0 there by
their real exponential representation. The constant u_0 has the same
regularity. In particular all endpoint derivatives are restrictions
of ordinary derivatives on an open neighborhood.

With rows indexed by width derivative order and the displayed column
order, write W_j=W(u_0,...,u_j). C034b and C034i give at every
sigma in the entire closed interval [1,2],

    W_0=1,
    W_1=k_1'<-k_1*S_4/2<0,
    W_2<-k_1*k_2*(50*S_4*S_8+S_4^3/5)<0,               (3)
    S_p=sum_rho gamma_rho^(-p), p=4,8.

The input estimates include 0<S_4,S_8<infinity. The final-prefix sign
uses C034i's later result, not C034b's historical unsigned bound.
Both endpoint signs in (3) are established by those inputs at the
endpoints themselves; strictness is not inferred from an interior
limit. No sign on [1/2,3] is needed or asserted. Thus every hypothesis
of the cited sufficient criterion holds with n=r=2, proving the ECT
assertion and its zero bound on [1,2].

### Coefficient independence and the evaluation matrix

For clarity, a nonzero coefficient vector cannot produce the zero
function. If f=c_0 u_0+c_1 u_1+c_2 u_2 were identically zero on [1,2],
then at the interior point sigma_*=3/2,

    [ u_0       u_1       u_2      ]
    [ u_0'      u_1'      u_2'     ] (sigma_*) c = 0.
    [ u_0''     u_1''     u_2''    ]

Indeed f,f',f'' vanish there. This matrix has determinant
W_2(sigma_*)!=0 by (3), so c=0. This verifies coefficient independence
without treating an identically zero combination as having finitely
many zeros.

If the square real matrix M in (1) were singular, finite-dimensional
linear algebra would give a real c!=0 with Mc=0. The row convention
means precisely f(1)=f(3/2)=f(2)=0 for that combination f. It is
nonidentically zero by the preceding paragraph and has three distinct
zeros in [1,2]. Each contributes at least one to the zero count, and
both endpoints belong to the source interval. This contradicts the
ECT bound of at most two. Hence M is nonsingular. No value or sign
of its determinant was used.

The transpose M^T is also invertible. Its first row is (1,1,1), and
its next rows are the values of k(1,sigma_i) and k(2,sigma_i).
C033w's m(1),m(2) are finite real numbers. Thus (2) has exactly one
real solution a, and finite atomic integration gives the stated mass
and observation identities. Distinct widths give |eta|([1,2])=
sum_i |a_i|, which is finite but has no bound of 2 from invertibility.
This consequence does not identify eta with an optimizer in C033w.

Only the finite solvability gap is removed. Conditioning, evaluated
entries and coefficients, the variation cap, full observations,
signed height/cancellation and Xi realization remain independent.
The earlier pointwise and unsigned-estimate failures are not erased;
the application uses the materially later audited prefix sign.

### Application audit1874 — 20 November 2026

**Verdict and source scope.** The ECT assertion, nonsingularity of (1)
and the interpretation of (2) pass without repair or enlarged hypotheses.
This audit uses unchanged SPECIALIZE assessment1872, separately approved
1873, and reuses source-notes1838's inspected primary statement and
nonvanishing proof case, cited above. It verifies a classical local
application, not a new general theorem or an unconditional zeta result.
The prior conceptual audits of the analytic estimates are inputs here;
their complete proofs are not re-audited by this finite-dimensional step.

**Exact functions and regularity.** C033w defines its observation kernel
by the transform of nu_sigma with zero drift and killing and identifies
it with exp(-b_sigma(sqrt(s))). At s=1,2 both square roots are positive
real, so these are precisely C034b/i's functions. The residual right-hand
side is the transform of C033w's mu obtained by removing [1,3/2] from
ell_1(t)dt; it is not a different law or a width mixture. As a probability
transform, each m(j) is real and finite. The width sites 1,3/2,2 lie in
the width interval [1,2], independently of that removed Levy interval.

C034b/audit1841 gives real C^2 regularity on the open neighborhood
(1/2,3), including the normalized second-width derivative with its
origin term. Thus restriction gives the real C^r hypothesis r=n=2
in the source; no analyticity in width or third-width derivative is
required. The constant first column is C^2 as well. Reality and strict
positivity of each k_j follow from the real exponential; no spatial
profile positivity is substituted for a source hypothesis.

**All prefixes and endpoints.** In derivative-row order, the constant
prefix is W_0=1 and expansion along the constant column gives
W_1=k_1' and W_2=k_1'k_2''-k_2'k_1''. These are exactly the orientations
in C034b/audit1841 and C034i/audit1870. The latter inputs give (3),
with positive finite S_4,S_8 and positive k_1,k_2, at every width in
the closed interval. In particular no prefix vanishes at either
endpoint. The larger width neighborhood supplies differentiability,
not an extended sign domain. These are all prefixes required by the
cited sufficient criterion; negative prefix signs are allowed. Its
closed-interval zero bound includes endpoints. No final-prefix-only
criterion or theorem about simple Wronskian zeros is used.

**Independence and the singularity contradiction.** If a combination
with coefficients c vanishes identically on [1,2], its value and first
two ordinary derivatives vanish at the interior point 3/2. Its jet is
the displayed Wronskian matrix times c. Since its determinant is the
nonzero W_2(3/2), c=0. Thus a real nonzero null vector of M would give
a nonidentically zero function. The rows of M give its values at
three distinct sites in [1,2], not derivative values or transposed
observations. Each zero has multiplicity at least one, irrespective
of whether some have higher multiplicity. The sites at 1 and 2 count
because the imported interval is closed. Three zeros therefore exceed
the ECT bound of two. This proves nonsingularity and uses neither a
determinant sign nor a numerical estimate of its size.

**Atomic matching and limits.** For a column of atom weights a,
(M^T a)_j=sum_i u_j(sigma_i)a_i, j=0,1,2. Its zeroth component is
sum_i a_i, and the other two are exactly int k(j,sigma) deta(sigma).
Hence invertibility gives one real mass-one solution with the stated
two observations for this exact m. The three atoms are distinct, so
their total variation is sum_i |a_i|. Invertibility proves finiteness
of this sum, but provides no comparison with 2. Neither ECT nor this
linear solve asserts nonnegative weights, feasibility in A_2, a
full-interval match, or a bound on an inverse.

All inherited label, conjugation, multiplicity, ordinate-zero exclusion,
strict strip, gamma>14, counting, through100, retained-zero and tail
qualifications remain. So do heat positivity, the separate fixed-j=0,1
errors, both fixed-v1 source qualifications, zero drift/killing and
Gaussian half-variance. Source-wide and finite-zero validity are not
independently verified. Conditioning, evaluated entries and residual,
weights/TV, full observations, signed height/cancellation and actual-Xi
realization remain open. Stops1839/1843/1847 are not counterexamples
to the later audited sign input, and stop1866 concerns an unchanged
source-review cycle. No stop is deleted or converted into a global ban.
The existing DAG inputs C033w, C034b and C034i suffice; C034g is unused.
No mathematical script, new general theorem proof or formalization is
needed or claimed for this audit.

## Mathlib

Full matching coverage is unchecked and unknown. No Mathlib theorem
is used or asserted absent. Finite-matrix invertibility and transpose
identities are standard supporting inputs, but no specific formal API
or formalization of the closed-interval ECT theorem and this qualified
actual-divisor application has been verified. The result is an informal
classical specialization under the retained source qualifications.
Application audit1874 does not change this coverage status.
