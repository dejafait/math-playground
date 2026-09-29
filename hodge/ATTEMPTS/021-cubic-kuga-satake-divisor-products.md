# Cubic Kuga--Satake tensor from products of divisors

Tested 2026-09-27. Outcome: NEGATIVE; the divisor-product recipe is
closed for the stated very-general rank-eighteen cubic RM setting.

## Proposed use

Supply beta_U on A^4 through divisor products, as one input to the
conditional Kuga--Satake transfer. Algebraicity of kappa would remain
separate. The span tested includes every divisor mixing the factors.

## WHY IT FAILS

[L031](../lemmas/L031-cubic-kuga-satake-tensor-outside-divisor-algebra.md)
constructs an element of the full polarization centralizer that
fixes all divisor classes but multiplies a nonzero component of
beta_U by four. The projected component comes from the actual
Clifford embedding of one RM eigenspace; the other two have zero
projection, so their coefficients cannot cancel it. The proof retains
all spin multiplicities and every permitted embedding/polarization
choice. Thus the whole tensor is outside the divisor algebra, not
just outside a smaller factorwise span. This excludes the proposed
source of cycles without showing beta_U is nonalgebraic. Published
constructions of exceptional algebraic classes require a separate
source comparison; no assertion about their applicability is made.
