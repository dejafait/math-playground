# Lemma 601: the fixed Jacobi mixed correlation converges but is not tempered

## Hypotheses

Let k(u)=K(|u|) be exactly the positive theta kernel of L019,
with the even real-axis continuation justified in L239. Let Q be
exactly the uncorrected profile defined in L600, in its DLMF elliptic
normalization. For real t consider the ordinary Lebesgue integral

M(t)=integral_R k(s+t)Q(s-t) ds.

There is no endpoint subtraction, symmetrization, regulator or weight
in this definition. Temperedness means that the regular distribution
on compactly supported smooth tests defined by M extends to S'(R).

## Conclusion

The integral is absolutely convergent for every real t, and M is a
real continuous function. Put

A_*=integral_R k(x)exp(-5x/2) dx,     c_*=(12/pi)A_*.

Then 0<A_*<infinity and c_*>0. The full translation-endpoint limits are

lim_(t->+infinity) exp(-5t)M(t)=-c_*,
lim_(t->-infinity) exp(-5t)M(t)=0.

In particular M(t)~ -c_*exp(5t) at plus infinity and
M(t)=o(exp(5t)) at minus infinity. Its regular distribution is not
tempered. This is a rejection of this fixed mixed term as an ordinary
tempered Fourier component, not a sign result for Xi or a rejection
of corrected profiles or identities with compensating terms.

## Proof

**Imported analytic facts and their scope.** Use the named Lebesgue
dominated convergence theorem, in the parameter form recorded in
Ovidiu Costin, OSU 805-12 course notes, Chapter 1, Theorem 1.256
and the following paragraph, printed p. 51 (PDF p. 56),
[course PDF](https://math.osu.edu/~costin/805-12/c1.pdf).
For distributions use Thierry Ramond, *Distributions and Partial
Differential Equations*, 19 January 2015, version 2.06, Definition
5.3.1 and Proposition 5.3.2, pp. 99-100,
[author PDF](https://www.math.u-psud.fr/~ramond/docs/cours/distributionsedp.pdf).
In particular, a necessary bound for a tempered extension is

|<T,phi>|<=C N_p(phi),  phi in C_c^infinity(R),
N_p(phi)=sum_(0<=alpha,beta<=p) sup_x |x^alpha phi^(beta)(x)|,

for some finite C and nonnegative integer p. These standard facts
are imported, not reproved. The prior source comparison is
`drafts/literature/2026-10-31-jacobi-mixed-correlation-admissibility.md`.
Weighted Young's theorem is not needed: the explicit envelope below
checks every shift directly. Tempered convolution is not invoked
with an unverified input.

**Global envelopes from the canonical profiles.** L019 and the even
real-axis identity of L239 give continuity, k(x)>0, and

k(x)<=C_k exp(9|x|/2)exp(-pi exp(2|x|)),  x in R.

Consequently w(x)=k(x)exp(-5x/2) is strictly positive and integrable:
it is bounded above by C_k exp(7|x|)exp(-pi exp(2|x|)), whose two
tails integrate by the substitution y=exp(2|x|). This proves
0<A_*=integral w<infinity.

Define R(u)=exp(5u/2)Q(u). L600 proves smoothness at every finite
u and the complete-series negative-endpoint estimate

R(u)=-12/pi+O(exp(-6u)exp(-pi exp(-2u)))  as u->-infinity.

The remainder tends to zero: with y=exp(-2u) it is O(y^3 exp(-pi y)).
At the positive endpoint the same lemma gives

|R(u)|<=C exp(7u)exp(-pi exp(2u)),  u>=0,

which tends to zero. Continuity on finite intervals and both endpoint
limits therefore supply a finite B_* with

|R(u)|<=B_*,  |Q(u)|<=B_*exp(-5u/2),  for all real u.       (1)

These bounds concern the entire Q, including its transformed zero
mode; no truncation or dropped term occurs.

**Every shift and local domination.** Make the translation x=s+t,
whose Jacobian is one. The absolute integrand obeys

|k(x)Q(x-2t)|<=B_*exp(5t)w(x).                            (2)

For each finite t the right side is integrable. For all |t|<=T it
is at most B_*exp(5T)w(x), a common integrable envelope. For each
x the integrand is continuous in t since Q is continuous. Dominated
convergence on each such compact interval now proves continuity of
M. In particular M is locally integrable and defines a regular
distribution on C_c^infinity(R). Equation (2) also gives

|M(t)|<=B_*A_*exp(5t),  t in R.                           (3)

**Both translation directions.** The exact scaled identity is

exp(-5t)M(t)=integral_R w(x)R(x-2t) dx.                   (4)

For fixed x, x-2t tends to minus infinity as t tends to plus
infinity, and to plus infinity as t tends to minus infinity.
The respective limits of R are -12/pi and zero. In both directions
the integrand in (4) is bounded in absolute value by B_*w(x),
independent of t and integrable on the full real line. Dominated
convergence gives exactly the two endpoint limits in the conclusion.
This proves more than finite-window convergence and retains the
factor 2 in the shifted argument, which produces the exponent 5t.

**Signed averaged mass contradicts temperedness.** Fix a nonnegative,
nonzero phi in C_c^infinity(R), with support contained in [-R_0,R_0].
For b>=0 put phi_b(t)=phi(t-b), and set

J=integral_R exp(5v)phi(v) dv>0.

Changing t=b+v and using the first endpoint limit gives

exp(-5b)<M,phi_b>
 =integral_R exp(5v)[exp(-5(b+v))M(b+v)]phi(v) dv
 -> -c_* J  as b->+infinity.                             (5)

To justify this passage, the square-bracket expression is bounded
by B_*A_* for every b,v by (3), and exp(5v)phi(v) is integrable
with compact support. Thus the named dominated convergence theorem
applies with all hypotheses verified. Equation (5) implies

|<M,phi_b>|>=(c_*J/2)exp(5b)  for all sufficiently large b. (6)

For each fixed integer p>=0, phi_b^(beta)(t)=phi^(beta)(t-b),
and its support lies in [b-R_0,b+R_0]. Hence for 0<=alpha,beta<=p,

sup_t |t^alpha phi_b^(beta)(t)|
 <=(1+b+R_0)^p sup_v |phi^(beta)(v)|.

Summing these finitely many bounds gives
N_p(phi_b)<=C_(p,phi)(1+b)^p. If M had a tempered extension, its
necessary seminorm bound imported above would then make (6)
impossible: exp(5b)/(1+b)^p tends to infinity for every fixed p.
The tests phi_b are compactly supported, so every extension must
agree with their ordinary M integrals. There is no ambiguity from
an attempted conditionally convergent action on Schwartz functions.

The obstruction uses noncancelling signed averaged mass, rather
than pointwise growth alone; it therefore does not confuse rapid
oscillation with non-temperedness. No Fourier identity involving Q
or positivity assumption was used. This is a routine specialization
of the existing endpoint estimates and standard analytic tests,
not a claim of mathematical novelty beyond the sources checked.

**Independent critical audit (2026-10-31).** The complete proof above
and L600's complete endpoint estimates were checked under the separately
approved scope in
`drafts/literature/2026-10-31-l601-mixed-correlation-critical-audit.md`.
No change of hypotheses or repair was needed. This records acceptance
of the specialization, not a new general theorem.

L019's bound at |x| and L239's real-axis evenness give the displayed
global k bound, including x=0. Multiplication by exp(-5x/2) gives
exponent 2x for x>=0 and 7|x| for x<=0, each bounded by 7|x|.
The resulting tail integral is bounded by a constant times
integral_1^infinity y^(5/2)exp(-pi y)dy, with y=exp(2|x|).
Continuity and strict positivity make A_* strictly positive.
L600's negative-endpoint remainder, multiplied by exp(5u/2),
is O(exp(-6u)exp(-pi exp(-2u)))=O(y^3 exp(-pi y)); its
positive-endpoint bound becomes C exp(7u)exp(-pi exp(2u)).
Both tend to zero at their respective endpoints. Together with
finite-interval continuity these justify a single finite B_* on R.

Independently substituting s=x-t gives s-t=x-2t and
Q(x-2t)=exp(-5x/2+5t)R(x-2t), verifying both (2) and (4).
B_*exp(5T)w dominates the absolute unscaled integrand on |t|<=T;
B_*w dominates the scaled integrand for every real t. These are
full-line integrable majorants. The endpoint orientation is reversed
by -2t: R tends to -12/pi as t tends to plus infinity and to zero
as t tends to minus infinity. Thus every-shift convergence,
continuity and both limits use verified domination, not a nonuniform
remainder moved through an integral.

The normalized bump integrand in (5) is dominated by
B_*A_* exp(5v)phi(v) and tends to -c_* exp(5v)phi(v), whose
integral is strictly negative. For any proposed extension bound with
fixed C,p, every translated derivative is supported in
[b-R_0,b+R_0], giving N_p(phi_b)<=C_(p,phi)(1+b)^p.
Equation (6) contradicts that particular bound as b tends to infinity,
for every possible fixed C,p. Every test is compactly supported, so
any extension must have precisely these ordinary integral pairings.
This verifies non-temperedness through signed averaged mass without
an inference from pointwise growth alone.

Only L019, the real-axis part of L239 and L600 enter this argument;
L233 is downstream context. The audit accepts exactly the stated
uncorrected-M stop. No complete identity, corrected-profile property,
independent residual bound or actual-Xi sign is obtained.

## Mathlib

Matching coverage for this fixed mixed correlation and its
non-temperedness has not been checked; availability is unknown.
Supporting dominated convergence and distribution-seminorm results
are imported from the precise analytic sources above. No Mathlib
absence or full formal theorem is claimed.
