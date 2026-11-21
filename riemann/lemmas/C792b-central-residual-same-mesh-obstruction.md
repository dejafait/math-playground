# Corollary 792b: the matched prefix fails same-mesh preservation

## Hypotheses

Let d>=5 be an integer, Q>1, and q=1/Q. Let T be a real diagonal
operator on polynomials of degree at most d, T(x^j)=c_j x^j, with

c_0=c_1=c_2=c_3=c_4=1,  0<c_5<1.

All later entries are arbitrary real numbers; they may vanish or be
negative. No invertibility, infinite extension or actual-Xi root premise
is assumed. Define

R_d(q;z)=prod_(k=0)^(d-1)(1+q^k z)=sum_(j=0)^d C_j^d(q)z^j,
H_q(z)=T R_d(q;z)=sum_(j=0)^d C_j^d(q)c_j z^j.

For application to the fixed central residual, use C792a's exact
c_j=R_j/F_j through index5. Its conditional prefix conclusion retains
the exact L791 solution, all original parameter/data widths and L792's
strict t_m,t_a,delta signs, S=B R_1, and the inherited L778 analytic,
evaluator and software contracts. Those numerical inputs are not replayed
or strengthened here. The abstract assertion above needs only the
displayed six coefficient conditions.

## Conclusion

H_q does not belong to Lamprecht's closed class bar(N_d(q)) of
nonpositive-rooted, weakly q-separated polynomials. Therefore T cannot
preserve, for every full-degree polynomial with simple positive roots
rho_(i+1)/rho_i>=Q, the property of having only positive roots with that
same lower ratio. This fails even when lower-degree nonzero images are
allowed. The full-degree weak-boundary witness is

P_q(x)=R_d(q;-x),  T P_q(x)=H_q(-x).

There are also strict-input witnesses: for each fixed d,q and T there
is eta in (0,q) such that every r in (q-eta,q) gives

P_r(x)=R_d(r;-x),  rho_(i+1)/rho_i=1/r>Q,
T P_r(x) outside the positive-rooted same-Q output class.

All these images are nonzero. The assertion is uniform as a quantified
statement for all d,Q and all later entries; no uniform numerical eta
or perturbation tolerance is claimed. It does not identify whether an
image loses root reality, positivity, or only the mesh. It does not
exclude positive-root preservation with mesh loss or transfer for the
particular matched-model family. All-degree actual signs remain open.
This is a known-method specialization, separately audited below (step592).

## Proof

**Precise source imports.** Martin Lamprecht, *Suffridge's Convolution
Theorem for Polynomials and Entire Functions Having Only Real Zeros*,
[arXiv:1210.1102v1](https://arxiv.org/html/1210.1102v1), 3 October 2012:
Section2.1, pp.3--5, defines the strict class N_d(q), its closure, and
extremals a R_d(q;b z), a,b real nonzero. Theorem4(b) classifies diagonal
multipliers by this closed q-symbol class. Section7, Theorem31(c),
pp.26--28, sends a nonextremal H in bar(N_d(q)) to
H *_q^d R_d(tau;z) in N_d(tau) for every 0<tau<q<=1.
Section6, Theorem27 and its full proof, pp.21--22, imply strict
log-concavity of its q-normalized coefficients at occupied indices.
The proof of Theorem4, immediately after Lemma32, explicitly combines
these two results. We import them; no convolution theorem is reproved.
The preexisting SPECIALIZE assessment covers their application here.

**Both symbol alternatives.** Suppose H_q belongs to bar(N_d(q)).
If it is extremal, H_q=a R_d(q;b z). All C_j^d(q) are positive,
so coefficient comparison gives c_j=a b^j. At j=0 it gives a=1;
at j=1 it gives b=1. At j=5 it would give c_5=1, a contradiction.
This also excludes the negative dilation extremal, without assuming
anything about the later entries or the degree of H_q.

In the remaining, nonextremal case set tau=q/2, so 0<tau<q<1.
The source's weighted convolution is

(sum C_j^d(q)a_j z^j) *_q^d (sum C_j^d(q)b_j z^j)
    =sum C_j^d(q)a_j b_j z^j.

Since R_d(tau;z) has q-normalized coefficient
C_j^d(tau)/C_j^d(q), Theorem31(c) says exactly that

K_tau(z)=sum C_j^d(tau)c_j z^j belongs to N_d(tau).

Theorem27 applies with ambient degree d and parameter tau, to these
normalized coefficients c_j. Index1 is occupied: c_0 and c_2 are
nonzero, on either side of it. Its required inequality is consequently

c_1^2>c_0 c_2.

Both sides equal1. This contradiction proves H_q not in bar(N_d(q)).
The argument includes degree drops and all possible later signs. In
particular it never replaces a weak inequality by a strict one at the
original parameter q: strictness is obtained by the cited theorem at
tau<q. Applying Theorem27 directly to a closed-class boundary element
would not justify that step.

**Full-degree positive inputs and closure.** Reflection commutes with T
coefficient by coefficient: T(f(-x))=(Tf)(-x). The d roots of P_q are
q^(-k), k=0,...,d-1, so they are positive, simple and have consecutive
ratio Q. Its image has constant coefficient1, and its coefficient of
x^5 is nonzero, so the image is neither zero nor constant even if its
degree drops below d.

To relate the output property to the source closure without assuming a
preserver on lower-degree inputs, consider any real polynomial h with
h(0)=1 and negative roots -t_0,...,-t_(m-1), where
0<t_0<...<t_(m-1) and t_(i+1)/t_i>=Q, m<=d. It factors exactly as
h(z)=prod_(i=0)^(m-1)(1+z/t_i). Replace t_i by
t_i(epsilon)=t_i(1+epsilon)^i for epsilon>0. The consecutive ratios
are now >Q. If m<d, append d-m roots with magnitudes
M,M^2,...,M^(d-m), choosing M sufficiently large that their internal
ratios and the ratio to t_(m-1)(epsilon) exceed Q. The resulting
degree-d product lies in N_d(q). Let epsilon decrease to0 and M
increase to infinity, preserving those inequalities. Coefficientwise
it converges to h: the finite retained factors converge to those of h,
and every appended factor converges to1. For m=0 use just the appended
factors, with limit1. Thus every such h belongs to bar(N_d(q)).
This explicitly permits degree loss in the putative output. Zero roots
cannot occur when h(0)=1; zero polynomials are likewise excluded.

If H_q(-x) had only positive roots with consecutive ratios >=Q,
this argument applied to h=H_q would place H_q in bar(N_d(q)),
contradicting the symbol conclusion. It proves the claimed failure on
P_q without extending the input quantifier to smaller degrees or using
the converse direction of Theorem4(b).

**Strict inputs.** Put H_r(z)=sum C_j^d(r)c_j z^j for 0<r<q.
Each coefficient depends continuously on r, and H_r tends to H_q as
r increases to q. Since bar(N_d(q)) is closed in the finite-dimensional
coefficient space and H_q is outside it, its complement is an open
neighborhood of H_q. Hence some eta in (0,q) satisfies
H_r outside bar(N_d(q)) whenever q-eta<r<q. The roots of the
full-degree P_r are r^(-k), with ratios 1/r>Q. Its nonzero image is
H_r(-x), with constant coefficient1. The preceding necessary closure
membership again excludes the prescribed same-Q output property.
No effective eta follows from this topological passage.

Finally C792a provides precisely the abstract prefix for the actual
fixed residual, so the result applies under its inherited premises.
The extremal test inputs here are generally not L791's model. Failure
on them does not alter L792's established particular-image conclusion.
No numerical script, finite sweep, zero-free estimate or RH-equivalent
positivity premise occurs in this proof.

### Separate conceptual audit, 5 November 2026 — step592

The preexisting SPECIALIZE assessment
`drafts/literature/2026-11-05-same-mesh-obstruction-audit-scope.md`
covers this audit. No defect was found in the stated obstruction or
its quantifiers. The following checks establish the previously pending
local verification, without strengthening the source theorem or
replaying C792a's inherited numerical premises.

**Source domain and normalization.** Rechecked the versioned primary
Lamprecht source cited above: Section2.1 definitions/Theorem4(b),
Theorem27 with its complete quadratic-reduction proof, the Section7
weighted-product definition, Theorem31(c) with its parameter-decrease
proof, and the explicit application of 31(c) followed by 27 in the
proof of Theorem4. These results use the ambient space of degree at
most d. Neither 31(c) nor 27 requires a nonzero degree-d coefficient.
Theorem4(b)'s universal-class characterization is background here; the
local full-degree witness proof does not invoke its converse on a
smaller input domain.

At fixed d and q, each C_j^d(q) is positive, so the normalized
coefficient representation is unique even when trailing coefficients
vanish. For an extremal symbol the equations at indices0 and1 force
a=1 and b=1; they exclude b<0 as well as all other dilations. The
index5 equation is then incompatible with 0<c_5<1. A lower-degree
symbol cannot be an extremal of this ambient degree, since a,b are
nonzero and C_d^d(q)>0.

In the nonextremal case, tau=q/2 satisfies every parameter restriction
of 31(c). In the weighted product, multiplication of the normalized
entries gives c_j C_j^d(tau)/C_j^d(q), hence the actual coefficient is
C_j^d(tau)c_j. Thus the c_j are the coefficients to which 27 applies
at parameter tau and ambient degree d, not at the actual output degree.
For index1 its support condition is witnessed by indices0 and2, both
equal to1. The forced strict inequality is exactly 1>1. It is obtained
only after strictification. Arbitrary signs or zeros at later indices
do not affect this contradiction. The constant coefficient remains1,
so no zero-polynomial exception is involved.

**Degree-loss closure.** The original approximation also satisfies the
source's all-pairs separation condition: strict adjacent ratios >Q>1
imply the required inequality for every pair of negative roots. To make
its joint limit explicit, for m>=1 set epsilon_l=1/l and choose
M_l>max{l,Q,Q t_(m-1)(1+1/l)^(m-1)}. Retain the m magnitudes
t_i(1+1/l)^i and append M_l,...,M_l^(d-m) if m<d. The junction
ratio and every appended adjacent ratio exceed Q. All roots are
negative, nonzero and simple. Each retained factor converges to
1+z/t_i, and each appended reciprocal magnitude tends to0.
There are only d factors, so every coefficient converges to that of h
in the fixed space R^(d+1), including the vanishing leading entries.
For m=d no appended factors are needed; for m=0 take M_l>max{l,Q}
and only the appended factors. This verifies all boundary cases of the
necessary closure membership, without assuming continuity of d finite
root locations when some escape to infinity.

Reflection commutes with a real diagonal T. The boundary witness P_q
has exactly d positive simple roots with ratio Q. Its image has
constant coefficient1 and nonzero coefficient of x^5, because d>=5
and c_5>0. Thus any permitted degree drop still leaves a nonzero image
of degree at least5. Were that image positive-rooted with the stated
mesh, its reflection would satisfy precisely the closure construction
just checked, contrary to the symbol conclusion.

**Strict-input quantifiers.** Fix d,q and the entire finite vector of
entries of T before taking a neighborhood. The complement of
bar(N_d(q)) is open in R^(d+1), so it contains a coefficient-norm ball
about H_q. The finite product defining R_d(r;z) makes every coefficient
of H_r continuous at r=q. The inverse image of that ball therefore
contains an interval about q; shrink its radius to eta with 0<eta<q.
Every r in (q-eta,q) then gives the claimed failure, rather than only
a sequence of failing inputs. P_r has degree d and ratios 1/r>Q;
its image still has constant coefficient1 and nonzero fifth coefficient.
This works also when c_d=0, because the neighborhood is taken in the
ambient coefficient space. The quantifiers are
for every d,q,T there exists eta, followed by every such r. They do
not give a common eta for varying d,q,T or varying later entries.

**Scope of the application.** C792a supplies exactly the six-entry
prefix under its unchanged L791/L792/L778 exact-data, full-width,
analytic, evaluator and software qualifications. Those inputs are not
independently revalidated by this audit. The test polynomials need
not be the matched model. No identification of the failure as loss of
reality, positivity or mesh alone is justified. Mesh-losing and
particular-family transfer, all-degree actual signs and RH remain open.
This is verification of the existing known-method specialization, not
a new multiplier theorem or beyond-source sign result. No mathematical
input or DAG edge is added. A repeated audit needs a specific defect
or changed hypothesis.

## Mathlib

Full matching coverage for Lamprecht's q-multiplier theorem and this
specialization is unchecked. Polynomial coefficient operations,
continuity and closure are supporting ingredients; no absence of a
matching theorem or formal verification of this proof is asserted.
