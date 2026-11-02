# Lemma 680: signed Poisson transfer excludes the full segment-positive action budget

## Hypotheses

Let q>=1 be an integer, n=12q+3, J=n-1 and tau=J/n. Retain
the entire L666 product and its rational continuation:

    x=-d=-5/4, R=11/8, U=R^2=121/64, t_j=j/n,
    B_u(v)=product_(0<=j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=(x/a)*product_(1<=j<n)
             [(x-t_j*u)/(a-t_j*u)]*[(U*u-t_j*a)/(U*u-t_j*x)],
    A_n(a)=mean_u conjugate(psi_n(u))*W_a(u), |a|>tau,
    mean_u F=(1/(2*pi))*integral_(-pi)^pi F(exp(i*phi)) dphi.

Here psi_n is an arbitrary complex L2 function for this normalized
measure. No Fourier restriction, symmetry, parameter zero, finite
polynomial or rational ansatz, displacement vector, or positivity in
an open parameter domain is assumed. Fix any real C and suppose

    ||psi_n||_2<=exp(n/100)*n^C,
    A_n(x)=1,
    Re A_n(x+i*y)>=0 for every real |y|<=b=9/20.             (H)

The quotient notation B_u(x)/B_u(a) means the displayed rational
formula also at removable singularities of the quotient.

## Conclusion

For each fixed C there is N_C such that no action satisfying (H)
exists for any n=12q+3 with n>=N_C. This is uniform over every
complex L2 preimage, including all possible free Fourier modes.

More precisely, set

    h=R-d=1/8, kappa=1412/1745>4/5,
    gamma=94502611/8000000000,
    B=19680067/8000000,
    delta=gamma-1/100=14502611/8000000000>0,
    D_C=21+4*max(C,0), n_C=ceil(128*D_C^2),
    K=exp(B)+(10/11)*exp(1/67).

Any action satisfying (H) with n>=n_C would necessarily satisfy

    kappa <= K*n^(C+3)*exp(-delta*n).                       (1)

The right side tends to zero for each fixed real C. Thus (1) is an
asymptotic contradiction, with no imposed zero or extra sign condition.

This is a local exclusion of the unrestricted segment-positive angular
separator at the specified budget. It strengthens the earlier
degree/pole/domain class exclusions only in this stated sense. It does
not refute RH, disprove the general cone estimate, supply a separator
for a discrete displacement set, or settle the original unit-residue
H, support or Xi realization. The independent conceptual audit in
Section 6 confirms this local result and its scope; no certified
originality or complete RH candidate is claimed.

## Proof

### 1. Imported inputs and the precise new comparison

The invocation-start EXPLORE assessment
`drafts/literature/2026-11-02-full-action-half-plane-poisson-transfer.md`
covers exactly this full-action test. Reuse the primary theorem and
the previously audited local bounds; no literature refresh is needed.

Import S. Axler, P. Bourdon and W. Ramey, *Harmonic Function Theory*,
second edition, Graduate Texts in Mathematics 137, Springer (2001),
Theorem 7.5, printed p.148
([author-hosted text](https://axler.net/HFT.pdf#page=152)). In dimension
two it says that a bounded continuous real function on the closed
upper half-plane, harmonic in the open half-plane, equals its
boundary Poisson integral. At s+i*h, h>0, the kernel is

    h/(pi*((y-s)^2+h^2)).

Theorem 7.3 and its proof (p.147), and Corollary 2.2 and its proof
(p.32), cover boundary continuity and bounded uniqueness in the
assessment. Positivity, unweighted boundary L1 integrability, and an
additional decay hypothesis at infinity are not required. This theorem
is imported, not reproved. Its boundedness hypothesis is verified for
the actual action below, rather than inferred from boundary data.

Use L666 (6) for the complete kernel, L679's independently audited
conditional central mass, and only L678 (1)/(14), the independently
audited auxiliary bound on both complementary rays. The rational ansatz
and zero used in L678's separate exclusion are not inputs here. Verify
L674 Section 2's parameter-circle attenuation explicitly below because
that input had not previously received an independent audit. Neither
its Herglotz conclusion nor its open-domain positivity is used.
The family-specific measure comparison and fixed-C contradiction are
the additional work; the cited harmonic theorem alone does not give them.

### 2. The full action is globally bounded on the required half-plane

For every |a|>tau, the possible parameter poles in the exact W_a are
a=0 and a=t_j*u. The other denominators obey

    |U*u-t_j*x|>=U-t_j*d>=U-d=41/64>0.

On any compact subset of |a|>tau, all parameter denominators and
their derivatives are uniformly controlled for |u|=1. Since
||psi_n||_1<=||psi_n||_2 under the normalized measure, dominated
differentiation of this finite rational kernel proves that A_n is
holomorphic on |a|>tau and continuous on every compact subset there.
In particular this includes a neighborhood of every finite point in
the closed half-plane Re a<=x. Apparent poles of B_u(a) are numerator
zeros of the continued W_a and introduce no additional singularities.

Global boundedness requires a further estimate. Write r=|a|>=d on
this closed half-plane. For t=t_j in [0,1), the nonzero-index factor
V_t in W_a obeys

    |V_t(a,u)|
      <= ((d+t)/(U-t*d))*((U+t*r)/(r-t)).

All denominators are positive. For fixed t,

    d/dr [(U+t*r)/(r-t)]=-(U+t^2)/(r-t)^2<0.

Consequently

    |V_t(a,u)| <= ((d+1)/(U-d))*((U+d)/(d-1))
                 =1809/41<45.

The retained j=0 factor is |x/a|=d/r. Thus, uniformly over the
entire closed half-plane and all angular points,

    |W_a(u)| <= (d/r)*45^(n-1),
    |A_n(a)| <= (d/r)*45^(n-1)*||psi_n||_2.                (2)

For each fixed n and preimage, (2) is a finite global bound. It even
gives decay at infinity, though the imported theorem does not need
that extra property. Uniformity in n of (2) is not being asserted or
used as a quantitative cost estimate.

Define F_n(z)=Re A_n(x+i*z) on Im z>=0. The map z=s+i*t sends
this half-plane to a=x-t+i*s with Re a<=x. Hence F_n is continuous
and bounded on the closed upper half-plane and harmonic inside, as
the real part of a holomorphic function. All hypotheses of the
cited Theorem 7.5 are now satisfied. With

    g_n(y)=Re A_n(x+i*y),

its evaluation at z=i*h, where x-h=-R, gives the exact identity

    Re A_n(-R)=integral_R h*g_n(y)/(pi*(h^2+y^2)) dy.       (3)

The integral is absolutely convergent: g_n is bounded and its
nonnegative kernel has integral one. No sign outside the central
segment, real-valued action, reflection symmetry or limit interchange
is used in (3).

### 3. Verification of the parameter-point attenuation

For |a|=R and |u|=1, expansion using |a|^2=U gives

    R^2*|a-t*u|^2=|U-t*a/u|^2, 0<=t<1.

Both factors are nonzero: |a-t*u|>=R-t>0 and
|U-t*a/u|>=R*(R-t)>0. Therefore |B_u(a)|=1 and
|W_a(u)|=|B_u(x)| on the entire parameter circle.

At x=-d, the squared modulus of a single B factor is

    R^2*(d^2+t^2+2*d*t*c)/(U^2+d^2*t^2+2*U*d*t*c),
    c=Re u in [-1,1].

The derivative of the fraction without R^2 with respect to c is

    2*d*t*(U-d^2)*(U-t^2)
       /(U^2+d^2*t^2+2*U*d*t*c)^2 >=0.

Indeed U>d^2, U>t^2, and the denominator is positive since U>d*t.
Thus the modulus is at most R*(d+t)/(U+d*t). This last expression
has positive t derivative R*(U-d^2)/(U+d*t)^2, so for j>=1
it is at most R*(d+1)/(U+d)=66/67. The j=0 factor is exactly
d/R=10/11. Multiplication and normalized Cauchy--Schwarz prove
precisely the L674 Section 2 estimate needed here:

    |A_n(-R)| <= P_n*||psi_n||_2,
    P_n=(10/11)*(66/67)^(n-1).                            (4)

This verification does not audit or assume L674's separate
positive-real-domain conclusion. It applies to arbitrary complex
preimages, with no assumption on the sign or phase of A_n(-R).

### 4. Actual boundary measures and both signed tails

For n>=n_C, L679 applies with exactly (H). Its normalized mass is

    M_n=(1/(2*pi))*integral_(-theta0)^theta0
                  g_n(d*tan(theta/2)) dtheta >=n^(-3),
    theta0=2*arctan(b/d)=2*arctan(9/25).

The substitution y=d*tan(theta/2) is a smooth increasing bijection
of the entire closed intervals. It gives

    M_n=integral_(-b)^b [d/(pi*(d^2+y^2))]*g_n(y) dy.      (5)

The ratio of the Poisson density in (3) to the density in (5) is

    rho(y)=(h/d)*(d^2+y^2)/(h^2+y^2).

As a function of v=y^2 its derivative is
(h/d)*(h^2-d^2)/(h^2+v)^2<0. Consequently for every |y|<=b,

    rho(y)>=rho(b)
      =(1/10)*(353/200)/(349/1600)=1412/1745=kappa>4/5.

Since g_n>=0 on this closed segment, (5) implies

    integral_(-b)^b h*g_n(y)/(pi*(h^2+y^2)) dy
       >=kappa*M_n>=kappa*n^(-3).                       (6)

Only on the complement is an absolute-value estimate used. L678's
auxiliary ray bound, which has no ansatz or prescribed-zero hypothesis,
and normalized Cauchy--Schwarz give

    |g_n(y)|<=|A_n(x+i*y)|
             <=||psi_n||_2*exp(B-gamma*n), |y|>=b.

The total Poisson measure of the two complementary rays is at most
one. Thus their complete signed contribution is at least
-||psi_n||_2*exp(B-gamma*n). The endpoints cause no omitted sign
case: both estimates hold there and singletons have zero measure.
Combining with (3) and (6), then using (4), yields

    kappa*n^(-3)
      <=Re A_n(-R)+||psi_n||_2*exp(B-gamma*n)
      <=||psi_n||_2*(P_n+exp(B-gamma*n)).                 (7)

In particular the signed complement has been paid on both entire
unbounded rays; there is no implicit positivity extension or discarded
tail. The normalization A_n(x)=1 enters through L679's mass, not
through a Harnack or Herglotz assertion for A_n.

### 5. Rate comparison, quantifiers and scope

The elementary integral inequality log(1+s)>=s/(1+s) for s>=0
gives log(67/66)>=1/67. Set delta_p=1/67-1/100=33/6700.
Then

    delta=14502611/8000000000 <1/500<delta_p,
    exp(n/100)*P_n
       <=(10/11)*exp(1/67)*exp(-delta_p*n)
       <=(10/11)*exp(1/67)*exp(-delta*n).

Applying the budget in (H) to (7) and multiplying by n^3 proves
(1), with the exact K stated in the conclusion. For fixed real C,

    log(K*n^(C+3)*exp(-delta*n))
       =log K+(C+3)*log n-delta*n -> -infinity.

Choose N_C>=n_C beyond an onset where the right side of (1) is
strictly less than kappa for every real n>=N_C. This choice depends
only on C and the displayed constants, never on psi_n. It applies
in particular to every allowed integer n=12q+3 beyond that onset.
No coherent family of preimages, effective numerical onset, or
exchange of n with an integral is required.

The bounded test therefore yields a full-action budget exclusion,
rather than a failure of the Poisson hypotheses or a nondecisive rate.
The obstruction is the combination of polynomial positive central
mass and exponentially small paid point and complete signed tails.
It leaves independently open actions with changed budgets or signs,
separators depending on only discrete displacement nodes, and every
cone/H/support/Xi implication not actually proved above. Historical
class stops remain valid within their original hypotheses.

### 6. Independent conceptual audit — 2 November 2026, step 64

Reused the unchanged EXPLORE assessment in Section 1, including its
inspected primary ABR Theorem 7.5 and bounded uniqueness proof cases.
Read the complete proof above, L666 (6), L674 Sections 1--2, L678's
full auxiliary ray-bound proof and its relevant audit, and L679's
complete mass proof and audit. Independently reconstructed the following
chain; no failed implication or changed bound was found. This is a
REPRODUCTION audit of the existing local obstruction, not another
discovery or a stronger theorem.

**Kernel and representation.** Direct division of the full B product
gives exactly the displayed W, with x/a from j=0. On Re a<=-d,
|a-t*u|>=|a|-t>=d-1>0 and |U*u-t*x|>=U-d=41/64.
For r=|a|, the factor (U+t*r)/(r-t) decreases in r, while
(d+t)/(U-t*d) and (U+t*d)/(d-t) increase in t on [0,1].
Their endpoint product is 1809/41<45. Thus (2) bounds the entire
closed half-plane for each fixed n and psi, including infinity.
Compact parameter derivative bounds, multiplied by the integrable
|psi|, justify holomorphy and continuity; L2 normalization supplies
the required L1 domination. These are bounds on the actual full
action, not a presumed Hardy norm or an estimate only on its boundary.

The holomorphic map z -> x+i*z sends Im z>=0 to Re a<=x,
and i*h to -R. Consequently the real harmonic function used in
Section 2 satisfies exactly the bounded closed-half-plane hypotheses
of the cited theorem. Its boundary data are g(y), with no conjugation
or orientation sign change. The Poisson measure has total mass one,
so the bounded signed data are absolutely integrable against it.
Equation (3) is therefore valid without unweighted L1 data, open-domain
positivity, a real preimage, or an interchange of an n limit and an
integral. In particular there is no unaccounted zero-boundary harmonic
term: boundedness is the imported uniqueness hypothesis.

**Point and inherited bounds.** The circle identity in Section 3
follows by expanding both squared moduli using |a|^2=U; neither
denominator vanishes because R>t. Differentiating the displayed
fraction gives its stated nonnegative derivative, and then the
t derivative is positive because U-d^2=21/64>0. This verifies
66/67 for all nonzero indices and exactly 10/11 at j=0.
Normalized Cauchy--Schwarz proves (4) for arbitrary complex psi.
Only this part of L674 is audited here; its separate Herglotz-domain
claim is not used or certified.

L679 has exactly (H), the same normalized theta mass and the same
fixed real C. Its full proof replay preserves the complex Chebyshev
approximation before taking real parts, the integrated error
4*epsilon_n, the Markov neighborhood at an endpoint maximum, and
n>=ceil(128*D_C^2). In particular m<=D_C*n and
epsilon_n<=1/(32*D_C^2*n^2)<=1/(32*m^2), for negative C also.
The corrected identity U-d=41/64 leaves the weaker bound 21/64
used there valid. Thus its mass is conditional on (H), with no
presumption that feasible actions exist.

L678's Sections 2--3 prove (1)/(14) from the full kernel alone;
the later rational ansatz and prescribed zero never enter them.
The contraction case uses monotonicity of
z/(sqrt(d^2+z^2)+t) for z>0; the excess case splits at y^2=U-d^2
and pays all bins with g(h)<0. Both estimates cover either sign of
y and the entire unbounded rays. The last grid bin omits j=n,
and n/200-1<=N_i<=n/200+1 suffices even when n<200.
The negative contraction terms use the lower count bound, and the
positive excess terms use the upper count bound, giving the stated B.

Inspected and replayed the complete exact Fraction script with

    python3 scripts/one-sided-hankel/repeated-pole-rational-cost-check.py

All 200 bins and their directed roundings are checked by its loop.
Read the complete /aggregate, /square_margins, /checks and /failures
values of its saved certificate
`scripts/one-sided-hankel/repeated-pole-rational-cost-check.json`
using `python3 ../scripts/loop/inspect_json.py` with the selected
`--pointer` and `--full`. All eight checks pass, failures is empty,
and the two integer sums are 482257365 and 9744310. Hence the
replayed gamma is 94502611/8000000000, B is 19680067/8000000,
and gamma-1/100 is exactly 14502611/8000000000>0.
The certificate verifies these constants; the preceding analytic
arguments, not a numerical screen, justify their use for every y,u,n.

**Signed transfer and quantifiers.** The exact tangent substitution
in (5) produces d/(pi*(d^2+y^2)), not the Poisson density at -R.
Their ratio decreases in y^2 and its minimum is
(1/10)*(353/200)/(349/1600)=1412/1745>4/5.
Multiplying this lower bound by g is valid precisely on [-b,b],
where g>=0. On both entire complementary rays use |g| and the
Poisson mass bound one. This yields (7) with the correct inequality
direction even when Re A(-R)<0. The point estimate enters as
Re A(-R)<=|A(-R)|; no hidden sign or phase assumption is needed.

Finally log(67/66)>=1/67 leaves delta_p=33/6700>1/500>delta.
The n-1 in (4) produces the retained factor exp(1/67) in K.
After multiplication by n^3 the budget gives exactly (1), including
n^C for every real C. Since (C+3)*log n-delta*n tends to minus
infinity for each fixed C, one onset works for every larger admissible
n and every eligible preimage; no family coherence is required.

The direct mathematical inputs remain L666, the point estimate in
L674, the auxiliary ray estimate in L678, and L679. The DAG records
exactly these inputs. Earlier domain, degree and pole exclusions are
comparisons only; their extra hypotheses have not been imported.
This confirms the full-segment route stop at the stated budget.
Discrete-node signs, changed budgets and all cone/H/support/Xi
bridges remain outside the conclusion.

## Mathlib

Full matching coverage of this kernel-specific exclusion has not been
checked. The reused assessment inspected
[Harmonic.Constructions](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/Harmonic/Constructions.html):
`AnalyticAt.harmonicAt_re` supports taking the real part of an analytic
function. It does not establish the closed-half-plane representation,
the imported L679 mass, the L678 ray constants, or the quantitative
comparison here. The primary citation above supplies the representation.
Unknown full Mathlib availability is not a claim of absence. Section 6
is an independent informal conceptual audit; no formal verification is
claimed.
