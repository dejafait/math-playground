# Finite Selmer descent audit, 2026-09-24

## Selection and scope

The starting notebook contains no lemmas, failed attempts, or unfinished local
changes. Changes elsewhere in the repository are outside this step.

The current Clay page links Andrew Wiles's official description:
<https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf>.
Its displayed conjecture on printed page 2 is equality of rational-point rank
and analytic order of vanishing. Remark 1 separately discusses the refined
coefficient formula. The distinction will be retained in the foundations.

The gap is to prove rank equality for every elliptic curve over Q, beyond the
established analytic-rank-zero and analytic-rank-one cases. A possible arithmetic
input is a rank certificate obtained from a finite initial segment of the
p-power Selmer groups. Even such a certificate would still need a theorem
relating it to the analytic order; that later step is unresolved.

Three mechanisms considered for this initial selection are finite Selmer
descent, cyclotomic Iwasawa theory, and constructions of rational points from
analytic derivatives. The first offers an immediate algebraic test. No
Iwasawa comparison or higher-derivative point construction is assumed here.

## Discriminating test

Test the inference that an initial tower behaving like rank two certifies two
rational-point directions. Retain the Kummer exact sequences, the downward
transition maps, rank parity, and even the restriction of an alternating
pairing. Continue a route using only this data if it forces the rank; abandon
that inference if finite paired torsion can give the same observed tower.

The exact standard input is the Kummer sequence in Milne, *Elliptic Curves*,
second edition (2021), Chapter IV, equation (29), printed page 113:
<https://www.jmilne.org/math/Books/EC2.pdf#page=118>.
It gives, with r the rank and T the rational torsion subgroup,

    log_p |Sel_{p^n}(E/Q)|
      = n r + log_p |T[p^n]| + log_p |Sha(E/Q)[p^n]|.

This is already a warning against equating a Selmer upper bound with rank.
Milne IV.5 also discusses higher descents and the divisible-Sha obstruction;
the proposed test must be treated as an explicit audit of known structure,
not as a new general theorem about elliptic curves.

## Construction recorded before verification

For a fixed observation depth N, choose M >= 2N and
A = (Z/p^M Z)^2, with pairing
b((a,b),(c,d)) = (ad-bc)/p^M mod Z. Compare

    rank-two model: S_n = (Z/p^n Z)^2, Sha = 0;
    rank-zero model: S_n = A[p^n], Sha = A.

The candidate isomorphism for n <= N sends (u,v) to
p^(M-n)(u,v). Downward maps should agree with reduction in the first model
and multiplication by p in the second. Restricted pairing values have the
factor p^(M-2n), hence should vanish at all observed levels. Verify
well-definedness, nondegeneracy on A, and compatibility of the transitions.

These are abstract exact-sequence models, not asserted realizations by
elliptic curves. They test a deduction from the named data alone, not the
possibility of computing ranks with additional arithmetic information.

The initial save preceded verification. The construction is now proved in
[L001](../lemmas/L001-finite-selmer-tower-rank-ambiguity.md), with the matched
observations distinguished explicitly from the unobserved rational Kummer
images. Small exact instances pass in
[the check output](../scripts/finite-selmer/check-results.json).
The completed outcome is an informative negative for the data-only
inference. No candidate proof of BSD has been obtained.
