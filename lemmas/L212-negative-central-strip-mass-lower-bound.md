# Lemma 212: negative central-strip mass lower bound

**Hypotheses.** Use the actual last-block setup and profiles of L198,
with fixed K>0 and h comparable to N^(3/2). Retain the original
cutoff of L188: R=C N^(3/2), where C>0 is fixed and bounds all
admissible displacements. Use L202's box F_N, choosing fixed H0>0
with h/(2πN^(3/2))>=H0 eventually and fixed
0<t<=min(K/4,H0/8,1). All statements are for sufficiently large
real N, with thresholds allowed to depend on these fixed parameters.

**Conclusion.** There are constants c_K,C_K>0 such that the exact
negative ordered central-strip mass satisfies

c_K Nh <= Y_mid^- <= C_K Nh.

In particular Y_mid^-=o(Nh) is false in this setup. This is a
statement about the negative part in the central strip, not the
signed total Y_N, the original quartic contribution, or RH.

**Proof.**

Write L=N^(3/2), q=min(C,1)/2 and W=floor(qL). Since q>0,
for all sufficiently large N this is a positive integer and

(q/2)L <= W <= qL <= min(R,L).                         (1)

The scale lower bound follows from floor(qL)>=qL-1 once qL>=2.
Thus the full-core scale condition of L202 holds with w=q/2.
This explicitly uses the fixed positive cutoff constant in L188;
an unspecified upper estimate R=O(L) alone would not suffice.
No cutoff is enlarged or removed.

L211 supplies a subset T_N of F_N with

#T_N > (3/131072)#F_N
     >= (3/131072)(t/48)^2 N³,                         (2)

whose selected integer m0=floor(sqrt(abcd))+1 is coprime to ab,
whose totient ratio phi(ab)/(ab) is at least exp(-2^25), and whose
full-core window is occupied at the W in (1). The explicit box
cardinality used here is L202's pair bound #F_N>=((t/48)L)^2.

We check all the conditions of L198 with the fixed positive constants

eta=min(q,exp(-2^25)), delta=1/10.

First, L202 places all four ordered integer factors in [N,2N].
Writing u=ab and v=cd, its product interval gives
|v-2N²|<=2tL<=KL. It also gives c/N<=6/5 and d/N>=8/5,
so c/N<=sqrt(2)-delta and d/N>=sqrt(2)+delta eventually.
Second, L199's exact full-core equivalence puts the occupied integer
in M_in, retaining both stationary endpoints, both product-support
endpoints, the asymmetric rho cutoff, and the strict floor-cell
upper correction -1. The coprimality gcd(m0,u)=1 is supplied by
L211, without a density replacement.
Third, let b_cell,t_cell be L191's integer displacement endpoints.
Full-core occupancy means b_cell<=-W and t_cell>=W. Therefore
its exact length satisfies

ell=t_cell-b_cell>=2W>=qL>=eta L.                       (3)

The excluded zero displacement does not change this definition of
ell: L198 uses interval length, not the number of permitted integers.
Finally phi(u)/u>=exp(-2^25)>=eta by construction.

Consequently every quadruple in T_N yields a tuple counted by
C_N(eta,delta). This map is injective because the ordered quadruple
is retained, even when different quadruples have identical products.
Equation (2) therefore proves condition (ii) of L198 with
c1=(3/131072)(t/48)^2>0. Its implication (ii) to (i) proves the
claimed lower bound. L197 proves the matching upper bound.
All choices were fixed before N tends to infinity, and only finitely
many eventual thresholds were combined.

## Qualifications and verification

The extremely small totient threshold is still a fixed positive
constant. No practical effective threshold in N is claimed. This
result completes the counting condition left open in L198; earlier
statements that it was unproved describe the scope of those lemmas.
The exterior signed mass can still cancel the negative strip, and
other arithmetic sectors are not estimated by this proof. No
all-degree positivity or RH conclusion is drawn.

Verification is analytic: the positive lower scale for R, integer
rounding in (1), the exact full-core endpoint implication, all five
counting restrictions, injectivity on ordered tuples, and the fixed
parameter quantifiers. The existing scripts
`python3 scripts/heat/check_full_core_window.py` and
`python3 scripts/heat/check_safe_factor_box.py` check the endpoint
algebra used here on finite cases; they do not verify asymptotic
population claims.
**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
