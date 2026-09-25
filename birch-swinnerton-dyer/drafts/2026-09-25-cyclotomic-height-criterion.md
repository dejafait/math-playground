# Cyclotomic height criterion audit, 2026-09-25

## Selection before the source and mathematical checks

Read the shared instructions, local goal and checkpoint, whole PROOF.md,
and DAG.md; inspected the existing changes and retained them. Reopened the
Clay page and its linked Wiles statement. The scope remains the rank/order
assertion, with the leading-coefficient refinement separate.

The main gap remains rank equality at arbitrary analytic order at least
two. The bounded intermediate target is the checkpoint's height test:
under finite Sha[p^infinity], determine whether nondegeneracy of the
cyclotomic p-adic height forces the natural map
X_(T)[T] -> X_(T)/T X_(T) to be an isomorphism. This would remove the
specialization defect in L002 and give a conditional arithmetic input to
a later comparison with complex analytic order. Neither Sha finiteness,
height nondegeneracy, nor that analytic comparison is assumed established.

This tests arithmetic information absent from both previous data-only
attempts. L001's finite tower ambiguity and L002's characteristic-ideal
ambiguity are preserved; neither is repeated as a new result. The
Schneider--Perrin-Riou theorem is a known candidate input, not a claimed
new theorem.

## Discriminating test and saved unfinished reasoning

Check a precise published statement in the good-ordinary setting. The
threshold needed is ord_T(f_X) = rank E(Q), conditional on finite
Sha[p^infinity] and a nonzero regulator. Together with L002 this would
force both nonnegative defects to vanish and hence prove the stated map
is an isomorphism. Check whether the converse requires finite Sha as well.

Continue the height route as a conditional reduction if that exact
criterion is supported, while retaining every unproved arithmetic
hypothesis. If the source gives only an upper bound, an analytic p-adic
BSD conjecture, or a mismatched Selmer group, do not import it as the
needed theorem. Record that distinction and stop that inference.

Initial source discovery found Stein--Wuthrich, Theorem 6.1, and a modern
restatement of Schneider--Perrin-Riou. Their exact ordinary hypotheses,
height normalization, and distinction between the algebraic
characteristic series and the analytic p-adic L-function still need to
be checked at this save. No new result is yet claimed.

## Completed test

The [height foundations](../foundations/04-cyclotomic-height-criterion.md)
record the exact source statements and scope. Stein--Wuthrich's global
non-CM assumption was found in Section 3 and retained for its converse.
Ray's Theorem 3.4 supplies the needed implication without that restriction,
with the four arithmetic hypotheses explicit. Schneider's original full
text was unavailable, so the theorem-number attribution is identified as
checked through Ray rather than through a reading of the original proof.

[L003](../lemmas/L003-cyclotomic-height-semisimplicity.md) proves the
implication to the requested map using L002. It also checks that corank
zero of p-primary Sha is equivalent to finiteness here, since its dual is
finitely generated over Z_p. This makes the two-defect criterion exact.

The discriminating test succeeds conditionally: finite Sha and nonzero
height regulator eliminate the specialization defect. This reaches
characteristic order = rational rank, not complex order = rational rank.
The proof does not supply either arithmetic hypothesis for all curves,
identify the height map with eta, or calculate a radical dimension.
The finished evidence is a standard arithmetic input newly connected to
the notebook's gap, not a conjectural solution or a repeated stop review.
