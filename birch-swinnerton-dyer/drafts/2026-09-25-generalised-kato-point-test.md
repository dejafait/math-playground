# Generalised Kato classes: rational-point threshold test

Date: 2026-09-25. Saved before the detailed source audit; the reasoning
below is unfinished and asserts no new theorem.

## Gap and intermediate target

The exact target remains rank E(Q) = m(E) for every E/Q. For m(E) = 2,
L004 would apply if two independent rational points and a certified
nonzero degree-two ordinary p-adic coefficient were supplied in its
non-CM, good-ordinary p >= 5 scope. This step tests only the missing
point input in Darmon--Rotger's 2016 construction of generalised Kato
classes. The p-adic coefficient and the universal higher-rank problem
remain separate unresolved steps.

The intermediate target is a proved implication from analytic rank two
to two independent elements of E(Q) tensor Q_p. This would give rank
at least two and, by finite generation, two independent rational points,
even without an explicit coordinate construction. A theorem giving only
classes in a larger Selmer group does not reach this threshold.

## Redundancy and discriminating test

The finite Selmer-data and characteristic-order failures in the existing
attempts preserve upper bounds but lack a marked Mordell--Weil lower
bound. The proposed geometric classes are additional arithmetic data,
so those failures do not rule out testing them. L004 already proves the
matching-bounds implication; another proof of that implication is not
the target here. No previous local audit of the 2016 construction exists.

Read the primary paper's precise theorems and conjectures. Check:
whether m(E) = 2 is an input; whether auxiliary hypotheses are uniform;
whether the output lies in the rational Kummer image; whether it is
proved nonzero; and whether two classes have proved independent images.
Continue direct use for L004 only if the point threshold is attained
without assuming rank two or finite Sha to supply the missing lower
bound. Otherwise record the precise failed implication, retain valid
Selmer conclusions, and choose a concrete test using that distinction.

## Source leads

- Darmon--Rotger, *Elliptic curves of rank two and generalised Kato
  classes*, Research in the Mathematical Sciences 3 (2016), article 27,
  DOI 10.1186/s40687-016-0074-9.
- Later work appears in the initial search, including Castella--Hsieh
  on nonvanishing. No later theorem is imported before checking its
  hypotheses. This turn is a bounded test of the point threshold, not
  an unrestricted literature survey.

## Mid-step finding and refined test

Theorem 3.1 supplies membership in a twisted Selmer group under central
vanishing. Corollary 3.6 supplies two independent twisted Selmer classes
under an additional nonzero triple-product p-adic value. Neither is a
two-rational-point theorem. Conjecture 3.2 contains the analytic/algebraic
rank comparison; Conjecture 3.12 contains Mordell--Weil membership and
the enhanced-regulator formula. These conjectures cannot be premises.

The specific adjoint rank-(2,0) formulas in Section 4.5.3 predict the two
diagonal classes on the same line and the off-diagonal classes zero.
Thus varying the four stabilisations is not a plausible independence
mechanism there, even on the conjectural description.

There is a narrower useful threshold to check before stopping this
import: for W = E(Q) tensor Q_p, the local logarithm W -> Q_p has rank
one whenever W is nonzero. Hence a nonzero vector in its kernel forces
rank E(Q) >= 2. A single nonzero class with zero localization can therefore
suffice if its rational Kummer membership is proved. The Selmer condition
alone leaves the V_p Sha quotient. The intended elementary deduction
will make that missing membership explicit and use completed local
points, not a naive algebraic tensor of E(Q_p).

## Completed assessment

The [source audit](../foundations/06-generalised-kato-scope.md) records
the construction hypotheses and precise published citations. The direct
two-point import fails the stated test; even the conjectural adjoint
formulas give at most one line. This is an informative negative about
that import, not a refutation of BSD or of the construction.

[L005](../lemmas/L005-strict-kummer-rank-two-threshold.md) proves the
alternative threshold and the exact Kummer quotient. It does not prove
that an available class meets the threshold. The rational lower bound
is still missing, as is the cyclotomic coefficient. The result justifies
testing a later nonvanishing theorem for Kummer membership explicitly,
instead of counting stabilisations as independent rational points.
