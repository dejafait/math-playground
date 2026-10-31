# Degree-six moment-flow calculation

The supplied EXPLORE assessment is reused without changed hypotheses.
The main gap is actual-Xi all-degree mixed positivity. This step tests
only the finite two-atom outward-flow implication stated there.

Plan: derive f_0,f_2,f_4,f_6 exactly from Romik (A.27), set z=t^2,
and count the cubic's positive roots by rational Sturm arithmetic.
Six distinct real t-roots mean three distinct positive z-roots;
zero and multiplicities must be checked separately. Numerical screening
is optional and cannot certify a witness. Record all tested rational
tuples (denominators at most 32), stopping at a certified loss or 10,000.
If initial hyperbolicity never appears, this is sampling evidence only
unless an exact analytic obstruction is established on the full domain.

Downstream: a witness rejects a moment-only preservation inference;
a proof here still leaves actual-theta initial conditions, arbitrary
measures/degrees, and Xi endpoint transfer unresolved. No local lemma
is an essential input to the finite algebra. L055/C055a/L057 and the
source's non-even numerical cubic failure are contrasts, not premises.

Environment: system python3 has no SymPy. Use standard-library rational
arithmetic rather than installing dependencies. Existing notebook edits
are preserved.

## Completed bounded attempt

**EXPLORATION, inconclusive.** The entire permitted 10,000-tuple search
was completed. There were 3,689 initial simple-hyperbolic cases, and no
certified loss at the selected larger radius. This proves neither
preservation nor the absence of a counterexample between sampled radii.
No new lemma or change to the main argument is warranted.

### Imported formula and exact reduction used by the calculation

The normalization is Dan Romik, *Orthogonal polynomial expansions for
the Riemann xi function*, arXiv:1902.06330v3 (5 May 2019),
[equations (A.21), (A.27) and (3.26)](https://arxiv.org/html/1902.06330v3).
The prior assessment already inspected these equations; no new source
claim or reproof of a source theorem is made. The finite recurrence
specialization is necessary to implement this particular test.

Writing z=t^2, the recurrence gives the even basis polynomials

    f_0(t/2) = 1,
    f_2(t/2) = z/2 - 3/4,
    f_4(t/2) = z^2/24 - 17z/24 + 21/32,
    f_6(t/2) = z^3/720 - 25z^2/288 + 2401z/2880 - 77/128.

They are generated successively by
(n+1)g_(n+1)=t g_n-(n+1/2)g_(n-1), g_0=1, g_1=t,
where g_n(t)=f_n(t/2). Set A=m_1 r^2, B=m_2 r^4, C=m_3 r^6.
The implemented cubic P_r(z)=p_r(t) has ascending coefficients

    d = 1 + 3A/4 + 21B/32 + 77C/128,
    c = -A/2 - 17B/24 - 2401C/2880,
    b = B/24 + 25C/288,
    a = -C/720.

On the stated domain m_3>0 implies m_1,m_2>0, so d>0,c<0,b>0,a<0.
Thus P_r(-x)>0 for x>=0: there are no nonpositive real z-roots.
Every positive z-root of multiplicity k supplies the two distinct
t-roots +/-sqrt(z), each of multiplicity k, since t^2-z has two
simple roots and the other factors are nonzero there. Conversely every
real t-root gives a positive z-root. Consequently six distinct real
t-roots are equivalent to three distinct positive roots of P_r.

The main script computes the rational Sturm sequence P,P', followed
by negative remainders, rescaling each remainder by a positive number.
Sturm's standard named theorem gives the positive distinct-root count
as V(0)-V(+infinity). Zero values are omitted; signs at infinity are
leading-coefficient signs. P(0)>0 excludes an endpoint root. The last
nonzero Euclidean remainder has degree zero exactly when gcd(P,P')=1,
which tests simplicity. No approximation or collision division is used.

The independent verifier constructs the four coefficients directly,
without the recurrence or Sturm code, and evaluates the cubic identity

    Delta=b^2 c^2-4ac^3-4b^3 d-27a^2 d^2+18abcd.

For a real cubic of nonzero discriminant, Delta>0 means three distinct
real roots and Delta<0 means one real root. This follows from
Delta=a^4 product_(i<j)(z_i-z_j)^2: three real roots give a positive
product; a conjugate pair gives its negative squared imaginary gap
times a positive modulus fourth power. The strict coefficient signs
above then make every real root positive. This provides an independent
exact check of every stored count and squarefree flag. No recorded
endpoint had Delta=0; no exceptional case is suppressed.

### Selection, complete evidence and nonvacuity

Run from the notebook:

    python3 scripts/pollaczek/moment_flow.py
    python3 scripts/pollaczek/verify_moment_flow.py

The first script uses Python Random with seed 20261030, drawing q in
{0,...,32}/32, sorting independent draws u in {0,...,32}/32 and
v in {1,...,32}/32, taking r_0=a/32 for a in {1,...,31} and r_1=b/32
for b in {a+1,...,32}. Draws are independent before the stated sorting
and radius conditioning. Cases with m_3=0 are rejected before testing.
All tested tuples (including any repetitions) are recorded explicitly;
all reduced denominators are <=32. This is a fixed-seed sample of the
rational grid, not an enumeration of that grid or the continuous domain.

Full evidence is in
`scripts/pollaczek/moment-flow-certificate.json` (all 10,000 tuples,
root counts, simplicity flags, basis, selection and witness field) and
`scripts/pollaczek/moment-flow-verification.json` (independent complete
replay, histogram, selected example and failures). Both programs report
actual and required bounds and the certificate paths. The replay checked
all domains, denominator bounds, counts, simplicity flags and outcome
flags, with no failures and no zero discriminants.

Counts of positive z-roots at (r_0,r_1) were:

| Counts | Tuples |
| --- | ---: |
| (1,1) | 3051 |
| (1,3) | 3260 |
| (3,3) | 3689 |
| (3,1) | 0 |

These correspond to (2,2), (2,6), (6,6), (6,2) real t-roots. They
establish no behavior at radii between a tuple's two endpoints.

For explicit nonvacuity, recorded zero-based tuple 5153 is
(q,u,v,r_0,r_1)=(3/4,5/8,3/4,7/8,1). At r_0 its cubic is

    117817820177/68719476736
    - (977318554037/1546188226560) z
    + (4235548877/154618822656) z^2
    - (90942677/386547056640) z^3.

Its exact signs at z=3,4,27,28,86,87 are respectively +,-,-,+,+,-.
The six complete rational evaluations are saved in the selected-example
object and were read in full. The three disjoint sign-change intervals
(3,4),(27,28),(86,87) give three distinct positive roots by continuity;
a cubic has no more than three. Hence this tuple has six simple real
initial t-roots, independently of Sturm or discriminant implementation.
Both endpoint discriminants are positive, as also recorded exactly.

Mathlib: a matching full preservation theorem was not checked. No claim
of absence is made. Sturm's theorem and elementary cubic algebra are
used as standard mathematical inputs, not as a Lean formalization.

## Continuation and limits

The sample exhausted this step's entire tuple budget. No further
sampling, extra degree, atom count or larger denominator is authorized
by this attempt. One analytic continuation on the unchanged assessed
target is justified: examine the explicit cubic discriminant as a
function of s=r^2, looking for a full-domain positive-to-negative crossing
or an exact exclusion of such crossings. The decisive test is still an
exact real-root loss or full-domain preservation with a nonvacuous
initial case. The present example supplies only the latter's nonvacuity.
The discriminant's sign as a function of the continuous parameters is
uncontrolled. A second unproductive attempt requires route reassessment.

This reuses the supplied assessment's allowance for a universal proof
on exactly the same real parameter domain; no new ready assessment is
written or approved here. Additional literature is unnecessary while
these target and hypotheses remain unchanged. A central creative Xi
proposal remains unjustified: a moment-only invariant and actual-theta
initial hyperbolicity have not been established. The independent gaps
listed at the start remain open. No result beyond the checked sources,
all-degree sign, RH proof/disproof, or complete candidate is claimed.
