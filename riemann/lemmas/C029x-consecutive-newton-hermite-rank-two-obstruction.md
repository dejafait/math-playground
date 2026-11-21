# C029x — A nonzero minor of the actual degree-six/seven Newton-form difference

## Hypotheses

Use exactly C029m's full Jensen-weighted family, with all odd
coefficients retained, and C029n's common normalization
S=sin(pi/8)/sqrt(2)>0. Thus, for N=6,7,

    U_N(t)=T_N(t)/S=sum_(k=0)^N w_(N,k) q_k p_k(t),
    w_(N,k)=N!/((N-k)!N^k),  q_k=beta_k/S,
    p_(-1)=0, p_0=1,
    (k+1)p_(k+1)=t p_k-(k+1/2)p_(k-1).

For a complete finite specification, set X=pi, s=positive sqrt(2),
epsilon_j=1,1+s,-1,-1-s for j=0,1,2,3 modulo 4, and

    v_n=-n! sum_(h=0)^n
        4^h(4^(h+1)-1) B_(2h+2) (2X)^(h+1) epsilon_(n-h)
        /((n-h)!(2h+2)!),
    q_k=4k(k-1)v_(k-2)+(8k^2+12k+7)v_k
           +(2k+3)(2k+5)v_(k+2).

Omit the first term for k=0,1. Only v_0,...,v_9 are needed. Specify
B_0=1 and B_j=-(1/(j+1))sum_(h=0)^(j-1)binom(j+1,h)B_h through
j=20, with B_1=-1/2. These are the finite formulas of A. Kuznetsov,
*Expansion of the Riemann Xi Function in Meixner–Pollaczek Polynomials*,
Canad. Math. Bull. 51 (2008), 561–569,
[DOI 10.4153/CMB-2008-055-0](https://doi.org/10.4153/CMB-2008-055-0),
recurrence (2), coefficients (4)/(13), printed pp563/566, and Jensen
weights pp568–569, as inspected in review2001 and C029q's audit2024.
No weighted convergence assertion or upstream reference [9] is used.

After certifying the actual degrees d_6=6,d_7=7, list each U_N's
roots with algebraic multiplicities. Write s_(N,k) for their k-th
power sum, s_(N,0)=d_N, and H_N=(s_(N,i+j))_(0<=i,j<d_N), precisely
the C029l/C029m convention, including repeated and zero roots. Fix

    D_6=H_7-diag(H_6,0)

in ascending monomial coordinates, with zero-padding in the last
row and column. Fix the principal index set {0,1,2} before calculation.
This is neither the derivative Bezoutian of C029q nor its embedding.

## Conclusion

The fixed principal minor M=D_6[{0,1,2},{0,1,2}] satisfies

    -348399239655.059699 <= det(M)
        <= -348399239655.059698 < 0.

All terminating decimals in this file denote exact rationals.
In particular rank(D_6)>=3, so the prescribed rank<=2 ansatz fails
at this pair. No larger rank, full inertia, later-degree obstruction,
eventual-only failure, or result about RH is asserted. This is a
source-gated finite specialization; its fixed-input independent audit
was completed in step2056 below. No certified originality is claimed.

## Proof

### Exact coefficients and permitted denominators

All p_k have rational coefficients, degree k and leading coefficient
1/k! by the displayed recurrence. Reconstruct the v_n,q_k, each
degree's own weights and the monomial coefficients in
Q[X,s]/(s^2-2). The certificate described below compares every one
exactly with C029q's complete coefficient specification. In particular
it does not substitute an undamped polynomial or use N=6 weights at
N=7. It also compares v_0,...,v_8 and q_0,...,q_6 with C029n's
coefficient record, and the Bernoulli recurrence gives B_20=-174611/330.

Use C029n's unchanged, proved 60-place rational enclosures of pi and
sqrt(2), not presumed decimal expansions. Its proof uses a 48-term
arctangent sum at 1/5 and 1/239 with positive remainder less than
v^97/97, the Machin identity with angle branch justified, and positive
square-root endpoints verified by integer squares. The program
recomputes and compares every term and remainder of both sums,
the complete Machin bounds and their containment in the original
interval, and the strict squared sqrt(2) inequalities. C029n's
analytic branch argument is imported, rather than inferred from this
arithmetic replay. The input certificate is pinned to SHA256
361e31b72ad348b17f6c2ac785c20f5ab73e27796025bd724af208543e0feaf7.

For each exact coefficient polynomial in X, enclose a+b*s with the
correct sign of b, then use interval Horner evaluation at the fixed
pi interval. Exact rational endpoint operations give

    [t^6]U_6 in [-0.000001241943,-0.000001241942],
    [t^7]U_7 in [ 0.000000073296, 0.000000073297].

These outward enclosures contain the full intervals, which agree
exactly with C029q's degree certificate. They prove actual degrees
six and seven. Division is only by the corresponding separated
leading intervals and by positive rational constants. A separated
interval [a,b] has reciprocal enclosure [1/b,1/a], since reciprocal
is decreasing on each of the two nonzero half-lines. Multiplication
uses the minimum and maximum of all four endpoint products;
addition uses endpoint sums. Induction through a finite expression
proves containment without assuming independence of repeated inputs.

### Newton identities and the fixed minor

Import the standard Newton identities in Michel Coste,
*An Introduction to Semialgebraic Geometry*, October 2002,
[Section1.4.1, pp17–18, Exercise1.13](https://perso.univ-rennes1.fr/michel.coste/polyens/SAG.pdf),
whose complete relevant scope was inspected in review2001 and reused
in assessment2052. They apply to any nonconstant real polynomial of
actual degree d and count roots with algebraic multiplicity. We need
neither simplicity nor a root-count/inertia theorem, and do not
reprove Newton's theorem.

For U_N=sum_(i=0)^d b_i t^i, set c_0=1 and c_j=b_(d-j)/b_d for
1<=j<=d. Its roots are unchanged by this monic normalization; no
convergence of monic polynomials is asserted. The imported formulas are

    s_0=d,
    s_k=-sum_(j=1)^(k-1)c_j s_(k-j)-k c_k,  1<=k<=d,
    s_k=-sum_(j=1)^d c_j s_(k-j),           k>d.

In particular the first case does not replace k c_k by c_k s_0,
and the second introduces no nonexistent c_k. Exact rational interval
evaluation of these recurrences through k=10 for d=6 and k=12 for
d=7 encloses every required moment. It stores all monic coefficients,
both branch choices, complete moment endpoints and both full Hermite
matrices. Roots are never approximated. Since these are algebraic
identities for their multiplicity-counting sums, arbitrary root
collisions do not change the justification. Reality follows also
from the real coefficient recurrences.

For i,j in {0,1,2}, both indices lie within the unpadded H_6 block,
so M_(i,j)=s_(7,i+j)-s_(6,i+j). In particular M_00=7-6=1 exactly.
The resulting full intervals lie inside this short rational table:

    M = [ 1  b  c ],
        [ b  c  d ]
        [ c  d  e ]

| Entry | Lower | Upper |
| --- | ---: | ---: |
| b | 87.125396 | 87.125397 |
| c | -4307.805192 | -4307.805191 |
| d | 742928.520301 | 742928.520302 |
| e | -57256421.023079 | -57256421.023078 |

These are outward coarsenings after the computation, not new or
sharper transcendental inputs. For a short check using only this
table, the six signed permutation products are, in lexicographic
permutation order,

    ce, -d*d, -b*b*e, b*d*c, c*b*d, -c*c*c.

Applying all four endpoint products at each multiplication and adding
the six signed intervals gives the complete coarse witness

    -348399246479522365753352756777/10^18 <= det(M)
        <= -348399229857130669120730436873/10^18.

Its upper endpoint is less than -348399000000<0, as one exact
integer comparison verifies. All six complete rational product
intervals are saved in the compact witness, and their sum and the
table have been inspected in full. This witness alone certifies
nonzero determinant; no preview of a large rational is proof.

Applying the same six-product formula to the uncoarsened minor gives
the tighter enclosure in the Conclusion. Every full endpoint remains
on disk; complete rational containment comparisons establish that
the short witness encloses it. The proof of the sign already follows
from the small table and coarse rational bound. By the standard
determinantal characterization of matrix rank over R, a nonzero
3-by-3 minor implies rank(D_6)>=3. This elementary linear algebra
criterion is used directly, without a new rank theorem or any
assertion about signs relative to an existing negative subspace.

### Reproduction, scope and remaining gaps

From the active notebook run

    python3 scripts/pollaczek/consecutive_hermite_rank_2054.py

The standard-library-only implementation imports no mathematical
helpers from prior scripts. Its complete certificate is
`scripts/pollaczek/consecutive-hermite-rank-2054.json`. It retains
the exact finite coefficient specification, Bernoulli numbers,
constant enclosures and hashes, both actual-degree checks, all monic
coefficients, s_(6,0),...,s_(6,10), s_(7,0),...,s_(7,12), both full
Hermite interval matrices, padded H_6, the entire D_6 enclosure,
the fixed minor, all six full signed products and their sum, and
the short rational witness. All 28 checks pass with no failures.
Complete coefficient identities are compared programmatically, not
inferred from partial previews. This is reproducible exact arithmetic
evidence and an informal containment proof, not formal verification
or an independent audit of the new script.

The rank-two necessary condition fails in the coordinates fixed
before calculation. No further minor, degree or input precision was
tried. C029q's affine-quotient obstruction and C029p's inertia contrast
remain separate; neither is substituted for this minor's proof.
This result does not stop eventual-only proposals or other embeddings.
Favorable signed evolution, initialization, singular/degree-drop cases,
uniformity and the unproved C029m eventual index bound remain open.
Weighted convergence/upstream[9] and all Xi transfer qualifications
are unused here and unchanged. There is no RH candidate.

### Independent fixed-input audit2056

The separate standard-library implementation
`scripts/pollaczek/consecutive_hermite_audit_2056.py` imports no
mathematical helpers from the original implementation. Run it from
this notebook with

    python3 scripts/pollaczek/consecutive_hermite_audit_2056.py

Its full certificate is
`scripts/pollaczek/consecutive-hermite-audit-2056.json`. All 108 checks
pass, with no failures. This is independent rational arithmetic and
an informal audit, not proof-assistant verification or new mathematics
beyond the original finite result.

The implementation uses dense pairs of rational coefficients for
Q[s][X]. It reconstructs B_0,...,B_20 by reciprocal-series inversion
of (exp(z)-1)/z and checks every displayed Bernoulli recurrence.
It reconstructs all v_0,...,v_9, q_0,...,q_7, p_0,...,p_7, both degrees'
own weights, every Jensen and monomial coefficient, and compares all
of them exactly against the original record and the appropriate
audited C029n/C029q inputs. It verifies their hashes, all 96 arctangent
terms and both remainders, the full Machin interval and its containment,
and both strict square-root endpoint inequalities. C029n's analytic
angle/remainder proof remains an imported input. No precision changed.

Both actual degrees and every separated division are checked before
monic normalization. The original interval expression order is replayed
through all monic coefficients and Newton moments, including s_0=6/7,
both k<=d and k>d cases, and k=10/12 respectively. Every saved endpoint
agrees exactly, not merely within an overlapping alternate enclosure.

For a separate reconstruction import O. Holtz and M. Tyaglov,
*Structured matrices, continued fractions, and root localization of
polynomials*, [arXiv:0912.4703v3](https://arxiv.org/pdf/0912.4703v3),
9 March 2011, Section4.1, (4.1)–(4.4), printed pp66–67.
The real-polynomial, actual-degree and positive-leading hypotheses
hold for the monic polynomial P=U_N/[t^d]U_N; normalization leaves
its roots and logarithmic derivative unchanged. The source's complete
root-factorization case includes positive integer algebraic
multiplicities. No simplicity, nonzero constant coefficient or positive
Hermite matrix is required. Coverage was inspected in review2052 and
rechecked in review2055; no general theorem is reproved here.

Put Q(z)=z^d P(1/z)=1+c_1 z+...+c_d z^d. The cited expansion identifies

    sum_(k>=0) s_k z^k = (d Q(z)-z Q'(z))/Q(z).

For this finite specialization, the audit constructs Q^(-1) modulo
z^(2d-1) as formal polynomials in independent indeterminates
c_1,...,c_d, then multiplies by dQ-zQ'. It retains every formal
coefficient through 2d-2 and verifies that every coefficient of
Q Q^(-1)-1 and Q sum(s_k z^k)-(dQ-zQ') in that range is identically
zero. It also checks the two Newton cases as exact formal identities,
rather than inferring them from numerical compatibility. Q(0)=1
justifies the formal inverse; this finite computation needs no
analytic series interchange or convergence assumption.

Evaluating these formal coefficient polynomials by rational interval
operations gives a second valid enclosure for every moment. Every
alternate interval contains its replay counterpart; they coincide
at degree six, and at degree seven through k=3. Later degree-seven
alternate intervals are strictly wider. Their determinant enclosure
also contains the replay enclosure and has the same displayed outward
six-decimal bounds. These containment comparisons supplement the exact
endpoint replay; they are not offered as validation of tighter
endpoints by overlap alone.

The audit checks every entry, dimension and symmetry of H_6,H_7,
the complete last-row/column padding and D_6, and the unchanged fixed
minor. All six signed raw products, their exact sum and the tight
Conclusion bounds match in full. Independently reconstructed outward
rounding matches the entire coarse table and every coarse signed
product, their sum, its integer-grid enclosure, and all entry/product/
sum containments. The exact positive gap from the coarse upper bound
to -348399000000 is

    229857130669120730436873/10^18 > 0.

The complete compact witness and comparison flags were inspected;
the large raw fractions were compared in full by exact rational
equality, not accepted from previews. Thus the tighter raw claim and
the shorter sign proof both survive. Only rank(D_6)>=3 for this fixed
pair is audited. No additional mathematical dependency, minor, degree,
root approximation or eventual-index claim is introduced; the original
28-check record is preserved unchanged.

## Mathlib

Full matching theorem and supporting Newton-sum/rank coverage not
checked. No absence claim or formalization is made. The proof imports
the named Newton identities and finite source coefficients above;
the content is only this explicitly bounded arithmetic test and its
independent reproduction audit. The logarithmic-derivative input above
does not change the unchecked Mathlib qualification.
