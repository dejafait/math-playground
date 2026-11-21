# Lemma 961: complete four-prime diagonal zero exclusion at the lower corner

## Hypotheses

Use L960's coefficient definition at the single exact centre

    t=98/625, x=6000000185827,
    R=x/(4pi)+t/16, N=floor(sqrt(R)),
    c_pol=(1/4)log(sqrt(1+x^2)/(4pi))-1/(2(1+x^2)),
    sigma=1/2+t*c_pol,
    a_n=exp(t(log n)^2/4-sigma log n).

These are definitions; none of L960's remainder, stability, modulus or
collision hypotheses are assumed here. Let P={2,3,5,7}, let Omega(n)
count prime factors with multiplicity, and define the complete slice

    Q(z)=sum_(1<=n<=N, every prime divisor of n in P) a_n z^Omega(n).

The n=1 term is included. This is obtained from L960's complete prime
polynomial by setting its four P coordinates to z and every other
prime coordinate to zero. In particular repeated prime powers and
all smooth composite terms are retained; this is not a multilinear head.

## Conclusion

N=690988. The slice has 1160 terms before collecting equal powers,
degree19 and constant coefficient1. It has no zero in |z|<=1.

More precisely, the Young exterior form defined below admits an exact
real LDL^T factorization whose19 diagonal pivots are all >67/100.
The interval computation certifies this stronger rational threshold;
only positivity is needed for zero exclusion.

This passes one necessary restriction of L960's closed-polydisc premise.
It proves neither that full premise nor its torus modulus bound, any
other slice or centre, physical-character bounds, collision exclusion,
zero-time continuation, or RH. No original root-location theorem or
novelty beyond the sources checked is claimed. The separate step146
independent arithmetic and proof/code audit below passes. This is an
informally checked certificate, not a formally verified program.

## Proof

### Standard input and reciprocal orientation

Import N.J.Young, *Norms of certain rational functions of a matrix and
Schur's criterion for polynomials*, Commentationes Mathematicae
Universitatis Carolinae19(4)(1978),673–688,
[Theorem3, pp.684–685; backward-shift specialization p.686](https://dml.cz/bitstream/handle/10338.dmlcz/105883/CommentatMathUnivCarol_019-1978-4_5.pdf).
If p has degree d>=1 and q(z)=z^d conjugate(p(1/conjugate(z))), and
A is a d-by-d matrix with spectral radius<1 such that I-A* A is
positive semidefinite of rank one, then all zeros of p lie in |z|<1
if and only if q(A)*q(A)-p(A)*p(A) is positive definite. No simple-root
or coprimality hypothesis is added. We use this strict binary criterion,
not a signature-count formula with an unchecked nonconjugacy hypothesis.

Write Q(z)=sum_(j=0)^d c_j z^j with real c_j. Every a_n>0 and c_0=1.
For the degree and leading coefficient certified below, set

    p(z)=Q#(z)=sum_(j=0)^d c_(d-j)z^j, q(z)=Q(z).

Both have degree d and nonzero constant coefficients. The involution
in Young's theorem takes p to q because the coefficients are real.
The zeros of p are the reciprocal conjugates of the zeros of Q,
with multiplicities; there is no zero at zero to lose in that statement.

Take the backward shift S(v_0,...,v_(d-1))=(v_1,...,v_(d-1),0).
It is nilpotent, so its spectral radius is zero. Also
I-S* S=diag(1,0,...,0), positive semidefinite of rank one. Thus

    H=Q(S)^T Q(S)-Q#(S)^T Q#(S)>0

implies that every root of Q# lies strictly inside the disk, equivalently
every root of Q lies strictly outside the closed disk. The orientation
is essential: applying an interior test directly to Q would answer a
different question. This argument also excludes boundary zeros without
an argument-principle boundary test or a separate root count.

### Exact support and included coefficients

Reproduction command, run from the notebook directory:

    python3 scripts/complete-prime-diagonal/certify_144.py

The complete output is `scripts/complete-prime-diagonal/certificate-144.json`.
It retains all1160 integers, their four exponent vectors, Omega values,
logarithm and a_n enclosures, all20 collected coefficient enclosures,
the19-by19 H and lower factor, all19 pivot enclosures, every gate/failure,
and the source/helper SHA256 hashes. It is an exact-integer computation
using Python's standard library, with no external numerical package.

Every box (lo,hi,bits=320) represents [lo/2^320,hi/2^320]. Machin pi,
sqrt and inclusion arithmetic first enclose R. The certificate's two
`natural_index_*_strict` margins enclose

    R-690988^2>0, 690989^2-R>0.

Both have positive lower endpoints. These are strict integer-floor gates
at this exact corner, not the wider rectangle's earlier lower wall.
They prove N=690988 without trusting an approximate square root.

The support recursion successively assigns each exponent of2,3,5,7.
At each level it multiplies the current integer by the selected prime
until the product exceeds N. Because every remaining prime power is
at least1, no omitted continuation can reenter [1,N]. Unique prime
factorization proves injectivity of exponent vectors and completeness
of this recursion. A separate integer-interval sieve divides each
n=1,...,N by2,3,5,7 until indivisible and retains exactly residual1.
The two full sorted lists agree; duplicates and all factorizations
are checked exactly. Their length is1160. The largest Omega is19:
2^19=524288<=N<1048576=2^20, and n>=2^Omega(n). Its positive term
proves the leading coefficient nonzero. The only Omega-zero term is1.

For an exponent vector e, the program encloses
u=sum e_p log p=log n using four included prime logarithms; addition
preserves the exact identity without needing independent errors. It
then encloses a_n=exp(t*u^2/4-sigma*u), checks every lower endpoint
positive and adds its interval to coefficient c_Omega(n). At n=1,
u=0 and the exponential is exactly1. All20 coefficients are included,
and c_0 has equal endpoints1. There is no omitted tail in this finite
polynomial and no uncertain phase or physical character substituted.

### Elementary evaluator and finite errors

Reuse unchanged Box, point_log/logarithm, exponential, root and machin
from `scripts/centred-moment/audit_certificate_142.py`. L960's elementary
inclusion proof supplies the mathematical method. No moment certificate,
quadrature function or moment inequality is used. The directly assessed
standard sources are Daumas–Lester–Munoz, *Verified Real Number
Calculations: A Library for Interval Arithmetic*,
[arXiv:0708.3721v1, III, Propositions9/10/12](https://arxiv.org/html/0708.3721),
and NIST DLMF [3.1(ii–iii)](https://dlmf.nist.gov/3.1#ii),
[4.6.4](https://dlmf.nist.gov/4.6.E4),
[4.2.19](https://dlmf.nist.gov/4.2.E19) and
[4.24.3](https://dlmf.nist.gov/4.24.E3).
These are algorithmic inputs, not formal verification of the Python code.
Independent specialization is warranted because the cited source's
stability band starts at156821/1000000, above this corner156800/1000000;
no ready certificate for this exact slice was located in the assessment.

For clarity the reused auditor's longer series have these explicit bounds.
For m in[1,2], z=(m-1)/(m+1) in[0,1/3], it uses120 summands and

    log m=2 sum_(j=0)^119 z^(2j+1)/(2j+1)+E,
    0<=E<=2z^241/(241(1-z^2)).

Every omitted denominator is>=241, proving the bound by a geometric
series. Exact range reduction x=2^k m and included k log2 handle every
positive rational input. Interval logarithms use monotonic endpoints.
For exp, exact halving places v in[0,1/8];96 summands give

    exp v=sum_(j=0)^95 v^j/j!+E,
    0<=E<=(v^96/96!)/(1-v/97).

Successive omitted ratios are<=v/97. The included lower sum is>=1;
repeated squaring and positive reciprocation handle the original
argument and negative arguments. Monotonicity handles interval inputs.
The helper's120 logarithm summands and96 exponential summands match
these bounds, rather than the shorter step140 counts. Machin's identity
uses160 and48 alternating-series terms at1/5 and1/239; consecutive
partial sums enclose each arctangent before the included subtraction.

All additions/negations have exact dyadic endpoints. Products take
the min/max of four endpoint products, with floor/ceiling after division
by2^320; rational constructors and reciprocals round outward exactly.
Division raises on a zero-containing divisor. The positive log inputs,
nonnegative sqrt inputs and positive exp lower bounds are checked by
the helper. Integer isqrt plus an exact square comparison encloses sqrt.
These statements establish inclusion operation by operation, including
the sigma formula, rather than treating displayed decimals as evidence.

### Exterior form and strict positivity certificate

Index matrix entries by0<=i,j<d. Since Q(S) is upper triangular with
entry c_(j-i) for j>=i, the implemented exact formula is

    H_ij=sum_(k=0)^min(i,j)
        (c_(i-k)c_(j-k)-c_(d-i+k)c_(d-j+k)).

In particular the first entry is1-c_d^2, consistent with the exterior
orientation. Interval evaluation encloses every exact real H_ij; it
does not replace Q by its midpoint polynomial. The matrix is symmetric.

Ordinary LDL^T elimination without pivoting uses the exact recursions

    D_j=H_jj-sum_(k<j) L_jk^2 D_k,
    L_ij=(H_ij-sum_(k<j)L_ik D_k L_jk)/D_j (i>j),
    L_jj=1, L_ij=0 (i<j).

Inductively, all earlier exact entries belong to their saved boxes.
The computed box for D_j therefore contains the exact D_j. Its strict
positive lower endpoint makes division legitimate and encloses each
following exact L_ij. The recursion algebraically constructs H=LDL^T;
the unit lower triangular L is invertible. Positive D_j imply
v^T H v=(L^T v)^T D(L^T v)>0 for every nonzero real v, and hence
positive definiteness as a complex Hermitian form as well.

All19 pivots pass. Their common exact rational lower bound is67/100,
verified by the19 integer comparisons100*lo_j>67*2^320. The smallest
lower endpoint occurs at pivot18 (zero-based); its exact value is

    359937399490813010351368583714034366515739341729221205346676966198400136077037846113184278859069
    /533996758980227520598755426542388028650676130589163192486760401955554931445160137505740521734144.

Its decimal display is approximately0.6740441649462156; the rational
inequality supplies the proof. The original strict requirement was>0,
not the stronger67/100 display bound. `failures` is empty. All20
coefficient enclosures, both floor margins and all19 full pivot intervals
were inspected after execution. Young's imported theorem now gives
the claimed closed-disk zero exclusion.

No inference from a sampled root, singular matrix, truncated smooth
head, numerical spectral radius or assumed stability is used. The
code's unused negative-witness branch is not a premise of this result
and has not been tested or independently validated by this successful run.

### Independent complete-certificate audit (step146)

The preexisting assessment is
`drafts/literature/2026-11-10-complete-prime-diagonal-audit-144.md`,
separately approved in step145. This is REPRODUCTION of the cited
strict criterion and elementary inclusion algorithms, not a new
root-location result. Reproduction command:

    python3 scripts/complete-prime-diagonal/audit_146.py

The full result is `scripts/complete-prime-diagonal/audit-146.json`.
The auditor imports neither original arithmetic module. It reconstructs
the exact corner with448-bit dyadic endpoints, a separate implementation
of the included elementary functions, and a different matrix elimination.
It preserves and reads the entire original certificate. The saved hashes
of `certify_144.py` and its step142 helper match their actual source bytes.

Here is the independent inclusion justification, including the changed
finite constants. A rational interval is rounded outward to denominator
2^448. Addition and negation use exact endpoint integers; multiplication
takes the four exact endpoint products and rounds their extrema outward.
Division instead takes all four exact endpoint quotients and their extrema,
with a zero-containing denominator rejected. Continuity and monotonicity
of the quotient in each coordinate on either zero-free denominator
half-line prove inclusion. This differs from the original multiplication
by an independently rounded reciprocal. Square roots use integer `isqrt`
of the scaled nonnegative endpoint integers and an exact final square
comparison, as above. Arbitrary-precision integers and Fraction are used;
floating values appear only in the final display.

For positive rational q, a bit-length estimate and an exact correction
give q=2^k m, 1<=m<2; log2 additionally permits m=2. With
z=(m-1)/(m+1), use190 summands of the same cited positive logarithm
series. The included terminal power is z^381 and the omitted tail lies in

    [0, 2z^381/(381(1-z^2))].

The denominator is positive because0<=z<=1/3. Add included k log2;
negative k is handled by ordinary signed interval multiplication.
Monotonic endpoint evaluation extends the construction to intervals.
For exp, exact halving places v in[0,1/4]. The128-term sum through
v^127/127! has nonnegative remainder bounded by

    (v^128/128!)/(1-v/129).

Every later term ratio is at most v/129<1. The partial sum has lower
bound at least1; repeated included squaring, and positive reciprocation
for a negative original argument, prove inclusion. Interval endpoints
are evaluated monotonically. Machin's formula is separately computed
using220 and70 alternating terms at1/5 and1/239; the adjacent exact
rational partial sums enclose each atan. Thus every fresh primitive box
contains the same exact value as its original counterpart. No external
moment, quadrature, approximate root or numerical spectral radius enters.

The auditor scans every integer1,...,690988, repeatedly divides by each
of2,3,5,7, and records the full exponent vector exactly when the residual
is1. Unique prime factorization proves this accepts precisely the smooth
support. Its sorted1160 vectors, integers and total exponents agree with
every original support record. Independently positive floor margins prove
that690988 is the actual cutoff. The2^19 witness and N<2^20 prove degree19.
All1160 fresh log and positive exponential boxes are enclosed in their
stored320-bit boxes. All four prime logs, all four constants, both floor
margins and all20 collected coefficients satisfy the same full-containment
test. In particular c_0=1 exactly and c_19>0. For each comparison the
auditor uses integer inequalities after multiplying the old endpoints by
2^128; it does not compare displayed decimals or midpoint polynomials.

To check the matrix orientation independently, construct the full upper
triangular matrices U_ij=c_(j-i), V_ij=c_(19-j+i) for j>=i, with zeros
below, and literally multiply H=U^T U-V^T V. This is exactly the cited
Young form for p=Q#, q=Q and the upper shift. The shift is nilpotent and
I-S^T S=diag(1,0,...,0); the required rank and spectral-radius hypotheses
hold. Both p and q have degree19 and nonzero constant coefficients, so
reciprocal conjugation loses no zero. The strict criterion excludes the
entire closed disk for Q, including its boundary. No coprimality,
simple-root or singular-signature premise has been imported.

All361 entries of fresh H are enclosed in the stored entries, and symmetry
is checked entrywise. The independent elimination starts with W=H. At
stage j it takes D_j=W_jj and L_ij=W_ij/D_j for i>j, then replaces each
trailing entry by

    W_ik <- W_ik-W_ij W_jk/D_j  (i,k>j).

The pivot row and column are unchanged during that trailing update.
The block identity

    [d b^T; b C] = [1 0; b/d I] diag(d,C-bb^T/d) [1 b^T/d; 0 I]

shows inductively that this Schur-complement procedure constructs the
same exact unique unit-lower LDL^T factorization as the original recursion.
At each stage the interval pivot has positive lower endpoint; hence the
division is legitimate, and inclusion propagates to the next exact Schur
complement. All19 fresh pivot intervals and all361 entries of L lie inside
their original stored boxes. Thus the check covers every pivot, rather than
only a final determinant or an eigenvalue approximation.

All19 fresh pivots and all19 original lower endpoints separately pass the
strict integer comparison against67/100. The fresh minimum is again at
index18, with lower endpoint approximately0.6740441649462156; its full exact
dyadic value is saved, and the original reduced rational printed above is
independently checked against the original minimum endpoint. The complete
original gate-name set (1168 gates) and every success flag are checked.
All7784 audit predicates pass; `failures` is empty. Full fresh support,
term boxes, coefficient boxes, H, L, pivots and individual comparison
records are retained on disk. Both floor margins and all full pivot
intervals were also inspected after execution. These are finite exact
enclosure checks with an informal code audit, not formal verification.

This resolves the previously pending independent audit, not any stronger
polydisc, physical, zero-time or Xi-sign claim. Absent contrary evidence,
an unchanged approval or replay of this successful certificate has no
further mathematical purpose. The unused original negative-witness branch
remains outside this successful-run audit.

## Mathlib

Full matching Young/Schur strict criterion and this exact finite
certificate: unknown in the sources checked; the step143 searches
did not locate a match, which is not evidence of absence. No Lean
formalization is claimed. Standard interval/linear algebra support is
not a substitute for a full matching theorem. No cross-notebook input.
