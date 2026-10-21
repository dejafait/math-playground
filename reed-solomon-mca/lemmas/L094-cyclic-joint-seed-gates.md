# L094 — The unused second gate gives a joint seed restriction

## Hypotheses

Use exactly L091–L093's setting: F=F_(97^20), H the order-sixteen
subgroup of F_97^*, arbitrary bijection h:Z/16Z -> H, and the full
alternating kernel K for blocks {t,t+1,t+4,t+6}. Indices are modulo
sixteen. Use L092's normalization sending h(0),h(7),h(5) to
infinity,0,1. The letters below are transformed labels, not necessarily
members of H:

    c=h(1), d=h(2), e=h(3), g=h(9), j=h(10), k=h(14),
    X=h(8), Y=h(15), m=h(12), n=h(11), z=h(6).

Use precisely L093's j,k,ell,t,u,Q,M,N,O,Z,W,E and rho_0,rho_1.
In particular Y=tX+u, m=M/ell, n=N/O, z=Z/W,
Q=q_2 X^2+q_1 X+q_0 with q_2!=0, and
E mod Q=rho_0+rho_1 X. Every pole, transformed H-membership,
inverse-projectivity and distinctness gate in L092/L093 remains in
force. No actual errors, original affine chart, weights or locators
are assumed. L090–L093 passed their separate critical audits.

## Conclusion

Put

    P=d(Y-X)(d-g)(d-j)(Z-cW)
       +(d-c)(Z-jW)(X-g)X(d-Y).

On every admitted reconstruction, S_0 is equivalent to P(X)=0.
The polynomial P has degree at most five. Set a=-q_1/q_2,
b=-q_0/q_2 and write P=sum_(i=0)^5 p_i X^i, padding zeros.
Its remainder modulo Q is sigma_0+sigma_1 X, where

    sigma_0=p_0+b p_2+ab p_3+(a^2 b+b^2)p_4
                 +(a^3 b+2ab^2)p_5,
    sigma_1=p_1+a p_2+(a^2+b)p_3+(a^3+2ab)p_4
                 +(a^4+3a^2 b+b^2)p_5.

Consequently K!=0 requires, in addition to L093's Delta=0,

    Psi=rho_1 sigma_0-rho_0 sigma_1=0,
    Xi=q_2 sigma_0^2-q_1 sigma_0 sigma_1+q_0 sigma_1^2=0.

All exceptional branches remain:

- If rho_1!=0, the only possible root is -rho_0/rho_1, and this
  gate additionally requires Psi=0. This leaves at most one completion.
- If rho_1=0,rho_0!=0, there is no completion.
- If rho_0=rho_1=0 and sigma_1!=0, the only possible root is
  -sigma_0/sigma_1, and it requires Xi=0. There is at most one completion.
- If rho_0=rho_1=sigma_1=0 but sigma_0!=0, there is no completion.
- If all four residual coefficients vanish, these gates leave L092's
  bound of at most two completions.

These are necessary restrictions, with no subgroup feasibility or
sufficiency assertion. S_0 is independent of the nine previously used
D-gates and S_8 on the enlarged algebraic domain of distinct normalized
labels: the exact diagnostic below satisfies those gates and all finite
reconstruction gates, but fails S_0. This last assertion has explicit
finite-computation dependence. Its witness is over F_(97^13), not the
prescribed F, and is not a transformed H-labeling. Independence or
nonvanishing on actual transformed H seeds is not proved. The uniform
zero-kernel question, actual-error application, arbitrary-family gap
and interval 11/q–16/q remain unchanged. This result passed the separate
step-248 critical audit below.

## Proof

### Scope and exact S_0 specialization

This is the saved unused-gate test on the unchanged EXPLORE target in
`drafts/literature/2026-10-14-cyclic-family-alternating-kernel.md`.
It reuses the existing source comparison and imports no new external
theorem. L091 supplies S_t, L092 supplies Q and unique completion, and
L093 supplies E and its residual. The new calculation is needed to
compare this particular unused gate with those inputs; it is not a
reproof of an external theorem or a claim of certified originality.

At t=0 L091's q,e,z,a are respectively d,X,0,Y. Its first term is
therefore Y(d-X)/(X(d-Y)). In its second term the local b=h(0)
is infinity; the ratio (q-b)/(e-b) is projectively one. The remaining
labels give the exact normalized equation

    Y(d-X)/(X(d-Y))
      +(d-c)(z-j)(X-g)/((d-g)(d-j)(z-c))=1.          (1)

This normalization is legitimate for S_t: its first summand is a
cross ratio, and its second is the product of the cross ratios

    (q-b)(e-f)/((q-f)(e-b)),
    (q-x)(d-k)/((q-k)(d-x)).

The cancellation formula for projective differences used in L092
preserves each factor, including the homogeneous infinity value.
No projective symmetry of H or of the moment matrix is assumed.

Bijectivity makes X,d-Y,d-g,d-j,z-c nonzero, since the corresponding
indices differ; X!=0 compares indices eight and seven. L093 also
retains W!=0. Substitute z=Z/W and clear the nonzero denominator

    X(d-Y)(d-g)(d-j)(Z-cW).

The difference of the first term and one has numerator
Y(d-X)-X(d-Y)=d(Y-X). This yields exactly P above. Thus clearing
is reversible on the admitted domain. Poles and repeated labels
remain rejected rather than being inferred from a cleared equation.

Y is affine and Z,W have degree at most two by L093. The first
summand of P has degree at most three and the second at most five,
so deg P<=5, including all cancellations and degree drops.

### Reduction and every residual branch

Modulo Q, X^2=aX+b. Besides the powers through X^4 in L093,
one more multiplication gives

    X^5=(a^4+3a^2 b+b^2)X+(a^3 b+2ab^2).

Substitution proves both sigma formulas using only q_2!=0. At a
common root of Q,E,P the two linear residuals vanish. Multiplying
them crosswise gives Psi=0 without division by either slope. The
same root substitution as in L093 gives Xi=0: if sigma_1!=0,
substitute -sigma_0/sigma_1 in Q; if sigma_1=0, existence forces
sigma_0=0. This retains the case where P is a multiple of Q.

When rho_1!=0, L093's unique candidate makes the new residual
equal Psi/rho_1, proving the first branch. The remaining branches
follow by solving the sigma equation only after both rho coefficients
vanish. A nonzero constant residual is inconsistent, and two zero
residuals leave the genuine quadratic. L092 makes every admitted
root determine at most one complete labeling. All original label
and remaining-gate tests must still follow; none of Delta,Psi,Xi
is asserted nonzero on the actual subgroup seed domain.

### An exact distinct-label diagnostic separating the gates

For this paragraph only enlarge the seed domain to an algebraic
extension of F_97. Let G be the residue class of T modulo

    f(T)=24+15T+13T^2+48T^3+60T^4+8T^5+80T^6
         +67T^7+51T^8+21T^9+15T^10+T^11+48T^12+T^13.

The complete exact verifier described below checks
T^(97^13)=T mod f and gcd(f,T^97-T)=1. Here is the elementary
field verification needed for this particular diagnostic. In an
algebraic closure, the roots of T^(97^13)-T form a field L: the
Frobenius power respects sums and products, and nonzero roots have
root inverses. The derivative is -1, so L has exactly 97^13 elements.
For any root G of f, the first modular check gives G in L. If its
minimal polynomial has degree d, then F_97[G] has 97^d elements.
Counting L as a vector space over that subfield gives d dividing
thirteen. The gcd check excludes d=1. Thus d=13 and the monic
degree-thirteen f is irreducible. Its quotient is F_(97^13).
This supplies the field check without an additional imported theorem;
it makes no subgroup or kernel assertion.

Set c=2,d=3,e=4,g=G, and use the formulas of L093 for j,k and all
coefficients. Set

    X=50+22G+50G^2+60G^3+67G^4+77G^5+30G^6
       +42G^7+14G^8+85G^9+39G^10+8G^11+43G^12.

Obtain Y,m,n,z from the stated formulas. Complete the last two
labels by D_0 and D_4, explicitly

    h(4)=[Y(z+X-g)-zX]/(Y-g),
    A_4=e+h(4)-j-m, B_4=jm-e h(4),
    C_4=e h(4)(j+m)-jm(e+h(4)),
    h(13)=(-B_4 X-C_4)/(A_4 X+B_4).

These formulas come from the pair triples (Y,infinity),(z,X),(h(4),g)
and (e,h(4)),(j,m),(X,h(13)), respectively. They specify the entire
witness without an omitted choice. The exact calculation finds all
sixteen labels distinct, all denominators nonzero, and

    D_1=D_10=D_15=D_8=D_3=D_2=D_0=D_4=D_6=0,
    S_8 holds, Q(X)=E(X)=0,
    P(X)=43+91G+81G^2+29G^3+68G^4+91G^5+14G^6
          +55G^7+15G^8+24G^9+47G^10+42G^11+63G^12 !=0.

The value of the left side of (1) minus one is

    87+19G+21G^2+78G^3+62G^4+13G^5+4G^6
      +13G^7+9G^8+10G^9+71G^10+26G^11+6G^12 !=0.

These are nonzero because their displayed degree is below thirteen.
In particular S_0 does not follow from those earlier gates even after
finite reconstruction and collision exclusions on this enlarged domain.
The witness does not meet the subgroup hypothesis; G has degree
thirteen over F_97 and does not even lie in F_(97^20). No labeling
or contradiction for the problem's finite subgroup follows.

Reproduction commands, relative to this notebook:

    python3 scripts/cyclic-shared-gates/s0_residual.py
    python3 scripts/cyclic-shared-gates/verify_s0_residual.py

The producer does exact polynomial arithmetic over F_97(G) on the
single symbolic slice c=2,d=3,e=4. It saves all rational coefficients,
both division identities, all labels and gates, and the full witness
in `scripts/cyclic-shared-gates/s0-residual-certificate.json`.
It compares the closed sigma formulas with polynomial long division.
Actual deg P is five, required at most five; both residual degrees
are one, required at most one. The symbolic factorization is a means
of constructing the displayed witness, not a subgroup census.

The independent verifier uses quotient-field multiplication and
Frobenius inversion, importing none of the producer's arithmetic.
It proves the modulus checks, checks all sixteen distinct projective
labels, all 130 saved nonzero gates, and evaluates all nine D-gates
as direct homogeneous three-by-three determinants. It checks S_8
and the failed S_0 directly, evaluates Q,E,P, and verifies the
clearing identity between P and the failed S_0 value. Its complete
replay is `scripts/cyclic-shared-gates/s0-residual-audit.json`;
all checks pass, with zero H-assignments and zero rank tests.
Both programs use Python and the same mathematical gate statements;
this is independent exact arithmetic replay, not a separate critical
audit or formal proof. The input specializations have since passed
their separate audits; the full L094 audit follows.

### Separate critical audit — October 16, 2026, step 248

The pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-16-cyclic-unused-s0-critical-audit.md`
covers exactly this saved-proof audit. No mathematical defect was found.
This validates the existing necessary restriction and enlarged-domain
diagnostic, without proving transformed-H feasibility or a rank bound.
The direct mathematical inputs remain L091/L092/L093. Their audited
gate, projective normalization, reconstruction and denominator claims
are used in exactly their stated scopes; L089/L090 and L010/L087/L088
remain retained through them. No L095 claim is used.

**Standard inputs and specialization.** Reuse Milne,
[*Fields and Galois Theory*](https://www.jmilne.org/math/CourseNotes/FT.pdf),
v5.10, September 2022, Sections 1.6–1.7, printed p. 10, for division
and root bounds over a field, and Propositions 4.20/4.23 and Corollaries
4.21–4.22, printed pp. 53–54, for finite-field structure and subfields.
These apply in characteristic 97. The divisor Q has nonzero leading
coefficient, so polynomial division requires neither distinct roots
nor nonzero q_0. The prime-degree specialization for the displayed f
is as follows: f divides T^(97^13)-T by the modular check, so each
irreducible factor has degree dividing 13 by the cited subfield result.
The gcd check with T^97-T excludes degree one. Every factor thus has
degree thirteen, and deg f=13 forces f itself irreducible. This imports
the standard field theorem and checks its application; the original
field paragraph above is not an additional original theorem.

Specialization of the rational coefficients uses the
[Stacks Project, Proposition 10.9.3, tag 00CP](https://stacks.math.columbia.edu/tag/00CP):
evaluation extends to the localization when the inverted denominators
map to units. Only the displayed denominators and those in the saved
rational coefficients are inverted. No evaluation map on the whole
rational function field is presumed. The precise projective inputs
are retained through the audited L091/L092 reductions; the calculation
below verifies this particular S_0 specialization rather than reprove
their general invariance theorem.

**Index substitution, infinity and poles.** L091 at index zero uses
local (q,e,z,a)=(d,X,0,Y) and (b,x,d,f,k)=(infinity,c,z,g,j).
Its first summand is Y(d-X)/(X(d-Y)). In the second summand,
(q-b)/(e-b) is one in homogeneous coordinates, giving exactly (1).
The two cross ratios written above exhaust its factors and justify
the common projectivity, including its unique infinity at index zero.
This changes coordinates algebraically, not the fixed subgroup.

The denominator factors X,d-Y,d-g,d-j,z-c are differences of
distinct labels (X is compared with the label zero at index seven).
L093 gives W!=0; hence Z-cW=W(z-c)!=0. The actual common denominator
is X(d-Y)(d-g)(d-j)(Z-cW). Subtracting one from the first fraction
gives d(Y-X)/(X(d-Y)); substituting z=Z/W in the second fraction
cancels W. Multiplication therefore gives exactly P, with both its
signs and factors as displayed. Clearing is reversible at every
admitted reconstruction. The first product has degree at most three,
the second at most five, since Y is affine and Z,W have degree at
most two. No numerical slice is used to establish this uniform bound.

**Remainders and all branches.** Multiplying the audited X^4 identity
by X and replacing X^2 by aX+b gives X^5 exactly as displayed.
Applying this to all six coefficients p_0,...,p_5 proves both sigma
formulas. Only q_2!=0 is required, already proved in L092 from beta t.
This retains u=q_0=0, q_1=0, repeated Q roots, every P degree drop,
and every zero residual coefficient.

At a common root, rho_0+rho_1 X=sigma_0+sigma_1 X=0. Subtracting
rho_0 times the second slope from sigma_0 times the first gives
Psi=0 without division. If sigma_1!=0, substitution into Q gives
Xi=0 after multiplying by sigma_1^2. If sigma_1=0, a common root
forces sigma_0=0, again giving Xi=0. L093 supplies Delta by the
same reasoning for rho. In particular, neither slope is assumed
nonzero merely because a quadratic root exists.

For rho_1!=0, the sole candidate is -rho_0/rho_1; its sigma residual
equals Psi/rho_1. If sigma_1=0 in this branch, Psi=0 forces sigma_0=0,
so no constant-residual exception is lost. Delta remains necessary
for this candidate to be a Q root. For rho_1=0,rho_0!=0 there is no
candidate. If both rho coefficients vanish, sigma_1!=0 gives exactly
the candidate -sigma_0/sigma_1 with Xi required; sigma_1=0,sigma_0!=0
gives none; and sigma_0=sigma_1=0 leaves Q unchanged. These exhaust
the stated branches, including both residuals identically zero. In
the last case a nonzero quadratic still has at most two distinct roots,
and L092 gives at most one completion per admitted root in every case.
Delta,Psi,Xi do not replace any finite, membership, collision or unused
gate test and are never claimed sufficient.

**Complete witness verification.** The complete existing verifier was
read and replayed. Its field multiplication reduces modulo the displayed
monic f. Thirteen iterated Frobenius powers and the Euclidean gcd check
are performed before field inversion is used. The latter computes
gcd(f,(T^97-T) mod f), which equals gcd(f,T^97-T). This proves exactly
the irreducibility conditions above, not a probabilistic test.

All sixteen projective labels are distinct: the fifteen finite labels
have different coefficient vectors and none is infinity. This checks
all 120 pairs, including the fifteen pairs involving infinity. The
130 saved nonzero gates comprise ten named algebraic gates, fifteen
finite rational denominators and all 105 finite-label differences.
The replay evaluates every rational numerator and denominator, checks
every saved gate value, and checks every saved reconstructed label.
Direct homogeneous determinants check D_1,D_10,D_15,D_8,D_3,D_2,D_0,
D_4,D_6 with their actual index pairs. It also checks S_8, failed S_0,
the complete Q,E,P evaluations, and the nonzero clearing identity.

An additional bridge reconstructs j,k,t,u and every M,N,O,Z,W,E,P
coefficient directly over the now-certified field from the printed
c=2,d=3,e=4,g=G and the complete printed X. It checks all those
coefficients against the specialized saved certificate, both complete
division identities, and the closed sigma formula. It reconstructs
Y,m,n,z,h(4),h(13) by the displayed formulas and compares all fifteen
finite labels, explicitly checks the seventeen displayed reconstruction
and S_0 denominators, and verifies the exact printed P and S_0-1 vectors.
The ten named gates and every finite-denominator/difference key are
also matched against the complete expected set, not just its size.

Reproduce this complete check with

    python3 scripts/cyclic-shared-gates/audit_s0_residual.py

The full additional evidence is
`scripts/cyclic-shared-gates/s0-critical-audit.json`. It invokes the
existing full verifier, whose complete output remains
`scripts/cyclic-shared-gates/s0-residual-audit.json`. Both original
certificate files are byte-identical to their pre-audit hashes in
`drafts/2026-10-16-cyclic-unused-s0-audit-before.json`. All checks pass;
actual P degree five meets maximum five and residual degree one meets
maximum one. Zero H assignments and zero rank tests were performed.
The additional bridge shares the reviewed verifier's quotient arithmetic
and Python, but not the producer's rational arithmetic. The uniform
proof above is not inferred from this single specialization.

Since the printed nonzero vectors have degree below thirteen, S_0
really fails at this distinct-label witness. Since 13 does not divide
20, the cited subfield theorem also confirms that G is outside the
prescribed F_(97^20); it cannot be a transformed H label, whose
normalizing projectivity is over F_97. Thus only the claimed enlarged
domain implication is refuted. No complete solution, actual H witness,
uniform seed obstruction or rank-27 example follows. ATTEMPTS/033–034
remain stopped, and the argument and direct DAG inputs are unchanged.

## Mathlib

Full matching coverage for these joint cyclic seed restrictions has
not been checked. No absence or formal-verification claim is made.
The moment inputs are the existing L091–L093 statements; the required
normalization, denominator clearing, degree-five reduction and all
zero-residual branches are justified above. The finite-field diagnostic
has the explicit computation and field qualifications just stated.
The separate step-248 audit checks these informal claims; full matching
Mathlib coverage remains not checked, and no formal proof is claimed.
