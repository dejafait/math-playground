# Order-two theta bracket: coefficientwise signing stops

Completed step: 2026-11-06-theta-rankin-cohen-coefficient-21.
Outcome: NEGATIVE; exact reproduction/specialization, not a new sign theorem.
Prior gate: [saved SPECIALIZE assessment](../drafts/literature/2026-11-06-theta-rankin-cohen-coefficient-diagnostic.md).

## Hypotheses

Let tau lie in the upper half-plane, q=exp(2 pi i tau), and
Theta(q)=sum_(n in Z) q^(n^2). Assign both factors weight 1/2 and use
Wei Wang, *Shimura lift of Rankin-Cohen brackets of eigenforms and
theta series*, [arXiv:2406.14254v1, 20 June 2024](https://arxiv.org/pdf/2406.14254v1),
Section 1, printed p2, with bracket order w=2:

    [f,g]_w = (2 pi i)^(-w) sum_(j=0)^w (-1)^j
      binom(k+w-1,w-j) binom(l+w-1,j) f^(j) g^(w-j).

Here derivatives are in tau. This definition was inspected in the
reused assessment; no modularity, Shimura or cusp-sign theorem enters.
The generalized binomial has binom(a,2)=a(a-1)/2 and binom(a,1)=a.

The analytic series is NIST [DLMF 20.2.3](https://dlmf.nist.gov/20.2#E3)
at z=0, with the disk of analyticity in Section 20.2(ii). DLMF's
usual nome exp(pi i zeta) agrees with this q when zeta=2 tau.
For real x>0, tau=i x/2 gives q=exp(-pi x) and
Theta(exp(-pi x))=theta(x)=1+2 psi(x), exactly the primitive law
defined in L016 and used in L019. For L019 take x=exp(2u), u>=0.
This identifies the primitive theta function, not L019's differentiated K.
Neither positivity of K nor any reciprocal-logarithm sign is an input.

## Conclusion

For B(q)=[Theta,Theta]_2 in this convention,

    [q]B = 3/2,       [q^2]B = -6.

Thus B fails coefficientwise nonnegativity at q^2, and -B fails it
at q. No nonzero real scalar multiple of B has all coefficients
nonnegative. The required threshold is zero for every coefficient;
each orientation has a strict negative coefficient already here.

## Exact calculation

Put D=q d/dq. The chain rule gives
(2 pi i)^(-j) d^j/dtau^j Theta(q(tau))=D^j Theta(q(tau)).
The binomial factors at j=0,1,2 are respectively 3/8, 9/4, 3/8,
and the middle term carries the minus sign. Consequently

    B = (3/4) Theta D^2 Theta - (9/4)(D Theta)^2.

Termwise application of D through order two is legitimate on every
closed disk |q|<=r<1: for derivative order j<=2 the absolute majorant
sum_(n in Z) |n|^(2j) r^(n^2) is finite (with the constant term
handled separately for j=0). A polynomial times a Gaussian is
summable. Thus the corresponding power series converge normally,
and their products have the usual Cauchy coefficients. In particular
this finite extraction uses no limit at |q|=1.

The only squares below 4 are 0 and 1, so, as analytic germs at zero,

    Theta       = 1 + 2q + O(q^4),
    D Theta     =     2q + O(q^4),
    D^2 Theta   =     2q + O(q^4).

The orders of the remainders follow from their power-series supports,
not differentiation of an unspecified error estimate. Hence

    coeff_q(Theta D^2 Theta)=2,   coeff_q^2(Theta D^2 Theta)=4,
    coeff_q((D Theta)^2)=0,      coeff_q^2((D Theta)^2)=4.

Substitution gives (3/4)*2-(9/4)*0=3/2 and
(3/4)*4-(9/4)*4=3-9=-6, as asserted. The constant theta term is
essential to the q coefficient. Replacing B by -B yields -3/2 and 6.
More generally a positive scalar retains the negative q^2 coefficient,
and a negative scalar makes the q coefficient negative. The zero
multiple supplies no signed arithmetic input.

## WHY IT FAILS

The proposed sufficient mechanism was a single global orientation of
this bracket with nonnegative nome coefficients. The two exact values
exclude that mechanism without increasing the cutoff. Mixed
coefficients do not decide the pointwise sign even on
0<q<=exp(-pi), do not rule out different representations, and do not
refute RH. L030-L032/C032a's actual-Xi all-degree mixed positivity
remains open. A bracket-to-K or transform-logarithm representation,
its boundary terms and normalization, and all-degree extension were
never established. They remain independent gaps, not premises.
There is no technical continuation on this coefficientwise route;
retain this evidence and seek a different independently testable
interface rather than extending the coefficient cutoff or sign audit.

## Mathlib

Full matching coverage of this bracket specialization is unchecked;
unknown availability is not absence. L016 lists supporting theta
results, but no Lean verification or matching bracket theorem is
claimed. This exact finite algebra needs no mathematical script,
numerical certificate or new lemma identifier. PROOF.md and DAG.md
do not change because no input to their argument has changed.
