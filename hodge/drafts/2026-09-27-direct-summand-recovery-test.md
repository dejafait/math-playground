# Direct-summand recovery: saved reasoning

The prior SPECIALIZE assessment matches the saved target exactly and
has no essential unread source. Its corrected obstruction theorem and
nilpotent-base criteria are reused. This step tests whether L018's
degree ordering is needed for existence of a recovered ideal lift.
The intended downstream use is an exclusion for every admissible
positive pair (m,n), with the converse still conditional on lifting f.

Write E=F direct sum G, F=I_C(-mH), G=O_X(-nH). The proposed replacement
for L018's chosen-inclusion argument is naturality of the full Ext^2
obstruction: if a flat E_A is perfect and kills o_E, the central
inclusion a:F -> E and retraction b:E -> F should give
o_F=b[2] o_E a=0. This would produce some perfect F_A independently of
whether either splitting map lifts in E_A. Derived reduction to the
field then needs to show F_A is an A-flat coherent sheaf.

The two ring comparisons must stay separate. For local R_A flat over
A, derived reduction modulo epsilon agrees with derived tensor over A
with C. Perfectness is tested along R_A -> R; concentration and base
flatness are tested along A -> C. The saved Stacks tags 07LU, 0H75 and
0654 address these respective passages.

L018's preceding extension recovery uses Ext^2(J,O_X(-m-n)), computed
from H^2(J(m+n)). Its displayed sequence after twisting only involves
I_C(n), O_X(m), and O_X; no difference of degrees occurs. L019 supplies
H^2(I_C(n))=0 for positive n. The remaining checks are the exact
extension-reduction map, the corrected obstruction theorem's ambient
hypotheses, and determinant/Hartogs reconstruction at all three
singular points. No enlarged statement is claimed until these checks
are complete.

Continue if these passages recover an embedded C for all m,n>0;
otherwise record the precise failed hypothesis. An exclusion would
still allow at most three of the four RM directions and would not
increase the 21-dimensional span on the existing family. The universal
Hodge gap, other representatives and ramified lifting remain separate.
The mechanism is standard obstruction theory; this is a specialization,
with no claim of originality.

## Completion on 2026-09-27

[L022](../lemmas/L022-direct-summand-recovery-all-positive-degrees.md)
completes all the checks above. Naturality on the central inclusion
and retraction kills the ideal summand's full obstruction; the cited
nilpotent-base results give a coherent A-flat sheaf lift. The degree-free
extension calculation and the determinant/Hartogs argument recover an
embedded C for every admissible m,n>0, with all three singular points
retained. No decomposition of the given middle lift is asserted.

The outcome is NEGATIVE for this whole first-order representative class.
At most three of the four RM directions can lift. Equality still needs
H^1(X,I_C(nH))=0 for the selected containing section. L020 and L021
remain valid; classifying their remaining cohomology range cannot
alter this exclusion. This is a reproduction/application of the
reviewed standard tools, not a claim of a new obstruction theory or
of progress beyond the checked literature. Ramified lifting with a
prescribed first-order motion remains untested for these unions.
