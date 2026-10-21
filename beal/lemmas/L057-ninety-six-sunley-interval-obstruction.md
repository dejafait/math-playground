# L057 — Uniform obstruction to the bounded Sunley interval certificate

## Hypotheses

Let L96 be exactly the degree-36 number field of L051-L052, and let
D be the absolute discriminant of its maximal integer ring. Those
inputs give

    D0=3^30*11^33 <= D <= Dmax=|d12|^3*|d3|^12,
    d12=-307926804295486824275116956724109113198514489839954427904,
    d3=-41229056.

For real 0<X<=10^6, let I(X) count all nonzero integral ideals of that
maximal ring with norm at most X. Let kappa>0 be the residue of its
Dedekind zeta function at one, and define

    c=I(X)/X,
    E=exp(5101/5) 37^(185/2) D^(1/37) (log D)^36 X^(-2/37),
    U=(e log D/70)^35.

Logarithms are natural. The interval tested is the raw symmetric
Sunley interval [c-E,c+E], without intersecting it with other bounds.

## Conclusion

Uniformly for all the stated D and X,

    E/U > Q=10*2^985*37^92*70^35 > 10^506.

Consequently this interval cannot have positive endpoints and endpoint
ratio (c+E)/(c-E) strictly below two. The necessary ratio bound is
E/U<1/2. This parks only this explicit counting-bound implementation
at the diagnostic cap 10^6; it does not give a lower bound on the
actual counting error, rule out other residue certificates or larger X,
or prove class/unit completeness or emptiness of a Beal branch.

## Proof

Import Sunley's counting estimate from Judith E. Sunley, *On the class
numbers of totally imaginary quadratic extensions of totally real
fields*, Bull. AMS **78** (1972), 74–76, Theorem 2(1), p.75,
[DOI](https://doi.org/10.1090/S0002-9904-1972-12859-3),
[original announcement mirror](https://scispace.com/pdf/on-the-class-numbers-of-totally-imaginary-quadratic-8849my12mw.pdf).
For its explicit all-X scope use Garcia–Lee, *Unconditional explicit
Mertens' theorems for number fields and Dedekind zeta residue bounds*,
Ramanujan J. **57** (2022), 1169–1191,
[arXiv:2007.10313v4, March 12, 2021](https://arxiv.org/pdf/2007.10313v4),
Theorem 5 and range discussion, p.5. For every number field of degree
n>=2 and every X>0 this states

    |I(X)-kappa X| <= exp(28.2n+5)(n+1)^(5(n+1)/2)
                      D^(1/(n+1))(log D)^n X^(1-2/(n+1)).

The CM premise of Sunley's separate Theorem 1 is not a premise here.
The announcement does not supply the full proof or explicit range;
Garcia–Lee's inspected restatement supplies the latter. Sunley's
thesis was not independently audited. We import the named result,
without reproof or use of the separately disputed Euler-product tail.
Substitution n=36 and division by positive X give |c-kappa|<=E.

Import Stéphane Louboutin, *Explicit bounds for residues of Dedekind
zeta functions, values of L-functions at s=1, and relative class
numbers*, J. Number Theory **85** (2000), 263–282,
[DOI](https://doi.org/10.1006/jnth.2000.2545),
[author-uploaded published text](https://www.researchgate.net/publication/222631087_Explicit_Bounds_for_Residues_of_Dedekind_Zeta_Functions_Values_of_L-Functions_at_s1_and_Relative_Class_Numbers),
Theorem 1, p.263, with concluding proof cases pp.270–271. For every
number field of degree n>1 it gives

    kappa <= (e log D/(2(n-1)))^(n-1).

Thus kappa<=U for n=36. Neither theorem requires GRH, normality, CM
or a specified signature. They concern the actual maximal-field
discriminant; the order discriminant appears only as L051's upper
bound. Exact field-specific evaluation is not supplied by these sources,
which is the reason for this specialization. No source reproof or
claim of originality is made.

All c,E,U are nonnegative, with E,U strictly positive since D>1.
If c-E>0, multiplication by this positive denominator shows

    (c+E)/(c-E)<2  iff  c+E<2c-2E  iff  c>3E.

Conversely c>3E implies c-E>0 and the ratio inequality. Since
c<=kappa+E, this criterion forces kappa>2E. The inequality kappa<=U
then forces U>2E, or E/U<1/2. This is a necessary condition only;
U is an upper bound, not a residue approximation.

Cancel the displayed positive factors exactly:

    E/U=exp(4926/5) 37^(185/2) 70^35
        D^(1/37) (log D) X^(-2/37).

Here 5101/5-35=4926/5 and the log exponent becomes 36-35=1.
This expression increases with D>1 and decreases with X>0, but the
following direct inequalities already cover the whole domain.

The elementary power series for e gives 2<e<3. For the upper bound,
k!>=2^(k-1) for k>=2, with a strict inequality for k>=3, so
sum_(k>=2) 1/k! < sum_(k>=2) 1/2^(k-1)=1. The first three terms
give the lower bound. The exact integer comparison D0>3^100 therefore
gives D>=D0>e^100 and log D>100. Also D^(1/37)>1,

    exp(4926/5)>e^985>2^985,
    37^(185/2)>37^92.

Finally X<=10^6 implies X^2<=10^12<10^37. Taking positive 37th
roots and reciprocals gives X^(-2/37)>1/10. Multiplying all these
strict positive bounds yields

    E/U > 2^985 * 37^92 * 70^35 * 100/10 = Q.

Exact integer arithmetic verifies Q>10^506, contradicting the
necessary E/U<1/2. This proof uses no rounded logarithm, numerical
grid, ideal count, class relation, actual signature or exact field
discriminant. It applies in particular to the actual discriminant
within L051-L052's certified range.

Reproduce the integer premises with

    python3 scripts/ninety-six-analytic-error/check_counting_error.py

The full certificate is
`scripts/ninety-six-analytic-error/counting-error-certificate.json`.
It records both discriminant endpoints, the cancelled exponents,
Q, and complete positive integer differences for every comparison.
The script checks those premises; the interval and transcendental
implications are proved above. An overlarge certified radius does not
imply a large actual error. A tighter or intersected certificate has
not been tested. No ambient-generation, class/unit/Selmer certificate,
full-disk disjointness or integer exclusion is obtained. The independent
critical audit below confirms the specialization without correction.

### Independent critical audit, 2026-10-11

All six complete fields of the original certificate were inspected and
independently checked by

    python3 scripts/ninety-six-analytic-error/audit_counting_error.py

The full evidence is
`scripts/ninety-six-analytic-error/counting-error-audit-certificate.json`.
The audit does not import or run the original producer. Rational
arithmetic starts from 28.2=282/10 and n=36; repeated integer products
independently reconstruct D0, Dmax, Q and every recorded difference.
All six complete fields match, all five differences are positive, and
all 17 checks pass. The two polynomial discriminants and field degree
remain the L051 inputs, rather than new field computations; L052's
audited maximal-discriminant lower bound is the same D0. The upper
endpoint is consistent but is not needed for the lower comparison.

The proof audit separately checks what the integer certificate cannot.
Both imported bounds apply to the maximal ring of the same degree-36
field, with no signature, normality or CM premise. Garcia–Lee's cited
all-X statement includes 0<X<1; division by positive X changes the
counting exponent from 35/37 to -2/37. In E/U the exponential exponent
is 5101/5-35=4926/5, and the logarithm exponent is one. Positivity
permits every cancellation and root comparison. The exact D0>3^100
and elementary e<3 give log D>100 even at D=D0. For every real
0<X<=10^6, X^2<=10^12<10^37 gives X^(-2/37)>1/10,
including the cap and arbitrarily small X. Together with e>2,
4926/5>985, 185/2>92 and D^(1/37)>1, these yield the strict
E/U>Q>10^506 without a numerical sampling premise.

For the interval test the denominator must first be positive.
Under that hypothesis its ratio is below two exactly when c>3E;
conversely c>3E makes the denominator positive. The upper side of
|c-kappa|<=E implies kappa>=c-E>2E, so kappa<=U forces
E/U<1/2. No converse is asserted, and equality at the required threshold
does not meet the strict ratio test. Hence no ideal count consistent
with the imported bounds can give the desired raw interval in the
stated domain. A large certified radius alone makes no assertion about
|c-kappa|. Intersected or tighter intervals, larger X, ambient class
generation and branch emptiness remain outside the conclusion.
No source theorem has been reproved and no originality beyond this
local verification is claimed.

## Mathlib

The full L96-specific obstruction and the cited Sunley and Louboutin
bounds were **not checked** in Mathlib. Unknown coverage is not evidence
of absence. The proof and exact arithmetic certificate provide informal
evidence only; no formal verification is claimed.
